---
description: The following functions are used by time providers.
ms.assetid: 05687a67-4e0b-4a44-9c2d-7e097be9008c
title: Time Provider Functions
ms.topic: article
ms.date: 05/31/2018
---

# Time Provider Functions

The following functions are used by time providers.



| Function                                                               | Description                                                                                            |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**AlertSamplesAvailFunc**](/windows/desktop/api/Timeprov/nc-timeprov-alertsamplesavailfunc)                     | Notifies the system that there are new samples available.                                              |
| [**GetTimeSysInfoFunc**](/windows/desktop/api/Timeprov/nc-timeprov-gettimesysinfofunc)                           | Retrieves the system time state information.                                                           |
| [**LogTimeProvEventFunc**](/windows/desktop/api/Timeprov/nc-timeprov-logtimeproveventfunc)                       | Logs a time provider event in the event log.                                                           |
| [**SetProviderStatusFunc**](/windows/desktop/api/Timeprov/nc-timeprov-setproviderstatusfunc)                 | Sets the time provider's status information.                                                           |
| [**SetProviderStatusInfoFreeFunc**](/windows/desktop/api/Timeprov/nc-timeprov-setproviderstatusinfofreefunc) | Frees a [**SetProviderStatusInfo**](/windows/desktop/api/Timeprov/ns-timeprov-setproviderstatusinfo) structure.                          |
| [**TimeProvClose**](/windows/desktop/api/Timeprov/nf-timeprov-timeprovclose)                                 | A callback function that is called by the time provider manager to shut down the time provider.        |
| [**TimeProvCommand**](/windows/desktop/api/Timeprov/nf-timeprov-timeprovcommand)                             | A callback function that is called by the time provider manager to send commands to the time provider. |
| [**TimeProvOpen**](/windows/desktop/api/Timeprov/nf-timeprov-timeprovopen)                                   | A callback function that is called by the time provider manager when the time provider DLL is loaded.  |



 

 

 



