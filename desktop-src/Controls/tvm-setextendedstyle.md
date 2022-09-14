---
title: TVM_SETEXTENDEDSTYLE message (Commctrl.h)
description: Informs the tree-view control to set extended styles. Send this message or use the macro TreeView\_SetExtendedStyle.
ms.assetid: 35cb6ac8-1c1e-4ecd-88b2-878d3f6ccaa5
keywords:
- TVM_SETEXTENDEDSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETEXTENDEDSTYLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETEXTENDEDSTYLE message

Informs the tree-view control to set extended styles. Send this message or use the macro [**TreeView\_SetExtendedStyle**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setextendedstyle).

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Mask used to select the styles to be set.

</dd> <dt>

*lParam* 
</dt> <dd>

Value that indicates the extended style. For more information on styles, see [Tree-View Control Extended Styles](tree-view-control-window-extended-styles.md).

</dd> </dl>

## Return value

If this message succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The extended styles for a tree-view control have nothing to do with the extended styles used with function [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) or function [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

