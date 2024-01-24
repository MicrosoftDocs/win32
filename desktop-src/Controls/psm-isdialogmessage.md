---
title: PSM_ISDIALOGMESSAGE message (Prsht.h)
description: Passes a message to a property sheet dialog box and indicates whether the dialog box processed the message. You can send this message explicitly or by using the PropSheet\_IsDialogMessage macro.
ms.assetid: 7629c3f8-0b10-4585-8a95-9309c75b3ebb
keywords:
- PSM_ISDIALOGMESSAGE message Windows Controls
topic_type:
- apiref
api_name:
- PSM_ISDIALOGMESSAGE
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_ISDIALOGMESSAGE message

Passes a message to a property sheet dialog box and indicates whether the dialog box processed the message. You can send this message explicitly or by using the [**PropSheet\_IsDialogMessage**](/windows/desktop/api/Prsht/nf-prsht-propsheet_isdialogmessage) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**MSG**](/windows/win32/api/winuser/ns-winuser-msg) structure that contains the message to be checked.

</dd> </dl>

## Return value

Returns **TRUE** if the message has been processed, or **FALSE** if the message has not been processed.

## Remarks

Your message loop should use the **PSM\_ISDIALOGMESSAGE** message with modeless property sheets to pass messages to the property sheet dialog box. On systems that support Unicode, use the Unicode versions of the [**GetMessage**](/windows/desktop/api/winuser/nf-winuser-getmessage) and [**PeekMessage**](/windows/desktop/api/winuser/nf-winuser-peekmessagea) functions (**GetMessageW** and **PeekMessageW**) to retrieve messages.

If the return value indicates that the message was processed, it must not be passed to the [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) or [**DispatchMessage**](/windows/desktop/api/winuser/nf-winuser-dispatchmessage) function.

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



## See also

<dl> <dt>

[**PropertySheet**](/windows/desktop/api/Prsht/nf-prsht-propertysheeta)
</dt> </dl>

 

