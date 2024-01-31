---
description: Gets the Shared User Data for a given DataId.
ms.assetid: a70ff2fc-8b86-441e-b40a-db0770f8a793
title: RtlGetSystemGlobalData function
ms.topic: reference
ms.date: 08/31/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlGetSystemGlobalData
api_type: 
- DllExport
api_location: 
- Ntdll.dll
- Vertdll.dll
---

# RtlGetSystemGlobalData function

\[This function may be changed or removed from Windows without further notice.\]

Gets the Shared User Data for a given DataId.

## Syntax

```cpp
NTSTATUS RtlGetSystemGlobalData (
    _In_ RTL_SYSTEM_GLOBAL_DATA_ID DataId,
    _Inout_ PVOID Buffer,
    _In_ ULONG Size
    )
```

## Parameters

*DataId* `[in]`

Supplies an ID of the features being queried from the Shared User Data.

*Buffer* `[in][out]`

A buffer in which to store the data.

*Size* `[in]`

The size of the buffer.

## Return value

Returns an `NTSTATUS` value indicating success or failure of the function.

## Remarks

## Requirements

| Requirement | Value |
|----------------|-------------------------------------|
| DLL | Ntdll.dll<br>Vertdll.dll |

## See also

[Enclaves APIs available in Vertdll](../trusted-execution/enclaves-available-in-vertdll.md)
