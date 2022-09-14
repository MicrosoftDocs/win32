---
title: RoFailFastWithErrorContextInternal2 function
description: Raises a non-continuable exception in the current process, and also allows you to include additional error context not already captured by the OS.
ms.topic: reference
ms.date: 03/13/2020
req.lib: RuntimeObject.lib
req.dll: ComBase.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- ComBase.dll
api_name:
- RoFailFastWithErrorContextInternal2
targetos: Windows
---

# RoFailFastWithErrorContextInternal2 function

Raises a non-continuable exception in the current process, and also allows you to include additional error context not already captured by the operating system (OS).

## Syntax

```cpp
void WINAPI RoFailFastWithErrorContextInternal2(
  HRESULT hrError,
  ULONG cStowedExceptions,
  _In_reads_opt_(cStowedExceptions) PSTOWED_EXCEPTION_INFORMATION_V2 aStowedExceptionPointers[]
);
```

## Parameters

`hrError`

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

The **HRESULT** associated with the current error. The exception is raised for any value of *hrError*.

`cStowedExceptions`

Type: **[ULONG](../../winprog/windows-data-types.md)**

The number of elements in the *aStowedExceptionPointers* array.

`aStowedExceptionPointers`

Type: **[PSTOWED_EXCEPTION_INFORMATION_V2](../../wer/stowed-exception-information-v2.md)\[\]**

An array of pointers to [**STOWED_EXCEPTION_INFORMATION_V2**](../../wer/stowed-exception-information-v2.md) structures. Each structure contains info describing a stowed exception. The info in these structures is then submitted to Windows Error Reporting (WER) along with the stowed exception information that was captured by the platform.

## Return value

This function doesn't return a value.

## Remarks

**RoFailFastWithErrorContextInternal2** isn't associated with an import library nor a header file. You can call it by first using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw) function (to load `ComBase.dll`), and then by calling the [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) function to retrieve the address of **RoFailFastWithErrorContextInternal2**.

For more info, see [RoFailFastWithErrorContext function](/windows/win32/api/roerrorapi/nf-roerrorapi-rofailfastwitherrorcontext).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
| **Library** | N/A |
| **DLL** | ComBase.dll |

## See also

* [RoFailFastWithErrorContext function](/windows/win32/api/roerrorapi/nf-roerrorapi-rofailfastwitherrorcontext)
