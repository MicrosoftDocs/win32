---
description: When an error occurs, the system administrator or support representative must determine what caused the error, attempt to recover any lost data, and prevent the error from recurring.
ms.assetid: 2a625c8a-afa2-484a-a0e3-df3ef774abe4
title: About Event Logging
ms.topic: article
ms.date: 05/31/2018
---

# About Event Logging

When an error occurs, the system administrator or support representative must determine what caused the error, attempt to recover any lost data, and prevent the error from recurring. It is helpful if applications, the operating system, and other system services record important events, such as low-memory conditions or excessive attempts to access a disk. The system administrator can then use the event log to help determine what conditions caused the error and identify the context in which it occurred. By periodically viewing the event log, the system administrator may be able to identify problems (such as a failing hard disk) before they cause damage.

> [!Note]  
> The Event Logging API was designed for applications that run on the Windows Server 2003, Windows XP, or Windows 2000 operating system. In Windows Vista, the event logging infrastructure was redesigned. Applications that are designed to run on the Windows Vista or later operating systems should now use [Windows Event Log](/windows/desktop/WES/windows-event-log) to log events.

 
This section discusses the programming interface for writing and consuming events using Event Logging.

-   [Event types](event-types.md)
-   [Logging guidelines](logging-guidelines.md)
-   [Event logging elements](event-logging-elements.md)
-   [Event logging operations](event-logging-operations.md)
-   [Event logging model](event-logging-model.md)
-   [Event logging security](event-logging-security.md)

> [!Note]  
> Applications that publish events that are larger than 64 kilobytes on a Windows Server 2003, Windows XP, or Windows 2000 computer will not be able to publish events on a Windows Vista or later computer.
