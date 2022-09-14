---
description: The SetSyncPoint method specifies whether the beginning of this sample is a synchronization point. This method implements the IMediaSample::SetSyncPoint method.
ms.assetid: 48fc5145-7cce-4e76-860d-45a0d5b43b67
title: CMediaSample.SetSyncPoint method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.SetSyncPoint
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.SetSyncPoint method

The `SetSyncPoint` method specifies whether the beginning of this sample is a synchronization point. This method implements the [**IMediaSample::SetSyncPoint**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setsyncpoint) method.

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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




