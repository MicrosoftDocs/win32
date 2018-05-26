---
Description: The SetDiscontinuity method specifies whether this sample represents a break in the data stream. This method implements the IMediaSampleSetDiscontinuity method.
ms.assetid: 29072130-1ec7-4b5b-8a43-5308b1365527
title: CMediaSample.SetDiscontinuity method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMediaSample.SetDiscontinuity method

The `SetDiscontinuity` method specifies whether this sample represents a break in the data stream. This method implements the [**IMediaSample::SetDiscontinuity**](/windows/win32/Strmif/nf-strmif-imediasample-setdiscontinuity?branch=master) method.

## Syntax


```C++
HRESULT SetDiscontinuity(
   BOOL bDiscont
);
```



## Parameters

<dl> <dt>

*bDiscont* 
</dt> <dd>

Boolean value that specifies whether this sample is a discontinuity. If **TRUE**, the media sample is discontinuous with the previous sample.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method updates the [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable, which specifies the discontinuity property.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




