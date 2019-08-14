---
title: Measuring Video Quality
description: Measuring Video Quality
ms.assetid: e1e76bed-a632-45e8-a8b3-13dd6969e85a
keywords:
- WM_CAP_GET_SEQUENCE_SETUP message
- capCaptureGetSetup macro
- WM_CAP_SET_SEQUENCE_SETUP message
- capCaptureSetSetup macro
ms.topic: article
ms.date: 05/31/2018
---

# Measuring Video Quality

One way to measure video quality is to limit the number of captured frames dropped during the capture operation. When streaming capture has finished, the quality value is compared with the ratio of dropped frames to total frames. If the percentage of dropped frames is greater than the value of the **wPercentDropForError** member of the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure, AVICap sends an error message to the error callback function if it is installed.

You can retrieve the current limit of dropped frames (expressed as a percentage) by using the [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md) message (or the [**capCaptureGetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturegetsetup) macro). You can set a new limit by specifying a percentage as the value of the **wPercentDropForError** member of the **CAPTUREPARMS** structure, and then sending the updated structure to the capture window by using the [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md) message (or the [**capCaptureSetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturesetsetup) macro). The default value of **wPercentDropForError** is 10 percent.

 

 




