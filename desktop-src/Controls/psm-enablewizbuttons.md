---
title: PSM_ENABLEWIZBUTTONS message (Prsht.h)
description: Enables or disables any of the standard buttons in an Aero wizard. You can send this message explicitly or use the PropSheet\_EnableWizButtons macro.
ms.assetid: 9e8ff2dc-c0e7-4754-8be2-2c7b65a524f4
keywords:
- PSM_ENABLEWIZBUTTONS message Windows Controls
topic_type:
- apiref
api_name:
- PSM_ENABLEWIZBUTTONS
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_ENABLEWIZBUTTONS message

Enables or disables any of the standard buttons in an Aero wizard. You can send this message explicitly or use the [**PropSheet\_EnableWizButtons**](/windows/desktop/api/Prsht/nf-prsht-propsheet_enablewizbuttons) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

One or more of the following values that specify which property sheet buttons are to be enabled. If a button value is included in both this parameter and *lParam*, it is enabled.



| Value                                                                                                                                                                                 | Meaning                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| <span id="PSWIZB_BACK"></span><span id="pswizb_back"></span><dl> <dt>**PSWIZB\_BACK**</dt> </dl>                               | The **Back** button.<br/>   |
| <span id="PSWIZB_CANCEL"></span><span id="pswizb_cancel"></span><dl> <dt>**PSWIZB\_CANCEL**</dt> </dl>                         | The **Cancel** button.<br/> |
| <span id="PSWIZB_DISABLEDFINISH"></span><span id="pswizb_disabledfinish"></span><dl> <dt>**PSWIZB\_DISABLEDFINISH**</dt> </dl> | The **Finish** button.<br/> |
| <span id="PSWIZB_FINISH"></span><span id="pswizb_finish"></span><dl> <dt>**PSWIZB\_FINISH**</dt> </dl>                         | The **Finish** button.<br/> |
| <span id="PSWIZB_NEXT"></span><span id="pswizb_next"></span><dl> <dt>**PSWIZB\_NEXT**</dt> </dl>                               | The **Next** button.<br/>   |



 

</dd> <dt>

*lParam* 
</dt> <dd>

One or more of the same values used in *wParam*, specifying which buttons are affected by this call. If a button value appears in this parameter but not in *wParam*, it indicates that the button should be disabled.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





