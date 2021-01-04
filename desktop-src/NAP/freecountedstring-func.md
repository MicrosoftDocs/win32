---
title: FreeCountedString function (NapUtil.h)
description: Frees a CountedString data structure.
ms.assetid: d080d247-9339-474b-866e-b412e82dd35f
keywords:
- FreeCountedString function NAP
topic_type:
- apiref
api_name:
- FreeCountedString
api_location:
- qutil.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# FreeCountedString function

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **FreeCountedString** function frees a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) data structure.

## Syntax


```C++
NAPAPI VOID WINAPI FreeCountedString(
  _In_ CountedString *countedString
);
```



## Parameters

<dl> <dt>

*countedString* \[in\]
</dt> <dd>

A pointer to the [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) data structure to free.

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

[**AllocCountedString**](alloccountedstring-func.md)
</dt> </dl>

 

 





