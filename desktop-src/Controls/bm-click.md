---
title: BM_CLICK message (Winuser.h)
description: Simulates the user clicking a button. This message causes the button to receive the WM\_LBUTTONDOWN and WM\_LBUTTONUP messages, and the button's parent window to receive a BN\_CLICKED notification code.
ms.assetid: f76ca5eb-170c-43fc-a239-67af15497f08
keywords:
- BM_CLICK message Windows Controls
topic_type:
- apiref
api_name:
- BM_CLICK
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BM\_CLICK message

Simulates the user clicking a button. This message causes the button to receive the [**WM\_LBUTTONDOWN**](/windows/desktop/inputdev/wm-lbuttondown) and [**WM\_LBUTTONUP**](/windows/desktop/inputdev/wm-lbuttonup) messages, and the button's parent window to receive a [BN\_CLICKED](bn-clicked.md) notification code.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

If the button is in a dialog box and the dialog box is not active, the **BM\_CLICK** message might fail. To ensure success in this situation, call the [**SetActiveWindow**](/windows/desktop/api/winuser/nf-winuser-setactivewindow) function to activate the dialog box before sending the **BM\_CLICK** message to the button.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

