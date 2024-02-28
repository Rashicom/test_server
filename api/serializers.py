from rest_framework import serializers
from .models import room, students, Shops, room_teachers, Url
from rest_framework.pagination import PageNumberPagination



class Roomserializer(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = "__all__"

class RoomTeachersserializer(serializers.ModelSerializer):
    class Meta:
        model = room_teachers
        fields = "__all__"

class StudentsSerializer(serializers.ModelSerializer):
    room_name = serializers.SerializerMethodField()
    teachers_list = serializers.SerializerMethodField()
    class Meta:
        model = students
        fields = "__all__"

    def get_room_name(self,obj):
        return obj.std_room.room_name
    def get_teachers_list(self,obj):
        tchr_list = obj.std_room.teacher_set.all()
        return RoomTeachersserializer(tchr_list, many=True).data
    

  
class CustomPagination(PageNumberPagination):
    page_size=50
    page_query_param = "page_size"
    max_page_size =100



class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        read_only_fields = [
            "is_blacklisted_by_tcil",
        ]
        fields = ["name", "url", "is_trusted"] + read_only_fields
