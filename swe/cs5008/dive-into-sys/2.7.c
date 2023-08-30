struct studentT {
	char name[64];
	int age;
	float gpa;
	int grad_yr;
}

struct studentT s;
s.age = 18;
s.gpa = 4.0;
s.grad_yr = 2020;

sptr = malloc(sizeof(struct studentT));
if (sptr == NULL) {
	printf("Error: malloc failed\n")
}