---
description: The ExpertMemorySize function returns the amount of memory allocated by the ExpertAllocMemory function.
ms.assetid: 60d3f33d-dc03-4c39-98fa-ec093398b51b
title: ExpertMemorySize function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExpertMemorySize
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# ExpertMemorySize function

The **ExpertMemorySize** function returns the amount of memory allocated by the [ExpertAllocMemory](expertallocmemory.md) function.

## Syntax


```C++
SIZE_T WINAPI ExpertMemorySize(
  _In_ HEXPERTKEY hExpertKey,
  _In_ LPVOID     pOriginalMemory
);
```



## Parameters

<dl> <dt>

*hExpertKey* \[in\]
</dt> <dd>

Unique expert identifier. Network Monitor passes *hExpertKey* to the expert when it calls the [Run](run.md) function.

</dd> <dt>

*pOriginalMemory* \[in\]
</dt> <dd>

Pointer to the memory address of the expert allocated by [ExpertAllocMemory](expertallocmemory.md).

</dd> </dl>

## Return value

The function returns the amount of allocated memory   in bytes.

## Remarks

For information on the **SIZE\_T** data type that **ExpertMemorySize** returns, see Data Types.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




