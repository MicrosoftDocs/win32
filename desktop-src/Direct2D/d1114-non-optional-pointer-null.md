---
title: D1114 Non Optional Pointer NULL
ms.assetid: 62f0f247-8359-4f75-b3ce-195202d491d5
description: The parameter for interface::method is not optional. A NULL pointer was passed. This will cause Direct2D to crash.
keywords:
- D1114 Non Optional Pointer NULL Direct2D
topic_type:
- apiref
api_name:
- D1114 Non Optional Pointer NULL
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
ms.custom: "seodec18"
---

# D1114: Non Optional Pointer NULL

The parameter \[*parameter*\] for *interface*::*method* is not optional. A **NULL** pointer was passed. This will cause Direct2D to crash.

### Placeholders

<dl> <dt>

<span id="parameter"></span><span id="PARAMETER"></span>*parameter*
</dt> <dd>

The name of the parameter that contains the **NULL** pointer.

</dd> <dt>

<span id="interface"></span><span id="INTERFACE"></span>*interface*
</dt> <dd>

The name of the interface to which the *method* belongs.

</dd> <dt>

<span id="method"></span><span id="METHOD"></span>*method*
</dt> <dd>

The name of the method that received the invalid parameter.

</dd> </dl> 




 

### Examples

The following example shows that the [**FillGeometry**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-fillgeometry) method receives a NULL pointer for the non-optional *geometry* parameter.


```C++
        m_pRenderTarget->FillGeometry(NULL, m_pYellowGreenBrush);
```



This example produces the following debug message:

``` syntax
D2D DEBUG ERROR - The parameter [geometry] for ID2D1RenderTarget::FillGeometry is not optional. 
A NULL pointer was passed. This will cause Direct2D to crash.
```

## Possible Causes

A NULL pointer was passed for a non-optional parameter.

## Fixes

Ensure that a non-optional parameter does not have a NULL pointer.

 

 
