---
title: Still-Image Capture
description: Still-Image Capture
ms.assetid: 9e84b385-aedb-4132-8a2d-72c32594083a
keywords:
- WM_CAP_GRAB_FRAME_NOSTOP message
- WM_CAP_GRAB_FRAME message
- capGrabFrameNoStop macro
- capGrabFrame macro
- WM_CAP_EDIT_COPY message
- capEditCopy macro
- WM_CAP_FILE_SAVEDIB message
- capFileSaveDIB macro
ms.topic: article
ms.date: 05/31/2018
---

# Still-Image Capture

If you want to capture a single frame as a still image, you can use the [**WM\_CAP\_GRAB\_FRAME\_NOSTOP**](wm-cap-grab-frame-nostop.md) or [**WM\_CAP\_GRAB\_FRAME**](wm-cap-grab-frame.md) message (or the [**capGrabFrameNoStop**](/windows/desktop/api/Vfw/nf-vfw-capgrabframenostop) or [**capGrabFrame**](/windows/desktop/api/Vfw/nf-vfw-capgrabframe) macro) to capture the digitized image in an internal frame buffer. You can freeze the display on the captured image by using WM\_CAP\_GRAB\_FRAME. Otherwise, use WM\_CAP\_GRAB\_FRAME\_NOSTOP.

Once captured, you can copy the image for use by other applications. You can copy an image from the frame buffer to the clipboard by using the [**WM\_CAP\_EDIT\_COPY**](wm-cap-edit-copy.md) message (or the [**capEditCopy**](/windows/desktop/api/Vfw/nf-vfw-capeditcopy) macro). You can also copy the image from the frame buffer to a device-independent bitmap (DIB) by using the [**WM\_CAP\_FILE\_SAVEDIB**](wm-cap-file-savedib.md) message (or the [**capFileSaveDIB**](/windows/desktop/api/Vfw/nf-vfw-capfilesavedib) macro).

Your application can also use the two single-frame capture messages to edit a sequence frame by frame, or to create a time-lapse photography sequence.

 

 




