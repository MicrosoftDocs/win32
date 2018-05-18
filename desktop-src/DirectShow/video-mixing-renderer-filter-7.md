---
Description: Video Mixing Renderer Filter 7
ms.assetid: 'c83e6c50-76f2-4aeb-944b-5b244c6bf776'
title: Video Mixing Renderer Filter 7
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
<li>[<strong>IAMCertifiedOutputProtection</strong>](iamcertifiedoutputprotection.md)</li>
<li>[<strong>IAMFilterMiscFlags</strong>](iamfiltermiscflags.md)</li>
<li>[<strong>IBaseFilter</strong>](ibasefilter.md)</li>
<li>[<strong>IKsPropertySet</strong>](ikspropertyset.md)</li>
<li>[<strong>IMediaPosition</strong>](imediaposition.md)</li>
<li>[<strong>IMediaSeeking</strong>](imediaseeking.md)</li>
<li>[<strong>IQualityControl</strong>](iqualitycontrol.md)</li>
<li>[<strong>IQualProp</strong>](iqualprop.md)</li>
<li>[<strong>IVMRAspectRatioControl</strong>](ivmraspectratiocontrol.md)</li>
<li>[<strong>IVMRDeinterlaceControl</strong>](ivmrdeinterlacecontrol.md)</li>
<li>[<strong>IVMRFilterConfig</strong>](ivmrfilterconfig.md)</li>
<li>[<strong>IVMRMixerBitmap</strong>](ivmrmixerbitmap.md)</li>
</ul>
Windowed mode:<br/>
<ul>
<li>[<strong>IBasicVideo</strong>](ibasicvideo.md)</li>
<li>[<strong>IBasicVideo2</strong>](ibasicvideo2.md)</li>
<li>[<strong>IVideoWindow</strong>](ivideowindow.md)</li>
<li>[<strong>IVMRMonitorConfig</strong>](ivmrmonitorconfig.md)</li>
</ul>
Windowless mode:<br/>
<ul>
<li>[<strong>IVMRWindowlessControl</strong>](ivmrwindowlesscontrol.md)</li>
<li>[<strong>IVMRMonitorConfig</strong>](ivmrmonitorconfig.md)</li>
</ul>
Renderless mode:<br/>
<ul>
<li>[<strong>IVMRSurfaceAllocatorNotify</strong>](ivmrsurfaceallocatornotify.md)</li>
</ul>
Mixer mode:<br/>
<ul>
<li>[<strong>IVMRMixerControl</strong>](ivmrmixercontrol.md)</li>
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
<li>[<strong>IAMVideoAccelerator</strong>](iamvideoaccelerator.md)</li>
<li>[<strong>IMemInputPin</strong>](imeminputpin.md)</li>
<li>[<strong>IOverlay</strong>](ioverlay.md) (see Remarks)</li>
<li>[<strong>IPin</strong>](ipin.md)</li>
<li>[<strong>IPinConnection</strong>](ipinconnection.md)</li>
<li>[<strong>IQualityControl</strong>](iqualitycontrol.md)</li>
<li>[<strong>IVMRVideoStreamControl</strong>](ivmrvideostreamcontrol.md)</li>
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

-   [**IVMRImagePresenter**](ivmrimagepresenter.md)
-   [**IVMRImagePresenterConfig**](ivmrimagepresenterconfig.md) (optional)
-   [**IVMRMonitorConfig**](ivmrmonitorconfig.md) (optional)
-   [**IVMRSurfaceAllocator**](ivmrsurfaceallocator.md)
-   [**IVMRWindowlessControl**](ivmrwindowlesscontrol.md) (optional)

For more information about custom allocator-presenters, see [Supplying a Custom Allocator-Presenter for VMR-7](supplying-a-custom-allocator-presenter-for-vmr-7.md).

An application can also provide a custom plug-in compositor that exposes the following interface:

-   [**IVMRImageCompositor**](ivmrimagecompositor.md)

To configure the VMR with a custom compositor, call [**IVMRFilterConfig::SetImageCompositor**](ivmrfilterconfig-setimagecompositor.md).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




