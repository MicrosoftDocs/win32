---
Description: The Pause method pauses the filter. This method implements the IMediaFilterPause method.
ms.assetid: 3e3afd14-1c92-4f2b-a367-e10caaeb3b63
title: CTransformFilter.Pause method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformFilter.Pause method

The `Pause` method pauses the filter. This method implements the [**IMediaFilter::Pause**](/windows/win32/Strmif/nf-strmif-imediafilter-pause?branch=master) method.

## Syntax


```C++
HRESULT Pause();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

This method calls the [**StartStreaming**](ctransformfilter-startstreaming.md) method. The **StartStreaming** method does nothing in the base class, but the derived class can override it.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




