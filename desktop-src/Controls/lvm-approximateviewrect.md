---
title: LVM_APPROXIMATEVIEWRECT message (Commctrl.h)
description: Calculates the approximate width and height required to display a given number of items. You can send this message explicitly or use the ListView\_ApproximateViewRect macro.
ms.assetid: a14331a8-217d-48c6-9489-fb90c4d31b91
keywords:
- LVM_APPROXIMATEVIEWRECT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_APPROXIMATEVIEWRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_APPROXIMATEVIEWRECT message

Calculates the approximate width and height required to display a given number of items. You can send this message explicitly or use the [**ListView\_ApproximateViewRect**](/windows/desktop/api/Commctrl/nf-commctrl-listview_approximateviewrect) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The number of items to be displayed in the control. If this parameter is set to -1, the message uses the total number of items in the control.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is the proposed x-dimension of the control, in pixels. This parameter can be set to -1 to allow the message to use the current width value.

The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) is the proposed y-dimension of the control, in pixels. This parameter can be set to -1 to allow the message to use the current height value.

</dd> </dl>

## Return value

Returns a **DWORD** value that holds the approximate width (in the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))) and height (in the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))) needed to display the items, in pixels.

## Remarks

Setting the size of the list-view control based on the dimensions provided by this message can optimize redraw and reduce flicker.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

