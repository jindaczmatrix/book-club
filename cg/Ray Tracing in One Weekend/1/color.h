#ifndef COLOR_H
#define COLOR_H

#include "vec3.h"  // 包含 vec3.h 文件

#include <iostream>

using color = vec3;  // 使用 vec3 类型的别名 color

// 定义写入颜色到输出流的函数
void write_color(std::ostream &out, color pixel_color) {
    // 将颜色的每个分量的 [0, 255] 的整数值写入输出流
    out << static_cast<int>(255.999 * pixel_color.x()) << ' '
        << static_cast<int>(255.999 * pixel_color.y()) << ' '
        << static_cast<int>(255.999 * pixel_color.z()) << '\n';
}

#endif