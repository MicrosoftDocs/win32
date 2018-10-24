---
title: CBN_SELENDCANCEL notification code
description: Sent when the user selects an item, but then selects another control or closes the dialog box. It indicates the user's initial selection is to be ignored. The parent window of the combo box receives this notification code through the WM\_COMMAND message.
ms.assetid: ac8d6d9f-4455-42d6-b0f1-5aaa55b8ee42
keywords:
- CBN_SELENDCANCEL notification code Windows Controls
topic_type:
- apiref
api_name:
- CBN_SELENDCANCEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBN\_SELENDCANCEL notification code

Sent when the user selects an item, but then selects another control or closes the dialog box. It indicates the user's initial selection is to be ignored. The parent window of the combo box receives this notification code through the [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
CBN_SELENDCANCEL

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

In a combo box with the [**CBS\_SIMPLE**](combo-box-styles.md) style, the CBN\_SELENDCANCEL notification code is not sent. The [CBN\_SELENDOK](cbn-selendok.md) notification code is sent immediately before every [CBN\_SELCHANGE](cbn-selchange.md) notification code.

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

[CBN\_SELCHANGE](cbn-selchange.md)
</dt> <dt>

[CBN\_SELENDOK](cbn-selendok.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659)
</dt> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





