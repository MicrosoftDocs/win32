---
Description: The SetSyncPoint method specifies whether the beginning of this sample is a synchronization point. This method implements the IMediaSampleSetSyncPoint method.
ms.assetid: 48fc5145-7cce-4e76-860d-45a0d5b43b67
title: CMediaSample.SetSyncPoint method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMediaSample.SetSyncPoint method

The `SetSyncPoint` method specifies whether the beginning of this sample is a synchronization point. This method implements the [**IMediaSample::SetSyncPoint**](/windows/win32/Strmif/nf-strmif-imediasample-setsyncpoint?branch=master) method.

## Syntax


```C++
HRESULT SetSyncPoint(
   BOOL bIsSyncPoint
);
```



## Parameters

<dl> <dt>

*bIsSyncPoint* 
</dt> <dd>

Boolean value that specifies whether this is a synchronization point. If **TRUE**, this is a synchronization point.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method updates the [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable, which specifies the synchronization-point property.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




