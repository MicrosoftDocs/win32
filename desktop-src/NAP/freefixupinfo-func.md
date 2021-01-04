---
title: FreeFixupInfo function (NapUtil.h)
description: Frees a FixupInfo data structure.
ms.assetid: 6bf71ccf-2618-46a3-8a04-9f83a5b7b429
keywords:
- FreeFixupInfo function NAP
topic_type:
- apiref
api_name:
- FreeFixupInfo
api_location:
- qutil.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# FreeFixupInfo function

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **FreeFixupInfo** function frees a [**FixupInfo**](/windows/win32/api/naptypes/ns-naptypes-fixupinfo) data structure.

## Syntax


```C++
NAPAPI VOID WINAPI FreeFixupInfo(
  _In_ FixupInfo *fixupInfo
);
```



## Parameters

<dl> <dt>

*fixupInfo* \[in\]
</dt> <dd>

A pointer to the [**FixupInfo**](/windows/win32/api/naptypes/ns-naptypes-fixupinfo) data structure to free.

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

[**AllocFixupInfo**](allocfixupinfo-func.md)
</dt> </dl>

 

 





