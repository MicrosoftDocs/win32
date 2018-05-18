---
Description: Video Mixing Renderer Filter 9
ms.assetid: '3885cca2-74b1-4066-8ecb-84c9841f9e66'
title: Video Mixing Renderer Filter 9
---

# Video Mixing Renderer Filter 9

In DirectX 9, the Video Mixing Renderer 9 (VMR-9) filter offers advanced video rendering capabilities on all platforms supported by DirectX. It is fully integrated with DirectX 9 3D capabilities. For example, that you can easily add video to games and other 3D environments or transform video images using the Direct3D pixel shaders and other effects.

This filter does not support video ports.

To maintain backward compatibility, the VMR-9 is not the default renderer on any system. To use this filter, add it to the filter graph explicitly and configure it before connecting any of its input pins. The VMR-9 uses its own set of interfaces, structures, and enumerations, which are not always identical to the corresponding data types used with the VMR-7.

The VMR-9 supports up to 16 monitors.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Filter Interfaces</td>
<td>The VMR-9 supports several distinct rendering modes. It supports a different set of interfaces depending on the rendering mode:<br/>
<ul>
<li>All modes: [<strong>IAMCertifiedOutputProtection</strong>](iamcertifiedoutputprotection.md), [<strong>IAMFilterMiscFlags</strong>](iamfiltermiscflags.md), [<strong>IBaseFilter</strong>](ibasefilter.md), [<strong>IMediaPosition</strong>](imediaposition.md), [<strong>IMediaSeeking</strong>](imediaseeking.md), [<strong>IQualityControl</strong>](iqualitycontrol.md), [<strong>IQualProp</strong>](iqualprop.md), [<strong>IVMRAspectRatioControl9</strong>](ivmraspectratiocontrol9.md), [<strong>IVMRDeinterlaceControl9</strong>](ivmrdeinterlacecontrol9.md), [<strong>IVMRFilterConfig9</strong>](ivmrfilterconfig9.md), [<strong>IVMRMixerBitmap9</strong>](ivmrmixerbitmap9.md), [<strong>IVMRMixerControl9</strong>](ivmrmixercontrol9.md)</li>
<li>Renderless mode: [<strong>IVMRSurfaceAllocatorNotify9</strong>](ivmrsurfaceallocatornotify9.md)</li>
<li>Windowed mode: [<strong>IBasicVideo</strong>](ibasicvideo.md), [<strong>IBasicVideo2</strong>](ibasicvideo2.md), [<strong>IVideoWindow</strong>](ivideowindow.md), [<strong>IVMRMonitorConfig9</strong>](ivmrmonitorconfig9.md)</li>
<li>Windowless mode: [<strong>IVMRMonitorConfig9</strong>](ivmrmonitorconfig9.md), [<strong>IVMRWindowlessControl9</strong>](ivmrwindowlesscontrol9.md)</li>
</ul>
To set the rendering mode, call [<strong>IVMRFilterConfig9::SetRenderingMode</strong>](ivmrfilterconfig9-setrenderingmode.md). For more information, see [VMR Modes of Operation](vmr-modes-of-operation.md).<br/></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>The input pins will connect with any type supported by the underlying video hardware.</td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IAMVideoAccelerator</strong>](iamvideoaccelerator.md), [<strong>IMemInputPin</strong>](imeminputpin.md), [<strong>IOverlay</strong>](ioverlay.md), [<strong>IQualityControl</strong>](iqualitycontrol.md), [<strong>IPin</strong>](ipin.md), [<strong>IPinConnection</strong>](ipinconnection.md), [<strong>IVMRVideoStreamControl9</strong>](ivmrvideostreamcontrol9.md)</td>
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
<td>CLSID_VideoMixingRenderer9</td>
</tr>
<tr class="odd">
<td>Property Page CLSID</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>Quartz.dll</td>
</tr>
<tr class="odd">
<td>[Merit](merit.md)</td>
<td>MERIT_DO_NOT_USE</td>
</tr>
<tr class="even">
<td>[Filter Category](filter-categories.md)</td>
<td>CLSID_LegacyAmFilterCategory</td>
</tr>
</tbody>
</table>



 

## Remarks

An application can provide a custom allocator-presenter object that exposes the following interfaces:

-   [**IVMRImagePresenter9**](ivmrimagepresenter9.md)
-   [**IVMRImagePresenterConfig9**](ivmrimagepresenterconfig9.md) (optional)
-   [**IVMRSurfaceAllocator9**](ivmrsurfaceallocator9.md)
-   [**IVMRSurfaceAllocatorEx9**](ivmrsurfaceallocatorex9.md) (optional)
-   [**IVMRWindowlessControl9**](ivmrwindowlesscontrol9.md) (optional)

For more information about custom allocator-presenters, see [Supplying a Custom Allocator-Presenter for VMR-9](supplying-a-custom-allocator-presenter-for-vmr-9.md).

An application can also provide a custom plug-in compositor that exposes the following interface:

-   [**IVMRImageCompositor9**](ivmrimagecompositor9.md)

To configure the VMR with a custom compositor, call [**IVMRFilterConfig9::SetImageCompositor**](ivmrfilterconfig9-setimagecompositor.md).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> </dl>

 

 




