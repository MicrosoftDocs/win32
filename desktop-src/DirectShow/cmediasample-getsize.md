---
Description: The GetSize method retrieves the size of the buffer. This method implements the IMediaSampleGetSize method.
ms.assetid: 14562ef4-f554-4d5a-83d3-1a29abae08a4
title: CMediaSample.GetSize method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMediaSample.GetSize method

The `GetSize` method retrieves the size of the buffer. This method implements the [**IMediaSample::GetSize**](/windows/win32/Strmif/nf-strmif-imediasample-getsize?branch=master) method.

## Syntax


```C++
LONG GetSize();
```



## Parameters

This method has no parameters.

## Return value

Returns the size of the buffer, in bytes.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




