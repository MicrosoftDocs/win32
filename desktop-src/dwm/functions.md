---
title: DWM Functions
description: This section contains information about the Desktop Window Manager (DWM) functions.
ms.assetid: 525807fe-c5d7-4997-87b9-a14d02c33cc3
keywords:
- Desktop Window Manager (DWM),reference
- DWM (Desktop Window Manager),reference
- Desktop Window Manager (DWM),functions
- DWM (Desktop Window Manager),functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DWM Functions

This section contains information about the Desktop Window Manager (DWM) functions.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>DwmAttachMilContent</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmattachmilcontent?branch=master)<br/></td>
<td>This function is not implemented.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmDefWindowProc</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmdefwindowproc?branch=master)<br/></td>
<td>Default window procedure for DWM hit testing within the non-client area.<br/> You also need to ensure that [<strong>DwmDefWindowProc</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmdefwindowproc?branch=master) is called for the [<strong>WM_NCMOUSELEAVE</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645626) message. If <strong>DwmDefWindowProc</strong> is not called for the <strong>WM_NCMOUSELEAVE</strong> message, DWM does not remove the highlighting from the <strong>Maximize</strong>, <strong>Minimize</strong>, and <strong>Close</strong> buttons when the cursor leaves the window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmDetachMilContent</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmdetachmilcontent?branch=master)<br/></td>
<td>This function is not implemented.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmEnableBlurBehindWindow</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmenableblurbehindwindow?branch=master)<br/></td>
<td>Enables the blur effect on a specified window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmEnableComposition</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmenablecomposition?branch=master)<br/></td>
<td>Enables or disables DWM composition. <br/>
<blockquote>
[!Note]<br />
This function is deprecated as of Windows 8. DWM can no longer be programmatically disabled.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmEnableMMCSS</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmenablemmcss?branch=master)<br/></td>
<td>Notifies the DWM to opt in to or out of Multimedia Class Schedule Service (MMCSS) scheduling while the calling process is alive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmExtendFrameIntoClientArea</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmextendframeintoclientarea?branch=master)<br/></td>
<td>Extends the window frame into the client area.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmFlush</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmflush?branch=master)<br/></td>
<td>Issues a flush call that blocks the caller until the next present, when all of the Microsoft DirectX surface updates that are currently outstanding have been made. This compensates for very complex scenes or calling processes with very low priority.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmGetColorizationColor</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmgetcolorizationcolor?branch=master)<br/></td>
<td>Retrieves the current color used for DWM glass composition. This value is based on the current color scheme and can be modified by the user. Applications can listen for color changes by handling the [<strong>WM_DWMCOLORIZATIONCOLORCHANGED</strong>](wm-dwmcolorizationcolorchanged.md) notification.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmGetCompositionTimingInfo</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmgetcompositiontiminginfo?branch=master)<br/></td>
<td>Retrieves the current composition timing information for a specified window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmGetGraphicsStreamClient</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmgetgraphicsstreamclient?branch=master)<br/></td>
<td>This function is not implemented.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmGetGraphicsStreamTransformHint</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmgetgraphicsstreamtransformhint?branch=master)<br/></td>
<td>This function is not implemented.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmGetTransportAttributes</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmgettransportattributes?branch=master)<br/></td>
<td>Retrieves transport attributes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmGetUnmetTabRequirements</strong>](/windows/win32/dwmapi/nf-dwmapi-dwmgetunmettabrequirements?branch=master)<br/></td>
<td><blockquote>
<strong>Note</strong>  This function is publically available, but nonfunctional, for Windows 10, version 1803.
</blockquote>
Checks the requirements needed to get tabs in the application title bar for the specified window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmGetWindowAttribute</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmgetwindowattribute?branch=master)<br/></td>
<td>Retrieves the current value of a specified attribute applied to a window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmInvalidateIconicBitmaps</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwminvalidateiconicbitmaps?branch=master)<br/></td>
<td>Called by an application to indicate that all previously provided iconic bitmaps from a window, both thumbnails and peek representations, should be refreshed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmIsCompositionEnabled</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmiscompositionenabled?branch=master)<br/></td>
<td>Obtains a value that indicates whether DWM composition is enabled. Applications on machines running Windows 7 or earlier can listen for composition state changes by handling the [<strong>WM_DWMCOMPOSITIONCHANGED</strong>](wm-dwmcompositionchanged.md) notification.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmModifyPreviousDxFrameDuration</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmmodifypreviousdxframeduration?branch=master)<br/></td>
<td>Changes the number of monitor refreshes through which the previous frame will be displayed. <br/> [<strong>DwmModifyPreviousDxFrameDuration</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmmodifypreviousdxframeduration?branch=master) is no longer supported. Starting with Windows 8.1, calls to <strong>DwmModifyPreviousDxFrameDuration</strong> always return E_NOTIMPL.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmQueryThumbnailSourceSize</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmquerythumbnailsourcesize?branch=master)<br/></td>
<td>Retrieves the source size of the DWM thumbnail.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmRegisterThumbnail</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmregisterthumbnail?branch=master)<br/></td>
<td>Creates a DWM thumbnail relationship between the destination and source windows.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmRenderGesture</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmrendergesture?branch=master)<br/></td>
<td>Notifies DWM that a touch contact has been recognized as a gesture, and that DWM should draw feedback for that gesture.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmSetDxFrameDuration</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmsetdxframeduration?branch=master)<br/></td>
<td>Sets the number of monitor refreshes through which to display the presented frame. <br/> [<strong>DwmSetDxFrameDuration</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmsetdxframeduration?branch=master) is no longer supported. Starting with Windows 8.1, calls to <strong>DwmSetDxFrameDuration</strong> always return E_NOTIMPL.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmSetIconicLivePreviewBitmap</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmseticoniclivepreviewbitmap?branch=master)<br/></td>
<td>Sets a static, iconic bitmap to display a <em>live preview</em> (also known as a <em>Peek preview</em>) of a window or tab. The taskbar can use this bitmap to show a full-sized preview of a window or tab.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmSetIconicThumbnail</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmseticonicthumbnail?branch=master)<br/></td>
<td>Sets a static, iconic bitmap on a window or tab to use as a thumbnail representation. The taskbar can use this bitmap as a thumbnail switch target for the window or tab.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmSetPresentParameters</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmsetpresentparameters?branch=master)<br/></td>
<td>Sets the present parameters for frame composition. <br/> [<strong>DwmSetPresentParameters</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmsetpresentparameters?branch=master) is no longer supported. Starting with Windows 8.1, calls to <strong>DwmSetPresentParameters</strong> always return E_NOTIMPL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmSetWindowAttribute</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmsetwindowattribute?branch=master)<br/></td>
<td>Sets the value of non-client rendering attributes for a window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmShowContact</strong>](https://msdn.microsoft.com/library/windows/desktop/hh706496)<br/></td>
<td>Called by an app or framework to specify the visual feedback type to draw in response to a particular touch or pen contact.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmTetherContact</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmtethercontact?branch=master)<br/></td>
<td>Enables the graphical feedback of touch and drag interactions to the user.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmTransitionOwnedWindow</strong>](https://msdn.microsoft.com/library/windows/desktop/hh405360)<br/></td>
<td>Coordinates the animations of tool windows with the DWM.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmUnregisterThumbnail</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmunregisterthumbnail?branch=master)<br/></td>
<td>Removes a DWM thumbnail relationship created by the [<strong>DwmRegisterThumbnail</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmregisterthumbnail?branch=master) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmUpdateThumbnailProperties</strong>](/windows/win32/Dwmapi/nf-dwmapi-dwmupdatethumbnailproperties?branch=master)<br/></td>
<td>Updates the properties for a DWM thumbnail.<br/></td>
</tr>
</tbody>
</table>



 

 

 





