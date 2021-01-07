---
description: The CCHeapSize function returns the size of the memory allocated by the CCHeapAlloc function.
ms.assetid: 45d0fd89-bcd1-4298-8cc3-834d86301f93
title: CCHeapSize function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCHeapSize
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# CCHeapSize function

The **CCHeapSize** function returns the size of the memory allocated by the **CCHeapAlloc** function.

## Syntax


```C++
SIZE_T WINAPI CCHeapSize(
   LPVOID lpMem
);
```



## Parameters

<dl> <dt>

*lpMem* 
</dt> <dd>

Pointer to the allocated memory.

</dd> </dl>

## Return value

If the function is successful, the return value is the size of the requested memory block   measured in bytes.

If the function is unsuccessful, the return value is **NULL**.

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

[CCHeapFree](ccheapfree.md)
</dt> <dt>

[CCHeapReAlloc](ccheaprealloc.md)
</dt> </dl>

 

 




