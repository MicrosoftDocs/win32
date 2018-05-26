---
Description: The get\_AvgFrameRate method calculates and retrieves the average frame rate achieved.
ms.assetid: f36fc020-8c1a-491f-9f55-18265fde8bf8
title: CBaseVideoRenderer.get\_AvgFrameRate method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseVideoRenderer.get\_AvgFrameRate method

The `get_AvgFrameRate` method calculates and retrieves the average frame rate achieved.

## Syntax


```C++
HRESULT get_AvgFrameRate(
   int *piAvgFrameRate
);
```



## Parameters

<dl> <dt>

*piAvgFrameRate* 
</dt> <dd>

Pointer to the number of frames per second since streaming began.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the [**IQualProp::get\_AvgFrameRate**](/windows/win32/Amvideo/nf-amvideo-iqualprop-get_avgframerate?branch=master) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




