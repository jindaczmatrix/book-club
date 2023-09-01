#ifndef HITTABLE_H
#define HITTABLE_H

#include "ray.h" // Include the "ray.h" header file.

class hit_record { // Declare a class named "hit_record".
	public:
		point3 p; // Declare a public member variable "p" of type "point3".
		vec3 normal; // Declare a public member variable "normal" of type "vec3".
		double t; // Declare a public member variable "t" of type "double".
};

class hittable {
  public:
    virtual ~hittable() = default;

    virtual bool hit(const ray& r, double ray_tmin, double ray_tmax, hit_record& rec) const = 0;
}; //virtual bool hit(const ray& r, double ray_tmin, double ray_tmax, hit_record& rec) const = 0;: 这是一个纯虚函数的声明。这是一个抽象函数，没有实际的实现，所以它的末尾有 = 0;。派生类必须实现这个函数。函数名为 hit，它接受一个 ray 对象 r、两个 double 类型的参数 ray_tmin 和 ray_tmax，还有一个 hit_record 对象的引用 rec。函数返回一个 bool 值，表示光线是否击中了物体。这个函数在派生类中会被实现以描述不同类型的可击中物体的行为。


#endif
