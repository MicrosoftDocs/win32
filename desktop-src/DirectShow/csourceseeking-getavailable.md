---
description: CSourceSeeking.GetAvailable method - The GetAvailable method retrieves the range of times in which seeking is efficient. This method implements the IMediaSeeking::GetAvailable method.
ms.assetid: 2a7b6cdb-47c3-4aeb-89ff-ea968c6a809b
title: CSourceSeeking.GetAvailable method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.GetAvailable
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CSourceSeeking.GetAvailable method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetAvailable` method retrieves the range of times in which seeking is efficient. This method implements the [**IMediaSeeking::GetAvailable**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getavailable) method.

## Syntax


```C++
HRESULT GetAvailable(
   LONGLONG *pEarliest,
   LONGLONG *pLatest
);
```



## Parameters

<dl> <dt>

*pEarliest* 
</dt> <dd>

Pointer to a variable that receives the earliest time for efficient seeking. The variable is set to zero.

</dd> <dt>

*pLatest* 
</dt> <dd>

Pointer to a variable that receives the latest time for efficient seeking. The variable is set to the value of the [**CSourceSeeking::m\_rtDuration**](csourceseeking-m-rtduration.md) member variable.

</dd> </dl>

## Return value

Returns S\_OK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




