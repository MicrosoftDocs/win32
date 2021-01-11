---
description: The CCHeapFree function releases the memory allocated by the CCHeapAlloc function.
ms.assetid: 4e1f3332-b0cb-4c21-8c36-59e14c9686cd
title: CCHeapFree function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCHeapFree
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# CCHeapFree function

The **CCHeapFree** function releases the memory allocated by the **CCHeapAlloc** function.

## Syntax


```C++
BOOL WINAPI CCHeapFree(
   LPVOID lpMem
);
```



## Parameters

<dl> <dt>

*lpMem* 
</dt> <dd>

Pointer to the memory that this function releases.

</dd> </dl>

## Return value

If the **CCHeapFree** function is successful, the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[SetCCInstPtr](setccinstptr.md)
</dt> <dt>

[GetCCInstPtr](getccinstptr.md)
</dt> <dt>

[CCHeapAlloc](ccheapalloc.md)
</dt> <dt>

[CCHeapReAlloc](ccheaprealloc.md)
</dt> <dt>

[CCHeapSize](ccheapsize.md)
</dt> </dl>

 

 




