# this is just an example code!!!
#!/bin/bash

ffmpeg -start_number 0 -framerate 10 -i %01d.jpg -vframes 100 -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4

# this creates a video called output.mp4, starting at image 0.jpg till 100 frames are reached (vframes) with a framerate of 10Hz