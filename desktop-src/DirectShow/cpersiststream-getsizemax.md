---
description: Retrieves the maximum byte size needed for the current stream, including the version number.
ms.assetid: 55ea4568-5ca4-4139-8def-bef20071835d
title: CPersistStream.GetSizeMax method (Pstream.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream.GetSizeMax
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPersistStream.GetSizeMax method

Retrieves the maximum byte size needed for the current stream, including the version number.

## Syntax


```C++
HRESULT GetSizeMax(
   ULARGE_INTEGER *pcbSize
);
```



## Parameters

<dl> <dt>

*pcbSize* 
</dt> <dd>

Pointer to the size in bytes needed to save this stream, including the version number.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the **IPersistStream::GetSizeMax** method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




