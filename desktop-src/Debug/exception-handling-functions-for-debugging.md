---
description: When an exception occurs in a process that is being debugged, the system notifies the debugger by passing the exception to it. This is known as first-chance notification. The system then suspends all threads in the process being debugged.
ms.assetid: 6fdc02ac-9c33-49a8-8614-8b0cc2bf811b
title: Exception Handling Functions for Debugging
ms.topic: article
ms.date: 05/31/2018
---

# Exception Handling Functions for Debugging

When an exception occurs in a process that is being debugged, the system notifies the debugger by passing the exception to it. This is known as *first-chance notification*. The system then suspends all threads in the process being debugged.

If the debugger does not handle the exception, the system attempts to locate an appropriate exception handler. If the system cannot locate an appropriate one, the system again notifies the debugger that an exception has occurred. This is known as *last-chance notification*. If the debugger does not handle the exception after the last-chance notification, the system terminates the process being debugged.

For more information, see [Debugger Exception Handling](debugger-exception-handling.md).

 

 



