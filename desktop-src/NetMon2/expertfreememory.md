---
description: The ExpertFreeMemory function frees memory acquired by calls to the ExpertAllocMemory and ExpertReallocMemory functions.
ms.assetid: 0e7cc791-98dd-4522-afab-76ac9e74c715
title: ExpertFreeMemory function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExpertFreeMemory
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# ExpertFreeMemory function

The **ExpertFreeMemory** function frees memory acquired by calls to the [**ExpertAllocMemory**](expertallocmemory.md) and [**ExpertReallocMemory**](expertreallocmemory.md) functions.

## Syntax


```C++
SIZE_T WINAPI ExpertFreeMemory(
       HEXPERTKEY hExpertKey,
  _In_ LPVOID     pMemory
);
```



## Parameters

<dl> <dt>

*hExpertKey* 
</dt> <dd>

Unique expert identifier. Network Monitor passes *hExpertKey* to the expert when it calls the [Run](run.md) function.

</dd> <dt>

*pMemory* \[in\]
</dt> <dd>

Pointer to the memory that Network Monitor allocates. The *pMemory* pointer can be returned by a previous call to [**ExpertAllocMemory**](expertallocmemory.md) or [**ExpertReallocMemory**](expertreallocmemory.md).

</dd> </dl>

## Return value

If the function is successful. the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value indicates the reason for the failure. If the return value is NMERR\_EXPERT\_TERMINATE, the expert immediately cleans up and returns.

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



 

 




