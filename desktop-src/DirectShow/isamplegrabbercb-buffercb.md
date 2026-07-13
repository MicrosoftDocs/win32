---
description: The BufferCB method is a callback method that receives a pointer to the sample buffer.
ms.assetid: 9ee16dd6-8d05-4a9a-84c3-1b3bb95eaa04
title: ISampleGrabberCB::BufferCB method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISampleGrabberCB.BufferCB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# ISampleGrabberCB::BufferCB method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **BufferCB** method is a callback method that receives a pointer to the sample buffer.

## Syntax


```C++
HRESULT BufferCB(
   double SampleTime,
   BYTE   *pBuffer,
   long   BufferLen
);
```



## Parameters

<dl> <dt>

*SampleTime* 
</dt> <dd>

Starting time of the sample, in seconds.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to a buffer that contains the sample data. The format of the data depends on the media type of the Sample Grabber's input pin. To get the media type, call [**ISampleGrabber::GetConnectedMediaType**](isamplegrabber-getconnectedmediatype.md).

</dd> <dt>

*BufferLen* 
</dt> <dd>

Length of the buffer pointed to by *pBuffer*, in bytes.

</dd> </dl>

## Return value

Returns S\_OK if successful, or an **HRESULT** error code otherwise.

## Remarks

This callback method receives a pointer to the data in the most recent media sample.

> [!Note]  
> This method receives a pointer to the original sample data, not a copy. The original documentation incorrectly stated that *pBuffer* contains a copy of the data.

 

To set up the callback, call [**ISampleGrabber::SetCallback**](isamplegrabber-setcallback.md).

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

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**ISampleGrabberCB Interface**](isamplegrabbercb.md)
</dt> </dl>

 

 




