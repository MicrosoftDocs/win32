---
description: Returns a pointer to the comment of a capture.
ms.assetid: 3ef5c5b3-5586-469f-8975-049713715403
title: GetCaptureComment function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCaptureComment
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetCaptureComment function

The **GetCaptureComment** function returns a pointer to the comment of a capture.

## Syntax


```C++
LPSTR WINAPI GetCaptureComment(
  _In_ HCAPTURE hCapture
);
```



## Parameters

<dl> <dt>

*hCapture* \[in\]
</dt> <dd>

A handle to the capture. For more information about obtaining the capture handle, see the Remarks section.

</dd> </dl>

## Return value

If the function is successful (that is, if the capture contains a comment), the return value is a pointer to the comment string.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

Do not alter the returned comment string which is the actual comment string that is in the loaded capture. Any changes can corrupt the capture. Attempts to modify the string result in an access violation.

The handle of the capture can be obtained in several ways, depending if the call is made by an expert or parser. For experts, the handle is specified in the **hCapture** member of the [EXPERTSTARTUPINFO](expertstartupinfo.md) structure. For parsers, the capture handle can be obtained by calling the [GetFrameCaptureHandle](getframecapturehandle.md) function.

To retrieve the comment of a capture from its capture file, call the [GetCaptureCommentFromFilename](getcapturecommentfromfilename.md) function.

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetCaptureComment** function.

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

[EXPERTSTARTUPINFO](expertstartupinfo.md)
</dt> <dt>

[GetCaptureCommentFromFilename](getcapturecommentfromfilename.md)
</dt> <dt>

[GetFrameCaptureHandle](getframecapturehandle.md)
</dt> </dl>

 

 




