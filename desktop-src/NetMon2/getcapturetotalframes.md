---
description: The GetCaptureTotalFrames function returns the total number of frames in the capture.
ms.assetid: a2b7902c-b80f-4a0a-b12a-2a139df30fca
title: GetCaptureTotalFrames function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCaptureTotalFrames
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetCaptureTotalFrames function

The **GetCaptureTotalFrames** function returns the total number of frames in the capture.

## Syntax


```C++
DWORD WINAPI GetCaptureTotalFrames(
  _In_ HCAPTURE hCapture
);
```



## Parameters

<dl> <dt>

*hCapture* \[in\]
</dt> <dd>

Handle to the capture. For information about obtaining the capture handle, see the Remarks section of this **GetCaptureTotalFrames** topic.

</dd> </dl>

## Return value

If the function is successful, the return value is the total number of frames in the capture.

If the function is unsuccessful, the return value is 0.

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetCaptureTotalFrames** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




