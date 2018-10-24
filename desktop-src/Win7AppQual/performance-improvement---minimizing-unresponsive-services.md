---
Description: .
ms.assetid: 51df3fb9-416d-46b8-b3a7-0281401fb390
title: Best Practices for Minimizing Unresponsive Services
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Best Practices for Minimizing Unresponsive Services

## Affected Platform

<dl> **Clients** – Windows Vista \| Windows 7  
</dl>

## Description

Unresponsive services can result in timeouts, terminated sessions, and even lost data. Employing best practices can greatly reduce the occurrence of unresponsive services.

## Best Practices

Make sure your applications and all of their dependent services and drivers respond to system power and shutdown notifications.

-   All applications should respond promptly and appropriately to shutdown messages such as WM\_QUERYENDSESSION and WM\_ENDSESSION that indicate a shutdown is in progress.
-   All services should promptly respond to SCM shutdown notifications. If they fail to do so, the machine treats them as unresponsive and initiates a 20-second time-out and stops them, opening up the possibility of lost data. This also adds 20 seconds to the shutdown time of a machine shutdown.
-   All services that have kernel device driver dependencies should respond promptly and appropriately to IRP\_MJ\_SHUTDOWN notification in their DispatchShutdown routines.

## Links to Other Resources

<dl>

[Windows Performance Toolkit](http://go.microsoft.com/fwlink/p/?linkid=111383)  
</dl>

 

 



