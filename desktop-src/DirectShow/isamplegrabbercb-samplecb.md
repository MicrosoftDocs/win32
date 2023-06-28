---
description: The SampleCB method is a callback method that receives a pointer to the media sample.
ms.assetid: e919b694-75cb-48c6-8427-5a7a886e0ff3
title: ISampleGrabberCB::SampleCB method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISampleGrabberCB.SampleCB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# ISampleGrabberCB::SampleCB method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SampleCB` method is a callback method that receives a pointer to the media sample.

## Syntax


```C++
HRESULT SampleCB(
   double       SampleTime,
   IMediaSample *pSample
);
```



## Parameters

<dl> <dt>

*SampleTime* 
</dt> <dd>

Starting time of the sample, in seconds.

</dd> <dt>

*pSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface of the sample.

</dd> </dl>

## Return value

Returns S\_OK if successful, or an **HRESULT** error code otherwise.

## Remarks

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

 

 




