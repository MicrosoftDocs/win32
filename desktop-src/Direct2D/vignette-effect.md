---
title: Vignette Effect
description: Fades the input image at the edges to a user-set color.
ms.assetid: 34da221f-44a2-1d01-d88d-d7846b9770b9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Vignette Effect

Fades the input image at the edges to a user-set color.

The CLSID for this effect is CLSID\_D2D1Vignette.

-   [Example Image](#example-image)
-   [Sample Code](#sample-code)
-   [Effect Properties](#effect-properties)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example Image

![example of effect output](images/vignette-effect.png)

## Sample Code


```C++
ComPtr<ID2D1Effect> vignetteEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Vignette, &amp;vignetteEffect);
 
vignetteEffect->SetInput(0, bitmap);
vignetteEffect->SetValue(D2D1_VIGNETTE_PROP_COLOR, );
vignetteEffect->SetValue(D2D1_VIGNETTE_PROP_TRANSITION_SIZE, 0.1f);
vignetteEffect->SetValue(D2D1_VIGNETTE_PROP_STRENGTH, 0.5f);
 
m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(vignetteEffect.Get());
m_d2dContext->EndDraw();


```



## Effect Properties

The properties for the vignette effect are defined by the [**D2D1\_VIGNETTE\_PROP**](/windows/win32/d2d1effects_2/ne-d2d1effects_2-d2d1_vignette_prop?branch=master) enumeration.

## Requirements



|                          |                                                   |
|--------------------------|---------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 10 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects\_2.h                                  |
| Library                  | d2d1.lib, dxguid.lib                              |



 

## Related topics

<dl> <dt>

[**ID2D1Effect**](/windows/win32/D2d1_1/?branch=master)
</dt> </dl>

 

 




