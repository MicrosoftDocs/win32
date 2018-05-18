---
title: MCIWNDM\_PLAYREVERSE message
description: The MCIWNDM\_PLAYREVERSE message plays the current content in the reverse direction, beginning at the current position and ending at the beginning of the content or until another command stops playback.
ms.assetid: '93a22454-eca6-453f-abbe-6cf20198dbad'
keywords: ["MCIWNDM_PLAYREVERSE message Windows Multimedia"]
topic_type:
- apiref
api_name:
- MCIWNDM_PLAYREVERSE
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# MCIWNDM\_PLAYREVERSE message

The **MCIWNDM\_PLAYREVERSE** message plays the current content in the reverse direction, beginning at the current position and ending at the beginning of the content or until another command stops playback. You can send this message explicitly or by using the [**MCIWndPlayReverse**](mciwndplayreverse.md) macro.


```C++
MCIWNDM_PLAYREVERSE 
wParam = 0; 
lParam = 0; 
```



## Return Value

Returns zero if successful or an error otherwise.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndPlayReverse**](mciwndplayreverse.md)
</dt> </dl>

 

 





