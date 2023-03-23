from drf_yasg import openapi
OkResponseAutoSchema = openapi.Schema(
  type=openapi.TYPE_OBJECT,
  properties={
    'message': openapi.Schema(type=openapi.TYPE_STRING, default='string'),
  }
)
NoContentAutoSchema = openapi.Schema(
  type=openapi.TYPE_STRING,
)
GetTokenPairAutoSchema = openapi.Schema(
  type=openapi.TYPE_OBJECT,
  properties={
    'refresh': openapi.Schema(type=openapi.TYPE_STRING, default='refresh token'),
      'access': openapi.Schema(type=openapi.TYPE_STRING, default='access token'),
  }
)

BasketTotalPriceResponseSchema = openapi.Schema(
  type=openapi.TYPE_OBJECT,
  properties={
    'total_price': openapi.Schema(type=openapi.TYPE_INTEGER, default='total_price'),
  }
)

BasketTotalQuantityResponseSchema = openapi.Schema(
  type=openapi.TYPE_OBJECT,
  properties={
    'total_quantity': openapi.Schema(type=openapi.TYPE_INTEGER, default='total_quantity'),
  }
)

UserAddressQuantityResponseSchema = openapi.Schema(
  type=openapi.TYPE_OBJECT,
  properties={
    'address_quantity': openapi.Schema(type=openapi.TYPE_INTEGER, default='address_quantity'),
  }
)

BasketAddDeleteResponseSchema = openapi.Schema(
  type=openapi.TYPE_OBJECT,
  properties={
    'amount': openapi.Schema(type=openapi.TYPE_INTEGER, default='amount'),
  }
)
