---
Description: Interfaces for Video Rendering and Overlay
ms.assetid: e4d4e456-61fb-492b-b817-30629681e270
title: Interfaces for Video Rendering and Overlay
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<td>[<strong>IAMLine21Decoder</strong>](/windows/win32/il21dec/nn-il21dec-iamline21decoder?branch=master)</td>
<td>Provides access to closed-captioned information and settings.</td>
</tr>
<tr class="even">
<td>[<strong>IAMOverlayFX</strong>](/windows/win32/Strmif/nn-strmif-iamoverlayfx?branch=master)</td>
<td>Apply overlay effects to the video surface. (Deprecated.)</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVideoDecimationProperties</strong>](/windows/win32/Strmif/nn-strmif-iamvideodecimationproperties?branch=master)</td>
<td>Control how DirectShow scales a video image if the video window is smaller than the native size of the video. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IBasicVideo2</strong>](/windows/win32/Control/nn-control-ibasicvideo2?branch=master)</td>
<td>Set video properties.</td>
</tr>
<tr class="odd">
<td>[<strong>IDDrawExclModeVideo</strong>](/windows/win32/Strmif/nn-strmif-iddrawexclmodevideo?branch=master)</td>
<td>Render video in Microsoft DirectDraw exclusive full-screen mode. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IDDrawExclModeVideoCallback</strong>](/windows/win32/Strmif/nn-strmif-iddrawexclmodevideocallback?branch=master)</td>
<td>Callback interface to receive notification about changes to the overlay position, size, and visibility. (Deprecated.)</td>
</tr>
<tr class="odd">
<td>[<strong>IDirectDrawVideo</strong>](/windows/win32/Amvideo/nn-amvideo-idirectdrawvideo?branch=master)</td>
<td>Disable specified DirectDraw capabilities. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IDirectDrawMediaSample</strong>](/windows/win32/Amstream/nn-amstream-idirectdrawmediasample?branch=master)</td>
<td>Access a DirectDraw surface allocated by the [Overlay Mixer](overlay-mixer-filter.md) filter.(Deprecated.)</td>
</tr>
<tr class="odd">
<td>[<strong>IMixerOCX</strong>](/windows/win32/Mixerocx/nn-mixerocx-imixerocx?branch=master)</td>
<td>Implemented on the Overlay Mixer. Enables windowless clients such as ActiveX® controls to get and set properties of the video rectangle and advise the filter of events.</td>
</tr>
<tr class="even">
<td>[<strong>IMixerOCXNotify</strong>](/windows/win32/Mixerocx/nn-mixerocx-imixerocxnotify?branch=master)</td>
<td>Implemented by windowless clients and called by the Overlay Mixer to send notifications of events affecting the video display rectangle.</td>
</tr>
<tr class="odd">
<td>[<strong>IMixerPinConfig2</strong>](/windows/win32/Mpconfig/nn-mpconfig-imixerpinconfig2?branch=master)</td>
<td>Set video color controls on the Overlay Mixer filter when mixing multiple video streams. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IQualProp</strong>](/windows/win32/Amvideo/nn-amvideo-iqualprop?branch=master)</td>
<td>Query a video renderer for performance information.</td>
</tr>
<tr class="odd">
<td>[<strong>IVideoWindow</strong>](/windows/win32/Control/nn-control-ivideowindow?branch=master)</td>
<td>Set video window properties.</td>
</tr>
<tr class="even">
<td><ul>
<li>[<strong>IVMRAspectRatioControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmraspectratiocontrol9?branch=master)</li>
<li>[<strong>IVMRDeinterlaceControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrdeinterlacecontrol9?branch=master)</li>
<li>[<strong>IVMRFilterConfig9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrfilterconfig9?branch=master)</li>
<li>[<strong>IVMRImageCompositor9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrimagecompositor9?branch=master)</li>
<li>[<strong>IVMRImagePresenter9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrimagepresenter9?branch=master)</li>
<li>[<strong>IVMRImagePresenterConfig9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrimagepresenterconfig9?branch=master)</li>
<li>[<strong>IVMRMixerBitmap9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrmixerbitmap9?branch=master)</li>
<li>[<strong>IVMRMixerControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrmixercontrol9?branch=master)</li>
<li>[<strong>IVMRMonitorConfig9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrmonitorconfig9?branch=master)</li>
<li>[<strong>IVMRSurface9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrsurface9?branch=master)</li>
<li>[<strong>IVMRSurfaceAllocator9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocator9?branch=master)</li>
<li>[<strong>IVMRSurfaceAllocatorEx9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocatorex9?branch=master)</li>
<li>[<strong>IVMRSurfaceAllocatorNotify9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocatornotify9?branch=master)</li>
<li>[<strong>IVMRWindowlessControl9</strong>](/windows/win32/Vmr9/nn-vmr9-ivmrwindowlesscontrol9?branch=master)</li>
</ul></td>
<td>Video Mixing Renderer 9 interfaces.</td>
</tr>
<tr class="odd">
<td><ul>
<li>[<strong>IVMRAspectRatioControl</strong>](/windows/win32/Strmif/nn-strmif-ivmraspectratiocontrol?branch=master)</li>
<li>[<strong>IVMRDeinterlaceControl</strong>](/windows/win32/Strmif/nn-strmif-ivmrdeinterlacecontrol?branch=master)</li>
<li>[<strong>IVMRFilterConfig</strong>](/windows/win32/Strmif/nn-strmif-ivmrfilterconfig?branch=master)</li>
<li>[<strong>IVMRImageCompositor</strong>](/windows/win32/Strmif/nn-strmif-ivmrimagecompositor?branch=master)</li>
<li>[<strong>IVMRImagePresenter</strong>](/windows/win32/Strmif/nn-strmif-ivmrimagepresenter?branch=master)</li>
<li>[<strong>IVMRImagePresenterConfig</strong>](/windows/win32/Strmif/nn-strmif-ivmrimagepresenterconfig?branch=master)</li>
<li>[<strong>IVMRMixerBitmap</strong>](/windows/win32/Strmif/nn-strmif-ivmrmixerbitmap?branch=master)</li>
<li>[<strong>IVMRMixerControl</strong>](/windows/win32/Strmif/nn-strmif-ivmrmixercontrol?branch=master)</li>
<li>[<strong>IVMRSurfaceAllocator</strong>](/windows/win32/Strmif/nn-strmif-ivmrsurfaceallocator?branch=master)</li>
<li>[<strong>IVMRSurfaceAllocatorNotify</strong>](/windows/win32/Strmif/nn-strmif-ivmrsurfaceallocatornotify?branch=master)</li>
<li>[<strong>IVMRWindowlessControl</strong>](/windows/win32/Strmif/nn-strmif-ivmrwindowlesscontrol?branch=master)</li>
</ul></td>
<td>Video Mixing Renderer 7 interfaces.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> </dl>

 

 



