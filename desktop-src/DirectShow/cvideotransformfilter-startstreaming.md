---
Description: The StartStreaming method is called when the filter switches to the paused state. This method overrides the CTransformFilter::StartStreaming method.
ms.assetid: fa05f88f-fed8-479d-b0b4-d9df982d51e7
title: CVideoTransformFilter.StartStreaming method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CVideoTransformFilter.StartStreaming method

The `StartStreaming` method is called when the filter switches to the paused state. This method overrides the [**CTransformFilter::StartStreaming**](ctransformfilter-startstreaming.md) method.

## Syntax


```C++
virtual HRESULT StartStreaming();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method resets all of the performance statistics.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Vtrans.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CVideoTransformFilter Class**](cvideotransformfilter.md)
</dt> </dl>

 

 




