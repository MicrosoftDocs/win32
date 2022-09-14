---
description: Notifies the window when the Text Input Panel is opening.
ms.assetid: 6eadd648-bffb-4227-bdcd-cd733f692734
title: MICROSOFT_TIP_OPENING_MSG message (Peninputpanel.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MICROSOFT\_TIP\_OPENING\_MSG message

Notifies the window when the Text Input Panel is opening.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Currently not used, should be **NULL**.

</dd> <dt>

*lParam* 
</dt> <dd>

Currently not used, should be **NULL**.

</dd> </dl>

## Return value

Applications should call [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) after handling this message. See **DefWindowProc** for information about its return values.

## Remarks

This notification lets you know when the input panel is opening. If you want to perform an action when this happens, handle the message, perform your operation in the handler, and then pass on the message to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca).

> [!Note]  
> This message is also sent when the Text Input Panel is already visible and the user switches from the keyboard to the handwriting skin.

 

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------|
| Client<br/> | Windows Vista<br/>                                                                   |
| Header<br/> | <dl> <dt>Peninputpanel.h</dt> </dl> |



 

