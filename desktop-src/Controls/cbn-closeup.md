---
title: CBN_CLOSEUP notification code
description: Sent when the list box of a combo box has been closed. The parent window of the combo box receives this notification code through the WM\_COMMAND message.
ms.assetid: 79b2108e-1ef3-433d-a0b0-ac9ad1a93905
keywords:
- CBN_CLOSEUP notification code Windows Controls
topic_type:
- apiref
api_name:
- CBN_CLOSEUP
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# CBN\_CLOSEUP notification code

Sent when the list box of a combo box has been closed. The parent window of the combo box receives this notification code through the [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
CBN_CLOSEUP

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) contains the control identifier of the combo box. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the combo box.

</dd> </dl>

## Remarks

If the user changed the current selection, the combo box also sends the [CBN\_SELCHANGE](cbn-selchange.md) notification code when the drop-down list closes. In general, you cannot predict the order in which notification codes will be sent. In particular, a CBN\_SELCHANGE notification code may occur either before or after a CBN\_CLOSEUP notification code.

To execute a specific process each time the user selects a list item, you can handle either the [CBN\_SELCHANGE](cbn-selchange.md) or CBN\_CLOSEUP notification code. Typically, you would wait for the CBN\_CLOSEUP notification code before processing a change in the current selection. This can be particularly important if a significant amount of processing is required.

This notification code is not sent to a combo box that has the [**CBS\_SIMPLE**](combo-box-styles.md) style.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[CBN\_DROPDOWN](cbn-dropdown.md)
</dt> <dt>

[CBN\_SELCHANGE](cbn-selchange.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659)
</dt> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





