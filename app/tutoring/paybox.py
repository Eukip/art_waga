from datetime import datetime
from .models import Exercise
from hashlib import md5
from urllib.parse import urlencode
from django.conf import settings

class PayboxRedirectService:
    """
    Operating for request to paybox,
    used when a client pays for his site at a tariff,
    """

    @classmethod
    def generate_paybox_url(cls, coupon, bought_coupon):
        """generate url for redirect to paybox for payment site rent"""

        paybox_params = {
            'pg_merchant_id': settings.PAYBOX_PROJECT_ID,
            'pg_amount': str(coupon.price_for_coupon),
            'pg_currency': settings.PAYBOX_CURRENCY,
            'pg_payment_id': str(coupon.id),
            'pg_order_id': str(bought_coupon.id),
            'pg_salt': settings.PAYBOX_SALT,
            'pg_description': str(coupon.title),
            'pg_language': settings.PAYBOX_LANGUAGE,
            'pg_success_url': settings.PG_SITE_URL + 'exercise/' + str(coupon.id),
            'pg_success_url_method': settings.PAYBOX_SUCCESS_URL_METHOD,
            'pg_result_url': settings.PAYBOX_RESULT_URL,
            'secret_key': settings.PAYBOX_SECRET_KEY,
            'pg_failure_url': settings.PG_SITE_URL + 'exercise/' + str(coupon.id),
            'pg_testing_mode': '0'
        }
        paybox_params = dict(sorted(paybox_params.items()))
        pg_sig_gen = cls.generate_sig(paybox_params.values())
        paybox_params['pg_sig'] = pg_sig_gen

        # secret_key used just for generation pg_sig(*подпись)
        del paybox_params['secret_key']
        url_params = urlencode(paybox_params)

        return f'{settings.PAYBOX_URL}?{url_params}'

    @staticmethod
    def generate_sig(sig_params):
        result = ['payment.php', ';'.join(sig_params)]
        pg_sig = ';'.join(result)
        pg_sig = md5(pg_sig.encode('UTF-8')).hexdigest()

        return pg_sig


class PayboxResultService:
    """Update SitePayment model after paybox successful/failed transactions"""

    @classmethod
    def success_update_site_payment(cls, paybox_data: dict, site_payment_id: int):
        """if the paybox transaction is successfully"""

        success_description = (
              f"Электронная почта: {paybox_data.get('pg_user_contact_email')}\n"
              f"Название платежной системы: {paybox_data.get('pg_card_brand')}\n"
              f"Номер платёжной карты: {paybox_data.get('pg_card_pan')}\n"
              f"Имя: {paybox_data.get('pg_card_owner')}\n"
              f"Сумма (pg_amount): {paybox_data.get('pg_amount')}\n"
              f"Сумма (ps_amount): {paybox_data.get('pg_amount')}\n"
        )
        update_fields = dict(
            is_paid=True,
            pg_currency=paybox_data.get('pg_currency'),
            payed_at=datetime.now(),
            success_transaction_description=success_description,
        )
        Exercise.objects.update_instance(
            instance_id=site_payment_id, **update_fields)

    @classmethod
    def failure_update_site_payment(cls, paybox_data: dict, site_payment_id: int):
        """if the paybox transaction is unsuccessful"""

        alternative_msg = 'неудачная транзакция \n' \
                          '(* отсутствует поле pg_failure_description)'
        fail_update_fields = dict(
            failure_transaction_description=paybox_data.get('pg_failure_description',
                                                            alternative_msg)
        )
        Exercise.objects.update_instance(
            instance_id=site_payment_id, **fail_update_fields)