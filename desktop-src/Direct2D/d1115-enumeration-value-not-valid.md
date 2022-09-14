---
title: D1115 Enumeration Value Not Valid
description: D1115 Enumeration Value Not Valid
ms.assetid: cfffd2b8-a7d3-4a60-8586-81d8435936a6
keywords:
- D1115 Enumeration Value Not Valid Direct2D
topic_type:
- apiref
api_name:
- D1115 Enumeration Value Not Valid
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# D1115: Enumeration Value Not Valid

The parameter \[*parameter*\] with value \[*value*\] for *interface*::*method* is not a valid enumeration value.

## Placeholders

<dl> <dt>

<span id="parameter"></span><span id="PARAMETER"></span>*parameter*
</dt> <dd>

The name of the parameter that received the unexpected type.

</dd> <dt>

<span id="value"></span><span id="VALUE"></span>*value*
</dt> <dd>

The invalid enumeration value.

</dd> <dt>

<span id="interface"></span><span id="INTERFACE"></span>*interface*
</dt> <dd>

The name of the interface to which the *method* belongs.

</dd> <dt>

<span id="method"></span><span id="METHOD"></span>*method*
</dt> <dd>

The name of the method that received the invalid enumeration value.

</dd> </dl> 




 

## Examples

The following example specifies a [**D2D1\_RENDER\_TARGET\_TYPE**](/windows/desktop/api/d2d1/ne-d2d1-d2d1_render_target_type) enumeration value of 30, which is outside the expected range.


```C++
        hr = m_pD2DFactory->CreateHwndRenderTarget(
            D2D1::RenderTargetProperties((D2D1_RENDER_TARGET_TYPE)(30)),
            D2D1::HwndRenderTargetProperties(m_hwnd, size),
            &m_pRenderTarget
            );
```



This example produces the following debug message:

``` syntax
D2D DEBUG ERROR - The parameter [renderTargetProperties->type] with value [30] 
for ID2D1Factory::CreateHwndRenderTarget is not a valid enumeration value.
```

## Possible Causes

A parameter used an invalid enumeration value.

## Fixes

Use a valid enumeration value.

> [!Note]  
> The debug layer currently checks only the individual enumeration values; it does not check whether a bitwise combination is valid.

 

 

 
