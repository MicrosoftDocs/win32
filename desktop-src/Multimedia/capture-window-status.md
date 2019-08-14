---
title: Capture Window Status
description: Capture Window Status
ms.assetid: c3f80cac-30b2-42f0-8a9c-4053728c558b
keywords:
- WM_CAP_GET_STATUS message
- capGetStatus macro
- CAPSTATUS structure
ms.topic: article
ms.date: 05/31/2018
---

# Capture Window Status

You can retrieve the current status of a capture window by using the [**WM\_CAP\_GET\_STATUS**](wm-cap-get-status.md) message (or the [**capGetStatus**](/windows/desktop/api/Vfw/nf-vfw-capgetstatus) macro). This message retrieves a copy of the [**CAPSTATUS**](/windows/win32/api/vfw/ns-vfw-capstatus) structure with the current values of its members. The **CAPSTATUS** structure contains information regarding the dimensions of the image, scroll position, and whether overlay or preview of the image is enabled. Because the information represented in **CAPSTATUS** is dynamic, your application should refresh the contents of the structure whenever the size or format of the captured video stream might have changed (such as after displaying the video format of the capture driver).

Changing the dimensions of the capture window has no effect on the dimensions of the actual captured video stream. The format dialog box displayed by the video capture device driver controls the dimensions of the captured video stream.

 

 




