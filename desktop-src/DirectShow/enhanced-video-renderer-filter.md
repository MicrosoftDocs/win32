---
description: The Enhanced Video Renderer (EVR) filter is a 16-channel video mixer and renderer. It has the same core functionality and plug-in model as the Media Foundation EVR media sink.
ms.assetid: ead99cb3-2be2-42c6-ac22-be0c2ddf28d5
title: Enhanced Video Renderer Filter
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Enhanced Video Renderer Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic applies to Windows Vista and later.

 

The Enhanced Video Renderer (EVR) filter is a 16-channel video mixer and renderer. It has the same core functionality and plug-in model as the Media Foundation EVR media sink.

The DirectShow EVR filter is documented in the Media Foundation SDK documentation; for more information, see [Enhanced Video Renderer](../medfound/enhanced-video-renderer.md).




| Label | Value |
|--------|-------|
| Filter Interfaces (through <strong>QueryInterface</strong>) | DirectShow interfaces:<ul><li><a href="/windows/desktop/api/Strmif/nn-strmif-iamcertifiedoutputprotection"><strong>IAMCertifiedOutputProtection</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-iamfiltermiscflags"><strong>IAMFilterMiscFlags</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a></li><li><a href="ikspropertyset.md"><strong>IKsPropertySet</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-imediaeventsink"><strong>IMediaEventSink</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></li><li><a href="/previous-versions/windows/desktop/api/Amvideo/nn-amvideo-iqualprop"><strong>IQualProp</strong></a></li></ul>Media Foundation interfaces:<br /><ul><li><a href="/windows/desktop/api/evr/nn-evr-ievrfilterconfig"><strong>IEVRFilterConfig</strong></a></li><li><a href="/windows/desktop/api/mfidl/nn-mfidl-imfgetservice"><strong>IMFGetService</strong></a></li><li><a href="/windows/desktop/api/evr/nn-evr-imfvideopositionmapper"><strong>IMFVideoPositionMapper</strong></a></li><li><a href="/windows/desktop/api/evr/nn-evr-imfvideorenderer"><strong>IMFVideoRenderer</strong></a></li></ul> | 
| Input Pin Media Types | Variable, depending on the graphics driver. | 
| Input Pin Interfaces (through <strong>QueryInterface</strong>) | DirectShow interfaces:<ul><li><a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a></li><li><a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></li></ul>Media Foundation interfaces:<br /><ul><li><a href="/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideomemoryconfiguration"><strong>IDirectXVideoMemoryConfiguration</strong></a></li><li><a href="/windows/desktop/api/evr9/nn-evr9-ievrvideostreamcontrol"><strong>IEVRVideoStreamControl</strong></a></li><li><a href="/windows/desktop/api/mfidl/nn-mfidl-imfgetservice"><strong>IMFGetService</strong></a></li></ul> | 
| Output Pin Media Types | Not applicable. | 
| Output Pin Interfaces | Not applicable. | 
| Filter CLSID | CLSID_EnhancedVideoRenderer | 
| Executable | evr.dll | 
| <a href="merit.md">Merit</a> | MERIT_DO_NOT_USE | 
| <a href="filter-categories.md">Filter Category</a> | CLSID_LegacyAmFilterCategory | 




 

## Remarks

In addition to the interfaces exposed through **QueryInterface**, the EVR exposes other interfaces through the [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) method. Some of these interfaces are implemented by the EVR presenter or the EVR mixer, rather than the EVR itself. If the application sets a custom presenter or mixer on the EVR, the custom versions might expose a different set of interfaces.



| Object     | Service Identifier                                              | Interfaces                                                                                                                                                                                                                                                                                                     |
|------------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EVR filter | MR\_VIDEO\_RENDER\_SERVICE(Queries EVR or presenter)<br/> | [**IMFVideoDeviceID**](/windows/desktop/api/evr/nn-evr-imfvideodeviceid)<br/> [**IMFVideoDisplayControl**](/windows/desktop/api/evr/nn-evr-imfvideodisplaycontrol)<br/> [**IMFVideoPositionMapper**](/windows/desktop/api/evr/nn-evr-imfvideopositionmapper)<br/> [**IMFVideoPresenter**](/windows/desktop/api/evr/nn-evr-imfvideopresenter)<br/>                                                          |
| EVR filter | MR\_VIDEO\_ACCELERATION\_SERVICE(Queries presenter)<br/>  | [**IDirect3DDeviceManager9**](/windows/desktop/api/dxva2api/nn-dxva2api-idirect3ddevicemanager9)                                                                                                                                                                                                                                                      |
| EVR filter | MR\_VIDEO\_MIXER\_SERVICE(Queries mixer)<br/>             | [**IMFVideoDeviceID**](/windows/desktop/api/evr/nn-evr-imfvideodeviceid)<br/> [**IMFVideoMixerBitmap**](/windows/desktop/api/evr9/nn-evr9-imfvideomixerbitmap)<br/> [**IMFVideoMixerControl**](/windows/desktop/api/evr/nn-evr-imfvideomixercontrol)<br/> [**IMFVideoPositionMapper**](/windows/desktop/api/evr/nn-evr-imfvideopositionmapper)<br/> [**IMFVideoProcessor**](/windows/desktop/api/evr9/nn-evr9-imfvideoprocessor)<br/> |
| Input pins | MR\_VIDEO\_ACCELERATION\_SERVICE                                | [**IDirectXVideoMemoryConfiguration**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideomemoryconfiguration)                                                                                                                                                                                                                                    |



 

The EVR can mix up to 16 video streams. The first input stream (pin 0) is called the *reference stream*. The reference stream always appears first in the z-order. Any additional streams are called substreams, and are mixed on top of the reference stream. The application can change the z-order of the substreams, but no substream can be first in the z-order.

The graphics driver determines which video formats are supported, but typically they are limited to the following:

-   Reference stream: Progressive or interlaced YUV with no per-pixel alpha (such as NV12 or YUY2); or progressive RGB.
-   Substreams: Progressive YUV with per-pixel-alpha, such as AYUV or AI44.

The available substream formats might depend on the format of the reference stream.

The EVR forwards seek commands upstream through pin 0. The substream pins do not forward seek commands. It is the responsibility of the source or splitter filter to keep the substreams synchronized with the reference stream.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

