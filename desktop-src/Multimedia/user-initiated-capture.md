---
title: User-Initiated Capture
description: User-Initiated Capture
ms.assetid: e0d245f3-ac79-42c4-9969-8c9ec66eac62
keywords:
- WM_CAP_GET_SEQUENCE_SETUP message
- capCaptureGetSetup macro
ms.topic: article
ms.date: 05/31/2018
---

# User-Initiated Capture

You can retrieve the current value of the user-initiated capture flag by using the [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md) message (or the [**capCaptureGetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturegetsetup) macro). The value of the flag is stored in the **fMakeUserHitOKToCapture** member of the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure. You can provide the user with precise control over when to start a capture session by setting this member to **TRUE**. AVICap displays a dialog box after allocating all video and audio buffers for a capture session. This lets the user eliminate capture delays because of software initialization. If your application uses a small number of video buffers, this dialog box is probably unnecessary. The default value is **FALSE**.

 

 




