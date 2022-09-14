---
description: The GetFrameCaptureHandle function returns a handle to the capture based on a given frame.
ms.assetid: 71b32799-194c-40f8-8438-36aebaba31c7
title: GetFrameCaptureHandle function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameCaptureHandle
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameCaptureHandle function

The **GetFrameCaptureHandle** function returns a handle to the capture based on a given frame.

## Syntax


```C++
HCAPTURE WINAPI GetFrameCaptureHandle(
  _In_ HFRAME hFrame
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to a frame.

</dd> </dl>

## Return value

If the function is successful, the return value is a handle to the capture.

If the function is unsuccessful, the return value is 0.

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetFrameCaptureHandle** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




