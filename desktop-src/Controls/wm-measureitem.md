---
title: WM\_MEASUREITEM message
description: Sent to the owner window of a combo box, list box, list-view control, or menu item when the control or menu is created.
ms.assetid: '6947bcd1-fd40-4238-b8f2-d4e06b90c0dc'
keywords: ["WM_MEASUREITEM message Windows Controls"]
topic_type:
- apiref
api_name:
- WM_MEASUREITEM
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# WM\_MEASUREITEM message

Sent to the owner window of a combo box, list box, list-view control, or menu item when the control or menu is created.

A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
WM_MEASUREITEM

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Contains the value of the **CtlID** member of the [**MEASUREITEMSTRUCT**](measureitemstruct.md) structure pointed to by the *lParam* parameter. This value identifies the control that sent the **WM\_MEASUREITEM** message. If the value is zero, the message was sent by a menu. If the value is nonzero, the message was sent by a combo box or by a list box. If the value is nonzero, and the value of the **itemID** member of the **MEASUREITEMSTRUCT** pointed to by *lParam* is (UINT) –1, the message was sent by a combo edit field.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**MEASUREITEMSTRUCT**](measureitemstruct.md) structure that contains the dimensions of the owner-drawn control or menu item.

</dd> </dl>

## Return value

If an application processes this message, it should return **TRUE**.

## Remarks

When the owner window receives the **WM\_MEASUREITEM** message, the owner fills in the [**MEASUREITEMSTRUCT**](measureitemstruct.md) structure pointed to by the *lParam* parameter of the message and returns; this informs the system of the dimensions of the control. If a list box or combo box is created with the [**LBS\_OWNERDRAWVARIABLE**](list-box-styles.md#lbs-ownerdrawvariable) or [**CBS\_OWNERDRAWVARIABLE**](combo-box-styles.md#cbs-ownerdrawvariable) style, this message is sent to the owner for each item in the control; otherwise, this message is sent once.

The system sends the **WM\_MEASUREITEM** message to the owner window of combo boxes and list boxes created with the OWNERDRAWFIXED style before sending the [**WM\_INITDIALOG**](https://msdn.microsoft.com/library/windows/desktop/ms645428) message. As a result, when the owner receives this message, the system has not yet determined the height and width of the font used in the control; function calls and calculations requiring these values should occur in the main function of the application or library.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**MEASUREITEMSTRUCT**](measureitemstruct.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_INITDIALOG**](https://msdn.microsoft.com/library/windows/desktop/ms645428)
</dt> </dl>

 

 





