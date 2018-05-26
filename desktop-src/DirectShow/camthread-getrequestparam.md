---
Description: The GetRequestParam method retrieves the latest request.
ms.assetid: f5bf4935-29ea-45b9-a57e-9fdcd9cde20a
title: CAMThread.GetRequestParam method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CAMThread.GetRequestParam method

The `GetRequestParam` method retrieves the latest request.

## Syntax


```C++
DWORD GetRequestParam() const;
```



## Parameters

This method has no parameters.

## Return value

Returns the value of the parameter that was passed most recently to the [**CAMThread::CallWorker**](camthread-callworker.md) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




