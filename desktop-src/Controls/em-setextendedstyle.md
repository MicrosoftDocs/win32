---
title: EM_SETEXTENDEDSTYLE message (Commctrl.h)
description: Informs the edit control to set extended styles. Send this message or use the macro Edit\_SetExtendedStyle.
ms.assetid: 4ca010c3-2c70-41e5-ade4-11e1895fda26
keywords:
- EM_SETEXTENDEDSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETEXTENDEDSTYLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 10/19/2018
---

# EM\_SETEXTENDEDSTYLE message

Informs the edit control to set extended styles. Send this message or use the macro [**Edit\_SetExtendedStyle**](/windows/desktop/api/Commctrl/nf-commctrl-edit_setextendedstyle).

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Mask used to select the styles to be set.

</dd> <dt>

*lParam* 
</dt> <dd>

Value that indicates the extended style. For more information on styles, see [Edit Control Extended Styles](edit-control-window-extended-styles.md).

</dd> </dl>

## Return value

If this message succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The extended styles for an edit control have nothing to do with the extended styles used with function [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) or function [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

