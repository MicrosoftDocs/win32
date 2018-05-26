---
Description: The following functions are used with communications resources.
ms.assetid: ba7d1a9e-6906-4923-a8eb-db58050ba699
title: Communications Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Communications Functions

The following functions are used with communications resources.



| Function                                                   | Description                                                                                                                    |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**BuildCommDCB**](/windows/win32/Winbase/nf-winbase-buildcommdcba?branch=master)                       | Fills a specified [**DCB**](/windows/win32/Winbase/ns-winbase-_dcb?branch=master) structure with values specified in a device-control string.                           |
| [**BuildCommDCBAndTimeouts**](/windows/win32/Winbase/nf-winbase-buildcommdcbandtimeoutsa?branch=master) | Translates a device-definition string into appropriate device-control block codes and places them into a device control block. |
| [**ClearCommBreak**](/windows/win32/Winbase/nf-winbase-clearcommbreak?branch=master)                   | Restores character transmission for a specified communications device and places the transmission line in a nonbreak state.    |
| [**ClearCommError**](/windows/win32/Winbase/nf-winbase-clearcommerror?branch=master)                   | Retrieves information about a communications error and reports the current status of a communications device.                  |
| [**CommConfigDialog**](/windows/win32/Winbase/nf-winbase-commconfigdialoga?branch=master)               | Displays a driver-supplied configuration dialog box.                                                                           |
| [**EscapeCommFunction**](/windows/win32/Winbase/nf-winbase-escapecommfunction?branch=master)           | Directs a specified communications device to perform an extended function.                                                     |
| [**GetCommConfig**](/windows/win32/Winbase/nf-winbase-getcommconfig?branch=master)                     | Retrieves the current configuration of a communications device.                                                                |
| [**GetCommMask**](/windows/win32/Winbase/nf-winbase-getcommmask?branch=master)                         | Retrieves the value of the event mask for a specified communications device.                                                   |
| [**GetCommModemStatus**](/windows/win32/Winbase/nf-winbase-getcommmodemstatus?branch=master)           | Retrieves modem control-register values.                                                                                       |
| [**GetCommProperties**](/windows/win32/Winbase/nf-winbase-getcommproperties?branch=master)             | Retrieves information about the communications properties for a specified communications device.                               |
| [**GetCommState**](/windows/win32/Winbase/nf-winbase-getcommstate?branch=master)                       | Retrieves the current control settings for a specified communications device.                                                  |
| [**GetCommTimeouts**](/windows/win32/Winbase/nf-winbase-getcommtimeouts?branch=master)                 | Retrieves the time-out parameters for all read and write operations on a specified communications device.                      |
| [**GetDefaultCommConfig**](/windows/win32/Winbase/nf-winbase-getdefaultcommconfiga?branch=master)       | Retrieves the default configuration for the specified communications device.                                                   |
| [**PurgeComm**](/windows/win32/Winbase/nf-winbase-purgecomm?branch=master)                             | Discards all characters from the output or input buffer of a specified communications resource.                                |
| [**SetCommBreak**](/windows/win32/Winbase/nf-winbase-setcommbreak?branch=master)                       | Suspends character transmission for a specified communications device and places the transmission line in a break state.       |
| [**SetCommConfig**](/windows/win32/Winbase/nf-winbase-setcommconfig?branch=master)                     | Sets the current configuration of a communications device.                                                                     |
| [**SetCommMask**](/windows/win32/Winbase/nf-winbase-setcommmask?branch=master)                         | Specifies a set of events to be monitored for a communications device.                                                         |
| [**SetCommState**](/windows/win32/Winbase/nf-winbase-setcommstate?branch=master)                       | Configures a communications device according to the specifications in a device-control block.                                  |
| [**SetCommTimeouts**](/windows/win32/Winbase/nf-winbase-setcommtimeouts?branch=master)                 | Sets the time-out parameters for all read and write operations on a specified communications device.                           |
| [**SetDefaultCommConfig**](/windows/win32/Winbase/nf-winbase-setdefaultcommconfiga?branch=master)       | Sets the default configuration for a communications device.                                                                    |
| [**SetupComm**](/windows/win32/Winbase/nf-winbase-setupcomm?branch=master)                             | Initializes the communications parameters for a specified communications device.                                               |
| [**TransmitCommChar**](/windows/win32/Winbase/nf-winbase-transmitcommchar?branch=master)               | Transmits a specified character ahead of any pending data in the output buffer of the specified communications device.         |
| [**WaitCommEvent**](/windows/win32/Winbase/nf-winbase-waitcommevent?branch=master)                     | Waits for an event to occur for a specified communications device.                                                             |



 

 

 



