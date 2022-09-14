---
title: Keys Ending Capture
description: Keys Ending Capture
ms.assetid: 932ed4ee-0928-41f7-a242-8b7435313647
keywords:
- WM_CAP_GET_SEQUENCE_SETUP message
- capCaptureGetSetup macro
- CAPTUREPARMS structure
- WM_CAP_SET_SEQUENCE_SETUP message
- capCaptureSetSetup macro
ms.topic: article
ms.date: 05/31/2018
---

# Keys Ending Capture

You can allow the user to abort a capture session by pressing a key or keystroke combination from the keyboard, or by pressing the right or left mouse button. If the user aborts a real-time capture session, the contents of the capture file are discarded. If the user aborts a step-frame capture session, the contents of the capture file up to the point of aborting the capture are saved.

You can retrieve the settings for aborting a capture session by using the [**WM\_CAP\_GET\_SEQUENCE\_SETUP**](wm-cap-get-sequence-setup.md) message (or the [**capCaptureGetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturegetsetup) macro). The current keystroke setting is stored in the **vKeyAbort** member of the [**CAPTUREPARMS**](/windows/win32/api/vfw/ns-vfw-captureparms) structure; the current mouse settings are stored in the **fAbortLeftMouse** and **fAbortRightMouse** members. You can set a new key or keystroke combination by specifying the keycode or keycode combination (as in a CTRL or SHIFT key combination) as the value of **vKeyAbort**, or set the left or right mouse button as the abort key by specifying the **fAbortLeftMouse** or **fAbortRightMouse** member. After you set these members, send the updated **CAPTUREPARMS** structure to the capture window by using the [**WM\_CAP\_SET\_SEQUENCE\_SETUP**](wm-cap-set-sequence-setup.md) message (or the [**capCaptureSetSetup**](/windows/desktop/api/Vfw/nf-vfw-capcapturesetsetup) macro). The default value of **vKeyAbort** is VK\_ESCAPE. You must call the [RegisterHotKey](/windows/win32/api/winuser/nf-winuser-registerhotkey) function before specifying a keystroke that can abort a capture session. The default values of **fAbortLeftMouse** and **fAbortRightMouse** are **TRUE**.

 

 