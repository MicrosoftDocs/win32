---
Description: 'The error mode indicates to the system how the application is going to respond to serious errors.'
ms.assetid: '288be838-6094-4824-9cae-99b7ff9eea74'
title: Error Mode
---

# Error Mode

The error mode indicates to the system how the application is going to respond to serious errors. Serious errors include disk failure, drive-not-ready errors, data misalignment, and unhandled exceptions. This error mode can be managed by either a per-thread or per-process basis. An application can let the system display a message box informing the user that an error has occurred, or it can handle the errors.

To handle these errors without user intervention, use [**SetErrorMode**](seterrormode.md) or the thread-specific [**SetThreadErrorMode**](setthreaderrormode.md). After calling one of these functions and specifying appropriate flags, the system will not display the corresponding error message boxes.

A process can retrieve its error mode using [**GetErrorMode**](geterrormode.md) or [**GetThreadErrorMode**](getthreaderrormode.md).

Best practice is that all applications call the process-wide [**SetErrorMode**](seterrormode.md) function with a parameter of **SEM\_FAILCRITICALERRORS** at startup. This is to prevent error mode dialogs from hanging the application.

Other than that, callers should favor the thread-specific versions of these functions since they are less disruptive to the normal behavior of the system.

 

 



