---
title: PSM\_ISDIALOGMESSAGE message
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PSM\_ISDIALOGMESSAGE message

Passes a message to a property sheet dialog box and indicates whether the dialog box processed the message. You can send this message explicitly or by using the [**PropSheet\_IsDialogMessage**](/windows/win32/Prsht/nf-prsht-propsheet_isdialogmessage?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**MSG**](https://msdn.microsoft.com/library/windows/desktop/ms644958) structure that contains the message to be checked.

</dd> </dl>

## Return value

Returns **TRUE** if the message has been processed, or **FALSE** if the message has not been processed.

## Remarks

Your message loop should use the **PSM\_ISDIALOGMESSAGE** message with modeless property sheets to pass messages to the property sheet dialog box. On systems that support Unicode, use the Unicode versions of the [**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) and [**PeekMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644943) functions (**GetMessageW** and **PeekMessageW**) to retrieve messages.

If the return value indicates that the message was processed, it must not be passed to the [**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955) or [**DispatchMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644934) function.

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/win32/Prsht/ns-prsht-_propsheetheadera_v2?branch=master)).

 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



## See also

<dl> <dt>

[**PropertySheet**](/windows/win32/Prsht/nf-prsht-propertysheeta?branch=master)
</dt> </dl>

 

 





