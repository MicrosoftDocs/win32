---
description: The GetSize method retrieves the size of the buffer. This method implements the IMediaSample::GetSize method.
ms.assetid: 14562ef4-f554-4d5a-83d3-1a29abae08a4
title: CMediaSample.GetSize method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.GetSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.GetSize method

The `GetSize` method retrieves the size of the buffer. This method implements the [**IMediaSample::GetSize**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getsize) method.

## Syntax


```C++
LONG GetSize();
```



## Parameters

This method has no parameters.

## Return value

Returns the size of the buffer, in bytes.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




