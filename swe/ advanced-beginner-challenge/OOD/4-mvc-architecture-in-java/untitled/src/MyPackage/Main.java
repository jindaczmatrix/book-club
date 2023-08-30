package MyPackage;

public class Main {
    private static Course retrieveCourseFromDB() {
        Course course = new Course();
        course.setName("java");
        course.setId("101");
        course.setCategory("programming");
        return course;
    }
    public static void main(String[] args) {
        Course model = retrieveCourseFromDB();
        CourseView view = new CourseView();
        CourseController controller = new CourseController(model, view);
        controller.updateView();
        controller.setCourseName("python3");
        System.out.println("nAfter updating, Course Details are as follows");
        controller.updateView();

    }
}