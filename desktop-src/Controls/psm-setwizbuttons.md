---
title: PSM_SETWIZBUTTONS message (Prsht.h)
description: Enables or disables the Back, Next, and Finish buttons in a wizard. You can also use the PropSheet\_SetWizButtons macro to post the message.
ms.assetid: e32abdb0-12d1-471e-a309-662389e0dba4
keywords:
- PSM_SETWIZBUTTONS message Windows Controls
topic_type:
- apiref
api_name:
- PSM_SETWIZBUTTONS
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_SETWIZBUTTONS message

Enables or disables the **Back**, **Next**, and **Finish** buttons in a wizard. You can also use the [**PropSheet\_SetWizButtons**](/windows/desktop/api/Prsht/nf-prsht-propsheet_setwizbuttons) macro to post the message.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Set this parameter to PSWIZBF\_ELEVATIONREQUIRED to display the elevated icon on the buttons specified in *lParam*. The elevated icon (or UAC shield icon) indicates that the elevation prompt will be used to prompt the user for approval or credentials. For more information, see [Designing UAC Applications for Windows Vista]( /previous-versions/bb756973(v=msdn.10)).

> [!Note]  
> Displaying the UAC shield icon is only supported in AeroWizards (PSH\_AEROWIZARD).

 

</dd> <dt>

*lParam* 
</dt> <dd>

Value that specifies which property sheet buttons are enabled. You can combine one or more of the following flags.



| Value                                                                                                                                                                                 | Meaning                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <span id="PSWIZB_BACK"></span><span id="pswizb_back"></span><dl> <dt>**PSWIZB\_BACK**</dt> </dl>                               | Enables the **Back** button. If this flag is not set, the **Back** button is displayed as disabled.<br/> |
| <span id="PSWIZB_DISABLEDFINISH"></span><span id="pswizb_disabledfinish"></span><dl> <dt>**PSWIZB\_DISABLEDFINISH**</dt> </dl> | Displays a disabled **Finish** button.<br/>                                                              |
| <span id="PSWIZB_FINISH"></span><span id="pswizb_finish"></span><dl> <dt>**PSWIZB\_FINISH**</dt> </dl>                         | Displays an enabled **Finish** button.<br/>                                                              |
| <span id="PSWIZB_NEXT"></span><span id="pswizb_next"></span><dl> <dt>**PSWIZB\_NEXT**</dt> </dl>                               | Enables the **Next** button. If this flag is not set, the **Next** button is displayed as disabled.<br/> |



 

</dd> </dl>

## Return value

No return value.

## Remarks

If your notification handler uses [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) to send a **PSM\_SETWIZBUTTONS** message, do nothing that will affect window focus until after the handler returns. For example, if you call [**MessageBox**](/windows/desktop/api/winuser/nf-winuser-messagebox) immediately after using **PostMessage** to send **PSM\_SETWIZBUTTONS**, the message box will receive focus. Since posted messages are not delivered until they reach the head of the message queue, the **PSM\_SETWIZBUTTONS** message will not be delivered until after the wizard has lost focus to the message box. As a result, the property sheet will not be able to properly set the focus for the buttons.

If you send the PSM\_SETWIZBUTTONS message during your handling of the [PSN\_SETACTIVE](psn-setactive.md) notification, use the [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) function rather than the [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) function. Otherwise, the system will not update the buttons properly. If you use the [**PropSheet\_SetWizButtons**](/windows/desktop/api/Prsht/nf-prsht-propsheet_setwizbuttons) macro to send this message, it will be posted. At any other time, you can use **SendMessage** to send **PSM\_SETWIZBUTTONS**.

Wizards display either three or four buttons below each page. This message is used to specify which buttons are enabled. Wizards normally display **Back**, **Cancel**, and either a **Next** or **Finish** button. You typically enable only the **Next** button for the welcome page, **Next** and **Back** for interior pages, and **Back** and **Finish** for the completion page. The **Cancel** button is always enabled. Normally, setting PSWIZB\_FINISH or PSWIZB\_DISABLEDFINISH replaces the **Next** button with a **Finish** button. To display **Next** and **Finish** buttons simultaneously, set the PSH\_WIZARDHASFINISH flag in the **dwFlags** member of the wizard's [**PROPSHEETHEADER**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2) structure when you create the wizard. Every page will then display all four buttons.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

