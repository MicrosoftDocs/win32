---
Description: Stops the filter. This method implements the IMediaFilterStop method.
ms.assetid: e95537d6-b3ec-49a4-aa28-333d69eff3bb
title: CTransformFilter.Stop method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformFilter.Stop method

Stops the filter. This method implements the [**IMediaFilter::Stop**](/windows/win32/Strmif/nf-strmif-imediafilter-stop?branch=master) method.

## Syntax


```C++
HRESULT Stop();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

After this method decommits both allocators, it calls the [**StopStreaming**](ctransformfilter-stopstreaming.md) method. The **StopStreaming** method does nothing in the base class, but the derived class can override it.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




