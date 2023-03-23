from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import Student


class StudentRetrieveSerializer(serializers.ModelSerializer):
    birth_day = serializers.DateField(
        format='%d-%m-%Y',
        input_formats=['%d-%m-%Y', ],
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'birth',
            'picture',
            'city',
            'school'

        )
        read_only_fields = ('id', 'uuid')


class TokenObtainPairWithoutPasswordSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()


class TokenObtainPairWithoutPasswordLoginSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()


class AccessTokenVerifySerializer(serializers.Serializer):
    access_token = serializers.CharField()
