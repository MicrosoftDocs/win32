---
description: The GetCaptureCommentFromFilename function extracts the capture comment from a capture file.
ms.assetid: d3665cb0-d54d-45f7-aef9-c2e603d6f773
title: GetCaptureCommentFromFilename function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCaptureCommentFromFilename
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetCaptureCommentFromFilename function

The **GetCaptureCommentFromFilename** function extracts the capture comment from a [*capture file*](c.md).

## Syntax


```C++
DWORD  WINAPI GetCaptureCommentFromFilename(
  _In_ LPSTR lpFilename,
  _In_ LPSTR lpComment,
  _In_ DWORD BufferSize
);
```



## Parameters

<dl> <dt>

*lpFilename* \[in\]
</dt> <dd>

Pointer to the name of the capture file.

</dd> <dt>

*lpComment* \[in\]
</dt> <dd>

Pointer to a pre-allocated string for the comment.

</dd> <dt>

*BufferSize* \[in\]
</dt> <dd>

Size of the string.

</dd> </dl>

## Return value

If the function is successful (that is, if the comment is found and copied, or there is no comment in the capture file), the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is an error code.



| Return code                                                                                                 | Description                                                                  |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt>**NMERR\_FILE\_READ\_ERROR**</dt> </dl>     | The capture comment cannot be read.<br/>                               |
| <dl> <dt>**NMERR\_INVALID\_FILE\_FORMAT**</dt> </dl> | The Comment frame is not a valid file format.<br/>                     |
| <dl> <dt>**NMERR\_FILE\_NOT\_FOUND**</dt> </dl>      | The file specified by the *lpFilename* parameter cannot be found.<br/> |
| <dl> <dt>**NMERR\_INVALID\_PARAMETER**</dt> </dl>    | One of the parameters is specified incorrectly.<br/>                   |



 

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetCaptureCommentFromFilename** function.

To retrieve the comment of a real-time capture, call the [GetCaptureComment](getcapturecomment.md) function.

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

[GetCaptureComment](getcapturecomment.md)
</dt> </dl>

 

 




