---
title: Convolve matrix effect
description: Use the convolve matrix effect to apply an arbitrary 2D kernel to an image. You can use this effect to blur, detect edges, emboss, or sharpen an image.
ms.assetid: D9C23AC4-0090-4F16-AC59-B952FB616FA9
keywords:
- convolve matrix effect
ms.topic: article
ms.date: 05/31/2018
---

# Convolve matrix effect

Use the convolve matrix effect to apply an arbitrary 2D kernel to an image. You can use this effect to blur, detect edges, emboss, or sharpen an image.

The CLSID for this effect is CLSID\_D2D1ConvolveMatrix.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
-   [Scale modes](#scale-modes)
-   [Border modes](#border-modes)
-   [Output bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image

The example here shows the input and output of the convolve matrix effect with a 3 x 3 kernel.



| Before                                                         |
|----------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg)     |
| After                                                          |
| ![the image after the transform.](images/6-convolvematrix.png) |



 


```C++
ComPtr<ID2D1Effect> convolveMatrixEffect;
m_d2dContext->CreateEffect(CLSID_D2D1ConvolveMatrix, &convolveMatrixEffect);

convolveMatrixEffect->SetInput(0, bitmap);
float matrix[9] = {-1, -1, -1, -1, 9, -1, -1, -1, -1};
convolveMatrixEffect->SetValue(D2D1_CONVOLVEMATRIX_PROP_KERNEL_MATRIX, matrix);

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(convolveMatrixEffect.Get());
m_d2dContext->EndDraw();
```



## Effect properties



| Display name and index enumeration                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| KernelUnitLength<br/> D2D1\_CONVOLVEMATRIX\_PROP\_KERNEL\_UNIT\_LENGTH<br/> | The size of one unit in the kernel. The units are in (DIPs/kernel unit), where a kernel unit is the size of the element in the convolution kernel. A value of 1 (DIP/kernel unit) corresponds to one pixel in a image at 96 DPI.<br/> The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                   |
| ScaleMode<br/> D2D1\_CONVOLVEMATRIX\_PROP\_SCALE\_MODE<br/>                 | The interpolation mode the effect uses to scale the image to the corresponding kernel unit length. There are six scale modes that range in quality and speed.<br/> The type is D2D1\_CONVOLVEMATRIX\_SCALE\_MODE.<br/> The default value is D2D1\_CONVOLVEMATRIX\_SCALE\_MODE\_LINEAR.<br/>                                                                                                                                                                                                                     |
| KernelSizeX<br/> D2D1\_CONVOLVEMATRIX\_PROP\_KERNEL\_SIZE\_X<br/>           | The width of the kernel matrix. The units are specified in kernel units. The type is UINT32.<br/> The default value is 3.<br/>                                                                                                                                                                                                                                                                                                                                                                                        |
| KernelSizeY<br/> D2D1\_CONVOLVEMATRIX\_PROP\_KERNEL\_SIZE\_Y<br/>           | The height of the kernel matrix. The units are specified in kernel units. The type is UINT32.<br/> The default value is 3.<br/>                                                                                                                                                                                                                                                                                                                                                                                       |
| KernelMatrix<br/> D2D1\_CONVOLVEMATRIX\_PROP\_KERNEL\_MATRIX<br/>           | The kernel matrix to be applied to the image. The kernel elements aren't bounded and are specified as floats.<br/> The first set of *KernelSizeX* numbers in the FLOAT\[\] corresponds to the first row in the kernel. The second set of *KernelSizeX* numbers correspond to the second row, and so on up to *KernelSizeY* rows.<br/> The type is FLOAT\[\].<br/> The default value is {0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, 0.0f, 0.0f}.<br/>                                                       |
| Divisor<br/> D2D1\_CONVOLVEMATRIX\_PROP\_DIVISOR<br/>                       | The kernel matrix is applied to a pixel and then the result is divided by this value. <br/> 0 behaves as a value of float epsilon.<br/> The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                                           |
| Bias<br/> D2D1\_CONVOLVEMATRIX\_PROP\_BIAS<br/>                             | The effect applies the kernel matrix, the divisor, and then the bias is added to the result. The bias is unbounded and unitless. The type is FLOAT.<br/> The default value is 0.0f.<br/>                                                                                                                                                                                                                                                                                                                              |
| KernelOffset<br/> D2D1\_CONVOLVEMATRIX\_PROP\_KERNEL\_OFFSET<br/>           | Shifts the convolution kernel from a centered position on the output pixel to a position you specify left/right and up/down. The offset is defined in kernel units.<br/> With some offsets and kernel sizes, the convolution kernel s samples won't land on a pixel image center. The pixel values for the kernel sample are computed by bilinear interpolation.<br/> The type is D2D1\_VECTOR\_2F.<br/> The default value is {0.0f, 0.0f}.<br/>                                                          |
| PreserveAlpha<br/> D2D1\_CONVOLVEMATRIX\_PROP\_PRESERVE\_ALPHA<br/>         | Specifies whether the convolution kernel is applied to the alpha channel or only the color channels.<br/> If you set this to **TRUE** the convolution kernel is applied only to the color channels.<br/> If you set this to **FALSE** the convolution kernel is applied to all channels.<br/> The type is BOOL.<br/> The default value is FALSE.<br/>                                                                                                                                               |
| BorderMode<br/> D2D1\_CONVOLVEMATRIX\_PROP\_BORDER\_MODE<br/>               | The mode used to calculate the border of the image, soft or hard. See [Border modes](https://www.bing.com/search?q=Border+modes) for more info.<br/> The type is D2D1\_BORDER\_MODE.<br/> The default value is D2D1\_BORDER\_MODE\_SOFT.<br/>                                                                                                                                                                                                                                                                                     |
| ClampOutput<br/> D2D1\_CONVOLVEMATRIX\_PROP\_CLAMP\_OUTPUT<br/>             | Whether the effect clamps color values to between 0 and 1 before the effect passes the values to the next effect in the graph. The effect clamps the values before it premultiplies the alpha .<br/> If you set this to TRUE the effect will clamp the values. If you set this to FALSE, the effect will not clamp the color values, but other effects and the output surface may clamp the values if they are not of high enough precision.<br/> The type is BOOL.<br/> The default value is FALSE.<br/> |



 

## Scale modes



| Enumeration                                              | Description                                                                                                                                                                                          |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_CONVOLVEMATRIX\_SCALE\_MODE\_NEAREST\_NEIGHBOR     | Samples the nearest single point and uses that. This mode uses less processing time, but outputs the lowest quality image.                                                                           |
| D2D1\_CONVOLVEMATRIX\_SCALE\_MODE\_LINEAR                | Uses a four point sample and linear interpolation. This mode outputs a higher quality image than nearest neighbor mode.                                                                              |
| D2D1\_CONVOLVEMATRIX\_SCALE\_MODE\_CUBIC                 | Uses a 16 sample cubic kernel for interpolation. This mode uses the most processing time, but outputs a higher quality image.                                                                        |
| D2D1\_CONVOLVEMATRIX\_SCALE\_MODE\_MULTI\_SAMPLE\_LINEAR | Uses 4 linear samples within a single pixel for good edge anti-aliasing. This mode is good for scaling down by small amounts on images with few pixels.                                              |
| D2D1\_CONVOLVEMATRIX\_SCALE\_MODE\_ANISOTROPIC           | Uses anisotropic filtering to sample a pattern according to the transformed shape of the bitmap.                                                                                                     |
| D2D1\_CONVOLVEMATRIX\_SCALE\_MODE\_HIGH\_QUALITY\_CUBIC  | Uses a variable size high quality cubic kernel to perform a pre-downscale the image if downscaling is involved in the transform matrix. Then uses the cubic interpolation mode for the final output. |



 

> [!Note]  
> If you don't select a mode, the effect defaults to D2D1\_CONVOLVEMATRIX\_SCALE\_MODE\_LINEAR.

 

## Border modes



| Name                     | Description                                                                                                                                                                                                                                                              |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_BORDER\_MODE\_SOFT | The effect pads the input image with transparent black pixels for samples outside of the input bounds when it applies the convolution kernel. This creates a soft edge for the image, and in the process expands the output bitmap by the size of the kernel.<br/> |
| D2D1\_BORDER\_MODE\_HARD | The effect extends the input image with a mirror-type border transform for samples outside of the input bounds. The size of the output bitmap is equal to the size of the input bitmap.<br/>                                                                       |



 

## Output bitmap

The size of the effect's output depends on the size of the convolution kernel, the kernel offset, the kernel unit length, and the border mode setting.

## Requirements



| Requirement | Value |
|--------------------------|------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects.h                                                                      |
| Library                  | d2d1.lib, dxguid.lib                                                               |



 

## Related topics

<dl> <dt>

[**ID2D1Effect**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect)
</dt> </dl>

 

