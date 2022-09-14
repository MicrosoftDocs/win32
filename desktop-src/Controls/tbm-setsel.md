---
title: TBM_SETSEL message (Commctrl.h)
description: Sets the starting and ending positions for the available selection range in a trackbar.
ms.assetid: 71f5b9f8-4850-44a8-8acf-adca9bda84c3
keywords:
- TBM_SETSEL message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETSEL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETSEL message

Sets the starting and ending positions for the available selection range in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Redraw flag. If this parameter is **TRUE**, the message redraws the trackbar after the selection range is set. If this parameter is **FALSE**, the message sets the selection range but does not redraw the trackbar.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the starting logical position for the selection range, and the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the ending logical position.

</dd> </dl>

## Return value

No return value.

## Remarks

This message is ignored if the trackbar does not have the [**TBS\_ENABLESELRANGE**](trackbar-control-styles.md) style.

**TBM\_SETSEL** allows you to restrict the pointer to only a portion of the range available to the progress bar.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TBM\_GETSELEND**](tbm-getselend.md)
</dt> <dt>

[**TBM\_GETSELSTART**](tbm-getselstart.md)
</dt> <dt>

[**TBM\_SETSELEND**](tbm-setselend.md)
</dt> <dt>

[**TBM\_SETSELSTART**](tbm-setselstart.md)
</dt> </dl>

 

