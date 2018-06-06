---
Description: Describes the relationship between the adapter refresh rate and the rate at which Present or Present operations are completed. These values also serve as flag values for the PresentationIntervals field of D3DCAPS9.
ms.assetid: a7d774c1-93c0-47d8-a8a7-e66e394726a3
title: D3DPRESENT
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DPRESENT

Describes the relationship between the adapter refresh rate and the rate at which [**Present**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-present) or [**Present**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3dswapchain9-present) operations are completed. These values also serve as flag values for the PresentationIntervals field of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-_d3dcaps9).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="D3DPRESENT_DONOTFLIP"></span><span id="d3dpresent_donotflip"></span><dl> <dt><strong>D3DPRESENT_DONOTFLIP</strong></dt> </dl></td>
<td style="text-align: left;">Use the front buffer as both the source and target surface during rendering. A frame synch is scheduled but the displayed surface does not change. This flag is only available when the application is in fullscreen mode and D3DSWAPEFFECT_FLIPEX has been specified. <br/> This flag is available in Direct3D 9Ex only.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="D3DPRESENT_DONOTWAIT"></span><span id="d3dpresent_donotwait"></span><dl> <dt><strong>D3DPRESENT_DONOTWAIT</strong></dt> </dl></td>
<td style="text-align: left;">A presentation cannot be scheduled by a hal device. If this flag is set in a call to [<strong>Present</strong>](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3dswapchain9-present), and the hardware is busy processing or waiting for a vertical sync interval, then Present will return D3DERR_WASSTILLDRAWING to indicate that the blit operation is incomplete.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="D3DPRESENT_FLIPRESTART"></span><span id="d3dpresent_fliprestart"></span><dl> <dt><strong>D3DPRESENT_FLIPRESTART</strong></dt> </dl></td>
<td style="text-align: left;">Reserved.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="D3DPRESENT_FORCEIMMEDIATE"></span><span id="d3dpresent_forceimmediate"></span><dl> <dt><strong>D3DPRESENT_FORCEIMMEDIATE</strong></dt> </dl></td>
<td style="text-align: left;">D3DPRESENT_INTERVAL_IMMEDIATE is enforced on this [<strong>Present</strong>](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3dswapchain9-present) call. This flag can only be specified when using D3DSWAPEFFECT_FLIPEX. Windowed and fullscreen presentation behaviors are the same. This is especially useful for media apps that want to discard frames that have been detected as late and present subsequent frames at composition time. An invalid parameter error will be returned if this flag is improperly specified. When multiple consecutive frames with D3DPRESENT_FORCEIMMEDIATEs are queued, only the last frame is displayed, for both windowed and fullscreen presentation. A sample application that uses D3DPRESENT_FORCEIMMEDIATE and D3DSWAPEFFECT_FLIPEX is the [D3D9ExFlipEx sample on the MSDN Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=179115). <br/> This flag is available in Direct3D 9Ex on Windows 7 or later operating systems.<br/> When using D3DSWAPEFFECT_FLIPEX, each frame presented using D3DPRESENT_INTERVAL_IMMEDIATE or D3DPRESENT_INTERVAL_FORCEIMMEDIATE will override the previous frame's present interval. For example, if you queue the following frames using the following swap effects: frame A (D3DPRESENT_INTERVAL_ONE), frame B(D3DPRESENT_INTERVAL_ONE), frame C(D3DPRESENT_INTERVAL_ONE), frame D(D3DPRESENT_INTERVAL_FORCEIMMEDIATE), frame D will override frame C's present interval. The displayed frames per present interval are frame A, frame B, (frame C overridden by) frame D.<br/> See Remarks.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="D3DPRESENT_INTERVAL_DEFAULT"></span><span id="d3dpresent_interval_default"></span><dl> <dt><strong>D3DPRESENT_INTERVAL_DEFAULT</strong></dt> </dl></td>
<td style="text-align: left;">This is nearly equivalent to D3DPRESENT_INTERVAL_ONE. See remarks.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="D3DPRESENT_INTERVAL_ONE"></span><span id="d3dpresent_interval_one"></span><dl> <dt><strong>D3DPRESENT_INTERVAL_ONE</strong></dt> </dl></td>
<td style="text-align: left;">The driver will wait for the vertical retrace period (the runtime will &quot;beam follow&quot; to prevent tearing). [<strong>Present</strong>](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-present) operations will not be affected more frequently than the screen refresh; the runtime will complete at most one Present operation per adapter refresh period. This is equivalent to using D3DSWAPEFFECT_COPYVSYNC in DirectX 8.1. This option is always available for both windowed and full-screen swap chains. See remarks.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="D3DPRESENT_INTERVAL_TWO"></span><span id="d3dpresent_interval_two"></span><dl> <dt><strong>D3DPRESENT_INTERVAL_TWO</strong></dt> </dl></td>
<td style="text-align: left;">The driver will wait for the vertical retrace period. [<strong>Present</strong>](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-present) operations will not be affected more frequently than every second screen refresh. Check the PresentationIntervals cap (see [<strong>D3DCAPS9</strong>](/windows/desktop/api/D3D9Caps/ns-d3d9caps-_d3dcaps9)) to see if D3DPRESENT_INTERVAL_TWO is supported by the driver.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="D3DPRESENT_INTERVAL_THREE"></span><span id="d3dpresent_interval_three"></span><dl> <dt><strong>D3DPRESENT_INTERVAL_THREE</strong></dt> </dl></td>
<td style="text-align: left;">The driver will wait for the vertical retrace period. [<strong>Present</strong>](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-present) operations will not be affected more frequently than every third screen refresh. Check the PresentationIntervals cap (see [<strong>D3DCAPS9</strong>](/windows/desktop/api/D3D9Caps/ns-d3d9caps-_d3dcaps9)) to see if D3DPRESENT_INTERVAL_THREE is supported by the driver.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="D3DPRESENT_INTERVAL_FOUR"></span><span id="d3dpresent_interval_four"></span><dl> <dt><strong>D3DPRESENT_INTERVAL_FOUR</strong></dt> </dl></td>
<td style="text-align: left;">The driver will wait for the vertical retrace period. [<strong>Present</strong>](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-present) operations will not be affected more frequently than every fourth screen refresh. Check the PresentationIntervals member (see [<strong>D3DCAPS9</strong>](/windows/desktop/api/D3D9Caps/ns-d3d9caps-_d3dcaps9)) to see if D3DPRESENT_INTERVAL_FOUR is supported by the driver.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="D3DPRESENT_INTERVAL_IMMEDIATE"></span><span id="d3dpresent_interval_immediate"></span><dl> <dt><strong>D3DPRESENT_INTERVAL_IMMEDIATE</strong></dt> </dl></td>
<td style="text-align: left;">The runtime updates the window client area immediately and might do so more than once during the adapter refresh period. This is equivalent to using D3DSWAPEFFECT_COPY in DirectX 8. [<strong>Present</strong>](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-present) operations might be affected immediately. This option is always available for both windowed and full-screen swap chains. See remarks.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="D3DPRESENT_LINEAR_CONTENT"></span><span id="d3dpresent_linear_content"></span><dl> <dt><strong>D3DPRESENT_LINEAR_CONTENT</strong></dt> </dl></td>
<td style="text-align: left;">The content of the back buffer to be presented is in the linear color space. <br/>
<ul>
<li>The presentation will implicitly convert from linear space to sRGB (gamma = 2.2). This is the only conversion that is supported.</li>
<li>Because this flag represents a property of the content of the back buffer, the flag can be specified during an [<strong>Present</strong>](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3dswapchain9-present) call. In other words, an application can present linear content in one frame, and then switch to corrected content in the next.</li>
<li>This flag is ignored when the swap chain is full screen. (Note that this flag is available only on the explicit swap chain version of [<strong>Present</strong>](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3dswapchain9-present). The [<strong>Present</strong>](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-present) method does not take a flags parameter.)</li>
<li>This flag is always accepted, but will only take effect when the driver exposes &gt;D3DCAPS3_LINEAR_TO_SRGB_PresentATION.</li>
<li>The only back buffer format supported is [X8R8G8B8](d3dformat.md).</li>
</ul>
See [Windowed Swap Chains](gamma.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="D3DPRESENT_VIDEO_RESTRICT_TO_MONITOR"></span><span id="d3dpresent_video_restrict_to_monitor"></span><dl> <dt><strong>D3DPRESENT_VIDEO_RESTRICT_TO_MONITOR</strong></dt> </dl></td>
<td style="text-align: left;">Clips the rendered contents to the monitor/device the adapter is targeting, shows thumbnails for the content in the Flip3D view and taskbar thumbnails on other monitors. <br/> This flag is available in Direct3D 9Ex only.<br/> See [Desktop Window Manager](https://msdn.microsoft.com/VS|winui|~\winui\desktopwindowmanager\overviews\dwm_overview.htm) for further details on this feature of Windows Vista. If you are not running in desktop composition mode, the flag gives the same behavior as [D3DPRESENTFLAG_DEVICECLIP](d3dpresentflag.md).<br/>
<blockquote>
[!Note]<br />
This flag should only be used with swap effect D3DSWAPEFFECT_FLIPEX. The use of this flag with <em>other</em> swap effects is being deprecated, and may not work in future versions of Windows.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="D3DPRESENT_UPDATEOVERLAYONLY"></span><span id="d3dpresent_updateoverlayonly"></span><dl> <dt><strong>D3DPRESENT_UPDATEOVERLAYONLY</strong></dt> </dl></td>
<td style="text-align: left;">Updates the overlay position or the colorkey data without causing an actual flip and without changing the duration with which the image is displayed.<br/> This flag is available in Direct3D 9Ex only.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="D3DPRESENT_HIDEOVERLAY"></span><span id="d3dpresent_hideoverlay"></span><dl> <dt><strong>D3DPRESENT_HIDEOVERLAY</strong></dt> </dl></td>
<td style="text-align: left;">Turns off the overlay hardware.<br/> This flag is available in Direct3D 9Ex only.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="D3DPRESENT_UPDATECOLORKEY"></span><span id="d3dpresent_updatecolorkey"></span><dl> <dt><strong>D3DPRESENT_UPDATECOLORKEY</strong></dt> </dl></td>
<td style="text-align: left;">Redraws the colorkey data.<br/> This flag is available in Direct3D 9Ex only.<br/></td>
</tr>
</tbody>
</table>



## Remarks

Windowed mode supports D3DPRESENT\_INTERVAL\_DEFAULT, D3DPRESENT\_INTERVAL\_IMMEDIATE, and D3DPRESENT\_INTERVAL\_ONE. D3DPRESENT\_INTERVAL\_DEFAULT and the D3DPRESENT\_INTERVAL\_ONE are nearly equivalent (see the information regarding timer resolution below). They perform similarly to COPY\_VSYNC in that there is only one present per frame, and they prevent tearing with beam-following. In contrast, D3DPRESENT\_INTERVAL\_IMMEDIATE will attempt to provide an unlimited presentation rate.

Full-screen mode supports similar usage as windowed mode by supporting D3DPRESENT\_INTERVAL\_IMMEDIATE regardless of the refresh rate or swap effect. D3DPRESENT\_INTERVAL\_DEFAULT uses the default system timer resolution whereas the D3DPRESENT\_INTERVAL\_ONE calls [**timeBeginPeriod**](https://msdn.microsoft.com/7168981c-9af8-4665-88a2-7d96a8f2b273) to enhance system timer resolution. This improves the quality of vertical sync, but consumes slightly more processing time. Both parameters attempt to synchronize vertically.

## Requirements



|                   |                                                                                   |
|-------------------|-----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 




