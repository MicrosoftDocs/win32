---
Description: The following functions are used by time providers.
ms.assetid: 05687a67-4e0b-4a44-9c2d-7e097be9008c
title: Time Provider Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Time Provider Functions

The following functions are used by time providers.



| Function                                                               | Description                                                                                            |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**AlertSamplesAvailFunc**](/windows/win32/Timeprov/nc-timeprov-alertsamplesavailfunc?branch=master)                     | Notifies the system that there are new samples available.                                              |
| [**GetTimeSysInfoFunc**](/windows/win32/Timeprov/nc-timeprov-gettimesysinfofunc?branch=master)                           | Retrieves the system time state information.                                                           |
| [**LogTimeProvEventFunc**](/windows/win32/Timeprov/nc-timeprov-logtimeproveventfunc?branch=master)                       | Logs a time provider event in the event log.                                                           |
| [**SetProviderStatusFunc**](/windows/win32/Timeprov/nc-timeprov-setproviderstatusfunc?branch=master)                 | Sets the time provider's status information.                                                           |
| [**SetProviderStatusInfoFreeFunc**](/windows/win32/Timeprov/nc-timeprov-setproviderstatusinfofreefunc?branch=master) | Frees a [**SetProviderStatusInfo**](/windows/win32/Timeprov/ns-timeprov-setproviderstatusinfo?branch=master) structure.                          |
| [**TimeProvClose**](/windows/win32/Timeprov/nf-timeprov-timeprovclose?branch=master)                                 | A callback function that is called by the time provider manager to shut down the time provider.        |
| [**TimeProvCommand**](/windows/win32/Timeprov/nf-timeprov-timeprovcommand?branch=master)                             | A callback function that is called by the time provider manager to send commands to the time provider. |
| [**TimeProvOpen**](/windows/win32/Timeprov/nf-timeprov-timeprovopen?branch=master)                                   | A callback function that is called by the time provider manager when the time provider DLL is loaded.  |



 

 

 



