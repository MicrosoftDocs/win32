---
title: LBN_SELCANCEL notification code (Winuser.h)
description: Notifies the application that the user has canceled the selection in a list box. The parent window of the list box receives this notification code through the WM\_COMMAND message.
ms.assetid: 82e39f22-090e-4dda-8ddc-6a1fe4704fc7
keywords:
- LBN_SELCANCEL notification code Windows Controls
topic_type:
- apiref
api_name:
- LBN_SELCANCEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LBN\_SELCANCEL notification code

Notifies the application that the user has canceled the selection in a list box. The parent window of the list box receives this notification code through the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.


```C++
LBN_SELCANCEL

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

## Remarks

This notification code is sent only by a list box that has the L[**BS\_NOTIFY**](button-styles.md) style.

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

[**LB\_SETCURSEL**](lb-setcursel.md)
</dt> <dt>

[LBN\_DBLCLK](lbn-dblclk.md)
</dt> <dt>

[LBN\_SELCHANGE](lbn-selchange.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](../winmsg/hiword.md)
</dt> <dt>

[**LOWORD**](../winmsg/loword.md)
</dt> <dt>

[**WM\_COMMAND**](/windows/desktop/menurc/wm-command)
</dt> </dl>

 

