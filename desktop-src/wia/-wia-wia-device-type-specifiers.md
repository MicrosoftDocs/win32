---
description: Windows Image Acquisition (WIA) Device Type Specifiers are constants that indicate the type of device attached to a user's computer.
ms.assetid: 569b99ab-628b-4a43-a6e5-0ae81524fcc0
title: WIA Device Type Specifiers
ms.topic: article
ms.date: 05/31/2018
---

# WIA Device Type Specifiers

Windows Image Acquisition (WIA) Device Type Specifiers are constants that indicate the type of device attached to a user's computer. Use the GET\_STIDEVICE\_TYPE macro to obtain these values from the WIA device type property. The following are valid WIA Device Type Specifiers: 

| Device Type                 | Meaning                                                                                                                     |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| StiDeviceTypeDefault        | Generic WIA device. During device enumerations, this constant is used to enumerate all WIA devices.                         |
| StiDeviceTypeDigitalCamera  | The device is a camera. *This specifier is not supported by* Windows Vista *and later.*                                     |
| StiDeviceTypeScanner        | The device is a scanner.                                                                                                    |
| StiDeviceTypeStreamingVideo | The device contains streaming video. *This specifier is not supported by* Windows Server 2003*,* Windows Vista, *or later.* |



 

 

 



