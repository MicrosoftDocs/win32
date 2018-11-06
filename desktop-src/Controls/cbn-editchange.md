---
title: CBN_EDITCHANGE notification code
description: Sent after the user has taken an action that may have altered the text in the edit control portion of a combo box.
ms.assetid: 2c5de5cd-24d3-4198-906e-b520369e0f61
keywords:
- CBN_EDITCHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- CBN_EDITCHANGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# CBN\_EDITCHANGE notification code

Sent after the user has taken an action that may have altered the text in the edit control portion of a combo box. Unlike the [CBN\_EDITUPDATE](cbn-editupdate.md) notification code, this notification code is sent after the system updates the screen. The parent window of the combo box receives this notification code through the [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
CBN_EDITCHANGE

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

If the combo box has the [**CBS\_DROPDOWNLIST**](combo-box-styles.md) style, this notification code is not sent.

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

[CBN\_EDITUPDATE](cbn-editupdate.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659)
</dt> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





