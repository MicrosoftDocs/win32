---
Description: The Stop method stops the filter. This method implements the IMediaFilterStop method.
ms.assetid: 68d77f9a-95a2-4a71-bbe1-28be76fbc538
title: CBaseFilter.Stop method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseFilter.Stop method

The `Stop` method stops the filter. This method implements the [**IMediaFilter::Stop**](/windows/win32/Strmif/nf-strmif-imediafilter-stop?branch=master) method.

## Syntax


```C++
HRESULT Stop();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the error.

## Remarks

This method calls the [**CBasePin::Inactive**](cbasepin-inactive.md) method on each of the filter's connected pins. It also sets the filter's state to State\_Stopped.

When the filter stops, it should reject samples from upstream, stop delivering samples downstream, shut down worker threads, and free any resources that it used for streaming.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




