---
title: D1106 Resource Is Wrong Type
ms.assetid: 79a618cb-1d05-4895-b801-7663890b456a
description: The given resource is not of an expected type.
keywords:
- D1106 Resource Is Wrong Type Direct2D
topic_type:
- apiref
api_name:
- D1106 Resource Is Wrong Type
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
ms.custom: "seodec18"
---

# D1106: Resource Is Wrong Type

The given resource \[*resource*\] is not of an expected type.

## Placeholders

<dl> <dt>

<span id="resource"></span><span id="RESOURCE"></span>*resource*
</dt> <dd>

The address of the resource.

</dd> </dl> 




 

## Possible Causes

An interface was improperly cast and used as a parameter for a method or function.

## Examples

The following example passes an [**ID2D1SolidColorBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1solidcolorbrush) when an [**ID2D1Geometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1geometry) is expected.


```C++
        m_pRenderTarget->FillGeometry(
            (ID2D1Geometry*)m_pYellowGreenBrush,
            m_pYellowGreenBrush
            );
```



This example produces the following debug message:

``` syntax
DEBUG ERROR - The given resource[003A2C98] is not of an expected type
```

## Fixes

Use the type required by the method.

 

 
