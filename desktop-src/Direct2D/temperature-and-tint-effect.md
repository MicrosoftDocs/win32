---
title: Temperature and Tint Effect
description: .
ms.assetid: 8df72105-26ea-2dea-a4de-ef06902b7e0b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Temperature and Tint Effect

The CLSID for this effect is CLSID\_D2D1TemperatureTint.

-   [Sample Code](#sample-code)
-   [Effect Properties](#effect-properties)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Sample Code


```C++
ComPtr<ID2D1Effect> temperatureTintEffect;
m_d2dContext->CreateEffect(CLSID_D2D1TemperatureTint, &amp;temperatureTintEffect);
 
temperatureTintEffect->SetInput(0, bitmap);
temperatureTintEffect->SetValue(D2D1_TEMPERATUREANDTINT_PROP_TEMPERATURE, 0.5f);
temperatureTintEffect->SetValue(D2D1_TEMPERATUREANDTINT_PROP_TINT, 0.5f);
 
m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(temperatureTintEffect.Get());
m_d2dContext->EndDraw();


```



## Effect Properties

The properties for the temperature and tint effect are defined by the [**D2D1\_TEMPERATUREANDTINT\_PROP**](/windows/win32/d2d1effects_2/ne-d2d1effects_2-d2d1_temperatureandtint_prop?branch=master) enumeration.

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

 

 




