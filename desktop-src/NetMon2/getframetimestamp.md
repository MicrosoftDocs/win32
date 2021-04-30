---
description: The GetFrameTimeStamp function returns the time stamp of a given frame.
ms.assetid: 4ac50400-6674-40fa-9a69-9c0ccb55b92c
title: GetFrameTimeStamp function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameTimeStamp
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameTimeStamp function

The **GetFrameTimeStamp** function returns the time stamp of a given frame.

## Syntax


```C++
__int64 WINAPI GetFrameTimeStamp(
  _In_ HFRAME hFrame
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame.

</dd> </dl>

## Return value

If the function is successful, the return value is the time stamp of the frame   in microseconds.

If the function is unsuccessful, the return value is minus one (-1).

## Remarks

The **GetFrameTimeStamp** function returns a time stamp that shows the elapsed time between the start of the capture process, and the recording of the frame.

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetFrameTimeStamp** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




