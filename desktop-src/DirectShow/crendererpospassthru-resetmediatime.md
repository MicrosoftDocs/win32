---
Description: The ResetMediaTime method resets the cached time stamps to zero.
ms.assetid: 80dd2ae3-0a83-4017-8860-a089bef9a919
title: CRendererPosPassThru.ResetMediaTime method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CRendererPosPassThru.ResetMediaTime method

The `ResetMediaTime` method resets the cached time stamps to zero.

## Syntax


```C++
HRESULT ResetMediaTime();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The filter should call this method whenever the time stamps cached by the [**CRendererPosPassThru::RegisterMediaTime**](crendererpospassthru-registermediatime.md) method become invalid. Specifically, it should call this method in response to the [**IPin::EndFlush**](/windows/win32/Strmif/nf-strmif-ipin-endflush?branch=master) and [**IMediaFilter::Stop**](/windows/win32/Strmif/nf-strmif-imediafilter-stop?branch=master) methods.

After this method is called, the [**CRendererPosPassThru::GetMediaTime**](crendererpospassthru-getmediatime.md) method returns zero for the start and end times.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




