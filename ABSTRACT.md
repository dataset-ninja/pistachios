
The authors have unveiled and made available a novel **Pesteh Dataset** focusing on pistachios, comprising six videos totaling 167 seconds in length, with a total of 3927 labeled pistachios. Their objective was to introduce a novel system for quantifying the various types of pistachios using computer vision techniques. A distinctive aspect of their approach is that, unlike numerous existing studies, their model is designed to count pistachios within videos rather than static images. This poses a unique challenge as it necessitates assigning each pistachio across consecutive frames of the video, ensuring that each instance is accurately counted only once.

## Motivation

In modern industries, automation plays a crucial role in enhancing efficiency and conserving resources. Among various sectors, the agricultural industry and its related fields stand out as needing further advancements in automation. Proper packaging of agricultural products not only boosts profitability but also minimizes crop losses. However, the classification of crop quality traditionally relies on human resources, leading to time-consuming processes, escalating costs, and often lacking the precision achieved by machines.

Pistachios, for instance, require human intervention for sorting and counting to evaluate crop quality based on whether their shells are ***open*** or ***close***. Typically, pistachios are sorted into categories based on the shape of their shells—either open-mouth or closed-mouth—each with distinct pricing and value. Renowned for their nutritional value, pistachio kernels are rich in unsaturated fatty acids, fiber, carbohydrates, proteins, and various essential vitamins, making them highly beneficial for human consumption. Regular consumption of pistachio kernels has been linked to reduced risks of heart disease and positive effects on blood pressure among non-diabetic individuals, while also aiding in cancer prevention.

Pistachios hold significant economic importance, particularly in Middle Eastern countries like Iran, where they are a key agricultural product. Iran, the USA, and Turkey are the leading producers of pistachios globally. Notably, pistachios come in various types, exhibiting differences in size, color, and flavor depending on their variety and place of cultivation. Broadly, pistachios can be categorized into three main types: round, long, and jumbo, each with distinctive shell characteristics. For instance, long pistachios typically have a narrower split compared to round and jumbo varieties, which display a more pronounced shell opening.

<img src="https://github.com/dataset-ninja/pistachios/assets/120389559/c12cb8f6-ecd3-46a3-bff5-4a94d7e6f778" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Pistachios Assortment.</span>

The average weight of a single pistachio shell is approximately 0.57 grams, translating to about 1750 shells per kilogram. Given this statistic, manually counting pistachios becomes an arduous and time-consuming task, ripe for automation through artificial intelligence. The detection and counting of pistachios serve multiple purposes, including facilitating proper packaging and assessing crop quality. Additionally, it aids in estimating future crop yields and breeding pistachio trees to enhance crop quality. Since open-mouth and closed-mouth pistachios differ significantly in price and demand, precise counting is essential for pistachio production and packaging facilities to ensure accurate inventory management. Moreover, segregating these two types of pistachios enhances the quality of export packages. The manual sorting of pistachios is not only labor-intensive but also economically impractical, making machine vision systems invaluable in this context. Furthermore, ***close*** pistachios, identified through such systems, can be recycled through mechanical opening methods, reducing losses and increasing overall crop yields. Machine vision, particularly leveraging deep learning techniques, has emerged as a powerful tool for automating tasks traditionally performed by humans. Deep convolutional neural networks, in particular, excel in recognizing and counting pistachios, although factors such as pistachio appearance and camera angles influence accuracy. The advancement of machine vision technology, coupled with the flexibility and adaptability of deep learning algorithms, offers promising prospects for automating pistachio counting and classification tasks with precision and efficiency.

## Dataset description

The authors' research marks the pioneering exploration into detecting, tracking, and counting pistachios along transportation lines, even under conditions of high density and occlusion. A significant challenge lies in accurately distinguishing between open-mouth and closed-mouth pistachios, as the former may appear as the latter when in motion or spinning on the transportation line. This phenomenon poses a formidable obstacle for many tracking algorithms, as the classification of pistachios may change between successive frames. However, the authors' tracking and counting model successfully addresses this challenge, achieving high levels of accuracy. To detect pistachios in video frames, the authors employ the RetinaNet object detector. They adopt a stratified approach by partitioning the dataset into five folds, reserving 20 percent of the dataset for testing purposes while utilizing the remainder for training.

<img src="https://github.com/dataset-ninja/pistachios/assets/120389559/9d63ccc2-9785-414e-84c9-00f5e2f8651f" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">General Schematic of the proposed model.</span>

In the authors' research, one of the most relevant studies is fruit detection and counting, which employs various tools including black and white (B/W) cameras, color cameras, thermal cameras, and spectral cameras. However, the nature of the data dictates that color becomes a crucial feature, rendering B/W cameras unsuitable for the task. Similarly, the spectral camera's time delay makes it impractical for this application. Despite its sensitivity to size, the thermal camera is not suitable for analyzing the data due to its inability to detect split pistachios. Consequently, the color camera emerges as the most suitable tool for the job. Additionally, color cameras offer the advantage of widespread availability, particularly in mobile phones, which can facilitate remote monitoring and control. While alternative methods such as sensors exist for counting, they are not suitable for this specific task due to the challenge of accurately counting split and non-split pistachios.


In Iran, pistachios are commonly referred to as Pesteh hence why the authors named their dataset Pesteh-Set. This dataset comprises two main components. The first part consists of 423 images, each meticulously labeled with ground truth data. The pistachios in these images are categorized into two classes: ***open*** and ***close*** with bounding boxes provided for each class. The number of pistachios per image varies from 1 to 27, totaling 3927 pistachios across all images. The second part of the dataset comprises six videos, totaling 9486 frames, which were utilized for the counting phase. These videos feature 561 pistachios in motion and over 350,000 individual pistachios collectively across all frames. Recorded using a cell phone camera with a resolution of 1920 × 1080 pixels, the dataset's videos are captured at varying frame rates. Five of the videos are recorded at a frame rate of 60 frames per second (fps), while the remaining video is recorded at 30 fps. The cell phone camera was positioned on a wall above the transportation line for the pistachios. This line was designed to allow the pistachios to roll, a crucial feature as it enables open-mouth pistachios to reveal their open side as they roll, which may not be visible otherwise.

<img src="https://github.com/dataset-ninja/pistachios/assets/120389559/3da5663e-db65-43ad-bcfe-aa43335e6492" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">The General View of how Pesteh-Set was recoreded and the proposed system for counting the pistachios.</span>

The authors utilized a self-developed program, leveraging the OpenCV library in Python, to label selected frames from the videos. In this labeling process, the pistachios were categorized into two classes: open-mouth and closed-mouth pistachios. Furthermore, the authors generously shared the self-developed labeling program along with all associated data, facilitating its use by other researchers to expand the Pistachio Dataset.

<img src="https://github.com/dataset-ninja/pistachios/assets/120389559/dc454742-b40b-40ab-a131-600a5098a937" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Some of the images in the Pesteh Set.</span>

|           | Number of Open-mouth Pistachios | Number of Closed-mouth Pistachios | Number of All the Pistachios |
|-----------|---------------------------------|------------------------------------|------------------------------|
| Video 1   | 50                              | 20                                 | 70                           |
| Video 2   | 60                              | 20                                 | 80                           |
| Video 3   | 70                              | 20                                 | 90                           |
| Video 4   | 90                              | 20                                 | 110                          |
| Video 5   | 100                             | 20                                 | 120                          |
| Video 6   | 39                              | 52                                 | 91                           |
| All Videos| 409                             | 152                                | 561                          |
| All Images| 1993                            | 1934                               | 3927                         |

<span style="font-size: smaller; font-style: italic;">This table shows the distribution of Pistachios in the Pesteh Set.</span>

