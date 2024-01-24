---
title: LB_SETTABSTOPS message (Winuser.h)
description: Sets the tab-stop positions in a list box.
ms.assetid: b96b974e-b1e6-4361-98bb-4dc21c752690
keywords:
- LB_SETTABSTOPS message Windows Controls
topic_type:
- apiref
api_name:
- LB_SETTABSTOPS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_SETTABSTOPS message

Sets the tab-stop positions in a list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the number of tab stops.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to the first member of an array of integers containing the tab stops. The integers represent the number of quarters of the average character width for the font that is selected into the list box. For example, a tab stop of 4 is placed at 1.0 character units, and a tab stop of 6 is placed at 1.5 average character units. However, if the list box is part of a dialog box, the integers are in dialog template units. The tab stops must be sorted in ascending order; backward tabs are not allowed.

</dd> </dl>

## Return value

If all the specified tabs are set, the return value is **TRUE**; otherwise, it is **FALSE**.

## Remarks

To respond to the **LB\_SETTABSTOPS** message, the list box must have been created with the [**LBS\_USETABSTOPS**](list-box-styles.md) style.

If *wParam* is 0 and *lParam* is **NULL**, the default tab stop is two dialog template units. If *wParam* is 1, the list box will have tab stops separated by the distance specified by *lParam*.

If *lParam* points to more than a single value, a tab stop will be set for each value in *lParam*, up to the number specified by *wParam*.

The values specified by *lParam* are in dialog template units, which are the device-independent units used in dialog box templates. To convert measurements from dialog template units to screen units (pixels), use the [**MapDialogRect**](/windows/desktop/api/winuser/nf-winuser-mapdialogrect) function.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The buffer pointed to by *lParam* must reside in writable memory, even though the message does not modify the array.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**MapDialogRect**](/windows/desktop/api/winuser/nf-winuser-mapdialogrect)
</dt> </dl>

 

