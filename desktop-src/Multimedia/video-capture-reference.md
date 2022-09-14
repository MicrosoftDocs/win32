---
title: Video Capture Reference
description: Video Capture Reference
ms.assetid: 5356c575-2a59-4459-b4eb-76967deb6877
keywords:
- Video for Windows (VFW),video capture reference
- VFW (Video for Windows),video capture reference
- AVICap,reference
ms.topic: article
ms.date: 05/31/2018
---

# Video Capture Reference

This section describes the functions, structures, messages, and macros associated with the AVICap window class. These elements are grouped as follows.

## Basic Capture Operations

-   [**capCreateCaptureWindow**](/windows/desktop/api/Vfw/nf-vfw-capcreatecapturewindowa)
-   [**WM\_CAP\_ABORT**](wm-cap-abort.md)
-   [**WM\_CAP\_DRIVER\_CONNECT**](wm-cap-driver-connect.md)
-   [**WM\_CAP\_SEQUENCE**](wm-cap-sequence.md)
-   [**WM\_CAP\_STOP**](wm-cap-stop.md)

## Capture Windows

-   [**CAPSTATUS**](/windows/win32/api/vfw/ns-vfw-capstatus)
-   [**capGetDriverDescription**](/windows/desktop/api/Vfw/nf-vfw-capgetdriverdescriptiona)
-   [**WM\_CAP\_DRIVER\_CONNECT**](wm-cap-driver-connect.md)
-   [**WM\_CAP\_DRIVER\_DISCONNECT**](wm-cap-driver-disconnect.md)
-   [**WM\_CAP\_GET\_STATUS**](wm-cap-get-status.md)

## Capture Drivers

-   [**CAPDRIVERCAPS**](/windows/win32/api/vfw/ns-vfw-capdrivercaps)
-   [**WM\_CAP\_DRIVER\_GET\_CAPS**](wm-cap-driver-get-caps.md)
-   [**WM\_CAP\_DRIVER\_GET\_NAME**](wm-cap-driver-get-name.md)
-   [**WM\_CAP\_DRIVER\_GET\_VERSION**](wm-cap-driver-get-version.md)
-   [**WM\_CAP\_GET\_AUDIOFORMAT**](wm-cap-get-audioformat.md)
-   [**WM\_CAP\_GET\_VIDEOFORMAT**](wm-cap-get-videoformat.md)
-   [**WM\_CAP\_SET\_AUDIOFORMAT**](wm-cap-set-audioformat.md)
-   [**WM\_CAP\_SET\_VIDEOFORMAT**](wm-cap-set-videoformat.md)

## Capture Driver Preview and Overlay Modes

-   [**WM\_CAP\_SET\_OVERLAY**](wm-cap-set-overlay.md)
-   [**WM\_CAP\_SET\_PREVIEW**](wm-cap-set-preview.md)
-   [**WM\_CAP\_SET\_PREVIEWRATE**](wm-cap-set-previewrate.md)
-   [**WM\_CAP\_SET\_SCALE**](wm-cap-set-scale.md)
-   [**WM\_CAP\_SET\_SCROLL**](wm-cap-set-scroll.md)

## Capture Driver Video Dialog Boxes

-   [**WM\_CAP\_DLG\_VIDEOCOMPRESSION**](wm-cap-dlg-videocompression.md)
-   [**WM\_CAP\_DLG\_VIDEODISPLAY**](wm-cap-dlg-videodisplay.md)
-   [**WM\_CAP\_DLG\_VIDEOFORMAT**](wm-cap-dlg-videoformat.md)
-   [**WM\_CAP\_DLG\_VIDEOSOURCE**](wm-cap-dlg-videosource.md)

## Audio Format

-   [**WM\_CAP\_GET\_AUDIOFORMAT**](wm-cap-get-audioformat.md)
-   [**WM\_CAP\_SET\_AUDIOFORMAT**](wm-cap-set-audioformat.md)

## Video Capture Settings

-   [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms)
-   [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md)
-   [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md)

## Capture File and Buffers

-   [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms)
-   [**WM\_CAP\_FILE\_ALLOCATE**](wm-cap-file-allocate.md)
-   [**WM\_CAP\_FILE\_GET\_CAPTURE\_FILE**](wm-cap-file-get-capture-file.md)
-   [**WM\_CAP\_FILE\_SAVEAS**](wm-cap-file-saveas.md)
-   [**WM\_CAP\_FILE\_SET\_CAPTURE\_FILE**](wm-cap-file-set-capture-file.md)

## Directly Using Capture Data

-   [**WM\_CAP\_SEQUENCE\_NOFILE**](wm-cap-sequence-nofile.md)

## Capture from MCI Device

-   [**WM\_CAP\_SET\_MCI\_DEVICE**](wm-cap-set-mci-device.md)

## Manual Frame Capture

-   [**WM\_CAP\_SINGLE\_FRAME**](wm-cap-single-frame.md)
-   [**WM\_CAP\_SINGLE\_FRAME\_CLOSE**](wm-cap-single-frame-close.md)
-   [**WM\_CAP\_SINGLE\_FRAME\_OPEN**](wm-cap-single-frame-open.md)

## Still-Image Capture

-   [**WM\_CAP\_EDIT\_COPY**](wm-cap-edit-copy.md)
-   [**WM\_CAP\_FILE\_SAVEDIB**](wm-cap-file-savedib.md)
-   [**WM\_CAP\_GRAB\_FRAME**](wm-cap-grab-frame.md)
-   [**WM\_CAP\_GRAB\_FRAME\_NOSTOP**](wm-cap-grab-frame-nostop.md)

## Advanced Capture Options

-   [**WM\_CAP\_FILE\_SET\_INFOCHUNK**](wm-cap-file-set-infochunk.md)
-   [**WM\_CAP\_GET\_USER\_DATA**](wm-cap-get-user-data.md)
-   [**WM\_CAP\_SET\_USER\_DATA**](wm-cap-set-user-data.md)

## Working with Palettes

-   [**WM\_CAP\_EDIT\_COPY**](wm-cap-edit-copy.md)
-   [**WM\_CAP\_PAL\_AUTOCREATE**](wm-cap-pal-autocreate.md)
-   [**WM\_CAP\_PAL\_MANUALCREATE**](wm-cap-pal-manualcreate.md)
-   [**WM\_CAP\_PAL\_OPEN**](wm-cap-pal-open.md)
-   [**WM\_CAP\_PAL\_PASTE**](wm-cap-pal-paste.md)
-   [**WM\_CAP\_PAL\_SAVE**](wm-cap-pal-save.md)

## Yielding to Other Applications

-   [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md)
-   [**WM\_CAP\_SET\_CALLBACK\_YIELD**](wm-cap-set-callback-yield.md)
-   [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md)

## AVICap Callback Functions

-   [**capControlCallback**](/windows/desktop/api/Vfw/nc-vfw-capcontrolcallback)
-   [**capErrorCallback**](/windows/desktop/api/Vfw/nc-vfw-caperrorcallbacka)
-   [**capStatusCallback**](/windows/desktop/api/Vfw/nc-vfw-capstatuscallbacka)
-   [**capVideoStreamCallback**](/windows/desktop/api/Vfw/nc-vfw-capvideocallback)
-   [**capWaveStreamCallback**](/windows/desktop/api/Vfw/nc-vfw-capwavecallback)
-   [**capYieldCallback**](/windows/desktop/api/Vfw/nc-vfw-capyieldcallback)
-   [**WM\_CAP\_SET\_CALLBACK\_CAPCONTROL**](wm-cap-set-callback-capcontrol.md)
-   [**WM\_CAP\_SET\_CALLBACK\_ERROR**](wm-cap-set-callback-error.md)
-   [**WM\_CAP\_SET\_CALLBACK\_FRAME**](wm-cap-set-callback-frame.md)
-   [**WM\_CAP\_SET\_CALLBACK\_STATUS**](wm-cap-set-callback-status.md)
-   [**WM\_CAP\_SET\_CALLBACK\_VIDEOSTREAM**](wm-cap-set-callback-videostream.md)
-   [**WM\_CAP\_SET\_CALLBACK\_WAVESTREAM**](wm-cap-set-callback-wavestream.md)
-   [**WM\_CAP\_SET\_CALLBACK\_YIELD**](wm-cap-set-callback-yield.md)

## Related topics

<dl> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 




