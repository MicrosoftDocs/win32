---
Description: The AlterQuality method notifies the filter that a quality change is requested. This method overrides the CTransformFilterAlterQuality method.
ms.assetid: 9a1d1379-8557-4b33-ab49-b5c6a684f685
title: CVideoTransformFilter.AlterQuality method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CVideoTransformFilter.AlterQuality method

The `AlterQuality` method notifies the filter that a quality change is requested. This method overrides the [**CTransformFilter::AlterQuality**](ctransformfilter-alterquality.md) method.

## Syntax


```C++
virtual HRESULT AlterQuality(
   Quality q
);
```



## Parameters

<dl> <dt>

*q* 
</dt> <dd>

[**Quality**](/windows/win32/strmif/ns-strmif-tagquality?branch=master) structure that contains the quality control message.

</dd> </dl>

## Return value

Returns E\_FAIL.

## Remarks

This method is called when the output pin receives a quality message (through the [**IQualityControl::Notify**](/windows/win32/Strmif/nf-strmif-iqualitycontrol-notify?branch=master) method).

The lateness value from *q* is stored in the **m\_itrLate** member variable. The return value of E\_FAIL indicates that the renderer should catch up by dropping frames, although the **CVideoTransformFilter** class will also drop frames under the right conditions.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Vtrans.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CVideoTransformFilter Class**](cvideotransformfilter.md)
</dt> <dt>

[**CVideoTransformFilter::ShouldSkipFrame**](cvideotransformfilter-shouldskipframe.md)
</dt> </dl>

 

 




