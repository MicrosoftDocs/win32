---
title: Video Buffers
description: Video Buffers
ms.assetid: 0dfe01ec-f997-4e5e-a73d-e6b712d0e19e
keywords:
- WM_CAP_GET_SEQUENCE_SETUP message
- capCaptureGetSetup macro
- WM_CAP_SET_SEQUENCE_SETUP message
- capCaptureSetSetup macro
ms.topic: article
ms.date: 05/31/2018
---

# Video Buffers

The buffers used with video capture reside in the memory heap. The number of buffers used in a capture operation can vary and depend on the value of the **wNumVideoRequested** member of the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure and available system memory.

You can retrieve the current value of requested video buffers by using the [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md) message (or the [**capCaptureGetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturegetsetup) macro). The current requested number of video buffers is stored in the **wNumVideoRequested** member of the **CAPTUREPARMS** structure. You can request the placement and number of buffers by updating this member, and then sending the updated **CAPTUREPARMS** structure to the capture window by using the [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md) message (or the [**capCaptureSetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturesetsetup) macro).

 

 




