---
description: The GetFrameNumber function returns the number of a frame.
ms.assetid: 97d343a3-2a1e-47d7-bfc2-b63f8d84b29d
title: GetFrameNumber function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameNumber
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameNumber function

The **GetFrameNumber** function returns the number of a frame.

## Syntax


```C++
DWORD WINAPI GetFrameNumber(
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

If the function is successful, the return value is a zero-based frame number.

If the function is not successful, the return value is minus one (-1).

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetFrameNumber** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




