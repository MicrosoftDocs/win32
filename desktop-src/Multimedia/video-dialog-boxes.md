---
title: Video Dialog Boxes
description: Video Dialog Boxes
ms.assetid: 65f0d8de-c782-4d91-b38e-b36445f07af3
keywords:
- WM_CAP_DLG_VIDEOSOURCE message
- capDlgVideoSource macro
- WM_CAP_DLG_VIDEOFORMAT message
- capDlgVideoFormat macro
- WM_CAP_DLG_VIDEODISPLAY message
- capDlgVideoDisplay macro
- WM_CAP_DLG_VIDEOCOMPRESSION message
- capDlgVideoCompression macro
ms.topic: article
ms.date: 05/31/2018
---

# Video Dialog Boxes

Each capture driver can provide up to four dialog boxes to control aspects of the video digitization and capture process, and to define compression attributes used in reducing the size of the video data. The contents of these dialog boxes are defined by the video capture driver.

The Video Source dialog box controls the selection of video input channels and parameters affecting the video image being digitized in the frame buffer. This dialog box enumerates the types of signals that connect the video source to the capture card (typically SVHS and composite inputs), and provides controls to change hue, contrast, or saturation. If the dialog box is supported by a video capture driver, you can display and update it by using the [**WM\_CAP\_DLG\_VIDEOSOURCE**](wm-cap-dlg-videosource.md) message (or the [**capDlgVideoSource**](/windows/desktop/api/Vfw/nf-vfw-capdlgvideosource) macro).

The Video Format dialog box controls selection of the digitized video frame dimensions and image-depth, and compression options of the captured video. If the dialog box is supported by a video capture driver, you can display and update it by using the [**WM\_CAP\_DLG\_VIDEOFORMAT**](wm-cap-dlg-videoformat.md) message (or the [**capDlgVideoFormat**](/windows/desktop/api/Vfw/nf-vfw-capdlgvideoformat) macro).

The Video Display dialog box controls the appearance of the video on the monitor during capture. The controls in this dialog box have no effect on the digitized video data, but they might affect the presentation of the digitized signal. For example, capture devices that support overlay might allow altering hue and saturation, key color, or alignment of the overlay. If the dialog box is supported by a video capture driver, you can display and update it by using the [**WM\_CAP\_DLG\_VIDEODISPLAY**](wm-cap-dlg-videodisplay.md) message (or the [**capDlgVideoDisplay**](/windows/desktop/api/Vfw/nf-vfw-capdlgvideodisplay) macro).

The Video Compression dialog box controls the post-capture video compression attributes. If the dialog box is supported by a video capture driver, you can display and update it by using the [**WM\_CAP\_DLG\_VIDEOCOMPRESSION**](wm-cap-dlg-videocompression.md) message (or the [**capDlgVideoCompression**](/windows/desktop/api/Vfw/nf-vfw-capdlgvideocompression) macro).

 

 




