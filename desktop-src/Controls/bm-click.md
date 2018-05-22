---
title: BM\_CLICK message
description: Simulates the user clicking a button. This message causes the button to receive the WM\_LBUTTONDOWN and WM\_LBUTTONUP messages, and the button's parent window to receive a BN\_CLICKED notification code.
ms.assetid: 'f76ca5eb-170c-43fc-a239-67af15497f08'
keywords: ["BM_CLICK message Windows Controls"]
topic_type:
- apiref
api_name:
- BM_CLICK
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# BM\_CLICK message

Simulates the user clicking a button. This message causes the button to receive the [**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607) and [**WM\_LBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms645608) messages, and the button's parent window to receive a [BN\_CLICKED](bn-clicked.md) notification code.

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

If the button is in a dialog box and the dialog box is not active, the **BM\_CLICK** message might fail. To ensure success in this situation, call the [**SetActiveWindow**](https://msdn.microsoft.com/library/windows/desktop/ms646311) function to activate the dialog box before sending the **BM\_CLICK** message to the button.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





