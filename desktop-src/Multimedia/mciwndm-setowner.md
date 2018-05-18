---
title: MCIWNDM\_SETOWNER message
description: The MCIWNDM\_SETOWNER message sets the window to receive notification messages associated with the MCIWnd window. You can send this message explicitly or by using the MCIWndSetOwner macro.
ms.assetid: 'c2d0f9d5-bf60-4036-a613-65ba1ed83110'
keywords: ["MCIWNDM_SETOWNER message Windows Multimedia"]
topic_type:
- apiref
api_name:
- MCIWNDM_SETOWNER
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# MCIWNDM\_SETOWNER message

The **MCIWNDM\_SETOWNER** message sets the window to receive notification messages associated with the MCIWnd window. You can send this message explicitly or by using the [**MCIWndSetOwner**](mciwndsetowner.md) macro.


```C++
MCIWNDM_SETOWNER 
wParam = (WPARAM) hwndP; 
lParam = 0; 
```



## Parameters

<dl> <dt>

<span id="hwndP"></span><span id="hwndp"></span><span id="HWNDP"></span>*hwndP*
</dt> <dd>

Handle to the window to receive the notification messages.

</dd> </dl>

## Return Value

Returns zero.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndSetOwner**](mciwndsetowner.md)
</dt> </dl>

 

 





