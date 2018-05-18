---
title: Alert Functions
description: The network management alert functions notify network service programs and applications of network events.
ms.assetid: 'e131191b-7413-45ff-84cd-b3a873d33ca1'
---

# Alert Functions

\[The alert functions are not supported as of Windows Vista because the alerter and messenger services are not supported.\]

The network management alert functions notify network service programs and applications of network events. An *event* is a particular instance of a process, occurrence, or state of hardware as defined by an application. The alert functions allow applications to indicate when predefined events occur.

**Windows Server 2003:** The alerter and messenger services are disabled by default on Windows Server 2003. You must re-enable the services before calling the network management Alert functions or the network management [Message functions](message-functions.md).

The alert functions are listed following.



| Function                                   | Description                                                                                                                                                                                            |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetAlertRaise**](netalertraise.md)     | Notifies all registered clients that a particular event has occurred.                                                                                                                                  |
| [**NetAlertRaiseEx**](netalertraiseex.md) | Simplifies notifying registered clients that a particular event has occurred, because, unlike **NetAlertRaise**, **NetAlertRaiseEx** does not require a [**STD\_ALERT**](std-alert-str.md) structure. |



 

The alerter service must be running on the client computer when you call the **NetAlertRaise** function or the **NetAlertRaiseEx** function. If the service is not running, the functions fail with **ERROR\_FILE\_NOT\_FOUND**. The alerter service on the client calls the [**NetMessageBufferSend**](netmessagebuffersend.md) function to send information to recipients.

Applications, network services, and internal network components use the network management alert functions to raise an alert, notifying various applications or users when a particular type of event occurs. The alert category functions, data types, structures, and constants are defined in the LMCONS.H, LMERR.H, and LMALERT.H header files. To access these definitions, define the constants INCL\_NETERRORS and INCL\_NETALERT, and include the header file LM.H.

The LMALERT.H file predefines the following alert classes (types of network events) for sending alerts:

-   Network events requiring administrative assistance
-   Addition of an entry to an error log file
-   Reception of a broadcast message by a user or an application
-   Completion of a print job
-   Use of certain applications or resources by users

You can define other classes of alerts for network applications as needed. For example, if an application on a server routinely writes large amounts of data to a disk drive, the application runs the risk of filling the disk. In this case, you might want to add the event "no free disk space' to trigger an alert that notifies the application to pause or to terminate the process that is filling the disk. The event name for an alert can be any text string.

When you raise an alert with a call to the [**NetAlertRaise**](netalertraise.md) function, the message data should consist of one [**STD\_ALERT**](std-alert-str.md) header structure, followed by additional fixed-length data that is alert-specific in one [**ADMIN\_OTHER\_INFO**](admin-other-info-str.md), [**ERRLOG\_OTHER\_INFO**](errlog-other-info-str.md), [**PRINT\_OTHER\_INFO**](print-other-info-str.md), or [**USER\_OTHER\_INFO**](user-other-info-str.md) structure. Additional variable-length data can follow the alert-specific structure. (Calls to the [**NetAlertRaiseEx**](netalertraiseex.md) function do not require a **STD\_ALERT** structure.) The calling application must allocate the memory for all structures and variable-length data, and free the memory after the call returns.

The following macros are available for use with alert data buffers.



| Macro                                          | Description                                                                                               |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**ALERT\_OTHER\_INFO**](alert-other-info.md) | Returns a pointer to the fixed-length data that follows the **STD\_ALERT** structure in an alert message. |
| [**ALERT\_VAR\_DATA**](alert-var-data.md)     | Returns a pointer to the variable-length data that follows the alert-specific data in an alert message.   |



 

Instead of using the network management alert functions, you may be able to use the Windows Management Instrumentation (WMI) SDK for event notification. For more information about the platforms that support the WMI event model, see [WMI Infrastructure](https://msdn.microsoft.com/library/aa394562) and [Monitoring Events](https://msdn.microsoft.com/library/aa392396) in the WMI documentation.

 

 




