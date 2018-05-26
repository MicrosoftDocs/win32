---
Description: The following functions are used in structured exception handling.
ms.assetid: 61cf055b-eb9a-4e56-9d36-21fc95adea77
title: Structured Exception Handling Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Structured Exception Handling Functions

The following functions are used in structured exception handling.

-   [**AbnormalTermination**](abnormaltermination.md)

    Indicates whether the **\_\_try** block of a termination handler terminated normally.

-   [**AddVectoredContinueHandler**](/windows/win32/WinBase/?branch=master)

    Registers a vectored continue handler.

-   [**AddVectoredExceptionHandler**](/windows/win32/WinBase/?branch=master)

    Registers a vectored exception handler.

-   [**GetExceptionCode**](getexceptioncode.md)

    Retrieves a code that identifies the type of exception that occurred.

-   [**GetExceptionInformation**](getexceptioninformation.md)

    Retrieves a machine-independent description of an exception, and information about the machine state that existed for the thread when the exception occurred.

-   [**RaiseException**](/windows/win32/WinBase/?branch=master)

    Raises an exception in the calling thread.

-   [**RemoveVectoredContinueHandler**](/windows/win32/WinBase/?branch=master)

    Unregisters a vectored continue handler.

-   [**RemoveVectoredExceptionHandler**](/windows/win32/WinBase/?branch=master)

    Unregisters a vectored exception handler.

-   [**RtlAddGrowableFunctionTable**](/windows/win32/WinNT/nf-winnt-rtladdgrowablefunctiontable?branch=master)

    Informs the system of a dynamic function table representing a region of memory containing code.

-   [**RtlDeleteGrowableFunctionTable**](/windows/win32/WinNT/nf-winnt-rtldeletegrowablefunctiontable?branch=master)

    Informs the system that a previously reported dynamic function table is no longer in use.

-   [**RtlGrowFunctionTable**](/windows/win32/WinNT/nf-winnt-rtlgrowfunctiontable?branch=master)

    Reports that a dynamic function table has increased in size.

-   [**SetUnhandledExceptionFilter**](/windows/win32/WinBase/?branch=master)

    Enables an application to supersede the top-level exception handler of each thread and process.

-   [**UnhandledExceptionFilter**](/windows/win32/WinBase/?branch=master)

    Passes unhandled exceptions to the debugger, if the process is being debugged.

-   [**VectoredHandler**](/windows/win32/WinNT/nc-winnt-pvectored_exception_handler?branch=master)

    An application-defined function that serves as a vectored exception handler.

The following functions are used only on 64-bit Windows.

-   [**RtlAddFunctionTable**](/windows/win32/WinNT/nf-winnt-rtladdfunctiontable?branch=master)

    Adds a dynamic function table to the dynamic function table list.

-   [**RtlCaptureContext**](/windows/win32/WinNT/nf-winnt-rtlcapturecontext?branch=master)

    Retrieves a context record in the context of the caller.

-   [**RtlDeleteFunctionTable**](/windows/win32/WinNT/nf-winnt-rtldeletefunctiontable?branch=master)

    Removes a dynamic function table from the dynamic function table list.

-   [**RtlInstallFunctionTableCallback**](/windows/win32/WinNT/nf-winnt-rtlinstallfunctiontablecallback?branch=master)

    Adds a dynamic function table to the dynamic function table list.

-   [**RtlRestoreContext**](/windows/win32/WinNT/nf-winnt-rtlrestorecontext?branch=master)

    Restores the context of the caller to the specified context record.

 

 



