---
description: The ExpertAllocMemory function allocates memory for the expert.
ms.assetid: 9ada5d3f-5f1d-4d3a-b79a-d51e021240f6
title: ExpertAllocMemory function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExpertAllocMemory
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# ExpertAllocMemory function

The **ExpertAllocMemory** function allocates memory for the expert.

## Syntax


```C++
LPVOID WINAPI ExpertAllocMemory(
        HEXPERTKEY hExpertKey,
  _In_  SIZE_T     nBytes,
  _Out_ LPDWORD    pError
);
```



## Parameters

<dl> <dt>

*hExpertKey* 
</dt> <dd>

Unique expert identifier. Network Monitor passes *hExpertKey* to the expert when it calls the [Run](run.md) function.

</dd> <dt>

*nBytes* \[in\]
</dt> <dd>

Allocated memory, measured in bytes.

</dd> <dt>

*pError* \[out\]
</dt> <dd>

Error indicator. If the function fails, the *nBytes* parameter contains the error code. If the error code is NMERR\_EXPERT\_TERMINATE, the expert must clean-up and return immediately.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to the allocated memory.

If the function is unsuccessful, the return value is **NULL**, and *pError* provides an error code that indicates the reason for the failure.

## Remarks

It is important to note that an expert should use the Network Monitor memory allocation functions (including [ExpertReallocMemory](expertreallocmemory.md)) for memory management. If your expert fails during run time, using these functions will allow Network Monitor to free the memory it has allocated.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




