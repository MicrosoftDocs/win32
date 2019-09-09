---
title: Video Capture Settings
description: Video Capture Settings
ms.assetid: f5c887ca-9430-4221-8748-5b389247b7a4
keywords:
- CAPTUREPARMS structure
- WM_CAP_GET_SEQUENCE_SETUP message
- capCaptureGetSetup macro
- WM_CAP_SET_SEQUENCE_SETUP message
- capCaptureSetSetup macro
ms.topic: article
ms.date: 05/31/2018
---

# Video Capture Settings

The [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure contains the control parameters for streaming video capture. This structure controls several aspects of the capture process, and allows you to perform the following tasks:

-   Specify the frame rate.
-   Specify the number of allocated video buffers.
-   Disable and enable audio capture.
-   Specify the time interval for the capture.
-   Specify whether an MCI device (VCR or videodisc) is used during capture.
-   Specify keyboard or mouse control for ending streaming.
-   Specify the type of video averaging applied during capture.

You can retrieve the current capture settings within the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure by sending the [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md) message (or the [**capCaptureGetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturegetsetup) macro) to a capture window. You can set one or more current capture settings by updating the appropriate members of the **CAPTUREPARMS** structure and then sending the [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md) message (or the [**capCaptureSetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturesetsetup) macro) and **CAPTUREPARMS** to a capture window.

 

 




