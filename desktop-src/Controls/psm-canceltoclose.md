---
title: PSM_CANCELTOCLOSE message (Prsht.h)
description: Sent by an application when it has performed changes since the most recent PSN\_APPLY notification that cannot be canceled. You can send this message explicitly or by using the PropSheet\_CancelToClose macro.
ms.assetid: 0a4b6176-7ddb-469f-8ebf-a31e533a8690
keywords:
- PSM_CANCELTOCLOSE message Windows Controls
topic_type:
- apiref
api_name:
- PSM_CANCELTOCLOSE
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_CANCELTOCLOSE message

Sent by an application when it has performed changes since the most recent [PSN\_APPLY](psn-apply.md) notification that cannot be canceled. You can send this message explicitly or by using the [**PropSheet\_CancelToClose**](/windows/desktop/api/Prsht/nf-prsht-propsheet_canceltoclose) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

No return value.

## Remarks

**PSM\_CANCELTOCLOSE** disables the **Cancel** button and changes the text of the **OK** button to "Close".

Most property sheets wait to perform irreversible changes until a PSN\_APPLY notification is received. However, in some circumstances, a property sheet may make irreversible changes outside the standard PSN\_APPLY/PSN\_RESET sequence. One example is a property sheet that contains an **Edit** button that is used to display a subdialog box for editing a property. When the user clicks **OK** to submit the change, the property sheet page has several options.

-   It can record the changes, but wait until it receives a PSN\_APPLY notification to apply them. This is the preferred approach.
-   It can apply the changes immediately after exiting the subdialog box, but remember the original settings. Those settings can be used to restore the original state if a PSN\_RESET notification is received.
-   It can apply the changes immediately and not attempt to restore the original settings when it receives a [PSN\_RESET](psn-reset.md) notification. This approach is not recommended, but may be necessary if the changes are too far-reaching for the other two options to be practical.

For the third option, applications should send a **PSM\_CANCELTOCLOSE** message to the property sheet. It indicates to the user that the changes made with the subdialog box cannot be reversed by clicking the **Cancel** button.

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





