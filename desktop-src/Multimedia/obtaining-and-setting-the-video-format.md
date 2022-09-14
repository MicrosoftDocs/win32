---
title: Obtaining and Setting the Video Format
description: Obtaining and Setting the Video Format
ms.assetid: 0e6baf24-7a79-45ab-9fc7-69334419956d
keywords:
- capGetVideoFormat macro
- capGetVideoFormatSize macro
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining and Setting the Video Format

The [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure is of variable length to accommodate standard and compressed data formats. Because this structure is of variable length, applications must always query the size of the structure and allocate memory before retrieving the current video format. The following example uses the [**capGetVideoFormatSize**](/windows/desktop/api/Vfw/nf-vfw-capgetvideoformatsize) macro to retrieve the buffer size and then calls the [**capGetVideoFormat**](/windows/desktop/api/Vfw/nf-vfw-capgetvideoformat) macro to retrieve the current video format.


```C++
LPBITMAPINFO lpbi;
DWORD dwSize;

dwSize = capGetVideoFormatSize(hWndC);
lpbi = GlobalAllocPtr (GHND, dwSize);
capGetVideoFormat(hWndC, lpbi, dwSize); 

// Access the video format and then free the allocated memory.
 
```



Applications can use the [**capSetVideoFormat**](/windows/desktop/api/Vfw/nf-vfw-capsetvideoformat) macro (or the [**WM\_CAP\_SET\_VIDEOFORMAT**](wm-cap-set-videoformat.md) message) to send a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) header structure to the capture window. Because video formats are device specific, your application should check the return value to determine if the format was accepted.

## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 