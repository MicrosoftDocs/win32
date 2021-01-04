---
title: FreeNetworkSoH function (NapUtil.h)
description: Frees a NetworkSoH data structure.
ms.assetid: a27d54a0-8b9c-4bf7-909c-1de5db55f429
keywords:
- FreeNetworkSoH function NAP
topic_type:
- apiref
api_name:
- FreeNetworkSoH
api_location:
- qutil.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# FreeNetworkSoH function

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **FreeNetworkSoH** function frees a [**NetworkSoH**](/windows/win32/api/naptypes/ns-naptypes-networksoh) data structure.

## Syntax


```C++
NAPAPI VOID WINAPI FreeNetworkSoH(
  _In_ NetworkSoH *networkSoh
);
```



## Parameters

<dl> <dt>

*networkSoh* \[in\]
</dt> <dd>

A pointer to the [**NetworkSoH**](/windows/win32/api/naptypes/ns-naptypes-networksoh) data structure to free.

</dd> </dl>

## Remarks

All the COM interfaces supported by the NAP system use standard COM memory management rules and the COM memory allocators (**CoTaskMemAlloc** and **CoTaskMemFree**):

-   **In** parameters are allocated and freed by the caller.
-   **Out** parameters are allocated by the callee and freed by the caller using **CoTaskMem**.
-   **In/out** parameters are allocated by the caller, freed and reallocated by the callee, and ultimately freed by the caller, using **CoTaskMem**.

All NAP functions for freeing memory also free all embedded pointers.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>NapUtil.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qutil.dll</dt> </dl> |



 

 





