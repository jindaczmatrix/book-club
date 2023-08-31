#include "color.h"
#include "vec3.h"
#include "ray.h"

#include <iostream>

double hit_sphere(const point3& center, double radius, const ray& r) {
    // Calculate the vector from the ray's origin to the center of the sphere
    vec3 oc = r.origin() - center;

    // Coefficients for the quadratic equation
    auto a = dot(r.direction(), r.direction());
    auto b = 2.0 * dot(oc, r.direction());
    auto c = dot(oc, oc) - radius * radius;

    // Calculate the discriminant of the quadratic equation
    auto discriminant = b * b - 4 * a * c;

    if (discriminant < 0) {
        return -1.0; // No intersection with the sphere
    } else {
        return (-b - sqrt(discriminant)) / (2.0 * a); // Return the smaller root
    }
}

color ray_color(const ray& r) {
    auto t = hit_sphere(point3(0,0,-1), 0.5, r);
    
    // Check if the ray hits the sphere
    if (t > 0.0) {
        vec3 N = unit_vector(r.at(t) - vec3(0,0,-1)); // Calculate normal at the intersection
        return 0.5 * color(N.x() + 1, N.y() + 1, N.z() + 1); // Convert normal to color
    }

    // If not hitting the sphere, calculate background color based on ray direction
    vec3 unit_direction = unit_vector(r.direction());
    auto a = 0.5 * (unit_direction.y() + 1.0);

    // Linear interpolation between white and blue gradient for sky color
    return (1.0 - a) * color(1.0, 1.0, 1.0) + a * color(0.5, 0.7, 1.0);
}


int main()
{
    auto aspect_ratio = 16.0 / 9.0;  // 宽高比
    int image_width = 400;  // 图像宽度

    // 计算图像高度，并确保它至少为1。
    int image_height = static_cast<int>(image_width / aspect_ratio);
    image_height = (image_height < 1) ? 1 : image_height;

    // 相机参数

    auto focal_length = 1.0;  // 焦距
    auto viewport_height = 2.0;  // 视口高度
    auto viewport_width = viewport_height * (static_cast<double>(image_width) / image_height);  // 视口宽度
    auto camera_center = point3(0, 0, 0);  // 相机位置

    // 计算视口上水平和垂直边缘的向量。
    auto viewport_u = vec3(viewport_width, 0, 0);  // 水平边缘向量
    auto viewport_v = vec3(0, -viewport_height, 0);  // 垂直边缘向量

    // 计算从像素到像素的水平和垂直增量向量。
    auto pixel_delta_u = viewport_u / image_width;  // 像素水平增量
    auto pixel_delta_v = viewport_v / image_height;  // 像素垂直增量

    // 计算左上角像素的位置。
    auto viewport_upper_left = camera_center
                             - vec3(0, 0, focal_length) - viewport_u / 2 - viewport_v / 2;  // 视口左上角位置
    auto pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v);  // 像素(0, 0) 的位置


    // render
    std::cout << "P3\n"
              << image_width << " " << image_height << "\n255\n";

    // Loop through each row (height) of the image.
    for (int j = 0; j < image_height; ++j)
    {
        std::clog << "\rScanlines remaining: " << (image_height - j) << ' ' << std::flush;
        // Loop through each column (width) of the image.
        for (int i = 0; i < image_width; ++i)
        {
            auto pixel_center = pixel00_loc + (i * pixel_delta_u) + (j * pixel_delta_v);
            auto ray_direction = pixel_center - camera_center;
            ray r(camera_center, ray_direction);

            color pixel_color = ray_color(r);
            write_color(std::cout, pixel_color);

            // // Calculate normalized values for red and green channels.
            // auto r = double(i) / (image_width - 1);
            // auto g = double(j) / (image_height - 1);

            // // Blue channel is set to 0.
            // auto b = 0;

            // // Convert the normalized channel values to integers in the range [0, 255].
            // int ir = static_cast<int>(255.999 * r);
            // int ig = static_cast<int>(255.999 * g);
            // int ib = static_cast<int>(255.999 * b);

            // // Print the RGB values as space-separated integers.
            // std::cout << ir << ' ' << ig << ' ' << ib << '\n';
        }
    }
    std::clog << "\rDone. 			\n";
}