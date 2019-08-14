---
title: Capture Rate
description: Capture Rate
ms.assetid: 70cac7ac-0f7e-431e-a099-b075ba5fb039
keywords:
- WM_CAP_GET_SEQUENCE_SETUP message
- capCaptureGetSetup macro
- CAPTUREPARMS structure
- WM_CAP_SET_SEQUENCE_SETUP message
- capCaptureSetSetup macro
ms.topic: article
ms.date: 05/31/2018
---

# Capture Rate

The capture rate is the number of frames that are captured each second of a capture session. You can retrieve the current capture rate by using the [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md) message (or the [**capCaptureGetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturegetsetup) macro). The current capture rate is stored in the **dwRequestMicroSecPerFrame** member of the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure. You can set the capture rate by specifying the number of microseconds between successive frames as the value of this member, then sending the updated **CAPTUREPARMS** structure to the capture window by using the [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md) message (or the [**capCaptureSetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturesetsetup) macro). The default value of **dwRequestMicroSecPerFrame** is 66667, which corresponds to 15 frames per second.

 

 




