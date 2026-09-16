---
title: Error Handling in COM (COM)
description: Error Handling in COM
ms.assetid: 15f3ae3e-1794-4948-a7aa-6309a703364b
ms.topic: reference
ms.date: 01/08/2025
---

# Error Handling in COM (COM)

Almost all COM functions and interface methods return a value of the type **HRESULT**. The **HRESULT** (the name can be read as "result handle") is a way of returning a success, warning, or error value. A **HRESULT** is actually not a handle (see [Why does HRESULT begin with H when it's not a handle to anything?](https://devblogs.microsoft.com/oldnewthing/20180117-00/?p=97815)); it's just a value with several fields encoded into it. As per the COM specification, a result of zero indicates success, and a nonzero result indicates failure.

> [!IMPORTANT]
> **Always check HRESULT return values.** Never ignore the return value of a COM function. Use the `FAILED()` and `SUCCEEDED()` macros (defined in `<winerror.h>`) — do not compare directly against `S_OK`, because success codes other than `S_OK` exist (for example, `S_FALSE`):
>
> ```cpp
> // ✅ Correct — handles all failure codes
> HRESULT hr = pStream->Read(buffer, cbSize, &cbRead);
> if (FAILED(hr)) {
>     // Handle error
>     return hr;
> }
>
> // ❌ Wrong — misses failure codes that aren't E_FAIL
> if (hr == E_FAIL) { ... }
>
> // ❌ Wrong — S_FALSE is success but != S_OK
> if (hr != S_OK) { /* this fires for S_FALSE too */ }
> ```
>
> **Modern helpers for error handling:**
> - `THROW_IF_FAILED(hr)` — [Windows Implementation Libraries (wil)](https://github.com/microsoft/wil) throws a C++ exception on failure
> - `winrt::check_hresult(hr)` — C++/WinRT equivalent, throws `winrt::hresult_error`
> - `LOG_IF_FAILED(hr)` — wil macro that logs on failure but continues execution

At the source code level, all error values consist of three parts, separated by underscores. The first part is the prefix that identifies the facility associated with the error, the second part is E for error, and the third part is a string that describes the actual condition. For example, **STG\_E\_MEDIUMFULL** is returned when there is no space left on a hard disk. The **STG** prefix indicates the storage facility, the **E** indicates that the status code represents an error, and the **MEDIUMFULL** provides specific information about the error. Many of the values that you might want to return from an interface method or function are defined in Winerror.h.

For more information about error handling, see the following sections:

-   [Structure of COM Error Codes](structure-of-com-error-codes.md)
-   [Codes in FACILITY\_ITF](codes-in-facility-itf.md)
-   [Using Macros for Error Handling](using-macros-for-error-handling.md)
-   [COM Error Handling in Java and Visual Basic](com-error-handling-in-java-and-visual-basic.md)
-   [Error Handling Strategies](error-handling-strategies.md)
-   [Handling Unknown Errors](handling-unknown-errors.md)

## Related topics

<dl> <dt>

[COM Error Codes](com-error-codes.md)
</dt> </dl>

 

 




