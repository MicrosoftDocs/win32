---
title: Tile effect
description: Use the tile effect to repeat the specified region of the image.
ms.assetid: C7505DBF-5F79-4407-84C4-634EA7EC06B7
keywords:
- tile effect
ms.topic: article
ms.date: 05/31/2018
---

# Tile effect

Use the tile effect to repeat the specified region of the image.

The CLSID for this effect is CLSID\_D2D1Tile.

## Example image



| Before                                                     |
|------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg) |
| After                                                      |
| ![the image after the transform.](images/9-tile.png)       |



 


```C++
ComPtr<ID2D1Effect> tileEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Tile, &tileEffect);

tileEffect->SetInput(0, bitmap);

tileEffect->SetValue(D2D1_TILE_PROP_RECT, D2D1::RectF(0.0f, 0.0f, 256.0f, 192.0f));

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(tileEffect.Get());
m_d2dContext->EndDraw();
```



## Effect properties



| Display name and index enumeration                | Type and default value                                              | Description                                                                                                                                        |
|---------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Rect<br/> D2D1\_TILE\_PROP\_RECT<br/> | D2D1\_VECTOR\_4F<br/> {0.0f, 0.0f, 100.0f, 100.0f}<br/> | The region of the image to be tiled. This property is a D2D1\_VECTOR\_4F defined as: (left, top, right, bottom). The units are in DIPs.<br/> |



 

## Output bitmap

This effect generates a logically infinite sized bitmap.

You can tile an image and output a certain size without any additional effects by setting the size when you call [**ID2D1DeviceContext::DrawImage**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1devicecontext-drawimage(id2d1image_constd2d1_point_2f_constd2d1_rect_f_d2d1_interpolation_mode_d2d1_composite_mode)).

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

 

