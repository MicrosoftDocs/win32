---
title: PSM_PRESSBUTTON message (Prsht.h)
description: Simulates the selection of a property sheet button. You can send this message explicitly or by using the PropSheet\_PressButton macro.
ms.assetid: 82a55a29-d916-47ee-b0a0-f685a3a386d9
keywords:
- PSM_PRESSBUTTON message Windows Controls
topic_type:
- apiref
api_name:
- PSM_PRESSBUTTON
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_PRESSBUTTON message

Simulates the selection of a property sheet button. You can send this message explicitly or by using the [**PropSheet\_PressButton**](/windows/desktop/api/Prsht/nf-prsht-propsheet_pressbutton) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the button to select. This parameter can be one of the following values.



| Value                                                                                                                                                            | Meaning                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PSBTN_APPLYNOW"></span><span id="psbtn_applynow"></span><dl> <dt>**PSBTN\_APPLYNOW**</dt> </dl> | Selects the **Apply** button. This value is not valid when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).<br/> |
| <span id="PSBTN_BACK"></span><span id="psbtn_back"></span><dl> <dt>**PSBTN\_BACK**</dt> </dl>             | Selects the **Back** button.<br/>                                                                                                         |
| <span id="PSBTN_CANCEL"></span><span id="psbtn_cancel"></span><dl> <dt>**PSBTN\_CANCEL**</dt> </dl>       | Selects the **Cancel** button.<br/>                                                                                                       |
| <span id="PSBTN_FINISH"></span><span id="psbtn_finish"></span><dl> <dt>**PSBTN\_FINISH**</dt> </dl>       | Selects the **Finish** button.<br/>                                                                                                       |
| <span id="PSBTN_HELP"></span><span id="psbtn_help"></span><dl> <dt>**PSBTN\_HELP**</dt> </dl>             | Selects the **Help** button. This value is not valid when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).<br/>  |
| <span id="PSBTN_NEXT"></span><span id="psbtn_next"></span><dl> <dt>**PSBTN\_NEXT**</dt> </dl>             | Selects the **Next** button.<br/>                                                                                                         |
| <span id="PSBTN_OK"></span><span id="psbtn_ok"></span><dl> <dt>**PSBTN\_OK**</dt> </dl>                   | Selects the **OK** button. This value is not valid when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).<br/>    |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





