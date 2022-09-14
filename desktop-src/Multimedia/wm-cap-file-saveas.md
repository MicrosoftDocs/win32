---
title: WM_CAP_FILE_SAVEAS message (Vfw.h)
description: The WM\_CAP\_FILE\_SAVEAS message copies the contents of the capture file to another file. You can send this message explicitly or by using the capFileSaveAs macro.
ms.assetid: fab37bee-3160-4ebc-b58f-46021ed49b55
keywords:
- WM_CAP_FILE_SAVEAS message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_FILE_SAVEAS
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_FILE\_SAVEAS message

The **WM\_CAP\_FILE\_SAVEAS** message copies the contents of the capture file to another file. You can send this message explicitly or by using the [**capFileSaveAs**](/windows/desktop/api/Vfw/nf-vfw-capfilesaveas) macro.


```C++
WM_CAP_FILE_SAVEAS 
wParam = (WPARAM) 0; 
lParam = (LPARAM) (LPVOID) (LPSTR) (szName); 
```



## Parameters

<dl> <dt>

<span id="szName"></span><span id="szname"></span><span id="SZNAME"></span>*szName*
</dt> <dd>

Pointer to the null-terminated string that contains the name of the destination file used to copy the file.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

If an error occurs and an error callback function is set using the [**WM\_CAP\_SET\_CALLBACK\_ERROR**](wm-cap-set-callback-error.md) message, the error callback function is called.

## Remarks

This message does not change the name or contents of the current capture file.

If the copy operation is unsuccessful due to a disk full error, the destination file is automatically deleted.

Typically, a capture file is preallocated for the largest capture segment anticipated and only a portion of it might be used to capture data. This message copies only the portion of the file containing the capture data.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Capture](video-capture.md)
</dt> <dt>

[Video Capture Messages](video-capture-messages.md)
</dt> </dl>

 

 





