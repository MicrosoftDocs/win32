---
description: The SetCCInstPtr function captures a context instance pointer.
ms.assetid: 31924608-4aa1-4801-a5de-d8de054e12d9
title: SetCCInstPtr function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetCCInstPtr
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# SetCCInstPtr function

The **SetCCInstPtr** function captures a context instance pointer.

## Syntax


```C++
VOID WINAPI SetCCInstPtr(
   LPVOID lpCurCaptureInst
);
```



## Parameters

<dl> <dt>

*lpCurCaptureInst* 
</dt> <dd>

Pointer to the instance data added to the capture.

</dd> </dl>

## Return value

None.

## Remarks

Use this function to store a pointer to a block that was allocated with the **CCHeapAlloc** function. Each parser can set a single instance of data on a capture.

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

[GetCCInstPtr](getccinstptr.md)
</dt> <dt>

[CCHeapAlloc](ccheapalloc.md)
</dt> <dt>

[CCHeapFree](ccheapfree.md)
</dt> <dt>

[CCHeapReAlloc](ccheaprealloc.md)
</dt> <dt>

[CCHeapSize](ccheapsize.md)
</dt> </dl>

 

 




