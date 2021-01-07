---
description: Sent by a File Manager extension to cause File Manager to repaint either its active window or all of its windows.
title: FM_REFRESH_WINDOWS message (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FM_REFRESH_WINDOWS
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: 210168c6-d83b-4ffd-93d4-d22fa748cef2
api_name: 
 - FM_REFRESH_WINDOWS
api_type: 
 - HeaderDef
api_location: 
 - Wfext.h
topic_type: 
 - APIRef
 - kbSyntax

---

# FM\_REFRESH\_WINDOWS message

Sent by a File Manager extension to cause File Manager to repaint either its active window or all of its windows.

## Parameters

<dl> <dt>

*fRepaint* 
</dt> <dd>

A value that indicates whether File Manager repaints its active window or all of its windows. If this parameter is **TRUE**, File Manager repaints all of its windows. Otherwise, File Manager repaints only its active window.

</dd> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

No return value.

## Remarks

File system changes caused by an extension are automatically detected by File Manager. An extension should use this message only in situations where drive connections are made or canceled.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> </dl>

 

 




