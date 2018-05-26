---
Description: The following functions are used in device management.
ms.assetid: 3918ba49-1549-4f0c-b9fd-303ef46b810e
title: Device Management Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Device Management Functions

The following functions are used in device management.



| Function                                                             | Description                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**DeviceIoControl**](/windows/win32/Winbase/nf-classpnp-classsenddeviceiocontrolsynchronous?branch=master)                           | Sends a control code directly to a specified device driver.                           |
| [**InstallNewDevice**](installnewdevice.md)                         | Installs a new device. The user is prompted to select the device.                     |
| [**RegisterDeviceNotification**](/windows/win32/Winuser/nf-winuser-registerdevicenotificationa?branch=master)     | Registers the device or type of device for which a window will receive notifications. |
| [**UnregisterDeviceNotification**](/windows/win32/Winuser/nf-winuser-unregisterdevicenotification?branch=master) | Closes the specified device notification handle.                                      |



 

The following functions are used with CD-ROM and DVD drives.



| Function                                                               | Description                                                                                         |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**CdromDisableDigitalPlayback**](/windows/win32/StorProp/nf-storprop-cdromdisabledigitalplayback?branch=master)     | Disables digital playback for the specified CD-ROM or DVD drive.                                    |
| [**CdromEnableDigitalPlayback**](/windows/win32/StorProp/nf-storprop-cdromenabledigitalplayback?branch=master)       | Enables digital playback for the specified CD-ROM or DVD drive.                                     |
| [**CdromIsDigitalPlaybackEnabled**](/windows/win32/StorProp/nf-storprop-cdromisdigitalplaybackenabled?branch=master) | Determines whether digital playback is enabled for the specified CD-ROM or DVD drive.               |
| [**CdromKnownGoodDigitalPlayback**](/windows/win32/Storprop/nf-storprop-cdromknowngooddigitalplayback?branch=master) | Determines whether the specified CD-ROM or DVD drive has digital playback that is known to be good. |
| [**DvdLauncher**](dvdlauncher.md)                                     | Verifies that the media region in the DVD drive matches the DVD drive region.                       |



 

 

 



