public class App {
    public static void main(String[] args) {
        Model m = new Model("S", "S");
        View v = new View("MVC tut");
        Controller c = new Controller(m, v);
        c.initController();
    }
}
