---
title: Posterize Effect
description: The posterize effect reduces the number of unique colors in an image.
ms.assetid: 'e6686998-1246-b3b7-6f4f-212568c3191c'
---

# Posterize Effect

The posterize effect reduces the number of unique colors in an image.

The CLSID for this effect is CLSID\_D2D1Posterize.

-   [Example Image](#example-image)
-   [Sample Code](#sample-code)
-   [Effect Properties](#effect-properties)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example Image

![example of effect output](images/posterize-effect.png)

## Sample Code


```C++
ComPtr<ID2D1Effect> posterizeEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Posterize, &amp;posterizeEffect);
 
posterizeEffect->SetInput(0, bitmap);
posterizeEffect->SetValue(D2D1_POSTERIZE_PROP_RED_VALUE_COUNT, 4);
posterizeEffect->SetValue(D2D1_POSTERIZE_PROP_GREEN_VALUE_COUNT, 4);
posterizeEffect->SetValue(D2D1_POSTERIZE_PROP_BLUE_VALUE_COUNT, 4);
 
m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(posterizeEffect.Get());
m_d2dContext->EndDraw();


```



## Effect Properties

The properties for the posterize effect are defined by the [**D2D1\_POSTERIZE\_PROP**](d2d1-posterize-prop.md) enumeration.

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

 

 




