---
title: HDM_GETITEMDROPDOWNRECT message (Commctrl.h)
description: Gets the bounding rectangle of the split button for a header item with style HDF\_SPLITBUTTON. Send this message explicitly or by using the Header\_GetItemDropDownRect macro.
ms.assetid: d7188dfb-4ffa-4641-b210-2c2ec480ca13
keywords:
- HDM_GETITEMDROPDOWNRECT message Windows Controls
topic_type:
- apiref
api_name:
- HDM_GETITEMDROPDOWNRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDM\_GETITEMDROPDOWNRECT message

Gets the bounding rectangle of the split button for a header item with style **HDF\_SPLITBUTTON**. Send this message explicitly or by using the [**Header\_GetItemDropDownRect**](/windows/desktop/api/Commctrl/nf-commctrl-header_getitemdropdownrect) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

The zero-based index of the header control item for which to retrieve the bounding rectangle.

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>

A pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that receives the bounding rectangle information. The message sender is responsible for allocating this structure. The coordinates returned in the RECT structure are expressed relative to the header control parent.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The header item must have style **HDF\_SPLITBUTTON**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[About Header Controls](header-controls.md)
</dt> </dl>

 

 





