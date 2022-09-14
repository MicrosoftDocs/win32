---
description: The QueryId method retrieves the pin identifier. This method overrides the CBasePin::QueryId method.
ms.assetid: 9543234c-5349-49d0-b410-1c461ee4eabe
title: CRendererInputPin.QueryId method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererInputPin.QueryId
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRendererInputPin.QueryId method

The `QueryId` method retrieves the pin identifier. This method overrides the [**CBasePin::QueryId**](cbasepin-queryid.md) method.

## Syntax


```C++
HRESULT QueryId(
   LPWSTR *Id
);
```



## Parameters

<dl> <dt>

*Id* 
</dt> <dd>

Receives a string containing the pin identifier.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                   | Description                          |
|-----------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory<br/>       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument<br/> |



 

## Remarks

This method allocates the wide-character string "In" and assigns it to the *Id* parameter. The caller must free the allocated memory, using the **CoTaskMemFree** function.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




