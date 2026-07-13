---
title: LBN_SETFOCUS notification code (Winuser.h)
description: Notifies the application that the list box has received the keyboard focus. The parent window of the list box receives this notification code through the WM\_COMMAND message.
ms.assetid: d9e5e035-98a5-4ece-ba40-6d341c101859
keywords:
- LBN_SETFOCUS notification code Windows Controls
topic_type:
- apiref
api_name:
- LBN_SETFOCUS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LBN\_SETFOCUS notification code

Notifies the application that the list box has received the keyboard focus. The parent window of the list box receives this notification code through the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.


```C++
LBN_SETFOCUS

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](../winmsg/loword.md) contains the identifier of the list box. The [**HIWORD**](../winmsg/hiword.md) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the list box.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[LBN\_KILLFOCUS](lbn-killfocus.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](../winmsg/hiword.md)
</dt> <dt>

[**LOWORD**](../winmsg/loword.md)
</dt> <dt>

[**WM\_COMMAND**](/windows/desktop/menurc/wm-command)
</dt> </dl>

 

