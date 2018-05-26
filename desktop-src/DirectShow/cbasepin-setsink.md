---
Description: The SetSink method sets an external quality manager. This method implements the IQualityControlSetSink method.
ms.assetid: 714e6839-954e-4231-824d-72a45f270f59
title: CBasePin.SetSink method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePin.SetSink method

The `SetSink` method sets an external quality manager. This method implements the [**IQualityControl::SetSink**](/windows/win32/Strmif/nf-strmif-iqualitycontrol-setsink?branch=master) method.

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

Pointer to the [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master) interface of the quality manager.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

Call this method to redirect quality-control messages to an external quality manager. For more information, see [Quality-Control Management](quality-control-management.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




