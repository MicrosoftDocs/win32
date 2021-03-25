---
description: Retrieves a type-information object, which can retrieve the type information for an interface.
ms.assetid: d54042d5-e9d3-415c-b90d-1fe7d38164f5
title: CMediaEvent.GetTypeInfo method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaEvent.GetTypeInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaEvent.GetTypeInfo method

Retrieves a type-information object, which can retrieve the type information for an interface.

## Syntax


```C++
HRESULT GetTypeInfo(
   UINT      itinfo,
   LCID      lcid,
   ITypeInfo **pptinfo
);
```



## Parameters

<dl> <dt>

*itinfo* 
</dt> <dd>

Type information to return. Pass zero to retrieve type information for the **IDispatch** implementation.

</dd> <dt>

*lcid* 
</dt> <dd>

Locale ID for the type information. For classes that support localized member names, an object might be able to return different type information for different languages. For classes that do not support localized member names, this parameter can be ignored.

</dd> <dt>

*pptinfo* 
</dt> <dd>

Address of a pointer to the type-information object requested.

</dd> </dl>

## Return value

Returns an E\_POINTER if *pptinfo* is invalid. Returns TYPE\_E\_ELEMENTNOTFOUND if *itinfo* is not zero. Returns S\_OK if is successful. Otherwise, returns an **HRESULT** from one of the calls to retrieve the type.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaEvent Class**](cmediaevent.md)
</dt> </dl>

 

 




