---
description: The GetNextTrans2 method retrieves the first transition that appears at the specified time or later. This method is equivalent to IAMTimelineTransable::GetNextTrans, but takes a REFTIME value.
ms.assetid: e6910e94-f289-4a5d-9976-1e8f7373c882
title: IAMTimelineTransable::GetNextTrans2 method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTransable.GetNextTrans2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineTransable::GetNextTrans2 method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetNextTrans2` method retrieves the first transition that appears at the specified time or later. This method is equivalent to [**IAMTimelineTransable::GetNextTrans**](iamtimelinetransable-getnexttrans.md), but takes a [**REFTIME**](reftime.md) value.

## Syntax


```C++
HRESULT GetNextTrans2(
  [out] IAMTimelineObj **ppTrans,
        REFTIME        *pInOut
);
```



## Parameters

<dl> <dt>

*ppTrans* \[out\]
</dt> <dd>

Receives a pointer to the transition object's [**IAMTimelineObj**](iamtimelineobj.md) interface.

</dd> <dt>

*pInOut* 
</dt> <dd>

Pointer to a variable that specifies the time in seconds. On input, this value specifies the time from which to find the transition. On output, if a transition is retrieved, this value is set to the stop time of the transition.

</dd> </dl>

## Return value

Returns S\_OK if the method retrieves a transition, or S\_FALSE if it does not find a transition. Otherwise, returns an **HRESULT** value indicating the cause of the failure.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineTransable Interface**](iamtimelinetransable.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




