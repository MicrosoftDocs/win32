---
description: CBaseDispatch.GetTypeInfoCount method - The GetTypeInfoCount method retrieves the number of type information interfaces the object provides.
ms.assetid: e09e6f6c-6ac8-4ce1-8ce1-ee5374d54183
title: CBaseDispatch.GetTypeInfoCount method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseDispatch.GetTypeInfoCount
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseDispatch.GetTypeInfoCount method

The `GetTypeInfoCount` method retrieves the number of type information interfaces the object provides.

## Syntax


```C++
HRESULT GetTypeInfoCount(
   UINT *pctinfo
);
```



## Parameters

<dl> <dt>

*pctinfo* 
</dt> <dd>

Pointer to a variable that receives the number of type-information interfaces provided by the object. When the method returns, the value is 1.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                               | Description                           |
|-------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                   |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseDispatch Class**](cbasedispatch.md)
</dt> </dl>

 

 




