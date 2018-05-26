---
title: WM\_CAP\_DLG\_VIDEOCOMPRESSION message
description: The WM\_CAP\_DLG\_VIDEOCOMPRESSION message displays a dialog box in which the user can select a compressor to use during the capture process.
ms.assetid: 526e4b5d-49a4-4bb5-92d6-cdd567636354
keywords:
- WM_CAP_DLG_VIDEOCOMPRESSION message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_DLG_VIDEOCOMPRESSION
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_CAP\_DLG\_VIDEOCOMPRESSION message

The **WM\_CAP\_DLG\_VIDEOCOMPRESSION** message displays a dialog box in which the user can select a compressor to use during the capture process. The list of available compressors can vary with the video format selected in the capture driver's Video Format dialog box. You can send this message explicitly or by using the [**capDlgVideoCompression**](/windows/win32/Vfw/nf-vfw-capdlgvideocompression?branch=master) macro.


```C++
WM_CAP_DLG_VIDEOCOMPRESSION 
wParam = (WPARAM) 0; 
lParam = 0L; 
```



## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

Use this message with capture drivers that provide frames only in the BI\_RGB format. This message is most useful in the step capture operation to combine capture and compression in a single operation. Compressing frames with a software compressor as part of a real-time capture operation is most likely too time-consuming to perform.

Compression does not affect the frames copied to the clipboard.

## Requirements



|                                     |                                                                                  |
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

 

 





