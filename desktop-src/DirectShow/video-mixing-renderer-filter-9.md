---
Description: Video Mixing Renderer Filter 9
ms.assetid: 3885cca2-74b1-4066-8ecb-84c9841f9e66
title: Video Mixing Renderer Filter 9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<li>All modes: [<strong>IAMCertifiedOutputProtection</strong>](/windows/desktop/api/Strmif/nn-strmif-iamcertifiedoutputprotection), [<strong>IAMFilterMiscFlags</strong>](/windows/desktop/api/Strmif/nn-strmif-iamfiltermiscflags), [<strong>IBaseFilter</strong>](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [<strong>IMediaPosition</strong>](/windows/desktop/api/Control/nn-control-imediaposition), [<strong>IMediaSeeking</strong>](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [<strong>IQualityControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol), [<strong>IQualProp</strong>](/windows/desktop/api/Amvideo/nn-amvideo-iqualprop), [<strong>IVMRAspectRatioControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmraspectratiocontrol9), [<strong>IVMRDeinterlaceControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrdeinterlacecontrol9), [<strong>IVMRFilterConfig9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrfilterconfig9), [<strong>IVMRMixerBitmap9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrmixerbitmap9), [<strong>IVMRMixerControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrmixercontrol9)</li>
<li>Renderless mode: [<strong>IVMRSurfaceAllocatorNotify9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocatornotify9)</li>
<li>Windowed mode: [<strong>IBasicVideo</strong>](/windows/desktop/api/Control/nn-control-ibasicvideo), [<strong>IBasicVideo2</strong>](/windows/desktop/api/Control/nn-control-ibasicvideo2), [<strong>IVideoWindow</strong>](/windows/desktop/api/Control/nn-control-ivideowindow), [<strong>IVMRMonitorConfig9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrmonitorconfig9)</li>
<li>Windowless mode: [<strong>IVMRMonitorConfig9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrmonitorconfig9), [<strong>IVMRWindowlessControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrwindowlesscontrol9)</li>
</ul>
To set the rendering mode, call [<strong>IVMRFilterConfig9::SetRenderingMode</strong>](/windows/desktop/api/Vmr9/nf-vmr9-ivmrfilterconfig9-setrenderingmode). For more information, see [VMR Modes of Operation](vmr-modes-of-operation.md).<br/></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>The input pins will connect with any type supported by the underlying video hardware.</td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IAMVideoAccelerator</strong>](/windows/desktop/api/videoacc/nn-videoacc-iamvideoaccelerator), [<strong>IMemInputPin</strong>](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [<strong>IOverlay</strong>](/windows/desktop/api/Strmif/nn-strmif-ioverlay), [<strong>IQualityControl</strong>](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol), [<strong>IPin</strong>](/windows/desktop/api/Strmif/nn-strmif-ipin), [<strong>IPinConnection</strong>](/windows/desktop/api/Strmif/nn-strmif-ipinconnection), [<strong>IVMRVideoStreamControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrvideostreamcontrol9)</td>
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

-   [**IVMRImagePresenter9**](/windows/desktop/api/Vmr9/nn-vmr9-ivmrimagepresenter9)
-   [**IVMRImagePresenterConfig9**](/windows/desktop/api/Vmr9/nn-vmr9-ivmrimagepresenterconfig9) (optional)
-   [**IVMRSurfaceAllocator9**](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocator9)
-   [**IVMRSurfaceAllocatorEx9**](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocatorex9) (optional)
-   [**IVMRWindowlessControl9**](/windows/desktop/api/Vmr9/nn-vmr9-ivmrwindowlesscontrol9) (optional)

For more information about custom allocator-presenters, see [Supplying a Custom Allocator-Presenter for VMR-9](supplying-a-custom-allocator-presenter-for-vmr-9.md).

An application can also provide a custom plug-in compositor that exposes the following interface:

-   [**IVMRImageCompositor9**](/windows/desktop/api/Vmr9/nn-vmr9-ivmrimagecompositor9)

To configure the VMR with a custom compositor, call [**IVMRFilterConfig9::SetImageCompositor**](/windows/desktop/api/Vmr9/nf-vmr9-ivmrfilterconfig9-setimagecompositor).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> </dl>

 

 




