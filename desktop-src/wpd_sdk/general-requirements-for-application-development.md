---
description: General Requirements for Application Development
ms.assetid: 8ac88d6f-fc4b-4253-932d-aaa3c801b18f
title: General Requirements for Application Development (WPD API)
ms.topic: article
ms.date: 05/31/2018
---

# General Requirements for Application Development (WPD API)

To create a Windows Portable Devices application, you must have the [Windows Software Development Kit (SDK)](https://developer.microsoft.com/windows/downloads) installed on your computer. The required headers and libraries appear in the following list.

-   PortableDeviceGuids.lib
-   PortableDevice.h
-   PortableDeviceTypes.h
-   PortableDeviceApi.h
-   Any other required libraries and headers required by your application to consume or render media files.

If your application supports the new Device Services interfaces, it will also include one or more of the following header files.

-   AnchorSyncDeviceService.h
-   BridgeDeviceService.h
-   CalendarDeviceService.h
-   ContactDeviceService.h
-   DeviceServices.h
-   FullEnumSyncDeviceService.h
-   HintsDeviceService.h
-   MessageDeviceService.h
-   MetadataDeviceService.h
-   NotesDeviceService.h
-   RingtoneDeviceService.h
-   StatusDeviceService.h
-   SyncDeviceService.h
-   TaskDeviceService.h

Of the files in the previous list, BridgeDeviceService.h and DeviceService.h are required for almost any application that supports Device Services; the other files define different types of device services and would be included as appropriate.

## Related topics

<dl> <dt>

[**Windows Portable Devices**](/windows/desktop/windows-portable-devices)
</dt> </dl>

 

 
