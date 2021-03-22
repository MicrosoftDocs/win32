---
description: Constructor method.
ms.assetid: df5efbb3-6bce-4e30-b1b1-d69bf64fa87d
title: CBaseRenderer.CBaseRenderer constructor (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.CBaseRenderer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.CBaseRenderer constructor

Constructor method.

## Syntax


```C++
CBaseRenderer(
   REFCLSID  RenderClass,
   TCHAR     *pName,
   LPUNKNOWN pUnk,
   HRESULT   *phr,
   UINT      TimerResolution = 1
);
```



## Parameters

<dl> <dt>

*RenderClass* 
</dt> <dd>

Class identifier of the renderer.

</dd> <dt>

*pName* 
</dt> <dd>

Pointer to a string containing the name of the filter, for debugging purposes.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Receives an **HRESULT** value.

</dd> <dt>

*TimerResolution* 
</dt> <dd>

Timer resolution.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




