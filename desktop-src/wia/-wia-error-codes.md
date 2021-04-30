---
description: 'Windows Image Acquisition (WIA) functions and methods can return error codes from the following list: Error CodeMeaningCodeWIA\_ERROR\_BUSYThe device is busy.'
ms.assetid: 3abbe92b-32b7-4820-b208-45c847243078
title: Error Codes (WIA)
ms.topic: article
ms.date: 05/31/2018
---

# Error Codes (WIA)

Windows Image Acquisition (WIA) functions and methods can return error codes from the following list: 

| Error Code                                      | Meaning                                                                                                                                                                                                                             | Code       |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| WIA\_ERROR\_BUSY                                | The device is busy. Close any apps that are using this device or wait for it to finish and then try again.                                                                                                                          | 0x80210006 |
| WIA\_ERROR\_COVER\_OPEN                         | One or more of the device’s cover is open.                                                                                                                                                                                          | 0x80210016 |
| WIA\_ERROR\_DEVICE\_COMMUNICATION               | Communication with the WIA device failed. Make sure that the device is powered on and connected to the PC. If the problem persists, disconnect and reconnect the device.                                                            | 0x8021000A |
| WIA\_ERROR\_DEVICE\_LOCKED                      | The device is locked. Close any apps that are using this device or wait for it to finish and then try again.                                                                                                                        | 0x8021000D |
| WIA\_ERROR\_EXCEPTION\_IN\_DRIVER               | The device driver threw an exception.                                                                                                                                                                                               | 0x8021000E |
| WIA\_ERROR\_GENERAL\_ERROR                      | An unknown error has occurred with the WIA device.                                                                                                                                                                                  | 0x80210001 |
| WIA\_ERROR\_INCORRECT\_HARDWARE\_SETTING        | There is an incorrect setting on the WIA device.                                                                                                                                                                                    | 0x8021000C |
| WIA\_ERROR\_INVALID\_COMMAND                    | The device doesn't support this command.                                                                                                                                                                                            | 0x8021000B |
| WIA\_ERROR\_INVALID\_DRIVER\_RESPONSE           | The response from the driver is invalid.                                                                                                                                                                                            | 0x8021000F |
| WIA\_ERROR\_ITEM\_DELETED                       | The WIA device was deleted. It's no longer available.                                                                                                                                                                               | 0x80210009 |
| WIA\_ERROR\_LAMP\_OFF                           | The scanner's lamp is off.                                                                                                                                                                                                          | 0x80210017 |
| WIA\_ERROR\_MAXIMUM\_PRINTER\_ENDORSER\_COUNTER | A scan job was interrupted because an Imprinter/Endorser item reached the maximum valid value for WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER, and was reset to 0. This feature is available with Windows 8 and later versions of Windows. | 0x80210021 |
| WIA\_ERROR\_MULTI\_FEED                         | A scan error occurred because of a multiple page feed condition. This feature is available with Windows 8 and later versions of Windows.                                                                                            | 0x80210020 |
| WIA\_ERROR\_OFFLINE                             | The device is offline. Make sure the device is powered on and connected to the PC.                                                                                                                                                  | 0x80210005 |
| WIA\_ERROR\_PAPER\_EMPTY                        | There are no documents in the document feeder.                                                                                                                                                                                      | 0x80210003 |
| WIA\_ERROR\_PAPER\_JAM                          | Paper is jammed in the scanner's document feeder.                                                                                                                                                                                   | 0x80210002 |
| WIA\_ERROR\_PAPER\_PROBLEM                      | An unspecified problem occurred with the scanner's document feeder.                                                                                                                                                                 | 0x80210004 |
| WIA\_ERROR\_WARMING\_UP                         | The device is warming up.                                                                                                                                                                                                           | 0x80210007 |
| WIA\_ERROR\_USER\_INTERVENTION                  | There is a problem with the WIA device. Make sure that the device is turned on, online, and any cables are properly connected.                                                                                                      | 0x80210008 |
| WIA\_S\_NO\_DEVICE\_AVAILABLE                   | No scanner device was found. Make sure the device is online, connected to the PC, and has the correct driver installed on the PC.                                                                                                   | 0x80210015 |



 

 

 



