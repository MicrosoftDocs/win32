---
title: PSM_APPLY message (Prsht.h)
description: Simulates the selection of the Apply button, indicating that one or more pages have changed and the changes need to be validated and recorded.
ms.assetid: 2948fb66-ad77-4552-88b6-455418515e4c
keywords:
- PSM_APPLY message Windows Controls
topic_type:
- apiref
api_name:
- PSM_APPLY
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSM\_APPLY message

Simulates the selection of the **Apply** button, indicating that one or more pages have changed and the changes need to be validated and recorded.

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

Returns **TRUE** if all pages successfully applied the changes, or **FALSE** otherwise.

## Remarks

The property sheet sends the [PSN\_KILLACTIVE](psn-killactive.md) notification code to the current page. If the current page returns **FALSE**, the property sheet sends the [PSN\_APPLY](psn-apply.md) notification code to all active pages. You can send the PSM\_APPLY message explicitly or by using the [**PropSheet\_Apply**](/windows/desktop/api/Prsht/nf-prsht-propsheet_apply) macro.

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





