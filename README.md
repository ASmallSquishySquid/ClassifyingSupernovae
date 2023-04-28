# ClassifyingSupernovae
Classifying supernovae as type 1 or type 2

Steps:
1. Bias subtract and flat divide images.
2. Combine the images
3. Find the min, max, and usable sky value for each image.
4. Get counts of each supernova using the different sky values.
5. Normalize for exposure time.
6. Plot V/R vs Ha/R using the min and max sky value counts as the errors.
7. Group the type 1 and type 2 supernovae.
8. Classify the unknown supernovae.