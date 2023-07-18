from rest_framework import serializers

class TranslatorSerializer(serializers.Serializer):
    description = serializers.CharField()
    language = serializers.DictField()

class DescriptionSerializer(serializers.Serializer):
    title = serializers.CharField(allow_blank=True, allow_null=True)
    information = serializers.CharField(allow_blank=True, allow_null =True)
    number = serializers.IntegerField()
    keywords = serializers.ListField()

class ImageSerializer(serializers.Serializer):
    title = serializers.CharField(allow_blank=True, allow_null=True)
    topic = serializers.DictField()
    effect = serializers.DictField()
    perspective = serializers.DictField()