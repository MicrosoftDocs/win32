---
Description: The Run method signals the streaming thread to run.
ms.assetid: 9aef7801-dcfb-4597-bccb-5ba19327b2d5
title: CSourceStream.Run method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSourceStream.Run method

The `Run` method signals the streaming thread to run.

## Syntax


```C++
HRESULT Run();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK or E\_UNEXPECTED.

## Remarks

In the base class, this method has the same effect as the [**CSourceStream::Pause**](csourcestream-pause.md) request, and is not used.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




