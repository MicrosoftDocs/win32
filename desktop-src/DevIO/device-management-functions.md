---
description: The following functions are used in device management.
ms.assetid: 3918ba49-1549-4f0c-b9fd-303ef46b810e
title: Device Management Functions
ms.topic: article
ms.date: 05/31/2018
---

# Device Management Functions

The following functions are used in device management.



| Function                                                             | Description                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)                           | Sends a control code directly to a specified device driver.                           |
| [**InstallNewDevice**](installnewdevice.md)                         | Installs a new device. The user is prompted to select the device.                     |
| [**RegisterDeviceNotification**](/windows/desktop/api/Winuser/nf-winuser-registerdevicenotificationa)     | Registers the device or type of device for which a window will receive notifications. |
| [**UnregisterDeviceNotification**](/windows/desktop/api/Winuser/nf-winuser-unregisterdevicenotification) | Closes the specified device notification handle.                                      |



 

The following functions are used with CD-ROM and DVD drives.



| Function                                                               | Description                                                                                         |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**CdromDisableDigitalPlayback**](/windows/desktop/api/StorProp/nf-storprop-cdromdisabledigitalplayback)     | Disables digital playback for the specified CD-ROM or DVD drive.                                    |
| [**CdromEnableDigitalPlayback**](/windows/desktop/api/StorProp/nf-storprop-cdromenabledigitalplayback)       | Enables digital playback for the specified CD-ROM or DVD drive.                                     |
| [**CdromIsDigitalPlaybackEnabled**](/windows/desktop/api/StorProp/nf-storprop-cdromisdigitalplaybackenabled) | Determines whether digital playback is enabled for the specified CD-ROM or DVD drive.               |
| [**CdromKnownGoodDigitalPlayback**](/windows/desktop/api/Storprop/nf-storprop-cdromknowngooddigitalplayback) | Determines whether the specified CD-ROM or DVD drive has digital playback that is known to be good. |
| [**DvdLauncher**](dvdlauncher.md)                                     | Verifies that the media region in the DVD drive matches the DVD drive region.                       |



 

 

 
