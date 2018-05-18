---
title: Hue to RGB Effect
description: Converts an HSL (Hue, Saturation, Lightness) or HSV (Hue, Saturation, Value) image to the RGB color space.
ms.assetid: '18e92535-9e89-bf8d-b8c3-a49b645fc417'
---

# Hue to RGB Effect

Converts an HSL (Hue, Saturation, Lightness) or HSV (Hue, Saturation, Value) image to the RGB color space.

HSL and HSV are two different models for representing an RGB color in a cylindrical color space. They are useful because they allow you to reason about a color using more intuitive concepts like hue and intensity versus combining red, green and blue values.

This effect passes through any input alpha values.

The CLSID for this effect is CLSID\_D2D1HueToRgb.

To reverse the behavior of this effect, use the [RGB to Hue effect](rgb-to-hue-effect.md).

-   [Sample Code](#sample-code)
-   [Effect Properties](#effect-properties)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Sample Code


```C++
ComPtr<ID2D1Effect> hueToRgbEffect;
m_d2dContext->CreateEffect(CLSID_D2D1HueToRgb, &amp;hueToRgbEffect);
 
hueToRgbEffect->SetInput(0, bitmap);
hueToRgbEffect->SetValue(D2D1_HUETORGB_INPUT_COLOR_SPACE, D2D1_HUETORGB_INPUT_COLOR_SPACE_HUE_SATURATION_LIGHTNESS);
 
m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(hueToRgbEffect.Get());
m_d2dContext->EndDraw();


```



## Effect Properties

The properties for the contrast effect are defined by the [**D2D1\_HUETORGB\_PROP**](d2d1-huetorgb-prop.md) enumeration.

## Requirements



|                          |                                                   |
|--------------------------|---------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 10 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects\_2.h                                  |
| Library                  | d2d1.lib, dxguid.lib                              |



 

## Related topics

<dl> <dt>

[**ID2D1Effect**](id2d1effect.md)
</dt> </dl>

 

 




