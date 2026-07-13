---
description: Disables thread attach and detach callouts to a DLL.
ms.assetid: be6ab13f-c74c-4a77-bf91-32c795d87099
title: LdrDisableThreadCalloutsForDll function
ms.topic: reference
ms.date: 08/31/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LdrDisableThreadCalloutsForDll
api_type: 
- DllExport
api_location: 
- Ntdll.dll
- Vertdll.dll
---

# LdrDisableThreadCalloutsForDll function

\[This function may be changed or removed from Windows without further notice.\]

Disables thread attach and detach callouts to a DLL.

## Syntax

```cpp
NTSTATUS LdrDisableThreadCalloutsForDll (
    _In_ PVOID DllHandle
    )
```

## Parameters

*DllHandle* `[in]`

Supplies a handle to a loaded DLL.

## Return value

Returns an `NTSTATUS` value indicating success or failure of the function.

## Remarks

This function should not be called with the data table lock held with shared access.

## Requirements

| Requirement | Value |
|----------------|-------------------------------------|
| DLL | Ntdll.dll<br>Vertdll.dll |

## See also

[Enclaves APIs available in Vertdll](../trusted-execution/enclaves-available-in-vertdll.md)
