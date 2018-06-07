---
title: DWM Functions
description: This section contains information about the Desktop Window Manager (DWM) functions.
ms.assetid: 525807fe-c5d7-4997-87b9-a14d02c33cc3
keywords:
- Desktop Window Manager (DWM),reference
- DWM (Desktop Window Manager),reference
- Desktop Window Manager (DWM),functions
- DWM (Desktop Window Manager),functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<td>[<strong>DwmAttachMilContent</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmattachmilcontent)<br/></td>
<td>This function is not implemented.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmDefWindowProc</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmdefwindowproc)<br/></td>
<td>Default window procedure for DWM hit testing within the non-client area.<br/> You also need to ensure that [<strong>DwmDefWindowProc</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmdefwindowproc) is called for the [<strong>WM_NCMOUSELEAVE</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645626) message. If <strong>DwmDefWindowProc</strong> is not called for the <strong>WM_NCMOUSELEAVE</strong> message, DWM does not remove the highlighting from the <strong>Maximize</strong>, <strong>Minimize</strong>, and <strong>Close</strong> buttons when the cursor leaves the window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmDetachMilContent</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmdetachmilcontent)<br/></td>
<td>This function is not implemented.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmEnableBlurBehindWindow</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmenableblurbehindwindow)<br/></td>
<td>Enables the blur effect on a specified window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmEnableComposition</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmenablecomposition)<br/></td>
<td>Enables or disables DWM composition. <br/>
<blockquote>
[!Note]<br />
This function is deprecated as of Windows 8. DWM can no longer be programmatically disabled.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmEnableMMCSS</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmenablemmcss)<br/></td>
<td>Notifies the DWM to opt in to or out of Multimedia Class Schedule Service (MMCSS) scheduling while the calling process is alive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmExtendFrameIntoClientArea</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmextendframeintoclientarea)<br/></td>
<td>Extends the window frame into the client area.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmFlush</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmflush)<br/></td>
<td>Issues a flush call that blocks the caller until the next present, when all of the Microsoft DirectX surface updates that are currently outstanding have been made. This compensates for very complex scenes or calling processes with very low priority.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmGetColorizationColor</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmgetcolorizationcolor)<br/></td>
<td>Retrieves the current color used for DWM glass composition. This value is based on the current color scheme and can be modified by the user. Applications can listen for color changes by handling the [<strong>WM_DWMCOLORIZATIONCOLORCHANGED</strong>](wm-dwmcolorizationcolorchanged.md) notification.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmGetCompositionTimingInfo</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmgetcompositiontiminginfo)<br/></td>
<td>Retrieves the current composition timing information for a specified window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmGetGraphicsStreamClient</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmgetgraphicsstreamclient)<br/></td>
<td>This function is not implemented.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmGetGraphicsStreamTransformHint</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmgetgraphicsstreamtransformhint)<br/></td>
<td>This function is not implemented.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmGetTransportAttributes</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmgettransportattributes)<br/></td>
<td>Retrieves transport attributes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmGetUnmetTabRequirements</strong>](/windows/desktop/api/dwmapi/nf-dwmapi-dwmgetunmettabrequirements)<br/></td>
<td><blockquote>
<strong>Note</strong>  This function is publically available, but nonfunctional, for Windows 10, version 1803.
</blockquote>
Checks the requirements needed to get tabs in the application title bar for the specified window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmGetWindowAttribute</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmgetwindowattribute)<br/></td>
<td>Retrieves the current value of a specified attribute applied to a window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmInvalidateIconicBitmaps</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwminvalidateiconicbitmaps)<br/></td>
<td>Called by an application to indicate that all previously provided iconic bitmaps from a window, both thumbnails and peek representations, should be refreshed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmIsCompositionEnabled</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmiscompositionenabled)<br/></td>
<td>Obtains a value that indicates whether DWM composition is enabled. Applications on machines running Windows 7 or earlier can listen for composition state changes by handling the [<strong>WM_DWMCOMPOSITIONCHANGED</strong>](wm-dwmcompositionchanged.md) notification.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmModifyPreviousDxFrameDuration</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmmodifypreviousdxframeduration)<br/></td>
<td>Changes the number of monitor refreshes through which the previous frame will be displayed. <br/> [<strong>DwmModifyPreviousDxFrameDuration</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmmodifypreviousdxframeduration) is no longer supported. Starting with Windows 8.1, calls to <strong>DwmModifyPreviousDxFrameDuration</strong> always return E_NOTIMPL.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmQueryThumbnailSourceSize</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmquerythumbnailsourcesize)<br/></td>
<td>Retrieves the source size of the DWM thumbnail.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmRegisterThumbnail</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmregisterthumbnail)<br/></td>
<td>Creates a DWM thumbnail relationship between the destination and source windows.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmRenderGesture</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmrendergesture)<br/></td>
<td>Notifies DWM that a touch contact has been recognized as a gesture, and that DWM should draw feedback for that gesture.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmSetDxFrameDuration</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmsetdxframeduration)<br/></td>
<td>Sets the number of monitor refreshes through which to display the presented frame. <br/> [<strong>DwmSetDxFrameDuration</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmsetdxframeduration) is no longer supported. Starting with Windows 8.1, calls to <strong>DwmSetDxFrameDuration</strong> always return E_NOTIMPL.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmSetIconicLivePreviewBitmap</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmseticoniclivepreviewbitmap)<br/></td>
<td>Sets a static, iconic bitmap to display a <em>live preview</em> (also known as a <em>Peek preview</em>) of a window or tab. The taskbar can use this bitmap to show a full-sized preview of a window or tab.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmSetIconicThumbnail</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmseticonicthumbnail)<br/></td>
<td>Sets a static, iconic bitmap on a window or tab to use as a thumbnail representation. The taskbar can use this bitmap as a thumbnail switch target for the window or tab.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmSetPresentParameters</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmsetpresentparameters)<br/></td>
<td>Sets the present parameters for frame composition. <br/> [<strong>DwmSetPresentParameters</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmsetpresentparameters) is no longer supported. Starting with Windows 8.1, calls to <strong>DwmSetPresentParameters</strong> always return E_NOTIMPL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmSetWindowAttribute</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmsetwindowattribute)<br/></td>
<td>Sets the value of non-client rendering attributes for a window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmShowContact</strong>](https://msdn.microsoft.com/library/windows/desktop/hh706496)<br/></td>
<td>Called by an app or framework to specify the visual feedback type to draw in response to a particular touch or pen contact.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmTetherContact</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmtethercontact)<br/></td>
<td>Enables the graphical feedback of touch and drag interactions to the user.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmTransitionOwnedWindow</strong>](https://msdn.microsoft.com/library/windows/desktop/hh405360)<br/></td>
<td>Coordinates the animations of tool windows with the DWM.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DwmUnregisterThumbnail</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmunregisterthumbnail)<br/></td>
<td>Removes a DWM thumbnail relationship created by the [<strong>DwmRegisterThumbnail</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmregisterthumbnail) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DwmUpdateThumbnailProperties</strong>](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmupdatethumbnailproperties)<br/></td>
<td>Updates the properties for a DWM thumbnail.<br/></td>
</tr>
</tbody>
</table>



 

 

 





