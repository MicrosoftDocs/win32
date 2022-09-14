---
title: RtlDisownModuleHeapAllocation function
description: Removes an allocation from tracking by Application Verifier so that it isn't flagged as a leak when the module that allocated the memory is unloaded.
ms.topic: reference
ms.date: 03/13/2022
req.lib: Ntdll.lib
req.dll: Ntdll.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- Ntdll.dll
api_name:
- RtlDisownModuleHeapAllocation
targetos: Windows
---

# RtlDisownModuleHeapAllocation function

Removes an allocation from tracking by Application Verifier so that it isn't flagged as a leak when the module that allocated the memory is unloaded.

## Syntax

```cpp
NTSTATUS WINAPI RtlDisownModuleHeapAllocation(
  _In_ HANDLE HeapHandle,
  _In_ PVOID Allocation
);
```

## Parameters

`HeapHandle`

Type: **[HANDLE](../../winprog/windows-data-types.md)**

The heap handle where the allocation is made.

`Allocation`

Type: **[PVOID](../../winprog/windows-data-types.md)**

A pointer to the memory allocation to be ignored by Application Verifier leak tracking.

## Return value

Returns **STATUS_SUCCESS**.

## Remarks

**RtlDisownModuleHeapAllocation** is provided so that Application Verifier can expect that an allocation might outlive the module that allocated it. In that case, Application Verifier can remove the allocation from its internal tracking so that it isn't flagged as a leak when the module that made the allocation is unloaded. This function is a no-op when Application Verifier isn't enabled.

**RtlDisownModuleHeapAllocation** isn't associated with a header file. But the associated import library, `Ntdll.lib`, is available in the Windows Driver Kit (WDK). You can also call **RtlDisownModuleHeapAllocation** by first using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw) function (to load `Ntdll.dll`), and then by calling the [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) function to retrieve the address of **RtlDisownModuleHeapAllocation**.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | N/A |
| **Library** | Ntdll.lib in the Windows Driver Kit (WDK) |
| **DLL** | Ntdll.dll |
