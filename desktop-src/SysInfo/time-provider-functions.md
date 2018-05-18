---
Description: 'The following functions are used by time providers.'
ms.assetid: '05687a67-4e0b-4a44-9c2d-7e097be9008c'
title: Time Provider Functions
---

# Time Provider Functions

The following functions are used by time providers.



| Function                                                               | Description                                                                                            |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**AlertSamplesAvailFunc**](alertsamplesavail.md)                     | Notifies the system that there are new samples available.                                              |
| [**GetTimeSysInfoFunc**](gettimesysinfo.md)                           | Retrieves the system time state information.                                                           |
| [**LogTimeProvEventFunc**](logtimeprovevent.md)                       | Logs a time provider event in the event log.                                                           |
| [**SetProviderStatusFunc**](setproviderstatusfunc.md)                 | Sets the time provider's status information.                                                           |
| [**SetProviderStatusInfoFreeFunc**](setproviderstatusinfofreefunc.md) | Frees a [**SetProviderStatusInfo**](setproviderstatusinfo-str.md) structure.                          |
| [**TimeProvClose**](timeprovclose.md)                                 | A callback function that is called by the time provider manager to shut down the time provider.        |
| [**TimeProvCommand**](timeprovcommand.md)                             | A callback function that is called by the time provider manager to send commands to the time provider. |
| [**TimeProvOpen**](timeprovopen.md)                                   | A callback function that is called by the time provider manager when the time provider DLL is loaded.  |



 

 

 



