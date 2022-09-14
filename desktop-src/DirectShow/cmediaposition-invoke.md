---
description: The Invoke method provides access to properties and methods exposed by the object.
ms.assetid: 3c03751d-239b-4cc5-bfab-8d1aed1074b8
title: CMediaPosition.Invoke method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaPosition.Invoke
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaPosition.Invoke method

The `Invoke` method provides access to properties and methods exposed by the object.

## Syntax


```C++
HRESULT Invoke(
   DISPID     dispidMember,
   REFIID     riid,
   LCID       lcid,
   WORD       wFlags,
   DISPPARAMS *pdispparams,
   VARIANT    *pvarResult,
   EXCEPINFO  *pexcepinfo,
   UINT       *puArgErr
);
```



## Parameters

<dl> <dt>

*dispidMember* 
</dt> <dd>

Identifier of the member. Use [**CMediaPosition::GetIDsOfNames**](cmediaposition-getidsofnames.md) to obtain the dispatch identifier.

</dd> <dt>

*riid* 
</dt> <dd>

Reserved for future use. Must be IID\_NULL.

</dd> <dt>

*lcid* 
</dt> <dd>

Locale context in which to interpret arguments.

</dd> <dt>

*wFlags* 
</dt> <dd>

Flags describing the context of the call.

</dd> <dt>

*pdispparams* 
</dt> <dd>

Pointer to a **DIPPARAMS** structure that contains the arguments.

</dd> <dt>

*pvarResult* 
</dt> <dd>

Pointer to a **VARIANT** that receives the result, or **NULL** if the caller expects no result.

</dd> <dt>

*pexcepinfo* 
</dt> <dd>

Pointer to a structure that receives exception information.

</dd> <dt>

*puArgErr* 
</dt> <dd>

Pointer to a variable that receives the index of the first argument that causes an error.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                              | Description                                      |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | Success.<br/>                              |
| <dl> <dt>**DISP\_E\_UNKNOWNINTERFACE**</dt> </dl> | The *riid* parameter is not IID\_NULL<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaPosition Class**](cmediaposition.md)
</dt> </dl>

 

 




