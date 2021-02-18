---
title: sh_mutex keyword
description: The \ sh\_mutex\ keyword specifies the system object is a handle to a mutex.
keywords:
- sh_mutex keyword MIDL
topic_type:
- apiref
api_name:
- sh_mutex
api_type:
- NA
ms.topic: reference
ms.date: 02/05/2021
---

# sh\_mutex keyword

The **sh\_mutex** keyword specifies that a `system_handle` holds a handle to a mutex.

``` syntax
[system_handle(sh_mutex)]

[system_handle(sh_mutex, access-rights)]
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
    HRESULT WaitOnThisMutex([in, system_handle(sh_mutex)] HANDLE mutex);
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

[Mutex Objects](../sync/mutex-objects.md)
</dt> <dt>

[Synchronization Object Security and Access Rights](../sync/synchronization-object-security-and-access-rights.md)
</dt> <dt>

[**CreateMutex** function](/windows/win32/api/synchapi/nf-synchapi-createmutexa)
</dt> <dt>

[**CreateMutexEx** function](/windows/win32/api/synchapi/nf-synchapi-createmutexexa)
</dt> </dl>