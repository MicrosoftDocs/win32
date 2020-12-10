---
title: PSM_SETBUTTONTEXT message (Prsht.h)
description: Sets the text on a button in an Aero wizard. You can send this message explicitly or by using the PropSheet\_SetButtonText macro.
ms.assetid: 30b7afd1-5094-430f-9c48-d87832d96050
keywords:
- PSM_SETBUTTONTEXT message Windows Controls
topic_type:
- apiref
api_name:
- PSM_SETBUTTONTEXT
- PSM_SETBUTTONTEXTW
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_SETBUTTONTEXT message

Sets the text on a button in an Aero wizard. You can send this message explicitly or by using the [**PropSheet\_SetButtonText**](/windows/desktop/api/Prsht/nf-prsht-propsheet_setbuttontext) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

One of the following values specifying the button whose text is set.



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

The text to set.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **PSM\_SETBUTTONTEXTW** (Unicode)<br/>                                       |



 

 





