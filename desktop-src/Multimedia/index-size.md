---
title: Index Size
description: Index Size
ms.assetid: 7902589d-5e08-4c0c-9a22-82d28ad2677e
keywords:
- WM_CAP_GET_SEQUENCE_SETUP message
- capCaptureGetSetup macro
- WM_CAP_SET_SEQUENCE_SETUP message
- capCaptureSetSetup macro
ms.topic: article
ms.date: 05/31/2018
---

# Index Size

Each AVI file uses an index of a specified size to locate video and audio data chunks within the file. An entry in the index locates one video frame or waveform-audio buffer. Consequently, the value of the index size indirectly sets the upper limit on the number of frames that can be captured in a file.

You can retrieve the current index size by using the [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md) message (or the [**capCaptureGetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturegetsetup) macro). The current index size is stored in the **dwIndexSize** member of the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure. You can specify a new index size as the value of **dwIndexSize** and then send the updated **CAPTUREPARMS** structure to the capture window by using the [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md) message (or the [**capCaptureSetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturesetsetup) macro). The default index size is 34,952 entries (allowing 32K frames and a proportional number of audio buffers).

 

 




