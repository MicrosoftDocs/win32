---
title: Communication with MCI Devices
description: Communication with MCI Devices
ms.assetid: a2532c29-553f-4ae3-8ad5-319fd9470e76
keywords:
- MCI devices,communicating
- MCIWndGetDeviceID macro
- mciSendCommand function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Communication with MCI Devices

It is possible for each MCI device to use one or more of the following as identifiers:

-   a device identifier
-   a device name
-   an alias
-   the filename of the currently loaded content.

MCIWnd provides macros you can use to retrieve this information. You can then use this information to communicate through MCI directly with MCI devices associated with MCIWnd windows.

You can retrieve the identifier of the current MCI device by using the [**MCIWndGetDeviceID**](/windows/win32/Vfw/nf-vfw-mciwndgetdeviceid?branch=master) macro. The MCI device identifier is a numerical value that identifies the instance of the MCI device your application is using. Your application can use this identifier when communicating with an MCI device by using the [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) function.

To retrieve the name of the current MCI device, use the [**MCIWndGetDevice**](/windows/win32/Vfw/nf-vfw-mciwndgetdevice?branch=master) macro. The MCI device name is a null-terminated string that identifies the device type associated with an MCIWnd window. Your application can use this name when communicating with an MCI device by using **mciSendCommand**.

You can retrieve the alias of the current MCI device by using the [**MCIWndGetAlias**](/windows/win32/Vfw/nf-vfw-mciwndgetalias?branch=master) macro. Your application can use this alias when communicating with an MCI device by using the [**mciSendString**](/windows/win32/Mmsystem/?branch=master) function.

Finally, you can retrieve the filename used by an MCI device by using the [**MCIWndGetFileName**](/windows/win32/Vfw/nf-vfw-mciwndgetfilename?branch=master) macro. The filename identifies the content currently associated with an MCIWnd window. Your application can use this filename when communicating with a MCI device by using **mciSendCommand** or **mciSendString**.

 

 




