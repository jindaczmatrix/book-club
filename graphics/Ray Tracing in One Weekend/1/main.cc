#include <iostream>
// Include the necessary header for input/output operations.

int main() {
    // Define the main function.

    // Declare variables for the image dimensions.
    int image_width = 256;
    int image_height = 256;

    // Print the PPM header to indicate the image format and dimensions.
    std::cout << "P3\n" << image_width << " " << image_height << "\n255\n";

    // Loop through each row (height) of the image.
    for (int j = 0; j < image_height; ++j) {
		std::clog << "\rScanlines remaining: " << (image_height-j) << ' ' << std::flush;
        // Loop through each column (width) of the image.
        for (int i = 0; i < image_width; ++i) {
            // Calculate normalized values for red and green channels.
            auto r = double(i) / (image_width - 1);
            auto g = double(j) / (image_height - 1);
            
            // Blue channel is set to 0.
            auto b = 0;

            // Convert the normalized channel values to integers in the range [0, 255].
            int ir = static_cast<int>(255.999 * r);
            int ig = static_cast<int>(255.999 * g);
            int ib = static_cast<int>(255.999 * b);

            // Print the RGB values as space-separated integers.
            std::cout << ir << ' ' << ig << ' ' << ib << '\n';
        }
    }
	std::clog << "\rDone. 			\n";
}