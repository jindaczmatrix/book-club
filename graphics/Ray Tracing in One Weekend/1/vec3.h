#ifndef VEC3_H
#define VEC3_H

#include <cmath>
#include <iostream>

using std::sqrt;

class vec3
{
public:
  double e[3]; // A private array to store the 3 components of the vector.

  // Constructors
  vec3() : e{0, 0, 0} {}                                   // Default constructor initializes vector to (0, 0, 0)
  vec3(double e0, double e1, double e2) : e{e0, e1, e2} {} // Initialize vector with specified components

  // Accessor methods
  double x() const { return e[0]; }
  double y() const { return e[1]; }
  double z() const { return e[2]; }

  // Unary negation operator (~) to negate all vector components
  vec3 operator~() const { return vec3(-e[0], -e[1], -e[2]); }

  // Indexing operator [] to access vector components
  double operator[](int i) const { return e[i]; }
  /*
  这是一个非常量成员函数，用于通过索引访问向量的元素。它返回一个指向索引为 i 的元素的引用，因此可以用于读取和修改元素的值。
  vec3 v(3, 4, 5);
  double& element_ref = v[1];  // 获取索引为1的元素的引用
  element_ref = 7.0;           // 修改索引为1的元素的值为7.0
  double new_value = v[1];     // 读取修改后的元素值
  */
  double &operator[](int i) { return e[i]; }

  // Compound assignment operators

  // Add another vector 'v' to this vector
  vec3 &operator+=(const vec3 &v)
  {
    e[0] += v.e[0];
    e[1] += v.e[1];
    e[2] += v.e[2];
    return *this;
  }

  // Multiply this vector by a scalar 't'
  vec3 &operator*=(double t)
  {
    e[0] *= t;
    e[1] *= t;
    e[2] *= t;
    return *this;
  }

  // Divide this vector by a scalar 't'
  vec3 &operator/=(double t)
  {
    return *this *= 1 / t; // Equivalent to multiplying by (1/t)
  }

  // Calculate the Euclidean length of the vector
  double length() const
  {
    return sqrt(length_squared());
  }

  // Calculate the squared length of the vector (faster than length())
  double length_squared() const
  {
    return e[0] * e[0] + e[1] * e[1] + e[2] * e[2];
  }
};

// point3 is alias for vec3, woule be useful for claeirty
using point3 = vec3;

// 输出运算符重载，用于将 vec3 输出到流中
inline std::ostream &operator<<(std::ostream &out, const vec3 &v)
{
  return out << v.e[0] << " " << v.e[1] << " " << v.e[2];
}

// 向量加法运算符重载
inline vec3 operator+(const vec3 &u, const vec3 &v)
{
  return vec3(u.e[0] + v.e[0], u.e[1] + v.e[1], u.e[2] + v.e[2]);
}

// 向量减法运算符重载
inline vec3 operator-(const vec3 &u, const vec3 &v)
{
  return vec3(u.e[0] - v.e[0], u.e[1] - v.e[1], u.e[2] - v.e[2]);
}

// 向量乘法运算符重载
inline vec3 operator*(const vec3 &u, const vec3 &v)
{
  return vec3(u.e[0] * v.e[0], u.e[1] * v.e[1], u.e[2] * v.e[2]);
}

// 向量和标量乘法运算符重载
inline vec3 operator*(double t, const vec3 &v)
{
  return vec3(t * v.e[0], t * v.e[1], t * v.e[2]);
}

// 标量和向量乘法运算符重载（前者是后者的特例）
inline vec3 operator*(const vec3 &v, double t)
{
  return t * v;
}

// 向量和标量除法运算符重载
inline vec3 operator/(vec3 v, double t)
{
  return (1 / t) * v;
}

// 计算两个向量的点乘
inline double dot(const vec3 &u, const vec3 &v)
{
  return u.e[0] * v.e[0] + u.e[1] * v.e[1] + u.e[2] * v.e[2];
}

// 计算两个向量的叉乘
inline vec3 cross(const vec3 &u, const vec3 &v)
{
  return vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1],
              u.e[2] * v.e[0] - u.e[0] * v.e[2],
              u.e[0] * v.e[1] - u.e[1] * v.e[0]);
}

// 生成一个与原向量方向相同但长度为1的单位向量
inline vec3 unit_vector(vec3 v)
{
  return v / v.length();
}

#endif