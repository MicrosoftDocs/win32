---
title: Directional blur effect
description: The directional blur effect is similar to Gaussian blur, except you can skew the blur in a particular direction.
ms.assetid: 59328FA4-5C27-4A81-AAB2-C5B25B3615C6
keywords:
- directional blur
ms.topic: article
ms.date: 05/31/2018
---

# Directional blur effect

The directional blur effect is similar to [Gaussian blur](gaussian-blur.md), except you can skew the blur in a particular direction. You can use this effect to make an image look as if it is in motion or to emphasize an animated image.

The CLSID for this effect is CLSID\_D2D1DirectionalBlur.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
-   [Optimization modes](#optimization-modes)
-   [Border modes](#border-modes)
-   [Output bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image



| Before                                                          |
|-----------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg)      |
| After                                                           |
| ![the image after the transform.](images/2-directionalblur.png) |



 


```C++
ComPtr<ID2D1Effect> directionalBlurEffect;
m_d2dContext->CreateEffect(CLSID_D2D1DirectionalBlur, &directionalBlurEffect);

directionalBlurEffect->SetInput(0, bitmap);
directionalBlurEffect->SetValue(D2D1_DIRECTIONALBLUR_PROP_STANDARD_DEVIATION, 7.0f);

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(directionalBlurEffect.Get());
m_d2dContext->EndDraw();
```



## Effect properties



| Display name and index enumeration                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StandardDeviation<br/> D2D1\_DIRECTIONALBLUR\_PROP\_STANDARD\_DEVIATION<br/> | The amount of blur to be applied to the image. You can compute the blur radius of the kernel by multiplying the standard deviation by 3. The units of both the standard deviation and blur radius are DIPs. A value of 0 DIPs disables this effect. The type is FLOAT.<br/> The default value is 3.0f.<br/>                                                                            |
| Angle<br/> D2D1\_DIRECTIONALBLUR\_PROP\_ANGLE<br/>                           | The angle of the blur relative to the x-axis, in the counterclockwise direction. The units are specified in degrees.<br/> The blur kernel is first generated using the same process as for the [Gaussian blur](gaussian-blur.md) effect. The kernel values are then transformed according to the blur angle.<br/> The type is FLOAT.<br/> The default value is 0.0f.<br/> |
| Optimization<br/> D2D1\_DIRECTIONALBLUR\_PROP\_OPTIMIZATION<br/>             | The optimization mode. See [Optimization modes](#optimization-modes) for more info.<br/> The type is D2D1\_DIRECTIONALBLUR\_OPTIMIZATION.<br/> The default value is D2D1\_DIRECTIONALBLUR\_OPTIMIZATION\_BALANCED. <br/>                                                                                                                                                         |
| BorderMode<br/> D2D1\_DIRECTIONALBLUR\_PROP\_BORDER\_MODE<br/>               | The mode used to calculate the border of the image, soft or hard. See [Border modes](#border-modes) for more info.<br/> The type is D2D1\_BORDER\_MODE.<br/> The default value is D2D1\_BORDER\_MODE\_SOFT.<br/>                                                                                                                                                                 |



 

## Optimization modes



| Name                                          | Description                                                                                                                           |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_DIRECTIONALBLUR\_OPTIMIZATION\_SPEED    | Applies internal optimizations such as pre-scaling at relatively small radii. Uses linear filtering.                                  |
| D2D1\_DIRECTIONALBLUR\_OPTIMIZATION\_BALANCED | Uses the same optimization thresholds as Speed mode, but uses trilinear filtering.                                                    |
| D2D1\_DIRECTIONALBLUR\_OPTIMIZATION\_QUALITY  | Only uses internal optimizations with large blur radii, where approximations are less likely to be visible. Uses trilinear filtering. |



 

## Border modes



| Name                     | Description                                                                                                                                                                                                              |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_BORDER\_MODE\_SOFT | The effect pads the image with transparent black pixels as it applies the blur kernel, resulting in a soft edge. <br/>                                                                                             |
| D2D1\_BORDER\_MODE\_HARD | The effect clamps the output to the size of the input image. When the effect applies the blur kernel, it extends the input image with a mirror-type border transform for samples outside of the input bounds.<br/> |



 

## Output bitmap

The size of the output bitmap increases based on the standard deviation, the angle of the effect, and the border mode. If the border mode is set to D2D1\_BORDER\_MODE\_SOFT the size of the output bitmap increases by the size of the blur kernel, represented in pixels. These equations can be used to calculate the size of the output bitmap.



| Requirement | Value |
|------------------------|-------------------------------------------------------------------|
| Output Bitmap Growth X | StandardDeviation (DIPs) \* 6 \* ((User DPI) / 96) \* cos(Angle)) |
| Output Bitmap Growth Y | StandardDeviation (DIPs) \* 6 \* ((User DPI) / 96) \* sin(Angle)) |



 

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

 

