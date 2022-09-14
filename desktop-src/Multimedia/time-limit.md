---
title: Time Limit
description: Time Limit
ms.assetid: 7c07755b-ba4d-4ec0-82ee-f76a533c6c5b
keywords:
- CAPTUREPARMS structure
- WM_CAP_GET_SEQUENCE_SETUP message
- capCaptureGetSetup macro
- CAPTUREPARMS structure
- WM_CAP_SET_SEQUENCE_SETUP message
- capCaptureSetSetup macro
ms.topic: article
ms.date: 05/31/2018
---

# Time Limit

You can limit the duration of a capture operation by using the **fLimitEnabled** and **wTimeLimit** members of the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure. The **fLimitEnabled** member indicates whether the capture operation is to be timed, while **wTimeLimit** specifies the maximum duration of the capture operation.

You can retrieve the values for **fLimitEnabled** and **wTimeLimit** by using the [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md) message (or the [**capCaptureGetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturegetsetup) macro). You can enable a timer for the capture operation by specifying **TRUE** as the value of **fLimitEnabled**, or you can set the duration of the capture operation by specifying a value, in seconds, for **wTimeLimit**. After you set these members, send the updated [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure to the capture window by using the [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md) message (or the [**capCaptureSetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturesetsetup) macro). The default value of **fLimitEnabled** is **FALSE**.

 

 




