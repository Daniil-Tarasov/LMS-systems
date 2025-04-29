from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from materials.validators import LinkToVideo


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkToVideo(field='link_to_video')]


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('title_course', 'description', 'lesson', 'count_lessons')

    def get_count_lessons(self, course):
        return course.lesson.count()
