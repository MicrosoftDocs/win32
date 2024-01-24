---
description: The GetCCInstPtr function returns the pointer to the instance data added to the capture context.
ms.assetid: 6fb103d3-583b-4460-8b9a-ff921751b0eb
title: GetCCInstPtr function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCCInstPtr
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetCCInstPtr function

The **GetCCInstPtr** function returns the pointer to the instance data added to the capture context.

## Syntax


```C++
LPVOID WINAPI GetCCInstPtr(void);
```



## Parameters

This function has no parameters.

## Return value

If the function is successful, the return value is a pointer to the instance data of a specific capture.

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

[CCHeapAlloc](ccheapalloc.md)
</dt> <dt>

[CCHeapFree](ccheapfree.md)
</dt> <dt>

[CCHeapReAlloc](ccheaprealloc.md)
</dt> <dt>

[CCHeapSize](ccheapsize.md)
</dt> </dl>

 

 




