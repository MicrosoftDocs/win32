---
title: Scale effect
description: Use this effect to scale an image up or down. The effect has six scaling modes nearest neighbor, linear, cubic, multi-sample linear, anisotropic, and high quality cubic.
ms.assetid: 99DFA8DB-384B-4F64-90A2-0D3D7E1ACF27
keywords:
- scale effect
ms.topic: article
ms.date: 05/31/2018
---

# Scale effect

Use this effect to scale an image up or down. The effect has six scaling modes: nearest neighbor, linear, cubic, multi-sample linear, anisotropic, and high quality cubic.

The CLSID for this effect is CLSID\_D2D1Scale.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
    -   [Border modes](#border-modes)
-   [Interpolation modes](#interpolation-modes)
-   [Output bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image

This example shows the scale effect zooming in 2 times the input and cropping to the original size.



| Before                                                     |
|------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg) |
| After                                                      |
| ![the image after the transform.](images/22-scale.png)     |



 


```C++
ComPtr<ID2D1Effect> scaleEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Scale, &scaleEffect);

scaleEffect->SetInput(0, bitmap);

scaleEffect->SetValue(D2D1_SCALE_PROP_CENTER_POINT, D2D1::Vector2F(256.0f, 192.0f));
scaleEffect->SetValue(D2D1_SCALE_PROP_SCALE, D2D1::Vector2F(2.0f, 2.0f));

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(scaleEffect.Get());
m_d2dContext->EndDraw();
```



## Effect properties



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Display name and index enumeration</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Scale<br/> D2D1_SCALE_PROP_SCALE<br/></td>
<td>The scale amount in the X and Y direction as a ratio of the output size to the input size. This property a D2D1_VECTOR_2Fdefined as: (X scale, Y scale). The scale amounts are FLOAT, unitless, and must be positive or 0.<br/> The type is D2D1_VECTOR_2F.<br/> The default value is {1.0f, 1.0f}.<br/></td>
</tr>
<tr class="even">
<td>CenterPoint<br/> D2D1_SCALE_PROP_CENTER_POINT<br/></td>
<td>The image scaling center point. This property is a D2D1_VECTOR_2F defined as: (point X, point Y). The units are in DIPs.<br/> Use the center point property to scale around a point other than the upper-left corner.<br/> The type is D2D1_VECTOR_2F.<br/> The default value is {0.0f, 0.0f}.<br/></td>
</tr>
<tr class="odd">
<td>BorderMode<br/> D2D1_SCALE_PROP_BORDER_MODE<br/></td>
<td>The mode used to calculate the border of the image, soft or hard. See <a href="#border-modes">Border modes</a> for more info. <br/> The type is D2D1_BORDER_MODE.<br/> The default value is D2D1_BORDER_MODE_SOFT.<br/></td>
</tr>
<tr class="even">
<td>Sharpness<br/> D2D1_SCALE_PROP_SHARPNESS<br/></td>
<td>In the high quality cubic interpolation mode, the sharpness level of the scaling filter as a float between 0 and 1. The values are unitless. You can use sharpness to adjust the quality of an image when you scale the image down.<br/> The sharpness factor affects the shape of the kernel. The higher the sharpness factor, the smaller the kernel.<br/>
<blockquote>
[!Note]<br />
This property affects only the high quality cubic interpolation mode.
</blockquote>
<br/> The type is FLOAT.<br/> The default value is 0.0f.<br/></td>
</tr>
<tr class="odd">
<td>InterpolationMode<br/> D2D1_SCALE_PROP_INTERPOLATION_MODE<br/></td>
<td>The interpolation mode the effect uses to scale the image. There are 6 scale modes that range in quality and speed. See <a href="#interpolation-modes">Interpolation modes</a> for more info. <br/> The type is D2D1_SCALE_INTERPOLATION_MODE.<br/> The default value is D2D1_SCALE_INTERPOLATION_MODE_LINEAR.<br/></td>
</tr>
</tbody>
</table>



 

### Border modes



| Name                     | Description                                                                                                                                                                                                                                                              |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_BORDER\_MODE\_SOFT | The effect pads the input image with transparent black pixels for samples outside of the input bounds when it applies the convolution kernel. This creates a soft edge for the image, and in the process expands the output bitmap by the size of the kernel.<br/> |
| D2D1\_BORDER\_MODE\_HARD | The effect extends the input image with a mirror-type border transform for samples outside of the input bounds. The size of the output bitmap is equal to the size of the input bitmap.<br/>                                                                       |



 

\`

## Interpolation modes



| Enumeration                                             | Description                                                                                                                                                                                          |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_SCALE\_INTERPOLATION\_MODE\_NEAREST\_NEIGHBOR     | Samples the nearest single point and uses that. This mode uses less processing time, but outputs the lowest quality image.                                                                           |
| D2D1\_SCALE\_INTERPOLATION\_MODE\_LINEAR                | Uses a four point sample and linear interpolation. This mode uses more processing time than the nearest neighbor mode, but outputs a higher quality image.                                           |
| D2D1\_SCALE\_INTERPOLATION\_MODE\_CUBIC                 | Uses a 16 sample cubic kernel for interpolation. This mode uses the most processing time, but outputs a higher quality image.                                                                        |
| D2D1\_SCALE\_INTERPOLATION\_MODE\_MULTI\_SAMPLE\_LINEAR | Uses 4 linear samples within a single pixel for good edge anti-aliasing. This mode is good for scaling down by small amounts on images with few pixels.                                              |
| D2D1\_SCALE\_INTERPOLATION\_MODE\_ANISOTROPIC           | Uses anisotropic filtering to sample a pattern according to the transformed shape of the bitmap.                                                                                                     |
| D2D1\_SCALE\_INTERPOLATION\_MODE\_HIGH\_QUALITY\_CUBIC  | Uses a variable size high quality cubic kernel to perform a pre-downscale the image if downscaling is involved in the transform matrix. Then uses the cubic interpolation mode for the final output. |



 

> [!Note]  
> If you don't select a mode, the effect defaults to D2D1\_SCALE\_INTERPOLATION\_MODE\_LINEAR.

 

> [!Note]  
> Anisotropic mode generates mipmaps when scaling, however, if you set the **Cached** property to true on the effects that are input to this effect, the mipmaps won't be generated every time for sufficiently small images.

 

## Output bitmap

The location and size of the output bitmap depends on the specified scale factor and the center point.

You can calculate the size of the output bitmap using this equation:<dl> BitmapSize?(Pixels)=Scale?\*Original Bitmap Size? (DIPs)\*(UserDPI/96)  
BitmapSize<sub>y</sub>(Pixels)=Scale<sub>y</sub>\*Original Bitmap Size<sub>y</sub> (DIPs)\*(UserDPI/96)  
</dl>

The effect rounds fractions of pixels up to the nearest whole pixel.

The location of the bitmap is (0, 0) or the value of the center point property.

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

 

