public enum FlightStatus{
    ACTIVE,
    CANCELLED,
    DELAYED,
    IN_FLIGHT,
    LANDED,
    SCHEDULED
}

public enum PaymentStatus{
    PENDING,
    COMPLETED,
    CANCELLED
}

public enum ReservationStatus{
    PENDING,
    CONFIRMED,
    CANCELLED
}

public enum SeatClass{
    ECONOMY,
    BUSINESS,
    FIRST
}

public enum SeatType {
    REGULAR,
    ACCESSIBLE,
    EMERGENCY_EXIT,
    PREMIUM
}

public enum AccountStatus {
    ACTIVE,
    BLOCKED,
    BANNED,
    COMPROMISED,
    ARCHIVED,
    UNKNOWN
}

public class Address {
    private String streetAddress;
    private String city;
    private String state;
    private String zipCode;
    private String country;
}

// Account, Person, Customer and Passenger: These classes represent the different people that interact with our system:

public class Accounts {
    private String id;
    private String password;
    private AccountStatus status;

    public boolean resetPassword();
}

public abstract class Person {
    private String name;
    private Address address;
    private String email;
    private String phone;

    private Account Account;
}

public class Customer extends Person {
    private String frequentFlyerNumber;

    public List<Itinerary> getItineraries();
}

public class Passenger {
    private String name;
    private String passportNumber;
    private Date dateOfBirth;

    public String getPassportNumber(){
        return this.passportNumber;
    }
}

// Airport, Aircraft, Seat and FlightSeat: These classes represent the top-level classes of the system:
public class Airport {
    private String name;
    private Address address;
    private String code;

    public List<Flight> getFlights();
}

public class Aircraft {
    priate String name;
    private String model;
    private int manufacturingYear;
    private List<Seat> seats;

    public List<FlightInstance> getFlights();
}

public class Seat {
    private String seatNumber;
    private SeatType type;
    private SeatClass seatClass;
}

public class FlightSeat extends Seat {
    private double fare;
    public double getFare();
}

//Flight Schedule classes, Flight, FlightInstance, FlightReservation, Itinerary: Here are the classes related to flights and reservations:

public class WeeklySchedule {
    private int dayOfWeek;
    private Time departureTime;
}

public class CustomSchedule {
    private Date customDate
    private Time departureTime;
}

public class Flight {
    priate String flightNumber;
    private Airport departure;
    private Airport arrival;
    private int durationINMinutes;

    private List<WeeklySchedule> weeklySchedules;
    private List<CustomSchedule> customSchedules;
    private List<FlightInstance> flightInstances;
}

public class FlightInstance {
    private Date departure;
    private String gate;
    private FlightStatus status;
    private Aircraft aircraft;

    public bool cancel();
    public void updateStatus(FlightStatus status);
}

public class FlightReservation {
    private String reservationNumber;
    private FlightInstance flightInstance;
    private Map<Passenger, FlightSeat> seatMap;
    private Date creationDate;
    private ReservationStatus status;

    public static FlightReservation fetchReservationDetails(String reservationNumber);
    public List<Passenger> getPassengers();
}

public class Itinerary {
    private String customerId;
    private Airport startingAirport;
    private Airport finalAirport;
    private Date creationDate;
    private List<FlightReservation> reservations;

    public List<FlightReservation> getReservations();
    public boolean makeReservation();
    public boolean makePayment();
}