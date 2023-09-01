#ifndef RAY_H
#define RAY_H

#include "vec3.h"

// 定义表示射线的类
class ray {
  public:
    ray() {}

    // 构造函数，初始化射线的起点和方向
    ray(const point3& origin, const vec3& direction) : orig(origin), dir(direction) {}

    // 返回射线的起点
    point3 origin() const  { return orig; }
    
    // 返回射线的方向
    vec3 direction() const { return dir; }

    // 根据参数 t 计算射线上的点
    point3 at(double t) const {
        return orig + t * dir;
    }

  private:
    point3 orig;  // 射线起点
    vec3 dir;     // 射线方向
};

#endif