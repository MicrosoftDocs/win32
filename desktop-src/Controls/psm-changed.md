---
title: PSM\_CHANGED message
description: Informs a property sheet that information in a page has changed. You can send this message explicitly or by using the PropSheet\_Changed macro.
ms.assetid: b092969f-31dc-4e3c-9100-d15f1bdd5aa5
keywords:
- PSM_CHANGED message Windows Controls
topic_type:
- apiref
api_name:
- PSM_CHANGED
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

# PSM\_CHANGED message

Informs a property sheet that information in a page has changed. You can send this message explicitly or by using the [**PropSheet\_Changed**](/windows/win32/Prsht/nf-prsht-propsheet_changed?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to the page that has changed.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

No return value.

## Remarks

The property sheet will enable the **Apply** button.

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/win32/Prsht/ns-prsht-_propsheetheadera_v2?branch=master)).

 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





