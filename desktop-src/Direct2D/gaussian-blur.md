---
title: Gaussian blur effect
description: Use the Gaussian blur effect to create a blur based on the Gaussian function over the entire input image.
ms.assetid: 6B8C9A0A-81D6-4CC2-B30B-995D4C2E59FC
keywords:
- Gaussian blur
ms.topic: article
ms.date: 05/31/2018
---

# Gaussian blur effect

Use the Gaussian blur effect to create a blur based on the Gaussian function over the entire input image.

You can use this effect to create glows and drop shadows and use the [composite](composite.md) effect to apply the result to the original image. It is useful in photo processing for filters like highlights and shadows. You can use the output of this effect for input into lighting effects, like the [Specular Lighting](specular-lighting.md) or [Diffuse Lighting](diffuse-lighting.md) effects, because the alpha channel is blurred, too and lighting effects use the alpha channel to determine surface geometry as a height map.

This effect is used by the built-in [Shadow](drop-shadow.md) effect.

The CLSID for this effect is CLSID\_D2D1GaussianBlur.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
-   [Optimization modes](#optimization-modes)
-   [Border modes](#border-modes)
-   [Output bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image



| Before                                                       |
|--------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg)   |
| After                                                        |
| ![the image after the transform.](images/1-gaussianblur.png) |



 


```C++
ComPtr<ID2D1Effect> gaussianBlurEffect;
m_d2dContext->CreateEffect(CLSID_D2D1GaussianBlur, &gaussianBlurEffect);

gaussianBlurEffect->SetInput(0, bitmap);
gaussianBlurEffect->SetValue(D2D1_GAUSSIANBLUR_PROP_STANDARD_DEVIATION, 3.0f);

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(gaussianBlurEffect.Get());
m_d2dContext->EndDraw();
```



## Effect properties



| Display name and index enumeration                                                    | Description                                                                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StandardDeviation<br/> D2D1\_GAUSSIANBLUR\_PROP\_STANDARD\_DEVIATION<br/> | The amount of blur to be applied to the image. You can compute the blur radius of the kernel by multiplying the standard deviation by 3. The units of both the standard deviation and blur radius are DIPs. A value of zero DIPs disables this effect entirely. The type is FLOAT.<br/> The default value is 3.0f.<br/> |
| Optimization<br/> D2D1\_GAUSSIANBLUR\_PROP\_OPTIMIZATION<br/>             | The optimization mode. See [Optimization modes](#optimization-modes) for more info. The type is D2D1\_GAUSSIANBLUR\_OPTIMIZATION.<br/> The default value is D2D1\_GAUSSIANBLUR\_OPTIMIZATION\_BALANCED.<br/>                                                                                                            |
| BorderMode<br/> D2D1\_GAUSSIANBLUR\_PROP\_BORDER\_MODE<br/>               | The mode used to calculate the border of the image, soft or hard. See [Border modes](#border-modes) for more info. <br/> The type is D2D1\_GAUSSIANBLUR\_BORDER\_MODE.<br/> The default value is D2D1\_BORDER\_MODE\_SOFT.<br/>                                                                                   |



 

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

The output of this effect can be larger than the input bitmap based on the blur radius and the border mode. If the border mode is set to D2D1\_BORDER\_MODE\_SOFT the s ize of the output bitmap increases by the size of the blur kernel, represented in pixels. This table provides an equation that you can use to compute the output bitmap.

`Output bitmap growth (X and Y) = StandardDeviation  (DIPs)*6*((User DPI)/96)`

So, if the image size increases by 10 pixels in each direction the upper left corner of the image will be located at (-5, -5) while the lower right will be at (105, 105).

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

 

