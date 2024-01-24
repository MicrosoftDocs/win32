---
description: The SetStartStop2 method sets the object's start and stop times, relative to the object's parent. This method is equivalent to IAMTimelineObj::SetStartStop, but takes REFTIME values.
ms.assetid: 0fc79c82-d8e1-4b87-9e59-6d9e6ca614f3
title: IAMTimelineObj::SetStartStop2 method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.SetStartStop2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineObj::SetStartStop2 method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetStartStop2` method sets the object's start and stop times, relative to the object's parent. This method is equivalent to [**IAMTimelineObj::SetStartStop**](iamtimelineobj-setstartstop.md), but takes [**REFTIME**](reftime.md) values.

## Syntax


```C++
HRESULT SetStartStop2(
   REFTIME Start,
   REFTIME Stop
);
```



## Parameters

<dl> <dt>

*Start* 
</dt> <dd>

New start time, in seconds, or –1 to keep the existing start time.

</dd> <dt>

*Stop* 
</dt> <dd>

New stop time, in seconds, or –1 to keep the existing stop time.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                  | Description                  |
|----------------------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid argument.<br/> |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>    | Not implemented.<br/>  |



 

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

[**IAMTimelineObj Interface**](iamtimelineobj.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




