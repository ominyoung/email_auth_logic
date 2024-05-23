from account.models import MyUser
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    original = serializers.SerializerMethodField()
    web = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ('original', 'web', 'thumbnail',)

    def get_original(self, obj):
        if bool(obj.profile):
            return self.context['request'].build_absolute_uri(obj.profile.url)
        return None

    def get_thumbnail(self, obj):
        if bool(obj.profile):
            return self.context['request'].build_absolute_uri(obj.profile_thumbnail.url)
        return None

    def get_web(self, obj):
        if bool(obj.profile):
            return self.context['request'].build_absolute_uri(obj.profile_website.url)
        return None