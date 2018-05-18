---
Description: Interfaces for Video Rendering and Overlay
ms.assetid: 'e4d4e456-61fb-492b-b817-30629681e270'
title: Interfaces for Video Rendering and Overlay
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
<td>[<strong>IAMLine21Decoder</strong>](iamline21decoder.md)</td>
<td>Provides access to closed-captioned information and settings.</td>
</tr>
<tr class="even">
<td>[<strong>IAMOverlayFX</strong>](iamoverlayfx.md)</td>
<td>Apply overlay effects to the video surface. (Deprecated.)</td>
</tr>
<tr class="odd">
<td>[<strong>IAMVideoDecimationProperties</strong>](iamvideodecimationproperties.md)</td>
<td>Control how DirectShow scales a video image if the video window is smaller than the native size of the video. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IBasicVideo2</strong>](ibasicvideo2.md)</td>
<td>Set video properties.</td>
</tr>
<tr class="odd">
<td>[<strong>IDDrawExclModeVideo</strong>](iddrawexclmodevideo.md)</td>
<td>Render video in Microsoft DirectDraw exclusive full-screen mode. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IDDrawExclModeVideoCallback</strong>](iddrawexclmodevideocallback.md)</td>
<td>Callback interface to receive notification about changes to the overlay position, size, and visibility. (Deprecated.)</td>
</tr>
<tr class="odd">
<td>[<strong>IDirectDrawVideo</strong>](idirectdrawvideo.md)</td>
<td>Disable specified DirectDraw capabilities. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IDirectDrawMediaSample</strong>](idirectdrawmediasample.md)</td>
<td>Access a DirectDraw surface allocated by the [Overlay Mixer](overlay-mixer-filter.md) filter.(Deprecated.)</td>
</tr>
<tr class="odd">
<td>[<strong>IMixerOCX</strong>](imixerocx.md)</td>
<td>Implemented on the Overlay Mixer. Enables windowless clients such as ActiveX® controls to get and set properties of the video rectangle and advise the filter of events.</td>
</tr>
<tr class="even">
<td>[<strong>IMixerOCXNotify</strong>](imixerocxnotify.md)</td>
<td>Implemented by windowless clients and called by the Overlay Mixer to send notifications of events affecting the video display rectangle.</td>
</tr>
<tr class="odd">
<td>[<strong>IMixerPinConfig2</strong>](imixerpinconfig2.md)</td>
<td>Set video color controls on the Overlay Mixer filter when mixing multiple video streams. (Deprecated.)</td>
</tr>
<tr class="even">
<td>[<strong>IQualProp</strong>](iqualprop.md)</td>
<td>Query a video renderer for performance information.</td>
</tr>
<tr class="odd">
<td>[<strong>IVideoWindow</strong>](ivideowindow.md)</td>
<td>Set video window properties.</td>
</tr>
<tr class="even">
<td><ul>
<li>[<strong>IVMRAspectRatioControl9</strong>](ivmraspectratiocontrol9.md)</li>
<li>[<strong>IVMRDeinterlaceControl9</strong>](ivmrdeinterlacecontrol9.md)</li>
<li>[<strong>IVMRFilterConfig9</strong>](ivmrfilterconfig9.md)</li>
<li>[<strong>IVMRImageCompositor9</strong>](ivmrimagecompositor9.md)</li>
<li>[<strong>IVMRImagePresenter9</strong>](ivmrimagepresenter9.md)</li>
<li>[<strong>IVMRImagePresenterConfig9</strong>](ivmrimagepresenterconfig9.md)</li>
<li>[<strong>IVMRMixerBitmap9</strong>](ivmrmixerbitmap9.md)</li>
<li>[<strong>IVMRMixerControl9</strong>](ivmrmixercontrol9.md)</li>
<li>[<strong>IVMRMonitorConfig9</strong>](ivmrmonitorconfig9.md)</li>
<li>[<strong>IVMRSurface9</strong>](ivmrsurface9.md)</li>
<li>[<strong>IVMRSurfaceAllocator9</strong>](ivmrsurfaceallocator9.md)</li>
<li>[<strong>IVMRSurfaceAllocatorEx9</strong>](ivmrsurfaceallocatorex9.md)</li>
<li>[<strong>IVMRSurfaceAllocatorNotify9</strong>](ivmrsurfaceallocatornotify9.md)</li>
<li>[<strong>IVMRWindowlessControl9</strong>](ivmrwindowlesscontrol9.md)</li>
</ul></td>
<td>Video Mixing Renderer 9 interfaces.</td>
</tr>
<tr class="odd">
<td><ul>
<li>[<strong>IVMRAspectRatioControl</strong>](ivmraspectratiocontrol.md)</li>
<li>[<strong>IVMRDeinterlaceControl</strong>](ivmrdeinterlacecontrol.md)</li>
<li>[<strong>IVMRFilterConfig</strong>](ivmrfilterconfig.md)</li>
<li>[<strong>IVMRImageCompositor</strong>](ivmrimagecompositor.md)</li>
<li>[<strong>IVMRImagePresenter</strong>](ivmrimagepresenter.md)</li>
<li>[<strong>IVMRImagePresenterConfig</strong>](ivmrimagepresenterconfig.md)</li>
<li>[<strong>IVMRMixerBitmap</strong>](ivmrmixerbitmap.md)</li>
<li>[<strong>IVMRMixerControl</strong>](ivmrmixercontrol.md)</li>
<li>[<strong>IVMRSurfaceAllocator</strong>](ivmrsurfaceallocator.md)</li>
<li>[<strong>IVMRSurfaceAllocatorNotify</strong>](ivmrsurfaceallocatornotify.md)</li>
<li>[<strong>IVMRWindowlessControl</strong>](ivmrwindowlesscontrol.md)</li>
</ul></td>
<td>Video Mixing Renderer 7 interfaces.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> </dl>

 

 



