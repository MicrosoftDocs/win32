---
title: CBN\_SELENDOK notification code
description: Sent when the user selects a list item, or selects an item and then closes the list. It indicates that the user's selection is to be processed. The parent window of the combo box receives this notification code through the WM\_COMMAND message.
ms.assetid: ef0ac46f-2db9-40d6-ba82-7e90d71fdd37
keywords:
- CBN_SELENDOK notification code Windows Controls
topic_type:
- apiref
api_name:
- CBN_SELENDOK
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBN\_SELENDOK notification code

Sent when the user selects a list item, or selects an item and then closes the list. It indicates that the user's selection is to be processed. The parent window of the combo box receives this notification code through the [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
CBN_SELENDOK

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

In a combo box with the [**CBS\_SIMPLE**](combo-box-styles.md#cbs-simple) style, the CBN\_SELENDOK notification code is sent immediately before every [CBN\_SELCHANGE](cbn-selchange.md) notification code.

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

[CBN\_SELENDCANCEL](cbn-selendcancel.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659)
</dt> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





