---
description: The CheckMediaType method determines if the pin accepts a specific media type. This method implements the pure virtual CBasePin::CheckMediaType method.
ms.assetid: 3db7c74c-a6aa-4b49-b2a5-9bf8db35fd7e
title: CSourceStream.CheckMediaType method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.CheckMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.CheckMediaType method

The `CheckMediaType` method determines if the pin accepts a specific media type. This method implements the pure virtual [**CBasePin::CheckMediaType**](cbasepin-checkmediatype.md) method.

## Syntax


```C++
virtual HRESULT CheckMediaType(
   const CMediaType *pMediaType
);
```



## Parameters

<dl> <dt>

*pMediaType* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that contains the proposed media type.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                            | Description                                          |
|----------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | This pin supports this media type.<br/>        |
| <dl> <dt>**E\_FAIL**</dt> </dl> | The pin does not support this media type.<br/> |



 

## Remarks

By default, the pin supports a single media type. This method retrieves the supported type by calling the single-parameter version of the [**CSourceStream::GetMediaType**](csourcestream-getmediatype.md) method, and compares it to the proposed type. If your pin supports more than one media type, override this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




