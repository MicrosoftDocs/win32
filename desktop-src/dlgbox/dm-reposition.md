---
title: DM_REPOSITION message (Winuser.h)
description: Repositions a top-level dialog box so that it fits within the desktop area. An application can send this message to a dialog box after resizing it to ensure that the entire dialog box remains visible.
ms.assetid: 8386d23e-06ea-4ea7-adde-ac97fc97861d
keywords:
- DM_REPOSITION message Dialog Boxes
topic_type:
- apiref
api_name:
- DM_REPOSITION
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DM\_REPOSITION message

Repositions a top-level dialog box so that it fits within the desktop area. An application can send this message to a dialog box after resizing it to ensure that the entire dialog box remains visible.


```C++
#define WM_USER              0x0400
#define DM_REPOSITION       (WM_USER+2)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

This message has no effect if the dialog box is a child window.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Dialog Boxes Overview](dialog-boxes.md)
</dt> </dl>

 

 





