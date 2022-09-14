---
title: Preview and Overlay Modes
description: Preview and Overlay Modes
ms.assetid: 11e7848f-efda-452c-a9c7-405e636a2ead
keywords:
- WM_CAP_SET_PREVIEW message
- capPreview macro
- WM_CAP_SET_PREVIEWRATE message
- capPreviewRate macro
- WM_CAP_SET_SCALE message
- capPreviewScale macro
ms.topic: article
ms.date: 05/31/2018
---

# Preview and Overlay Modes

A capture driver can implement two methods for viewing an incoming video stream: preview mode and overlay mode. If a capture driver implements both methods, the user can choose which method to use.

Preview mode transfers digitized frames from the capture hardware to system memory and then displays the digitized frames in the capture window by using graphics device interface (GDI) functions. Applications might decrease the preview rate when the parent window loses focus, and increase the preview rate when the parent window gains focus. This action improves general system responsiveness because the preview operation is processor intensive.

There are three messages to control the preview operation.

-   Use the [**WM\_CAP\_SET\_PREVIEW**](wm-cap-set-preview.md) message to enable or disable preview mode by sending the (or the [**capPreview**](/windows/desktop/api/Vfw/nf-vfw-cappreview) macro) to a capture window.
-   Use the [**WM\_CAP\_SET\_PREVIEWRATE**](wm-cap-set-previewrate.md) message (or the [**capPreviewRate**](/windows/desktop/api/Vfw/nf-vfw-cappreviewrate) macro) to set the rate at which frames are displayed in preview mode
-   Use the [**WM\_CAP\_SET\_SCALE**](wm-cap-set-scale.md) message (or the [**capPreviewScale**](/windows/desktop/api/Vfw/nf-vfw-cappreviewscale) macro) to enable or disable scaling of the preview video.

When preview and scaling are both enabled, the captured video frame is stretched to the dimensions of the capture window. Enabling preview mode automatically disables overlay mode.

Overlay mode is a hardware function that displays the contents of the capture buffer on the monitor without using CPU resources. You can enable and disable overlay mode by sending the [**WM\_CAP\_SET\_OVERLAY**](wm-cap-set-overlay.md) message (or the [**capOverlay**](/windows/desktop/api/Vfw/nf-vfw-capoverlay) macro) to a capture window. Enabling overlay mode automatically disables preview mode.

You can also set the scroll position of the video frame within the client area of the capture window for preview mode or overlay mode by sending the [**WM\_CAP\_SET\_SCROLL**](wm-cap-set-scroll.md) message (or the [**capSetScrollPos**](/windows/desktop/api/Vfw/nf-vfw-capsetscrollpos) macro) to a capture window.

 

 




