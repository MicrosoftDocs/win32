---
description: The StopAt method informs the pin when to stop delivering data. This method implements the IAMStreamControl::StopAt method.
ms.assetid: cc9f0fdc-253b-4feb-95ce-56ebc575a49b
title: CBaseStreamControl.StopAt method (Strmctl.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseStreamControl.StopAt
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseStreamControl.StopAt method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `StopAt` method informs the pin when to stop delivering data. This method implements the [**IAMStreamControl::StopAt**](/windows/desktop/api/Strmif/nf-strmif-iamstreamcontrol-stopat) method.

## Syntax


```C++
HRESULT StopAt(
   const REFERENCE_TIME *ptStop = NULL,
         BOOL           bSendExtra = FALSE,
         DWORD          dwCookie = 0
);
```



## Parameters

<dl> <dt>

*ptStop* 
</dt> <dd>

Pointer to a [**REFERENCE\_TIME**](reference-time.md) value that specifies when the pin should stop delivering data.

</dd> <dt>

*bSendExtra* 
</dt> <dd>

Specifies a Boolean value that indicates whether to send an extra sample after the scheduled stop time. If **TRUE**, the pin sends one extra sample.

</dd> <dt>

*dwCookie* 
</dt> <dd>

Specifies a value to send along with the start notification.

</dd> </dl>

## Return value

Returns S\_OK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Strmctl.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseStreamControl Class**](cbasestreamcontrol.md)
</dt> </dl>

 

 




