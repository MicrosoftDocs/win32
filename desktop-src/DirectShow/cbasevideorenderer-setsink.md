---
Description: The SetSink method sets the IQualityControl object that will receive quality messages.
ms.assetid: f5789781-1871-4fea-9d1f-bd1a21b70439
title: CBaseVideoRenderer.SetSink method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseVideoRenderer.SetSink method

The `SetSink` method sets the [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master) object that will receive quality messages.

## Syntax


```C++
HRESULT SetSink(
   IQualityControl *piqc
);
```



## Parameters

<dl> <dt>

*piqc* 
</dt> <dd>

Pointer to the [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master) object to which the notifications should be sent.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the [**IQualityControl::SetSink**](/windows/win32/Strmif/nf-strmif-iqualitycontrol-setsink?branch=master) method on the video renderer.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




