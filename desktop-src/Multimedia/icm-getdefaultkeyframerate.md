---
title: ICM\_GETDEFAULTKEYFRAMERATE message
description: The ICM\_GETDEFAULTKEYFRAMERATE message queries a video compression driver for its default (or preferred) key-frame spacing. You can send this message explicitly or by using the ICGetDefaulteyFrameRate macro.
ms.assetid: '2ebe37cc-3ec2-4b52-bd8f-71c44b704647'
keywords: ["ICM_GETDEFAULTKEYFRAMERATE message Windows Multimedia"]
topic_type:
- apiref
api_name:
- ICM_GETDEFAULTKEYFRAMERATE
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# ICM\_GETDEFAULTKEYFRAMERATE message

The **ICM\_GETDEFAULTKEYFRAMERATE** message queries a video compression driver for its default (or preferred) key-frame spacing. You can send this message explicitly or by using the [**ICGetDefaulteyFrameRate**](icgetdefaultkeyframerate.md) macro.


```C++
ICM_GETDEFAULTKEYFRAMERATE 
wParam = (DWORD_PTR) (LPVOID) &amp;dwICValue; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="dwICValue"></span><span id="dwicvalue"></span><span id="DWICVALUE"></span>*dwICValue*
</dt> <dd>

Address to contain the preferred key-frame spacing.

</dd> </dl>

## Return Value

Returns ICERR\_OK if the driver supports this message or ICERR\_UNSUPPORTED otherwise.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Compression Manager](video-compression-manager.md)
</dt> <dt>

[Video Compression Messages](video-compression-messages.md)
</dt> </dl>

 

 





