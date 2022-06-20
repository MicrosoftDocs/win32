---
title: sh_process keyword
description: The \ sh\_process\ keyword specifies the system object is a handle to a process.
keywords:
- sh_process keyword MIDL
topic_type:
- apiref
api_name:
- sh_process
api_type:
- NA
ms.topic: reference
ms.date: 02/05/2021
---

# sh\_process keyword

The **sh\_process** keyword specifies that a `system_handle` holds a handle to a process.

``` syntax
[system_handle(sh_process)]

[system_handle(sh_process, access-rights)]
```

## Parameters

This keyword is a parameter for [**system_handle**](system-handle.md).

The [**system_handle**](system-handle.md) documentation also contains details on optional use of the *access-rights* parameter. The default behavior is `DUPLICATE_SAME_ACCESS` per [**DuplicateHandle** function](/windows/win32/api/handleapi/nf-handleapi-duplicatehandle) specifications.

## Remarks

In order to use this keyword with the `system_handle` attribute, the `-target` flag must be set to `NT100` (or higher) when running midl.exe.

## Examples

``` syntax
interface MyInterface : IUnknown                         
{         
    HRESULT GetStubProcess([out, system_handle(sh_process)] HANDLE* processHandle);

    HRESULT WatchProcess([in, system_handle(sh_process, PROCESS_QUERY_INFORMATION | PROCESS_QUERY_LIMITED_INFORMATION)] HANDLE processHandle);
}
```

## Requirements

| &nbsp; | &nbsp; |
|-|-|
| Minimum supported client | Windows 10 Anniversary Update (version 1607, build 14393) |
| Minimum supported server | Windows Server 2016 (build 14393) |

## See also

<dl> <dt>

[**system_handle**](system-handle.md)
</dt> <dt>

[About Processes and Threads](../procthread/about-processes-and-threads.md)
</dt> <dt>

[Process Security and Access Rights](../procthread/process-security-and-access-rights.md)
</dt> <dt>

[**CreateProcess** function](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)
</dt> <dt>

[**OpenProcess** function](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess)
</dt> </dl>