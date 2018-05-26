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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Capture Settings

The [**CAPTUREPARMS**](/windows/win32/Vfw/ns-vfw-tagcaptureparms?branch=master) structure contains the control parameters for streaming video capture. This structure controls several aspects of the capture process, and allows you to perform the following tasks:

-   Specify the frame rate.
-   Specify the number of allocated video buffers.
-   Disable and enable audio capture.
-   Specify the time interval for the capture.
-   Specify whether an MCI device (VCR or videodisc) is used during capture.
-   Specify keyboard or mouse control for ending streaming.
-   Specify the type of video averaging applied during capture.

You can retrieve the current capture settings within the [**CAPTUREPARMS**](/windows/win32/Vfw/ns-vfw-tagcaptureparms?branch=master) structure by sending the [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md) message (or the [**capCaptureGetSetup**](/windows/win32/Vfw/nf-vfw-capcapturegetsetup?branch=master) macro) to a capture window. You can set one or more current capture settings by updating the appropriate members of the **CAPTUREPARMS** structure and then sending the [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md) message (or the [**capCaptureSetSetup**](/windows/win32/Vfw/nf-vfw-capcapturesetsetup?branch=master) macro) and **CAPTUREPARMS** to a capture window.

 

 




