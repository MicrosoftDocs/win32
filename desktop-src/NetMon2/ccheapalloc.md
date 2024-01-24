---
description: The CCHeapAlloc function allocates memory on a capture-by-capture basis.
ms.assetid: 6403c35f-d78f-48dc-90cc-0b76260bbab7
title: CCHeapAlloc function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCHeapAlloc
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# CCHeapAlloc function

The **CCHeapAlloc** function allocates memory on a capture-by-capture basis.

## Syntax


```C++
LPVOID WINAPI CCHeapAlloc(
   DWORD dwBytes,
   BOOL  bZeroInit
);
```



## Parameters

<dl> <dt>

*dwBytes* 
</dt> <dd>

Requested length of memory allocated.

</dd> <dt>

*bZeroInit* 
</dt> <dd>

Indicator of whether allocated memory was initialized. If the parameter value is **TRUE**, the allocated memory initializes to zero.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to the allocated memory. When you have finished using the allocated memory, free the memory by calling the [**CCHeapFree**](ccheapfree.md) function.

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

[**SetCCInstPtr**](setccinstptr.md)
</dt> <dt>

[**GetCCInstPtr**](getccinstptr.md)
</dt> <dt>

[**CCHeapFree**](ccheapfree.md)
</dt> <dt>

[**CCHeapReAlloc**](ccheaprealloc.md)
</dt> <dt>

[**CCHeapSize**](ccheapsize.md)
</dt> </dl>

 

 




