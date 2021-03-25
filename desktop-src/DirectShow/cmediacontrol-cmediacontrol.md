---
description: Constructor method.
ms.assetid: 00549dfe-5dd4-445e-bad3-eb6bcfea8f5f
title: CMediaControl.CMediaControl constructor (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaControl.CMediaControl
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaControl.CMediaControl constructor

Constructor method.

## Syntax


```C++
CMediaControl(
   const TCHAR     *pName,
         LPUNKNOWN pUnk
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to the name of the object for debugging purposes.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object.

</dd> </dl>

## Remarks

Allocate the *pName* parameter in static memory. This name appears on the debugging terminal upon creation and deletion of the object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaControl Class**](cmediacontrol.md)
</dt> </dl>

 

 




