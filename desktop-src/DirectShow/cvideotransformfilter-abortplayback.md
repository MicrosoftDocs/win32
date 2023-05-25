---
description: The AbortPlayback method is used to signal a streaming error. It sends an EC\_ERRORABORT event to the Filter Graph Manager, and sends an end-of-stream notification downstream.
ms.assetid: b48ec72f-d220-4b27-98fc-88eaa4f663eb
title: CVideoTransformFilter.AbortPlayback method (Vtrans.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CVideoTransformFilter.AbortPlayback
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CVideoTransformFilter.AbortPlayback method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `AbortPlayback` method is used to signal a streaming error. It sends an [**EC\_ERRORABORT**](ec-errorabort.md) event to the Filter Graph Manager, and sends an end-of-stream notification downstream.

## Syntax


```C++
HRESULT AbortPlayback(
   HRESULT hr
);
```



## Parameters

<dl> <dt>

*hr* 
</dt> <dd>

**HRESULT** value of the operation that failed. This value is used as the first event parameter for the EC\_ERRORABORT event.

</dd> </dl>

## Return value

Returns the value of the *hr* parameter.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Vtrans.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CVideoTransformFilter Class**](cvideotransformfilter.md)
</dt> </dl>

 

 




