---
description: The GetFrame function returns a handle to a given frame within a capture.
ms.assetid: 'd40bc364-0028-4006-a6c2-6ee100366ba3'
title: GetFrame function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrame
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrame function

The **GetFrame** function returns a handle to a given frame within a capture.

## Syntax


```C++
HFRAME WINAPI GetFrame(
  _In_ HCAPTURE hCapture,
  _In_ DWORD    FrameNumber
);
```



## Parameters

<dl> <dt>

*hCapture* \[in\]
</dt> <dd>

Handle to a capture. To obtain the capture handle, call the [GetFrameCaptureHandle](getframecapturehandle.md) function.

</dd> <dt>

*FrameNumber* \[in\]
</dt> <dd>

Number (zero-based) of the frame. The number of the first frame in a capture is zero.

</dd> </dl>

## Return value

If the function is successful, the return value is a handle to the frame.

If the function is unsuccessful (that is, if *hCapture* is invalid, or the frame number is out of range), the return value is **NULL**.

## Remarks

Use the **GetFrame** function to obtain the frame handle needed when locating instances of a property. The functions used to locate property instances are [FindPropertyInstance](findpropertyinstance.md) which locates the first instance, and [FindPropertyInstanceRestart](findpropertyinstancerestart.md) which locates the next instance.

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetFrame** function.

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

[FindPropertyInstance](findpropertyinstance.md)
</dt> <dt>

[FindPropertyInstanceRestart](findpropertyinstancerestart.md)
</dt> </dl>

 

 




