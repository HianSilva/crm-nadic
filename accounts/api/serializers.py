from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # O campo 'name' do seu requisito é mapeado para first_name e last_name
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User.objects.create_user(username=username, password=password)

        user.email = validated_data.get('email', '')
        user.first_name = validated_data.get('first_name', '')
        user.last_name = validated_data.get('last_name', '')
        user.save()

        try:
            seller_group = Group.objects.get(name='Seller')
            user.groups.add(seller_group)
        except Group.DoesNotExist:
            pass

        return user
