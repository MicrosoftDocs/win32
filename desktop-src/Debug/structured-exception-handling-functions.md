---
Description: The following functions are used in structured exception handling.
ms.assetid: 61cf055b-eb9a-4e56-9d36-21fc95adea77
title: Structured Exception Handling Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Structured Exception Handling Functions

The following functions are used in structured exception handling.

-   [**AbnormalTermination**](abnormaltermination.md)

    Indicates whether the **\_\_try** block of a termination handler terminated normally.

-   [**AddVectoredContinueHandler**](https://msdn.microsoft.com/en-us/library/ms679273(v=VS.85).aspx)

    Registers a vectored continue handler.

-   [**AddVectoredExceptionHandler**](https://msdn.microsoft.com/en-us/library/ms679274(v=VS.85).aspx)

    Registers a vectored exception handler.

-   [**GetExceptionCode**](getexceptioncode.md)

    Retrieves a code that identifies the type of exception that occurred.

-   [**GetExceptionInformation**](getexceptioninformation.md)

    Retrieves a machine-independent description of an exception, and information about the machine state that existed for the thread when the exception occurred.

-   [**RaiseException**](https://msdn.microsoft.com/en-us/library/ms680552(v=VS.85).aspx)

    Raises an exception in the calling thread.

-   [**RemoveVectoredContinueHandler**](https://msdn.microsoft.com/en-us/library/ms680567(v=VS.85).aspx)

    Unregisters a vectored continue handler.

-   [**RemoveVectoredExceptionHandler**](https://msdn.microsoft.com/en-us/library/ms680571(v=VS.85).aspx)

    Unregisters a vectored exception handler.

-   [**RtlAddGrowableFunctionTable**](/windows/desktop/api/WinNT/nf-winnt-rtladdgrowablefunctiontable)

    Informs the system of a dynamic function table representing a region of memory containing code.

-   [**RtlDeleteGrowableFunctionTable**](/windows/desktop/api/WinNT/nf-winnt-rtldeletegrowablefunctiontable)

    Informs the system that a previously reported dynamic function table is no longer in use.

-   [**RtlGrowFunctionTable**](/windows/desktop/api/WinNT/nf-winnt-rtlgrowfunctiontable)

    Reports that a dynamic function table has increased in size.

-   [**SetUnhandledExceptionFilter**](https://msdn.microsoft.com/en-us/library/ms680634(v=VS.85).aspx)

    Enables an application to supersede the top-level exception handler of each thread and process.

-   [**UnhandledExceptionFilter**](https://msdn.microsoft.com/en-us/library/ms681401(v=VS.85).aspx)

    Passes unhandled exceptions to the debugger, if the process is being debugged.

-   [**VectoredHandler**](/windows/desktop/api/WinNT/nc-winnt-pvectored_exception_handler)

    An application-defined function that serves as a vectored exception handler.

The following functions are used only on 64-bit Windows.

-   [**RtlAddFunctionTable**](/windows/desktop/api/WinNT/nf-winnt-rtladdfunctiontable)

    Adds a dynamic function table to the dynamic function table list.

-   [**RtlCaptureContext**](/windows/desktop/api/WinNT/nf-winnt-rtlcapturecontext)

    Retrieves a context record in the context of the caller.

-   [**RtlDeleteFunctionTable**](/windows/desktop/api/WinNT/nf-winnt-rtldeletefunctiontable)

    Removes a dynamic function table from the dynamic function table list.

-   [**RtlInstallFunctionTableCallback**](/windows/desktop/api/WinNT/nf-winnt-rtlinstallfunctiontablecallback)

    Adds a dynamic function table to the dynamic function table list.

-   [**RtlRestoreContext**](/windows/desktop/api/WinNT/nf-winnt-rtlrestorecontext)

    Restores the context of the caller to the specified context record.

 

 



