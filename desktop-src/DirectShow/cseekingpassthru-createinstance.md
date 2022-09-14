---
description: The CreateInstance method creates an instance of the object. This method supports creation of the object through a class factory. For more information, see CFactoryTemplate.
ms.assetid: 88dfa933-6fa1-4b57-8b0d-579233fa960c
title: CSeekingPassThru.CreateInstance method (Seekpt.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSeekingPassThru.CreateInstance
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSeekingPassThru.CreateInstance method

The `CreateInstance` method creates an instance of the object. This method supports creation of the object through a class factory. For more information, see [**CFactoryTemplate**](cfactorytemplate.md).

## Syntax


```C++
static CUnknown* CreateInstance(
   LPUNKNOWN pUnk,
   HRESULT   *phr
);
```



## Parameters

<dl> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. Ignored.

</dd> </dl>

## Return value

Returns a pointer to a new **CSeekingPassThru** object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Seekpt.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSeekingPassThru Class**](cseekingpassthru.md)
</dt> </dl>

 

 




