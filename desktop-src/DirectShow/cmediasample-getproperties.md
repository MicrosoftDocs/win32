---
description: The GetProperties method retrieves the properties of the sample. This method implements the IMediaSample2::GetProperties method.
ms.assetid: c2a6d611-9c17-41fb-bb6d-f5b17f1c9966
title: CMediaSample.GetProperties method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.GetProperties
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.GetProperties method

The `GetProperties` method retrieves the properties of the sample. This method implements the [**IMediaSample2::GetProperties**](/windows/desktop/api/Strmif/nf-strmif-imediasample2-getproperties) method.

## Syntax


```C++
HRESULT GetProperties(
   DWORD cbProperties,
   BYTE  *pbProperties
);
```



## Parameters

<dl> <dt>

*cbProperties* 
</dt> <dd>

Length of property data to retrieve, in bytes.

</dd> <dt>

*pbProperties* 
</dt> <dd>

Pointer to a buffer of size *cbProperties*.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                               | Description                           |
|-------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                   |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




