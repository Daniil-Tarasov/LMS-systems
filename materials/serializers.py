from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    class Meta:
        model = Course
        fields = ('title_course', 'description', 'count_lessons')

    def get_count_lessons(self, course):
        return course.lesson.count()


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
