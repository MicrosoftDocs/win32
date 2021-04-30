---
title: Displacement map effect
description: Use the displacement map effect to displace the pixels of the input image by the intensity values of a second input image.
ms.assetid: 07AA64B1-B570-428E-924F-D7DF3E4DB3F8
keywords:
- displacement map effect
ms.topic: article
ms.date: 05/31/2018
---

# Displacement map effect

Use the displacement map effect to displace the pixels of the input image by the intensity values of a second input image.

The CLSID for this effect is CLSID\_D2D1DisplacementMap.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
-   [Color channels](#color-channels)
-   [Output Bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image



| Before                                                           |
|------------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg)       |
| After                                                            |
| ![the image after the transform.](images/19-displacementmap.png) |



 


```C++
ComPtr<ID2D1Effect> displacementMapEffect;
m_d2dContext->CreateEffect(CLSID_D2D1DisplacementMap, &displacementMapEffect);

displacementMapEffect->SetInput(0, bitmap);
displacementMapEffect->SetValue(D2D1_DISPLACEMENTMAP_PROP_SCALE, 100.0f);

// The second input of the displacement effect determines how the input image is transformed.
// For this example, we will use a turbulence effect as the second input to randomly distort the image.
ComPtr<ID2D1Effect> turbulenceEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Turbulence, &turbulenceEffect);
displacementMapEffect->SetInputEffect(1, turbulenceEffect.Get());

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(displacementMapEffect.Get());
m_d2dContext->EndDraw();
```



The locations of the pixels in the output are determined using this formula:

C' (x,y)=C(x+ scale\*(XChannelSelector(Displacement Bitmap (x,y))-0.5),y+ scale\*(YChannelSelector(Displacement Bitmap (x,y))-0.5))

Where:<dl> *C  (x, y)* is the output pixel at (x, y).  
*C (x, y)* is the input pixel at (x, y).  
*Displacement Bitmap (x, y)* is the displacement pixel intensity at the specified coordinates  
*XChannelSelector* the intensity of the selected RGBA channel from the displacement bitmap that displaces the input image in the X direction.  
*YChannelSelector* the intensity of the selected RGBA channel from the displacement bitmap that displaces the input image in the Y direction.  
</dl>

The effect resamples the input image according to the scale property and the intensity of the displacement image. It uses bilinear interpolation if sampling from between pixels in the input image.

This effect works on straight and premultiplied alpha images. The output alpha format is the same as the input format.

## Effect properties



| Display name and index enumeration                                                   | Type and default value                                                   | Description                                                                                                                                                                               |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scale<br/> D2D1\_DISPLACEMENTMAP\_PROP\_SCALE<br/>                       | FLOAT<br/> 0.0f<br/>                                         | Multiplies the intensity of the selected channel from the displacement image. The higher you set this property, the more the effect displaces the pixels<br/>                       |
| XChannelSelect<br/> D2D1\_DISPLACEMENTMAP\_PROP\_X\_CHANNEL\_SELECT<br/> | D2D1\_CHANNEL\_SELECTOR<br/> D2D1\_CHANNEL\_SELECTOR\_A<br/> | The effect extracts the intensity from this color channel and uses it to spatially displace the image in the X direction. See [Color channels](#color-channels) for more info.<br/> |
| YChannelSelect<br/> D2D1\_DISPLACEMENTMAP\_PROP\_Y\_CHANNEL\_SELECT<br/> | D2D1\_CHANNEL\_SELECTOR<br/> D2D1\_CHANNEL\_SELECTOR\_A<br/> | The effect extracts the intensity from this color channel and uses it to spatially displace the image in the Y direction. See [Color channels](#color-channels) for more info.<br/> |



 

## Color channels



| Enumeration                | Description                                                      |
|----------------------------|------------------------------------------------------------------|
| D2D1\_CHANNEL\_SELECTOR\_R | The effect extracts the intensity output from the red channel.   |
| D2D1\_CHANNEL\_SELECTOR\_G | The effect extracts the intensity output from the green channel. |
| D2D1\_CHANNEL\_SELECTOR\_B | The effect extracts the intensity output from the blue channel.  |
| D2D1\_CHANNEL\_SELECTOR\_A | The effect extracts the intensity output from the alpha channel. |



 

## Output Bitmap

You can determine the maximum size of the output bitmap with these equations:

Output Bitmap? Pixels=(Input Bitmap Size?(DIPs)+Scale)\*(User DPI/96)

Output Bitmap<sub>y</sub> Pixels=(Input Bitmap Size<sub>y</sub>(DIPs) + Scale)\*(User DPI/96)

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

 

