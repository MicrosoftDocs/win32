---
title: Loggers
description: Loggers
ms.assetid: 7cb3e4d5-5afc-4329-9268-4cb608e27178
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Loggers

A logger is the mechanism WPA uses to collect and collate events captured in a session and to write that information to a file. Loggers are intrinsically bound to sessions and buffers because logger parameters configure how session data is managed.

The logger name given to a session uniquely indentifies that session to both WPA and the Windows operating system. There can only be one logging session with a given name on a system. The logging session also requires exclusive write access to the WPA trace file.

There are two types of loggers that correspond to the system view and the application view described in the [System View and Application View](system-view-and-application-view.md) section of this document.

-   **The default logger for kernel events, "NT Kernel Logger".** This is the only logger that can collect certain kernel events. No other logger may use that name.

-   **The User Mode logger.** This logger type collects events coming from code executing within the user mode.

To view active loggers on the system use the command line syntax:


```
Xperf -loggers
```



For an example of logger query output please see the [Lost Buffers](avoiding-lost-buffers.md) section of this document.

 

 




