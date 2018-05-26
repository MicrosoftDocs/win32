---
title: Exposure Effect
description: Increase or decreases the exposure of the image.
ms.assetid: d384f539-5c19-53c7-e52b-bf833e221449
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Exposure Effect

Increase or decreases the exposure of the image.

The CLSID for this effect is CLSID\_D2D1Exposure.

-   [Example Image](#example-image)
-   [Sample Code](#sample-code)
-   [Effect Properties](#effect-properties)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example Image

![example of effect output](images/exposure-effect.png)

## Sample Code


```C++
ComPtr<ID2D1Effect> exposureEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Exposure, &amp;exposureEffect);
 
exposureEffect->SetInput(0, bitmap);
exposureEffect->SetValue(D2D1_EXPOSURE_PROP_EXPOSURE_VALUE, 1.0f);
 
m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(exposureEffect.Get());
m_d2dContext->EndDraw();


```



## Effect Properties

The properties for the exposure effect are defined by the [**D2D1\_EXPOSURE\_PROP**](/windows/win32/d2d1effects_2/ne-d2d1effects_2-d2d1_exposure_prop?branch=master) enumeration.

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

 

 




