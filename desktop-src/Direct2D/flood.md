---
title: Flood effect
description: Use the flood effect to generate a bitmap based on the specified color and alpha value. You can use this effect when you want a specific color as an input for an effect, like a background color.
ms.assetid: F80A6DC0-E18C-4324-BE4A-FE40C5722988
keywords:
- flood effect
ms.topic: article
ms.date: 05/31/2018
---

# Flood effect

Use the flood effect to generate a bitmap based on the specified color and alpha value. You can use this effect when you want a specific color as an input for an effect, like a background color.

> [!Note]  
> The effect passes along the specified color value as specified. You must manually pre-multiply the values if you plan to pass the output to effects that expect a pre-multiplied input.

 

The CLSID for this effect is CLSID\_D2D1Flood.

The flood effect has no input image.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
-   [Output bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image

![example image of the flood effect outputting green.](images/20-flood.png)


```C++
ComPtr<ID2D1Effect> floodEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Flood, &floodEffect);

floodEffect->SetValue(D2D1_FLOOD_PROP_COLOR, D2D1::Vector4F(0.0f, 1.0f, 0.0f, 1.0f));

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(floodEffect.Get());
m_d2dContext->EndDraw();
```



## Effect properties



| Display name and index enumeration                   | Description                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Color<br/> D2D1\_FLOOD\_PROP\_COLOR<br/> | The color and opacity of the bitmap. This property is a D2D1\_VECTOR\_4F. The individual values for each channel are of type FLOAT, unbounded and unitless. The effect doesn't modify the values for the channels.<br/> The RGBA values for each channel range from 0 to 1.<br/> The type is D2D1\_VECTOR\_4F.<br/> The default value is {0.0f, 0.0f, 0.0f, 1.0f}.<br/> |



 

## Output bitmap

This effect generates a logically infinite sized bitmap.

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

 

