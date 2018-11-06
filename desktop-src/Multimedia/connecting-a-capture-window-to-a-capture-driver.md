---
title: Connecting a Capture Window to a Capture Driver
description: Connecting a Capture Window to a Capture Driver
ms.assetid: 78d4aaf5-6216-4eec-84d4-6727d1822983
keywords:
- WM_CAP_DRIVER_CONNECT message
- capDriverConnect macro
- capGetDriverDescription function
- WM_CAP_DRIVER_GET_NAME message
- capDriverGetName macro
- WM_CAP_DRIVER_GET_VERSION message
- capDriverGetVersion macro
- WM_CAP_DRIVER_DISCONNECT message
- capDriverDisconnect macro
ms.topic: article
ms.date: 05/31/2018
---

# Connecting a Capture Window to a Capture Driver

You can dynamically connect or disconnect a capture window to a capture driver. You can connect or associate a capture window with a capture driver by using the [**WM\_CAP\_DRIVER\_CONNECT**](wm-cap-driver-connect.md) message (or the [**capDriverConnect**](/windows/desktop/api/Vfw/nf-vfw-capdriverconnect) macro). After a capture window and capture driver are connected, you can send device-specific messages to the capture driver associated with a capture window.

If you have more than one capture device installed on a system, you can connect a capture window to a particular video capture device driver by specifying an integer for the *wParam* parameter of the WM\_CAP\_DRIVER\_CONNECT message. The integer is an index that identifies a video capture driver listed in the registry or in the \[drivers\] section of the SYSTEM.INI file. Use zero for the first index entry.

You can retrieve the name and version of an installed capture driver by using the [**capGetDriverDescription**](/windows/desktop/api/Vfw/nf-vfw-capgetdriverdescriptiona) function. Your application can use this function to enumerate the installed capture devices and drivers, so the user can select a capture device to connect to a capture window.

You can retrieve the name of the capture device driver connected to a capture window by using the [**WM\_CAP\_DRIVER\_GET\_NAME**](wm-cap-driver-get-name.md) message (or the [**capDriverGetName**](/windows/desktop/api/Vfw/nf-vfw-capdrivergetname) macro). To retrieve the version of an installed capture driver, use the [**WM\_CAP\_DRIVER\_GET\_VERSION**](wm-cap-driver-get-version.md) message (or the [**capDriverGetVersion**](/windows/desktop/api/Vfw/nf-vfw-capdrivergetversion) macro).

You can disconnect a capture window from a capture driver by using the [**WM\_CAP\_DRIVER\_DISCONNECT**](wm-cap-driver-disconnect.md) message (or the [**capDriverDisconnect**](/windows/desktop/api/Vfw/nf-vfw-capdriverdisconnect) macro).

When an capture window is destroyed, any connected video capture device drivers are automatically disconnected.

 

 




