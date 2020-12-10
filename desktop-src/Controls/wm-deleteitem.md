---
title: WM_DELETEITEM message (Winuser.h)
description: Sent to the owner of a list box or combo box when the list box or combo box is destroyed or when items are removed by the LB\_DELETESTRING, LB\_RESETCONTENT, CB\_DELETESTRING, or CB\_RESETCONTENT message.
ms.assetid: c3adf8fb-45f2-44f1-8821-6ffa7d76dc78
keywords:
- WM_DELETEITEM message Windows Controls
topic_type:
- apiref
api_name:
- WM_DELETEITEM
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DELETEITEM message

Sent to the owner of a list box or combo box when the list box or combo box is destroyed or when items are removed by the [**LB\_DELETESTRING**](lb-deletestring.md), [**LB\_RESETCONTENT**](lb-resetcontent.md), [**CB\_DELETESTRING**](cb-deletestring.md), or [**CB\_RESETCONTENT**](cb-resetcontent.md) message. The system sends a **WM\_DELETEITEM** message for each deleted item. The system sends the **WM\_DELETEITEM** message for any deleted list box or combo box item with nonzero item data.


```C++
WM_DELETEITEM

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the identifier of the control that sent the **WM\_DELETEITEM** message.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**DELETEITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-deleteitemstruct) structure that contains information about the item deleted from a list box.

</dd> </dl>

## Return value

An application should return **TRUE** if it processes this message.

## Remarks

Microsoft Windows NT and later: Windows sends a **WM\_DELETEITEM** message only for items deleted from an owner-drawn list box (with the [**LBS\_OWNERDRAWFIXED**](list-box-styles.md) or [**LBS\_OWNERDRAWVARIABLE**](list-box-styles.md) style) or owner-drawn combo box (with the [**CBS\_OWNERDRAWFIXED**](combo-box-styles.md) or [**CBS\_OWNERDRAWVARIABLE**](combo-box-styles.md) style).

Windows 95: Windows sends the **WM\_DELETEITEM** message for any deleted list box or combo box item with nonzero item data.

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

[**CB\_DELETESTRING**](cb-deletestring.md)
</dt> <dt>

[**CB\_RESETCONTENT**](cb-resetcontent.md)
</dt> <dt>

[**DELETEITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-deleteitemstruct)
</dt> <dt>

[**LB\_DELETESTRING**](lb-deletestring.md)
</dt> <dt>

[**LB\_RESETCONTENT**](lb-resetcontent.md)
</dt> </dl>

 

 





