---
title: CBN_SELCHANGE notification code (Winuser.h)
description: Sent when the user changes the current selection in the list box of a combo box.
ms.assetid: 2d0d711c-dfc4-485b-97bb-9ccfa7c5864b
keywords:
- CBN_SELCHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- CBN_SELCHANGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CBN\_SELCHANGE notification code

Sent when the user changes the current selection in the list box of a combo box. The user can change the selection by clicking in the list box or by using the arrow keys. The parent window of the combo box receives this notification code in the form of a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.


```C++
CBN_SELCHANGE

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) contains the control identifier of the combo box. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the combo box.

</dd> </dl>

## Remarks

To get the index of the current selection, send the [**CB\_GETCURSEL**](cb-getcursel.md) message to the control.

The CBN\_SELCHANGE notification code is not sent when the current selection is set using the [**CB\_SETCURSEL**](cb-setcursel.md) message.

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

[CBN\_CLOSEUP](cbn-closeup.md)
</dt> <dt>

[CBN\_DBLCLK](cbn-dblclk.md)
</dt> <dt>

[**CB\_GETCURSEL**](cb-getcursel.md)
</dt> <dt>

[**CB\_SETCURSEL**](cb-setcursel.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> <dt>

[**WM\_COMMAND**](/windows/desktop/menurc/wm-command)
</dt> </dl>

 

