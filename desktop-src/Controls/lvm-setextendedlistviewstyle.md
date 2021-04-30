---
title: LVM_SETEXTENDEDLISTVIEWSTYLE message (Commctrl.h)
description: Sets extended styles in list-view controls. You can send this message explicitly or use the ListView\_SetExtendedListViewStyle or ListView\_SetExtendedListViewStyleEx macro.
ms.assetid: eb3f47ed-484a-49a8-94b0-e50ee081bd69
keywords:
- LVM_SETEXTENDEDLISTVIEWSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETEXTENDEDLISTVIEWSTYLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETEXTENDEDLISTVIEWSTYLE message

Sets extended styles in list-view controls. You can send this message explicitly or use the [**ListView\_SetExtendedListViewStyle**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setextendedlistviewstyle) or [**ListView\_SetExtendedListViewStyleEx**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setextendedlistviewstyleex) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

**DWORD** value that specifies which styles in *lParam* are to be affected. This parameter can be a combination of [**Extended List-View Styles**](extended-list-view-styles.md). Only the extended styles in *wParam* will be changed. All other styles will be maintained as they are. If this parameter is zero, all of the styles in *lParam* will be affected.

</dd> <dt>

*lParam* 
</dt> <dd>

**DWORD** value that specifies the extended list-view control styles to set. This parameter can be a combination of [**Extended List-View Styles**](extended-list-view-styles.md). Styles that are not set, but that are specified in *wParam*, are removed.

</dd> </dl>

## Return value

Returns a **DWORD** value that contains the previous extended list-view control styles.

## Remarks

The *wParam* parameter allows you to modify one or more extended styles without having to retrieve the existing styles first. For example, if you pass [**LVS\_EX\_FULLROWSELECT**](extended-list-view-styles.md) for *wParam* and 0 for *lParam*, the **LVS\_EX\_FULLROWSELECT** style will be cleared but all other styles will remain the same.

For backward compatibility reasons, the [**ListView\_SetExtendedListViewStyle**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setextendedlistviewstyle) macro has not been updated to use *wParam*. To use the *wParam* value, use the [**ListView\_SetExtendedListViewStyleEx**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setextendedlistviewstyleex) macro.

When you use this message to set the [**LVS\_EX\_CHECKBOXES**](extended-list-view-styles.md) style, any previously set state image index will be discarded. All check boxes will be initialized to the unchecked state. The state image index is contained in bits 12 through 15 of the **state** member of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





