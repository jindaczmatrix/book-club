#ifndef SPHERE_H
#define SPHERE_H

#include "hittable.h"
#include "vec3.h"

// 定义表示球体的类，继承自 hittable 类
class sphere : public hittable {
	private:
		point3 center;  // 球心坐标
		double radius;  // 半径

	public:
		// 构造函数，初始化球心坐标和半径
		sphere(point3 _center, double _radius): center(_center), radius(_radius) {}

		// 实现 hittable 类的虚函数 hit，用于检测射线与球的相交
		bool hit(const ray& r, double ray_tmin, double ray_tmax, hit_record& rec) const override {
			vec3 oc = r.origin() - center;  // 射线起点到球心的向量
	    auto a = r.direction().length_squared();  // 射线方向的长度的平方
	    auto half_b = dot(oc, r.direction());  // half_b 表示 oc 与射线方向的点积
	    auto c = oc.length_squared() - radius * radius;  // c 表示球心到射线起点的距离的平方减去半径的平方

	    auto discriminant = half_b * half_b - a * c;  // 计算判别式
			if (discriminant < 0) return false;  // 判别式小于 0 表示无实根，不相交
			auto sqrtd = sqrt(discriminant);  // 计算判别式的平方根

			// 寻找在可接受范围内的最近根
			auto root = (-half_b - sqrtd) / a;
			if (root <= ray_tmin || ray_tmax <= root) {
				root = (-half_b + sqrtd) / a;
				if (root <= ray_tmin || ray_tmax <= root) {
					root = (-half_b + sqrtd) / a;
					if (root <= ray_tmin || ray_tmax <= root)
						return false;
				}
				rec.t = root;  // 记录相交点参数 t
				rec.p = r.at(rec.t);  // 计算相交点坐标
				rec.normal = (rec.p - center) / radius;  // 计算法向量

				return true;  // 返回相交
			}
		}
};

#endif
