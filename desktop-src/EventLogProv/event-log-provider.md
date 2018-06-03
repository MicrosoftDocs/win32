---
Description: The Event Log provider supplies access to data from the event log service, and notification of events.
ms.assetid: 24dec59e-686e-4154-ba08-e8fe613fa166
title: Event Log Provider
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Event Log Provider

The Event Log provider supplies the following:

-   Access to data from the Event Log service.
-   Notifications of events.

The Event Log service writes events to one of several log files. The Event Log provider uses the [**Win32\_NTEventLogFile**](win32-nteventlogfile.md) class to map data from the event logs to WMI objects. The Event Log provider also uses the [**Win32\_NTLogEvent**](win32-ntlogevent.md) class to represent events. The two [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instance names are MS\_NT\_EVENTLOG\_PROVIDER and MS\_NT\_EVENTLOG\_EVENT\_PROVIDER.

As an instance, method, and event provider, the Event Log provider implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104)
-   [**ExecNotificationQueryAsync**](https://msdn.microsoft.com/library/aa392106)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

The Ntevt.mof file contains the Event Log provider, association, and registration classes. You can access the Event Log provider classes only in the root\\cimv2 namespace.

The Event Log provider supports the following classes:

-   [**Win32\_NTEventlogFile**](win32-nteventlogfile.md)
-   [**Win32\_NTLogEvent**](win32-ntlogevent.md)
-   [**Win32\_NTLogEventLog**](win32-ntlogeventlog.md)
-   [**Win32\_NTLogEventUser**](win32-ntlogeventuser.md)
-   [**Win32\_NTLogEventComputer**](win32-ntlogeventcomputer.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 



