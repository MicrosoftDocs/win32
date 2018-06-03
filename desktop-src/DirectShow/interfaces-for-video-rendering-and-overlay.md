---
Description: Interfaces for Video Rendering and Overlay
ms.assetid: e4d4e456-61fb-492b-b817-30629681e270
title: Interfaces for Video Rendering and Overlay
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces for Video Rendering and Overlay

These interfaces support application control over video rendering. Note that some of these interfaces are now deprecated, because the Video Mixing Renderer filter provides superior rendering and overlay control.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Interface</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>IAMLine21Decoder</strong>](/windows/desktop/api/il21dec/nn-il21dec-iamline21decoder)</td>
<td>Provides access to closed-captioned information and settings.</td>
</tr>
<tr class="even">
<td>[<strong>IAMOverlayFX</strong>](/windows/desktop/api/Strmif/nn-strmif-iamoverlayfx)</td>
<td>Apply overlay effects to the video surface. (Deprecated.)</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVideoDecimationProperties</strong>](/windows/desktop/api/Strmif/nn-strmif-iamvideodecimationproperties)</td>
<td>Control how DirectShow scales a video image if the video window is smaller than the native size of the video. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IBasicVideo2</strong>](/windows/desktop/api/Control/nn-control-ibasicvideo2)</td>
<td>Set video properties.</td>
</tr>
<tr class="odd">
<td>[<strong>IDDrawExclModeVideo</strong>](/windows/desktop/api/Strmif/nn-strmif-iddrawexclmodevideo)</td>
<td>Render video in Microsoft DirectDraw exclusive full-screen mode. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IDDrawExclModeVideoCallback</strong>](/windows/desktop/api/Strmif/nn-strmif-iddrawexclmodevideocallback)</td>
<td>Callback interface to receive notification about changes to the overlay position, size, and visibility. (Deprecated.)</td>
</tr>
<tr class="odd">
<td>[<strong>IDirectDrawVideo</strong>](/windows/desktop/api/Amvideo/nn-amvideo-idirectdrawvideo)</td>
<td>Disable specified DirectDraw capabilities. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IDirectDrawMediaSample</strong>](/windows/desktop/api/Amstream/nn-amstream-idirectdrawmediasample)</td>
<td>Access a DirectDraw surface allocated by the [Overlay Mixer](overlay-mixer-filter.md) filter.(Deprecated.)</td>
</tr>
<tr class="odd">
<td>[<strong>IMixerOCX</strong>](/windows/desktop/api/Mixerocx/nn-mixerocx-imixerocx)</td>
<td>Implemented on the Overlay Mixer. Enables windowless clients such as ActiveX® controls to get and set properties of the video rectangle and advise the filter of events.</td>
</tr>
<tr class="even">
<td>[<strong>IMixerOCXNotify</strong>](/windows/desktop/api/Mixerocx/nn-mixerocx-imixerocxnotify)</td>
<td>Implemented by windowless clients and called by the Overlay Mixer to send notifications of events affecting the video display rectangle.</td>
</tr>
<tr class="odd">
<td>[<strong>IMixerPinConfig2</strong>](/windows/desktop/api/Mpconfig/nn-mpconfig-imixerpinconfig2)</td>
<td>Set video color controls on the Overlay Mixer filter when mixing multiple video streams. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IQualProp</strong>](/windows/desktop/api/Amvideo/nn-amvideo-iqualprop)</td>
<td>Query a video renderer for performance information.</td>
</tr>
<tr class="odd">
<td>[<strong>IVideoWindow</strong>](/windows/desktop/api/Control/nn-control-ivideowindow)</td>
<td>Set video window properties.</td>
</tr>
<tr class="even">
<td><ul>
<li>[<strong>IVMRAspectRatioControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmraspectratiocontrol9)</li>
<li>[<strong>IVMRDeinterlaceControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrdeinterlacecontrol9)</li>
<li>[<strong>IVMRFilterConfig9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrfilterconfig9)</li>
<li>[<strong>IVMRImageCompositor9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrimagecompositor9)</li>
<li>[<strong>IVMRImagePresenter9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrimagepresenter9)</li>
<li>[<strong>IVMRImagePresenterConfig9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrimagepresenterconfig9)</li>
<li>[<strong>IVMRMixerBitmap9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrmixerbitmap9)</li>
<li>[<strong>IVMRMixerControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrmixercontrol9)</li>
<li>[<strong>IVMRMonitorConfig9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrmonitorconfig9)</li>
<li>[<strong>IVMRSurface9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurface9)</li>
<li>[<strong>IVMRSurfaceAllocator9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocator9)</li>
<li>[<strong>IVMRSurfaceAllocatorEx9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocatorex9)</li>
<li>[<strong>IVMRSurfaceAllocatorNotify9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocatornotify9)</li>
<li>[<strong>IVMRWindowlessControl9</strong>](/windows/desktop/api/Vmr9/nn-vmr9-ivmrwindowlesscontrol9)</li>
</ul></td>
<td>Video Mixing Renderer 9 interfaces.</td>
</tr>
<tr class="odd">
<td><ul>
<li>[<strong>IVMRAspectRatioControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmraspectratiocontrol)</li>
<li>[<strong>IVMRDeinterlaceControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrdeinterlacecontrol)</li>
<li>[<strong>IVMRFilterConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrfilterconfig)</li>
<li>[<strong>IVMRImageCompositor</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrimagecompositor)</li>
<li>[<strong>IVMRImagePresenter</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrimagepresenter)</li>
<li>[<strong>IVMRImagePresenterConfig</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrimagepresenterconfig)</li>
<li>[<strong>IVMRMixerBitmap</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrmixerbitmap)</li>
<li>[<strong>IVMRMixerControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrmixercontrol)</li>
<li>[<strong>IVMRSurfaceAllocator</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrsurfaceallocator)</li>
<li>[<strong>IVMRSurfaceAllocatorNotify</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrsurfaceallocatornotify)</li>
<li>[<strong>IVMRWindowlessControl</strong>](/windows/desktop/api/Strmif/nn-strmif-ivmrwindowlesscontrol)</li>
</ul></td>
<td>Video Mixing Renderer 7 interfaces.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> </dl>

 

 



