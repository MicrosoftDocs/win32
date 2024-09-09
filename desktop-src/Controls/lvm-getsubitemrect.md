---
title: LVM_GETSUBITEMRECT message (Commctrl.h)
description: Retrieves information about the bounding rectangle for a subitem in a list-view control.
ms.assetid: 985876b2-6eb3-4c96-88ea-ddec67ef5b5a
keywords:
- LVM_GETSUBITEMRECT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETSUBITEMRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETSUBITEMRECT message

Retrieves information about the bounding rectangle for a subitem in a list-view control. You can send this message explicitly or by using the [**ListView\_GetSubItemRect**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getsubitemrect) macro (recommended). This message is intended to be used only with list-view controls that use the [**LVS\_REPORT**](list-view-window-styles.md) style.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the subitem's parent item.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that will receive the subitem bounding rectangle information. Its members must be initialized according to the following member/value relationships:



| Value                                                                                                                             | Meaning                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| <span id="top"></span><span id="TOP"></span><dl> <dt>**top**</dt> </dl>    | The one-based index of the subitem.<br/>                                                                                    |
| <span id="left"></span><span id="LEFT"></span><dl> <dt>**left**</dt> </dl> | Flag value (see remarks). Indicates the portion of the list-view subitem for which to retrieve the bounding rectangle.<br/> |



 

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

Following are the flag values that may be set.



| Requirement | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------|
| **Flag Value** | **Meaning**                                                                                                         |
| LVIR\_BOUNDS   | Returns the bounding rectangle of the entire item, including the icon and label.                                    |
| LVIR\_ICON     | Returns the bounding rectangle of the icon or small icon.                                                           |
| LVIR\_LABEL    | Returns the bounding rectangle of the entire item, including the icon and label. This is identical to LVIR\_BOUNDS. |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

