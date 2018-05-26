---
title: PSM\_GETTABCONTROL message
description: Retrieves the handle to the tab control of a property sheet. You can send this message explicitly or by using the PropSheet\_GetTabControl macro.
ms.assetid: 5ddea541-c8e0-4357-b08e-3b5e64be377f
keywords:
- PSM_GETTABCONTROL message Windows Controls
topic_type:
- apiref
api_name:
- PSM_GETTABCONTROL
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

# PSM\_GETTABCONTROL message

Retrieves the handle to the tab control of a property sheet. You can send this message explicitly or by using the [**PropSheet\_GetTabControl**](/windows/win32/Prsht/nf-prsht-propsheet_gettabcontrol?branch=master) macro.

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

Returns the handle to the tab control.

## Remarks

> [!Note]  
> This message is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/win32/Prsht/ns-prsht-_propsheetheadera_v2?branch=master)).

 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





