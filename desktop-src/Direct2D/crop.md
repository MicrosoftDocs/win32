---
title: Crop effect
description: Use the crop effect to output a specified region of an image.
ms.assetid: DFB7DE20-F202-4E7F-AE63-94BF817B6E30
keywords:
- crop effect
ms.topic: article
ms.date: 05/31/2018
---

# Crop effect

Use the crop effect to output a specified region of an image.

The CLSID for this effect is CLSID\_D2D1Crop.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
-   [Output bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image



| Before                                                     |
|------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg) |
| After                                                      |
| ![the image after the transform.](images/8-crop.png)       |



 


```C++
ComPtr<ID2D1Effect> cropEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Crop, &cropEffect);

cropEffect->SetInput(0, bitmap);
cropEffect->SetValue(D2D1_CROP_PROP_RECT, D2D1::RectF(0.0f, 0.0f, 256.0f, 192.0f));

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(cropEffect.Get());
m_d2dContext->EndDraw();
```



## Effect properties




| Display name and index enumeration | Type and default value | Description | 
|------------------------------------|------------------------|-------------|
| Rect<br /> | D2D1_VECTOR_4F<br /> | The region to be cropped specified as a vector in the form (left, top, width, height).<br /> | 
| D2D1_CROP_PROP_RECT<br /> | {-FLT_MAX, -FLT_MAX, FLT_MAX, FLT_MAX}<br /> | The units are in DIPs. <br /><blockquote><p>[!Note]</p><p>The Rect will be truncated if it overlaps the edge boundaries of the input image.<br /></p></blockquote><br /> | 
| D2D1_CROP_PROP_BORDER_MODE<br /> | D2D1_BORDER_MODE <br /> D2D1_BORDER_MODE_SOFT <br /> | <ul><li>D2D1_BORDER_MODE_SOFT : If the crop rectangle falls on fractional pixel coordinates, the effect applies antialiasing which results in a soft edge.</li><li>D2D1_BORDER_MODE_HARD : If the crop rectangle falls on fractional pixel coordinates, the effect clamps which results in a hard edge.</li></ul> | 




 

## Output bitmap

The output of this effect is the size of the Rect property. The length and width are calc

ulated using the equations here: <dl> Output length in Pixels=(Rect.Right-Rect.Left)\*(User's DPI/96)  
Output height in pixels=(Rect.Bottom-Rect.Top)\*(User's DPI/96)  
</dl>

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

 

