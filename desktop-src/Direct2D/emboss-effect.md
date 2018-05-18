---
title: Emboss Effect
description: Creates a grayscale version of the image that appears as though it has been stamped into paper.
ms.assetid: '74f63875-35cd-f335-62cd-410a953e53ea'
---

# Emboss Effect

Creates a grayscale version of the image that appears as though it has been stamped into paper.

The CLSID for this effect is CLSID\_D2D1Emboss.

-   [Example Image](#example-image)
-   [Sample Code](#sample-code)
-   [Effect Properties](#effect-properties)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example Image

![example of effect output](images/emboss-effect.png)

## Sample Code


```C++
ComPtr<ID2D1Effect> embossEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Emboss, &amp;embossEffect);
 
embossEffect->SetInput(0, bitmap);
embossEffect->SetValue(D2D1_EMBOSS_PROP_HEIGHT, 1.0f);
embossEffect->SetValue(D2D1_EMBOSS_PROP_DIRECTION, 0.0f);
 
m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(embossEffect.Get());
m_d2dContext->EndDraw();


```



## Effect Properties

The properties for the emboss effect are defined by the [**D2D1\_EMBOSS\_PROP**](d2d1-emboss-prop.md) enumeration.

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

 

 




