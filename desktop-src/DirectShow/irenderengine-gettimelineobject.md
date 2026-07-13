---
description: The GetTimelineObject method retrieves the timeline that the render engine is currently using.
ms.assetid: 74398f85-07b2-42fa-bb4f-a1e7e1669e3f
title: IRenderEngine::GetTimelineObject method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRenderEngine.GetTimelineObject
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IRenderEngine::GetTimelineObject method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetTimelineObject` method retrieves the timeline that the render engine is currently using.

## Syntax


```C++
HRESULT GetTimelineObject(
  [out] IAMTimeline **ppTimeline
);
```



## Parameters

<dl> <dt>

*ppTimeline* \[out\]
</dt> <dd>

Receives a pointer to the timeline's [**IAMTimeline**](iamtimeline.md) interface. It receives the value **NULL** if there is no timeline.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                            | Description                                    |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Success.<br/>                            |
| <dl> <dt>**E\_POINTER**</dt> </dl>              | Invalid pointer.<br/>                    |
| <dl> <dt>**E\_MUST\_INIT\_RENDERER**</dt> </dl> | Render engine failed to initialize.<br/> |



 

## Remarks

On return, if the value of *\*ppTimeline* is non-**NULL**, the **IAMTimeline** interface has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

[**IRenderEngine Interface**](irenderengine.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




