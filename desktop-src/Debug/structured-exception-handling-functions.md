---
Description: 'The following functions are used in structured exception handling.'
ms.assetid: '61cf055b-eb9a-4e56-9d36-21fc95adea77'
title: Structured Exception Handling Functions
---

# Structured Exception Handling Functions

The following functions are used in structured exception handling.

-   [**AbnormalTermination**](abnormaltermination.md)

    Indicates whether the **\_\_try** block of a termination handler terminated normally.

-   [**AddVectoredContinueHandler**](addvectoredcontinuehandler.md)

    Registers a vectored continue handler.

-   [**AddVectoredExceptionHandler**](addvectoredexceptionhandler.md)

    Registers a vectored exception handler.

-   [**GetExceptionCode**](getexceptioncode.md)

    Retrieves a code that identifies the type of exception that occurred.

-   [**GetExceptionInformation**](getexceptioninformation.md)

    Retrieves a machine-independent description of an exception, and information about the machine state that existed for the thread when the exception occurred.

-   [**RaiseException**](raiseexception.md)

    Raises an exception in the calling thread.

-   [**RemoveVectoredContinueHandler**](removevectoredcontinuehandler.md)

    Unregisters a vectored continue handler.

-   [**RemoveVectoredExceptionHandler**](removevectoredexceptionhandler.md)

    Unregisters a vectored exception handler.

-   [**RtlAddGrowableFunctionTable**](rtladdgrowablefunctiontable.md)

    Informs the system of a dynamic function table representing a region of memory containing code.

-   [**RtlDeleteGrowableFunctionTable**](rtldeletegrowablefunctiontable.md)

    Informs the system that a previously reported dynamic function table is no longer in use.

-   [**RtlGrowFunctionTable**](rtlgrowfunctiontable.md)

    Reports that a dynamic function table has increased in size.

-   [**SetUnhandledExceptionFilter**](setunhandledexceptionfilter.md)

    Enables an application to supersede the top-level exception handler of each thread and process.

-   [**UnhandledExceptionFilter**](unhandledexceptionfilter.md)

    Passes unhandled exceptions to the debugger, if the process is being debugged.

-   [**VectoredHandler**](vectoredhandler.md)

    An application-defined function that serves as a vectored exception handler.

The following functions are used only on 64-bit Windows.

-   [**RtlAddFunctionTable**](rtladdfunctiontable.md)

    Adds a dynamic function table to the dynamic function table list.

-   [**RtlCaptureContext**](rtlcapturecontext.md)

    Retrieves a context record in the context of the caller.

-   [**RtlDeleteFunctionTable**](rtldeletefunctiontable.md)

    Removes a dynamic function table from the dynamic function table list.

-   [**RtlInstallFunctionTableCallback**](rtlinstallfunctiontablecallback.md)

    Adds a dynamic function table to the dynamic function table list.

-   [**RtlRestoreContext**](rtlrestorecontext.md)

    Restores the context of the caller to the specified context record.

 

 



