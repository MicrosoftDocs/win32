---
Description: The Enhanced Video Renderer (EVR) filter is a 16-channel video mixer and renderer. It has the same core functionality and plug-in model as the Media Foundation EVR media sink.
ms.assetid: ead99cb3-2be2-42c6-ac22-be0c2ddf28d5
title: Enhanced Video Renderer Filter
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enhanced Video Renderer Filter

> [!Note]  
> This topic applies to Windows Vista and later.

 

The Enhanced Video Renderer (EVR) filter is a 16-channel video mixer and renderer. It has the same core functionality and plug-in model as the Media Foundation EVR media sink.

The DirectShow EVR filter is documented in the Media Foundation SDK documentation; for more information, see [Enhanced Video Renderer](http://go.microsoft.com/fwlink/p/?linkid=104315).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces (through <strong>QueryInterface</strong>)</td>
<td>DirectShow interfaces:
<ul>
<li><a href="/windows/desktop/api/Strmif/nn-strmif-iamcertifiedoutputprotection"><strong>IAMCertifiedOutputProtection</strong></a></li>
<li><a href="/windows/desktop/api/Strmif/nn-strmif-iamfiltermiscflags"><strong>IAMFilterMiscFlags</strong></a></li>
<li><a href="/windows/desktop/api/Strmif/nn-strmif-ibasefilter"><strong>IBaseFilter</strong></a></li>
<li><a href="ikspropertyset"><strong>IKsPropertySet</strong></a></li>
<li><a href="/windows/desktop/api/Strmif/nn-strmif-imediaeventsink"><strong>IMediaEventSink</strong></a></li>
<li><a href="/windows/desktop/api/Strmif/nn-strmif-imediaseeking"><strong>IMediaSeeking</strong></a></li>
<li><a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></li>
<li><a href="/windows/desktop/api/Amvideo/nn-amvideo-iqualprop"><strong>IQualProp</strong></a></li>
</ul>
Media Foundation interfaces:<br/>
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms694298"><strong>IEVRFilterConfig</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms694261"><strong>IMFGetService</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms695386"><strong>IMFVideoPositionMapper</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms698954"><strong>IMFVideoRenderer</strong></a></li>
</ul></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>Variable, depending on the graphics driver.</td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces (through <strong>QueryInterface</strong>)</td>
<td>DirectShow interfaces:
<ul>
<li><a href="/windows/desktop/api/Strmif/nn-strmif-imeminputpin"><strong>IMemInputPin</strong></a></li>
<li><a href="/windows/desktop/api/Strmif/nn-strmif-ipin"><strong>IPin</strong></a></li>
<li><a href="/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol"><strong>IQualityControl</strong></a></li>
</ul>
Media Foundation interfaces:<br/>
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms703164"><strong>IDirectXVideoMemoryConfiguration</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms704789"><strong>IEVRVideoStreamControl</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/desktop/ms694261"><strong>IMFGetService</strong></a></li>
</ul></td>
</tr>
<tr class="even">
<td>Output Pin Media Types</td>
<td>Not applicable.</td>
</tr>
<tr class="odd">
<td>Output Pin Interfaces</td>
<td>Not applicable.</td>
</tr>
<tr class="even">
<td>Filter CLSID</td>
<td>CLSID_EnhancedVideoRenderer</td>
</tr>
<tr class="odd">
<td>Executable</td>
<td>evr.dll</td>
</tr>
<tr class="even">
<td><a href="merit">Merit</a></td>
<td>MERIT_DO_NOT_USE</td>
</tr>
<tr class="odd">
<td><a href="filter-categories">Filter Category</a></td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Remarks

In addition to the interfaces exposed through **QueryInterface**, the EVR exposes other interfaces through the [**IMFGetService::GetService**](https://msdn.microsoft.com/library/windows/desktop/ms696978) method. Some of these interfaces are implemented by the EVR presenter or the EVR mixer, rather than the EVR itself. If the application sets a custom presenter or mixer on the EVR, the custom versions might expose a different set of interfaces.



| Object     | Service Identifier                                              | Interfaces                                                                                                                                                                                                                                                                                                     |
|------------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EVR filter | MR\_VIDEO\_RENDER\_SERVICE(Queries EVR or presenter)<br/> | [**IMFVideoDeviceID**](https://msdn.microsoft.com/library/windows/desktop/ms703065)<br/> [**IMFVideoDisplayControl**](https://msdn.microsoft.com/library/windows/desktop/ms704002)<br/> [**IMFVideoPositionMapper**](https://msdn.microsoft.com/library/windows/desktop/ms695386)<br/> [**IMFVideoPresenter**](https://msdn.microsoft.com/library/windows/desktop/ms700214)<br/>                                                          |
| EVR filter | MR\_VIDEO\_ACCELERATION\_SERVICE(Queries presenter)<br/>  | [**IDirect3DDeviceManager9**](https://msdn.microsoft.com/library/windows/desktop/ms704727)                                                                                                                                                                                                                                                      |
| EVR filter | MR\_VIDEO\_MIXER\_SERVICE(Queries mixer)<br/>             | [**IMFVideoDeviceID**](https://msdn.microsoft.com/library/windows/desktop/ms703065)<br/> [**IMFVideoMixerBitmap**](https://msdn.microsoft.com/library/windows/desktop/ms697041)<br/> [**IMFVideoMixerControl**](https://msdn.microsoft.com/library/windows/desktop/ms700190)<br/> [**IMFVideoPositionMapper**](https://msdn.microsoft.com/library/windows/desktop/ms695386)<br/> [**IMFVideoProcessor**](https://msdn.microsoft.com/library/windows/desktop/ms694106)<br/> |
| Input pins | MR\_VIDEO\_ACCELERATION\_SERVICE                                | [**IDirectXVideoMemoryConfiguration**](https://msdn.microsoft.com/library/windows/desktop/ms703164)                                                                                                                                                                                                                                    |



 

The EVR can mix up to 16 video streams. The first input stream (pin 0) is called the *reference stream*. The reference stream always appears first in the z-order. Any additional streams are called substreams, and are mixed on top of the reference stream. The application can change the z-order of the substreams, but no substream can be first in the z-order.

The graphics driver determines which video formats are supported, but typically they are limited to the following:

-   Reference stream: Progressive or interlaced YUV with no per-pixel alpha (such as NV12 or YUY2); or progressive RGB.
-   Substreams: Progressive YUV with per-pixel-alpha, such as AYUV or AI44.

The available substream formats might depend on the format of the reference stream.

The EVR forwards seek commands upstream through pin 0. The substream pins do not forward seek commands. It is the responsibility of the source or splitter filter to keep the substreams synchronized with the reference stream.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




