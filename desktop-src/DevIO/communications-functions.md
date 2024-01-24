---
description: The following functions are used with communications resources.
ms.assetid: ba7d1a9e-6906-4923-a8eb-db58050ba699
title: Communications Functions
ms.topic: article
ms.date: 05/31/2018
---

# Communications Functions

The following functions are used with communications resources.



| Function                                                   | Description                                                                                                                    |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**BuildCommDCB**](/windows/desktop/api/Winbase/nf-winbase-buildcommdcba)                       | Fills a specified [**DCB**](/windows/desktop/api/Winbase/ns-winbase-dcb) structure with values specified in a device-control string.                           |
| [**BuildCommDCBAndTimeouts**](/windows/desktop/api/Winbase/nf-winbase-buildcommdcbandtimeoutsa) | Translates a device-definition string into appropriate device-control block codes and places them into a device control block. |
| [**ClearCommBreak**](/windows/desktop/api/Winbase/nf-winbase-clearcommbreak)                   | Restores character transmission for a specified communications device and places the transmission line in a nonbreak state.    |
| [**ClearCommError**](/windows/desktop/api/Winbase/nf-winbase-clearcommerror)                   | Retrieves information about a communications error and reports the current status of a communications device.                  |
| [**CommConfigDialog**](/windows/desktop/api/Winbase/nf-winbase-commconfigdialoga)               | Displays a driver-supplied configuration dialog box.                                                                           |
| [**EscapeCommFunction**](/windows/desktop/api/Winbase/nf-winbase-escapecommfunction)           | Directs a specified communications device to perform an extended function.                                                     |
| [**GetCommConfig**](/windows/desktop/api/Winbase/nf-winbase-getcommconfig)                     | Retrieves the current configuration of a communications device.                                                                |
| [**GetCommMask**](/windows/desktop/api/Winbase/nf-winbase-getcommmask)                         | Retrieves the value of the event mask for a specified communications device.                                                   |
| [**GetCommModemStatus**](/windows/desktop/api/Winbase/nf-winbase-getcommmodemstatus)           | Retrieves modem control-register values.                                                                                       |
| [**GetCommProperties**](/windows/desktop/api/Winbase/nf-winbase-getcommproperties)             | Retrieves information about the communications properties for a specified communications device.                               |
| [**GetCommState**](/windows/desktop/api/Winbase/nf-winbase-getcommstate)                       | Retrieves the current control settings for a specified communications device.                                                  |
| [**GetCommTimeouts**](/windows/desktop/api/Winbase/nf-winbase-getcommtimeouts)                 | Retrieves the time-out parameters for all read and write operations on a specified communications device.                      |
| [**GetDefaultCommConfig**](/windows/desktop/api/Winbase/nf-winbase-getdefaultcommconfiga)       | Retrieves the default configuration for the specified communications device.                                                   |
| [**PurgeComm**](/windows/desktop/api/Winbase/nf-winbase-purgecomm)                             | Discards all characters from the output or input buffer of a specified communications resource.                                |
| [**SetCommBreak**](/windows/desktop/api/Winbase/nf-winbase-setcommbreak)                       | Suspends character transmission for a specified communications device and places the transmission line in a break state.       |
| [**SetCommConfig**](/windows/desktop/api/Winbase/nf-winbase-setcommconfig)                     | Sets the current configuration of a communications device.                                                                     |
| [**SetCommMask**](/windows/desktop/api/Winbase/nf-winbase-setcommmask)                         | Specifies a set of events to be monitored for a communications device.                                                         |
| [**SetCommState**](/windows/desktop/api/Winbase/nf-winbase-setcommstate)                       | Configures a communications device according to the specifications in a device-control block.                                  |
| [**SetCommTimeouts**](/windows/desktop/api/Winbase/nf-winbase-setcommtimeouts)                 | Sets the time-out parameters for all read and write operations on a specified communications device.                           |
| [**SetDefaultCommConfig**](/windows/desktop/api/Winbase/nf-winbase-setdefaultcommconfiga)       | Sets the default configuration for a communications device.                                                                    |
| [**SetupComm**](/windows/desktop/api/Winbase/nf-winbase-setupcomm)                             | Initializes the communications parameters for a specified communications device.                                               |
| [**TransmitCommChar**](/windows/desktop/api/Winbase/nf-winbase-transmitcommchar)               | Transmits a specified character ahead of any pending data in the output buffer of the specified communications device.         |
| [**WaitCommEvent**](/windows/desktop/api/Winbase/nf-winbase-waitcommevent)                     | Waits for an event to occur for a specified communications device.                                                             |



 

 

 



