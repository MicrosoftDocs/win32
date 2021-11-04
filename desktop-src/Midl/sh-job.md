---
title: sh_job keyword
description: The \ sh\_job\ keyword specifies the system object is a handle to a job.
keywords:
- sh_job keyword MIDL
topic_type:
- apiref
api_name:
- sh_job
api_type:
- NA
ms.topic: reference
ms.date: 02/05/2021
---

# sh\_job keyword

The **sh\_job** keyword specifies that a `system_handle` holds a handle to a job.

``` syntax
[system_handle(sh_job)]

[system_handle(sh_job, access-rights)]
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
    HRESULT SetJob([in, system_handle(sh_job)] HANDLE job);

    HRESULT GetJobForAccounting([out, system_handle(sh_job, JOB_OBJECT_QUERY)] HANDLE* pJob);
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

[Job Objects](../procthread/job-objects.md)
</dt> <dt>

[Job Object Security and Access Rights](../procthread/job-object-security-and-access-rights.md)
</dt> <dt>

[**CreateJobObject** function](/windows/win32/api/winbase/nf-winbase-createjobobjecta)
</dt> </dl>
