from rest_framework import serializers

from rest_api.models import Store, PaymentType


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'


class StoresSerializer(serializers.ModelSerializer):
    p_type = serializers.SlugRelatedField(many=True, read_only=`True`, slug_field='payment_type')
    class Meta:
        model = Store
        fields = '__all__'
