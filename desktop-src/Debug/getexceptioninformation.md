---
Description: Retrieves a computer-independent description of an exception, and information about the computer state that exists for the thread when the exception occurs. This function can be called only from within the filter expression of an exception handler.
ms.assetid: e982794a-d5f1-4fb4-a2b9-aa8da18cb8ae
title: GetExceptionInformation macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetExceptionInformation macro

Retrieves a computer-independent description of an exception, and information about the computer state that exists for the thread when the exception occurs. This function can be called only from within the filter expression of an exception handler.

> [!Note]  
> The Microsoft C/C++ Optimizing Compiler interprets this function as a keyword, and its use outside the appropriate exception-handling syntax generates a compiler error.

 

## Syntax


```C++
LPEXCEPTION_POINTERS GetExceptionInformation(void);
```



## Parameters

This macro has no parameters.

## Return value

A pointer to an [**EXCEPTION\_POINTERS**](/windows/win32/WinNT/ns-winnt-_exception_pointers?branch=master) structure that contains pointers to the following two structures:

-   [**EXCEPTION\_RECORD**](/windows/win32/WinNT/ns-winnt-_exception_record?branch=master) structure that contains a description of the exception.
-   [**CONTEXT**](/windows/win32/WinNT/ns-winnt-_arm64_nt_context?branch=master) structure that contains the computer state information.

## Remarks

The filter expression (from which the function is called) is evaluated if an exception occurs during execution of the **\_\_try** block, and it determines whether or not the **\_\_except** block is executed.

The filter expression can invoke a filter function. The filter function cannot call **GetExceptionInformation**. However, the return value of **GetExceptionInformation** can be passed as a parameter to a filter function.

To pass the [**EXCEPTION\_POINTERS**](/windows/win32/WinNT/ns-winnt-_exception_pointers?branch=master) information to the exception-handler block, the filter expression or filter function must copy the pointer or the data to safe storage that the handler can later access.

In the case of nested handlers, each filter expression is evaluated until one is evaluated as **EXCEPTION\_EXECUTE\_HANDLER** or **EXCEPTION\_CONTINUE\_EXECUTION**. Each filter expression can invoke **GetExceptionInformation** to get exception information.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**CONTEXT**](/windows/win32/WinNT/ns-winnt-_arm64_nt_context?branch=master)
</dt> <dt>

[**EXCEPTION\_POINTERS**](/windows/win32/WinNT/ns-winnt-_exception_pointers?branch=master)
</dt> <dt>

[**EXCEPTION\_RECORD**](/windows/win32/WinNT/ns-winnt-_exception_record?branch=master)
</dt> <dt>

[**GetExceptionCode**](getexceptioncode.md)
</dt> <dt>

[**GetXStateFeaturesMask**](/windows/win32/WinBase/nf-winbase-getxstatefeaturesmask?branch=master)
</dt> <dt>

[Structured Exception Handling Functions](structured-exception-handling-functions.md)
</dt> <dt>

[Structured Exception Handling Overview](structured-exception-handling.md)
</dt> <dt>

[Enable Windows Support for Intel AVX](appqual.enable_windows_7_support_for_intel_avx)
</dt> </dl>

 

 




