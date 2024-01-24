---
description: The ExpertReallocMemory function increases or decreases the amount of memory allocated by Network Monitor.
ms.assetid: 78b99a66-692a-4e83-8b0d-d68caf156bb6
title: ExpertReallocMemory function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExpertReallocMemory
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# ExpertReallocMemory function

The **ExpertReallocMemory** function increases or decreases the amount of memory allocated by Network Monitor.

## Syntax


```C++
LPVOID WINAPI ExpertReallocMemory(
  _In_  HEXPERTKEY hExpertKey,
  _In_  LPVOID     pOriginalMemory,
  _In_  SIZE_T     nBytes,
  _Out_ LPDWORD    pError
);
```



## Parameters

<dl> <dt>

*hExpertKey* \[in\]
</dt> <dd>

Unique identifier passed to the expert at [**Run**](run.md) or [**Configure**](configure.md).

</dd> <dt>

*pOriginalMemory* \[in\]
</dt> <dd>

Pointer to the memory allocated by Network Monitor. The *pOriginalMemory* pointer can be returned by a previous call to [**ExpertAllocMemory**](expertallocmemory.md) or **ExpertReallocMemory**.

</dd> <dt>

*nBytes* \[in\]
</dt> <dd>

Size of reallocated memory.

</dd> <dt>

*pError* \[out\]
</dt> <dd>

On return, an error code if the function fails. If the error code is NMERR\_EXPERT\_TERMINATE, the expert must clean up and return immediately.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to the allocated memory.

If the function is unsuccessful, the return value is **NULL**, and *pError* (if it is a non-**NULL** value) indicates the reason for the failure.

## Remarks

It is important to note that an expert should use the Network Monitor memory allocation functions for memory management. If your expert fails during run time, using these functions will allow Network Monitor to free the memory it has allocated.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




