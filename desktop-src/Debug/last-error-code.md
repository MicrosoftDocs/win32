---
description: When an error occurs, most system functions return an error code, usually 0, NULL, or &\#8211;1.
ms.assetid: fd5b0d6e-78cf-4f51-b61d-d32576cd485a
title: Last-Error Code
ms.topic: article
ms.date: 05/31/2018
---

# Last-Error Code

When an error occurs, most system functions return an error code, usually 0, **NULL**, or –1. Many system functions also set an additional error code called the *last-error code*. This error code is maintained separately for each running thread; an error in one thread does not overwrite the last-error code in another thread. Any function can call the [**SetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-setlasterror) or [**SetLastErrorEx**](/windows/desktop/api/Winuser/nf-winuser-setlasterrorex) function to set the last-error code for the current thread. These functions are intended primarily for dynamic-link libraries (DLL), so they can provide information to the calling application. Note that some functions call **SetLastError** or **SetLastErrorEx** with 0 when they succeed, wiping out the error code set by the most recently failed function, while others do not.

An application can retrieve the last-error code by using the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function; the error code may tell more about what actually occurred to make the function fail. The documentation for system functions will indicate the conditions under which the function sets the last-error code.

The system defines a set of error codes that can be set as last-error codes or be returned by these functions. Error codes are 32-bit values (bit 31 is the most significant bit). Bit 29 is reserved for application-defined error codes; no system error code has this bit set. If you define error codes for your application, set this bit to indicate that the error code has been defined by an application and to ensure that the error codes do not conflict with any system-defined error codes. For more information, see WinError.h and [System Error Codes](system-error-codes.md).

 

 
