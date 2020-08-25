---
title: Communication with MCI Devices
description: Communication with MCI Devices
ms.assetid: a2532c29-553f-4ae3-8ad5-319fd9470e76
keywords:
- MCI devices,communicating
- MCIWndGetDeviceID macro
- mciSendCommand function
ms.topic: article
ms.date: 05/31/2018
---

# Communication with MCI Devices

It is possible for each MCI device to use one or more of the following as identifiers:

-   a device identifier
-   a device name
-   an alias
-   the filename of the currently loaded content.

MCIWnd provides macros you can use to retrieve this information. You can then use this information to communicate through MCI directly with MCI devices associated with MCIWnd windows.

You can retrieve the identifier of the current MCI device by using the [**MCIWndGetDeviceID**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetdeviceid) macro. The MCI device identifier is a numerical value that identifies the instance of the MCI device your application is using. Your application can use this identifier when communicating with an MCI device by using the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function.

To retrieve the name of the current MCI device, use the [**MCIWndGetDevice**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetdevice) macro. The MCI device name is a null-terminated string that identifies the device type associated with an MCIWnd window. Your application can use this name when communicating with an MCI device by using **mciSendCommand**.

You can retrieve the alias of the current MCI device by using the [**MCIWndGetAlias**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetalias) macro. Your application can use this alias when communicating with an MCI device by using the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function.

Finally, you can retrieve the filename used by an MCI device by using the [**MCIWndGetFileName**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetfilename) macro. The filename identifies the content currently associated with an MCIWnd window. Your application can use this filename when communicating with a MCI device by using **mciSendCommand** or **mciSendString**.

 

 