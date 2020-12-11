---
title: PSM_SHOWWIZBUTTONS message (Prsht.h)
description: Shows or hides buttons in a wizard. You can send this message explicitly or by using the PropSheet\_ShowWizButtons macro.
ms.assetid: 669c4e51-cac1-40e1-8f23-afae0e41fc9b
keywords:
- PSM_SHOWWIZBUTTONS message Windows Controls
topic_type:
- apiref
api_name:
- PSM_SHOWWIZBUTTONS
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_SHOWWIZBUTTONS message

Shows or hides buttons in a wizard. You can send this message explicitly or by using the [**PropSheet\_ShowWizButtons**](/windows/desktop/api/Prsht/nf-prsht-propsheet_showwizbuttons) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

One or more of the following values that specify which property sheet buttons are to be shown. If a button value is included in both this parameter and *lParam*, it is shown.



| Value                                                                                                                                                                                 | Meaning                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| <span id="PSWIZB_BACK"></span><span id="pswizb_back"></span><dl> <dt>**PSWIZB\_BACK**</dt> </dl>                               | The **Back** button.<br/>                                                            |
| <span id="PSWIZB_CANCEL"></span><span id="pswizb_cancel"></span><dl> <dt>**PSWIZB\_CANCEL**</dt> </dl>                         | The **Cancel** button.<br/>                                                          |
| <span id="PSWIZB_DISABLEDFINISH"></span><span id="pswizb_disabledfinish"></span><dl> <dt>**PSWIZB\_DISABLEDFINISH**</dt> </dl> | The **Finish** button.<br/>                                                          |
| <span id="PSWIZB_FINISH"></span><span id="pswizb_finish"></span><dl> <dt>**PSWIZB\_FINISH**</dt> </dl>                         | The **Finish** button.<br/>                                                          |
| <span id="PSWIZB_NEXT"></span><span id="pswizb_next"></span><dl> <dt>**PSWIZB\_NEXT**</dt> </dl>                               | The **Next** button.<br/>                                                            |
| <span id="PSWIZB_SHOW"></span><span id="pswizb_show"></span><dl> <dt>**PSWIZB\_SHOW**</dt> </dl>                               | Set only this flag (defined as zero) to hide all buttons specified in *lParam*.<br/> |
| <span id="PSWIZB_RESTORE"></span><span id="pswizb_restore"></span><dl> <dt>**PSWIZB\_RESTORE**</dt> </dl>                      | Not implemented.<br/>                                                                |



 

</dd> <dt>

*lParam* 
</dt> <dd>

One or more of the same values used in *wParam*, specifying which buttons are affected by this call. If a button value appears in this parameter but not in *wParam*, the button is hidden.

</dd> </dl>

## Return value

No return value.

## Remarks

Wizards display either three or four buttons below each page. This message is used to specify which buttons are visible. Wizards normally display **Back**, **Cancel**, and either a **Next** or **Finish** button. The **Cancel** button is always visible.

Typically, set **PSWIZB\_FINISH** or **PSWIZB\_DISABLEDFINISH** to replace the **Next** button with a **Finish** button. To display **Next** and **Finish** buttons simultaneously, set the **PSH\_WIZARDHASFINISH** flag in the **dwFlags** member of the [**PROPSHEETHEADER**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2) structure when you create the wizard. Every page will then display all four buttons: **Back**, **Next**, **Cancel**, and **Finish**.

If you use the [**PropSheet\_ShowWizButtons**](/windows/desktop/api/Prsht/nf-prsht-propsheet_showwizbuttons) macro to send this message, it will be posted. At any other time, you can use [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) to send **PSM\_SHOWWIZBUTTONS**.

If your notification handler uses [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) to send a **PSM\_SHOWWIZBUTTONS** message, do nothing that will affect window focus until after the handler returns. For example, if you call [**MessageBox**](/windows/desktop/api/winuser/nf-winuser-messagebox) immediately after using **PostMessage** to send **PSM\_SHOWWIZBUTTONS**, the message box will receive focus. Since posted messages are not delivered until they reach the head of the message queue, the **PSM\_SHOWWIZBUTTONS** message will not be delivered until after the wizard has lost focus to the message box. As a result, the property sheet will not be able to properly set the focus for the buttons.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

