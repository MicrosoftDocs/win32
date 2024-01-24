---
description: The SetOneShot method specifies whether the Sample Grabber filter halts after the filter receives a sample.
ms.assetid: 7e3a3e8c-1834-425b-9657-279ab4451a2b
title: ISampleGrabber::SetOneShot method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISampleGrabber.SetOneShot
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# ISampleGrabber::SetOneShot method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **SetOneShot** method specifies whether the [**Sample Grabber**](sample-grabber-filter.md) filter halts after the filter receives a sample.

## Syntax


```C++
HRESULT SetOneShot(
   BOOL OneShot
);
```



## Parameters

<dl> <dt>

*OneShot* 
</dt> <dd>

A Boolean value that specifies whether the Sample Grabber filter halts after receiving a sample.



| Value                                                                                                                                    | Meaning                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| <span id="TRUE"></span><span id="true"></span><dl> <dt>****TRUE****</dt> </dl>    | The Sample Grabber halts after the first sample. <br/>                                                      |
| <span id="FALSE"></span><span id="false"></span><dl> <dt>****FALSE****</dt> </dl> | After the first sample, the Sample Grabber continues to process samples. This is the default behavior.<br/> |



 

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Use this method to get a single sample from the stream, as follows:

1.  Call **SetOneShot** with the value **TRUE**.
2.  Optionally, use the [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interface to seek to a position in the stream.
3.  Call [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run) to run the filter graph.
4.  Call [**IMediaEvent::WaitForCompletion**](/windows/desktop/api/Control/nf-control-imediaevent-waitforcompletion) to wait for the graph to halt. Alternatively, call [**IMediaEvent::GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent) to get graph events, until you receive the [**EC\_COMPLETE**](ec-complete.md) event.

After the Sample Grabber halts, the filter graph is still in a running state. You can seek or pause the graph to get another sample.

> [!Note]  
> An earlier version of the documentation stated that the filter graph stops after the sample is received. That is not accurate. The stream ends, but the graph remains in the running state.

 

The Sample Grabber implements one-shot mode by calling [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) on the downstream filter and returning S\_FALSE from the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method of it.

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

[Using the Sample Grabber](using-the-sample-grabber.md)
</dt> <dt>

[**ISampleGrabber Interface**](isamplegrabber.md)
</dt> </dl>

 

 




