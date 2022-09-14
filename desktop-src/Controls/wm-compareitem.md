---
title: WM_COMPAREITEM message (Winuser.h)
description: Sent to determine the relative position of a new item in the sorted list of an owner-drawn combo box or list box.
ms.assetid: 22882730-9fd6-4b45-a563-d7b00ed26564
keywords:
- WM_COMPAREITEM message Windows Controls
topic_type:
- apiref
api_name:
- WM_COMPAREITEM
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_COMPAREITEM message

Sent to determine the relative position of a new item in the sorted list of an owner-drawn combo box or list box. Whenever the application adds a new item, the system sends this message to the owner of a combo box or list box created with the [**CBS\_SORT**](combo-box-styles.md) or [**LBS\_SORT**](list-box-styles.md) style.


```C++
WM_COMPAREITEM

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the identifier of the control that sent the **WM\_COMPAREITEM** message.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**COMPAREITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-compareitemstruct) structure that contains the identifiers and application-supplied data for two items in the combo or list box.

</dd> </dl>

## Return value

The return value indicates the relative position of the two items. It may be any of the values shown in the following table.



| Return code                                                                          | Description                                                  |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**Value**</dt> </dl> | Meaning<br/>                                           |
| <dl> <dt>**-1**</dt> </dl>    | Item 1 precedes item 2 in the sorted order.<br/>       |
| <dl> <dt>**0**</dt> </dl>     | Items 1 and 2 are equivalent in the sorted order.<br/> |
| <dl> <dt>**1**</dt> </dl>     | Item 1 follows item 2 in the sorted order.<br/>        |



 

## Remarks

When the owner of an owner-drawn combo box or list box receives this message, the owner returns a value indicating which of the items specified by the [**COMPAREITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-compareitemstruct) structure will appear before the other. Typically, the system sends this message several times until it determines the exact position for the new item.

If a dialog box procedure handles this message, it should cast the desired return value to a **BOOL** and return the value directly. The DWL\_MSGRESULT value set by the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function is ignored.

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

[**COMPAREITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-compareitemstruct)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga)
</dt> </dl>

 

