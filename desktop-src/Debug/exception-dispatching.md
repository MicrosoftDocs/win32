---
description: When a hardware or software exception occurs, the processor stops execution at the point at which the exception occurred and transfers control to the system.
ms.assetid: 35a1b9bd-8da9-47e6-beda-e0b159bd840d
title: Exception Dispatching
ms.topic: article
ms.date: 05/31/2018
---

# Exception Dispatching

When a hardware or software exception occurs, the processor stops execution at the point at which the exception occurred and transfers control to the system. First, the system saves both the machine state of the current thread and information that describes the exception. The system then attempts to find an exception handler to handle the exception.

The machine state of the thread in which the exception occurred is saved in a [**CONTEXT**](/windows/desktop/api/WinNT/ns-winnt-arm64_nt_context) structure. This information (called the *context record*) enables the system to continue execution at the point of the exception if the exception is successfully handled. The description of the exception (called the **exception record**) is saved in an [**EXCEPTION\_RECORD**](/windows/desktop/api/WinNT/ns-winnt-exception_record) structure. Because it stores the machine-dependent information of the context record separately from the machine-independent information of the exception record, the exception-handling mechanism is portable to different platforms.

The information in both the context and exception records is available by means of the [**GetExceptionInformation**](getexceptioninformation.md) function, and can be made available to any exception handlers that are executed as a result of the exception. The exception record includes the following information.

-   An exception code that identifies the type of exception.
-   Flags indicating whether the exception is continuable. Any attempt to continue execution after a noncontinuable exception generates another exception.
-   A pointer to another exception record. This facilitates creation of a linked list of exceptions if nested exceptions occur.
-   The address at which the exception occurred.
-   An array of arguments that provide additional information about the exception.

When an exception occurs in user-mode code, the system uses the following search order to find an exception handler:

1.  If the process is being debugged, the system notifies the debugger. For more information, see [Debugger Exception Handling](debugger-exception-handling.md).
2.  If the process is not being debugged, or if the associated debugger does not handle the exception, the system attempts to locate a frame-based exception handler by searching the stack frames of the thread in which the exception occurred. The system searches the current stack frame first, then searches through preceding stack frames in reverse order.
3.  If no frame-based handler can be found, or no frame-based handler handles the exception, but the process is being debugged, the system notifies the debugger a second time.
4.  If the process is not being debugged, or if the associated debugger does not handle the exception, the system provides default handling based on the exception type. For most exceptions, the default action is to call the [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) function.

When an exception occurs in kernel-mode code, the system searches the stack frames of the kernel stack in an attempt to locate an exception handler. If a handler cannot be located or no handler handles the exception, the system is shut down as if the [**ExitWindows**](/windows/win32/api/winuser/nf-winuser-exitwindows) function had been called.

 

 
