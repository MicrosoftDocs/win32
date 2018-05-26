---
Description: Video Mixing Renderer Filter 9
ms.assetid: 3885cca2-74b1-4066-8ecb-84c9841f9e66
title: Video Mixing Renderer Filter 9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<li>All modes: [<strong>IAMCertifiedOutputProtection</strong>](/windows/win32/Strmif/nn-strmif-iamcertifiedoutputprotection?branch=master), [<strong>IAMFilterMiscFlags</strong>](/windows/win32/Strmif/nn-strmif-iamfiltermiscflags?branch=master), [<strong>IBaseFilter</strong>](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [<strong>IMediaPosition</strong>](/windows/win32/Control/nn-control-imediaposition?branch=master), [<strong>IMediaSeeking</strong>](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master), [<strong>IQualProp</strong>](/windows/win32/Amvideo/nn-amvideo-iqualprop?branch=master), [<strong>IVMRAspectRatioControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmraspectratiocontrol9?branch=master), [<strong>IVMRDeinterlaceControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrdeinterlacecontrol9?branch=master), [<strong>IVMRFilterConfig9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrfilterconfig9?branch=master), [<strong>IVMRMixerBitmap9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrmixerbitmap9?branch=master), [<strong>IVMRMixerControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrmixercontrol9?branch=master)</li>
<li>Renderless mode: [<strong>IVMRSurfaceAllocatorNotify9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocatornotify9?branch=master)</li>
<li>Windowed mode: [<strong>IBasicVideo</strong>](/windows/win32/Control/nn-control-ibasicvideo?branch=master), [<strong>IBasicVideo2</strong>](/windows/win32/Control/nn-control-ibasicvideo2?branch=master), [<strong>IVideoWindow</strong>](/windows/win32/Control/nn-control-ivideowindow?branch=master), [<strong>IVMRMonitorConfig9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrmonitorconfig9?branch=master)</li>
<li>Windowless mode: [<strong>IVMRMonitorConfig9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrmonitorconfig9?branch=master), [<strong>IVMRWindowlessControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrwindowlesscontrol9?branch=master)</li>
</ul>
To set the rendering mode, call [<strong>IVMRFilterConfig9::SetRenderingMode</strong>](/windows/win32/Vmr9/nf-vmr9-ivmrfilterconfig9-setrenderingmode?branch=master). For more information, see [VMR Modes of Operation](vmr-modes-of-operation.md).<br/></td>
</tr>
<tr class="even">
<td>Input Pin Media Types</td>
<td>The input pins will connect with any type supported by the underlying video hardware.</td>
</tr>
<tr class="odd">
<td>Input Pin Interfaces</td>
<td>[<strong>IAMVideoAccelerator</strong>](/windows/win32/videoacc/nn-videoacc-iamvideoaccelerator?branch=master), [<strong>IMemInputPin</strong>](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [<strong>IOverlay</strong>](/windows/win32/Strmif/nn-strmif-ioverlay?branch=master), [<strong>IQualityControl</strong>](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master), [<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [<strong>IPinConnection</strong>](/windows/win32/Strmif/nn-strmif-ipinconnection?branch=master), [<strong>IVMRVideoStreamControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrvideostreamcontrol9?branch=master)</td>
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

-   [**IVMRImagePresenter9**](/windows/win32/Vmr9/nn-vmr9-ivmrimagepresenter9?branch=master)
-   [**IVMRImagePresenterConfig9**](/windows/win32/Vmr9/nn-vmr9-ivmrimagepresenterconfig9?branch=master) (optional)
-   [**IVMRSurfaceAllocator9**](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocator9?branch=master)
-   [**IVMRSurfaceAllocatorEx9**](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocatorex9?branch=master) (optional)
-   [**IVMRWindowlessControl9**](/windows/win32/Vmr9/nn-vmr9-ivmrwindowlesscontrol9?branch=master) (optional)

For more information about custom allocator-presenters, see [Supplying a Custom Allocator-Presenter for VMR-9](supplying-a-custom-allocator-presenter-for-vmr-9.md).

An application can also provide a custom plug-in compositor that exposes the following interface:

-   [**IVMRImageCompositor9**](/windows/win32/Vmr9/nn-vmr9-ivmrimagecompositor9?branch=master)

To configure the VMR with a custom compositor, call [**IVMRFilterConfig9::SetImageCompositor**](/windows/win32/Vmr9/nf-vmr9-ivmrfilterconfig9-setimagecompositor?branch=master).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> </dl>

 

 




