---
title: FreeConnections function (NapUtil.h)
description: Frees a Connections data structure.
ms.assetid: bb339d71-f8e3-48d8-834d-8b957e0cb5ec
keywords:
- FreeConnections function NAP
topic_type:
- apiref
api_name:
- FreeConnections
api_location:
- qutil.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# FreeConnections function

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **FreeConnections** function frees a [**Connections**](connections-struct.md) data structure.

## Syntax


```C++
NAPAPI VOID WINAPI FreeConnections(
  _In_ Connections *connections
);
```



## Parameters

<dl> <dt>

*connections* \[in\]
</dt> <dd>

A pointer to the [**Connections**](connections-struct.md) structure to free.

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



## See also

<dl> <dt>

[**AllocConnections**](allocconnections-func.md)
</dt> </dl>

 

 





