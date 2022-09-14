---
title: EM_SETTABSTOPS message (Winuser.h)
description: The EM\_SETTABSTOPS message sets the tab stops in a multiline edit control.
ms.assetid: d6fe2828-4ae9-4652-ace0-2f71e146f777
keywords:
- EM_SETTABSTOPS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETTABSTOPS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETTABSTOPS message

The **EM\_SETTABSTOPS** message sets the tab stops in a multiline edit control. When text is copied to the control, any tab character in the text causes space to be generated up to the next tab stop.

This message is processed only by multiline edit controls. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The number of tab stops contained in the array. If this parameter is zero, the *lParam* parameter is ignored and default tab stops are set at every 32 dialog template units. If this parameter is 1, tab stops are set at every *n* dialog template units, where *n* is the distance pointed to by the *lParam* parameter. If this parameter is greater than 1, *lParam* is a pointer to an array of tab stops.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an array of unsigned integers specifying the tab stops, in dialog template units. If the *wParam* parameter is 1, this parameter is a pointer to an unsigned integer containing the distance between all tab stops, in dialog template units.

</dd> </dl>

## Return value

If all the tabs are set, the return value is **TRUE**.

If all the tabs are not set, the return value is **FALSE**.

## Remarks

The **EM\_SETTABSTOPS** message does not automatically redraw the edit control window. If the application is changing the tab stops for text already in the edit control, it should call the [**InvalidateRect**](/windows/desktop/api/winuser/nf-winuser-invalidaterect) function to redraw the edit control window.

The values specified in the array are in dialog template units, which are the device-independent units used in dialog box templates. To convert measurements from dialog template units to screen units (pixels), use the [**MapDialogRect**](/windows/desktop/api/winuser/nf-winuser-mapdialogrect) function.

**Rich Edit:** Supported in Microsoft Rich Edit 3.0 and later. A rich edit control can have the maximum number of tab stops specified by MAX\_TAB\_STOPS. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Other Resources**
</dt> <dt>

[**InvalidateRect**](/windows/desktop/api/winuser/nf-winuser-invalidaterect)
</dt> <dt>

[**MapDialogRect**](/windows/desktop/api/winuser/nf-winuser-mapdialogrect)
</dt> </dl>

 

