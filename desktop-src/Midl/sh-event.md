---
title: sh_event keyword
description: The \ sh\_event\ keyword specifies the system object is a handle to an event.
keywords:
- sh_event keyword MIDL
topic_type:
- apiref
api_name:
- sh_event
api_type:
- NA
ms.topic: reference
ms.date: 02/05/2021
---

# sh\_event keyword

The **sh\_event** keyword specifies that a `system_handle` holds a handle to an event.

``` syntax
[system_handle(sh_event)]

[system_handle(sh_event, access-rights)]
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
    HRESULT NotifyThisEvent([in, system_handle(sh_event)] HANDLE listeningToThisEvent);
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

[Event Objects](../sync/event-objects.md)
</dt> <dt>

[Synchronization Object Security and Access Rights](../sync/synchronization-object-security-and-access-rights.md)
</dt> <dt>

[**CreateEvent** function](/windows/win32/api/synchapi/nf-synchapi-createeventa)
</dt> <dt>

[**CreateEventEx** function](/windows/win32/api/synchapi/nf-synchapi-createeventexa)
</dt> </dl>
