---
title: sh_reg_key keyword
description: The \ sh\_reg\_key\ keyword specifies the system object is a handle to a registry key.
keywords:
- sh_reg_key keyword MIDL
topic_type:
- apiref
api_name:
- sh_reg_key keyword
api_type:
- NA
ms.topic: reference
ms.date: 02/05/2021
---

# sh\_reg\_key keyword

The **sh\_reg\_key** keyword specifies that a `system_handle` holds a handle to a registry key.

``` syntax
[system_handle(sh_reg_key)]

[system_handle(sh_reg_key, access-rights)]
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
    HRESULT GetConfigurationKey([out, system_handle(sh_reg_key)] HANDLE* key);

    HRESULT SetKeyForWatch([in, system_handle(sh_reg_key, KEY_READ)] HANDLE watchKey);
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

[Registry](../sysinfo/registry.md)
</dt> <dt>

[Registry Key Security and Access Rights](../sysinfo/registry-key-security-and-access-rights.md)
</dt> <dt>

[**RegOpenKeyEx** function](/windows/win32/api/winreg/nf-winreg-regopenkeyexa)
</dt> <dt>
