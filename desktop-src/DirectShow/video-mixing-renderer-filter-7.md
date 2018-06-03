---
Description: Video Mixing Renderer Filter 7
ms.assetid: c83e6c50-76f2-4aeb-944b-5b244c6bf776
title: Video Mixing Renderer Filter 7
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Video Mixing Renderer Filter 7

This topic applies to Windows XP or later.

In Windows XP and later, the Video Mixing Renderer 7 (VMR-7) is the default video renderer. It is called the VMR-7 because internally it uses DirectDraw 7. In DirectX 9, a similar but separate filter, the VMR-9, is available for redistribution on non-XP systems. The VMR-9 uses Direct3D 9.

> [!Note]  
> The VMR is available on Windows XP and later. It is not available through the DirectX redistributable, or on previous versions of Windows. For most scenarios, applications should use the [Video Mixing Renderer 9](video-mixing-renderer-filter-9.md).

 

Features of the VMR include:

-   True alpha blending of up to 16 input streams
-   Access to the composited image before it is rendered
-   A plug-in model that enables third-parties to implement custom video effects.
-   Support for up to 15 monitors.

During graph building on Windows XP and later, the Filter Graph Manager will not use the older Video Renderer or Overlay Mixer filters, unless the application explicitly creates them and adds to the graph.

For more information, see [Using the Video Mixing Renderer](using-the-video-mixing-renderer.md).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>All modes:
<ul>
<li>[<strong>IAMCertifiedOutputProtection</strong>](/windows/desktop/api/Strmif/nn-strmif-iamcertifiedoutputprotection)</li>
<li>[<strong>IAMFilterMiscFlags</strong>](/windows/desktop/api/Strmif/nn-strmif-iamfiltermiscflags)</li>
<li>[<strong>IBaseFilter</strong>](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)</li>
<li>[<strong>IKsPropertySet</strong>](ikspropertyset.md)</li>
<li>[<strong>IMediaPosition</strong>](/windows/desktop/api/Control/nn-control-imediaposition)</li>
<li>[<strong>IMediaSeeking</strong>](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)</li>
<li>[<strong>IQualityControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)</li>
<li>[<strong>IQualProp</strong>](/windows/desktop/api/Amvideo/nn-amvideo-iqualprop)</li>
<li>[<strong>IVMRAspectRatioControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmraspectratiocontrol)</li>
<li>[<strong>IVMRDeinterlaceControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrdeinterlacecontrol)</li>
<li>[<strong>IVMRFilterConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrfilterconfig)</li>
<li>[<strong>IVMRMixerBitmap</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrmixerbitmap)</li>
</ul>
Windowed mode:<br/>
<ul>
<li>[<strong>IBasicVideo</strong>](/windows/desktop/api/Control/nn-control-ibasicvideo)</li>
<li>[<strong>IBasicVideo2</strong>](/windows/desktop/api/Control/nn-control-ibasicvideo2)</li>
<li>[<strong>IVideoWindow</strong>](/windows/desktop/api/Control/nn-control-ivideowindow)</li>
<li>[<strong>IVMRMonitorConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrmonitorconfig)</li>
</ul>
Windowless mode:<br/>
<ul>
<li>[<strong>IVMRWindowlessControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrwindowlesscontrol)</li>
<li>[<strong>IVMRMonitorConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrmonitorconfig)</li>
</ul>
Renderless mode:<br/>
<ul>
<li>[<strong>IVMRSurfaceAllocatorNotify</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrsurfaceallocatornotify)</li>
</ul>
Mixer mode:<br/>
<ul>
<li>[<strong>IVMRMixerControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrmixercontrol)</li>
</ul>
For information about the various VMR-7 modes, see [VMR Modes of Operation](vmr-modes-of-operation.md).<br/></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>Major type: MEDIATYPE_VideoSubtype: Depends on the graphics hardware. Must be uncompressed video.<br/></td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td><ul>
<li>[<strong>IAMVideoAccelerator</strong>](/windows/desktop/api/videoacc/nn-videoacc-iamvideoaccelerator)</li>
<li>[<strong>IMemInputPin</strong>](/windows/desktop/api/Strmif/nn-strmif-imeminputpin)</li>
<li>[<strong>IOverlay</strong>](/windows/desktop/api/Strmif/nn-strmif-ioverlay) (see Remarks)</li>
<li>[<strong>IPin</strong>](/windows/desktop/api/Strmif/nn-strmif-ipin)</li>
<li>[<strong>IPinConnection</strong>](/windows/desktop/api/Strmif/nn-strmif-ipinconnection)</li>
<li>[<strong>IQualityControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)</li>
<li>[<strong>IVMRVideoStreamControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrvideostreamcontrol)</li>
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
<td>There are two CLSIDs associated with this filter:
<ul>
<li>CLSID_VideoMixingRenderer: Creates the VMR-7. If there are not enough system resources to create the VMR-7, the call to <strong>CoCreateInstance</strong> fails.</li>
<li>CLSID_VideoRendererDefault: Creates the VMR-7 if system resources are available, or else creates the old [Video Renderer](video-renderer-filter.md) filter.</li>
</ul>
Use CLSID_VideoMixingRenderer if you need the specific capabilities of the VMR-7. Otherwise, use CLSID_VideoRendererDefault, which is almost certain not to fail, because it falls back to the old Video Renderer filter.<br/></td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>Not applicable.</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>Quartz.dll</td>
</tr>
<tr class="odd">
<td>[Merit](merit.md)</td>
<td>MERIT_PREFERRED + 1</td>
</tr>
<tr class="even">
<td>[Filter Category](filter-categories.md)</td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Remarks

The input pin exposes the **IOverlay** interface only when the VMR-7 filter is in windowed mode. The only **IOverlay** method that the pin implements is **GetWindowHandle**, which enables an application to obtain a handle to the filter's video window. All other **IOverlay** methods return E\_NOTIMPL. In windowless mode, the filter does not create a video window, so the pin does not expose the interface.

An application can provide a custom allocator-presenter object that exposes the following interfaces:

-   [**IVMRImagePresenter**](/windows/desktop/api/Strmif/nn-strmif-ivmrimagepresenter)
-   [**IVMRImagePresenterConfig**](/windows/desktop/api/Strmif/nn-strmif-ivmrimagepresenterconfig) (optional)
-   [**IVMRMonitorConfig**](/windows/desktop/api/Strmif/nn-strmif-ivmrmonitorconfig) (optional)
-   [**IVMRSurfaceAllocator**](/windows/desktop/api/Strmif/nn-strmif-ivmrsurfaceallocator)
-   [**IVMRWindowlessControl**](/windows/desktop/api/Strmif/nn-strmif-ivmrwindowlesscontrol) (optional)

For more information about custom allocator-presenters, see [Supplying a Custom Allocator-Presenter for VMR-7](supplying-a-custom-allocator-presenter-for-vmr-7.md).

An application can also provide a custom plug-in compositor that exposes the following interface:

-   [**IVMRImageCompositor**](/windows/desktop/api/Strmif/nn-strmif-ivmrimagecompositor)

To configure the VMR with a custom compositor, call [**IVMRFilterConfig::SetImageCompositor**](/windows/desktop/api/Strmif/nf-strmif-ivmrfilterconfig-setimagecompositor).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




