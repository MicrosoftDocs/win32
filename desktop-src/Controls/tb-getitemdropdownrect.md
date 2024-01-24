---
title: TB_GETITEMDROPDOWNRECT message (Commctrl.h)
description: Gets the bounding rectangle of the dropdown window for a toolbar item with style BTNS\_DROPDOWN.
ms.assetid: 4b59c96b-8d75-44c1-b771-c1d62502a2c2
keywords:
- TB_GETITEMDROPDOWNRECT message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETITEMDROPDOWNRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETITEMDROPDOWNRECT message

Gets the bounding rectangle of the dropdown window for a toolbar item with style [**BTNS\_DROPDOWN**](toolbar-control-and-button-styles.md).

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

The zero-based index of the toolbar control item for which to retrieve the bounding rectangle.

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>A pointer to a <a href="/windows/win32/api/windef/ns-windef-rect">**RECT**</a> structure to receive the bounding rectangle information. The message sender is responsible for allocating this structure. The coordinates returned in the **RECT** structure are expressed as client coordinates.</dd> </dl>

## Return value

Always returns nonzero.

## Remarks

The item must have the [**BTNS\_DROPDOWN**](toolbar-control-and-button-styles.md) style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

