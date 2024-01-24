---
title: CBEM_SETITEM message (Commctrl.h)
description: Sets the attributes for an item in a ComboBoxEx control.
ms.assetid: 752df8ea-fd5e-47fa-b729-d019bdde0904
keywords:
- CBEM_SETITEM message Windows Controls
topic_type:
- apiref
api_name:
- CBEM_SETITEM
- CBEM_SETITEMA
- CBEM_SETITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CBEM\_SETITEM message

Sets the attributes for an item in a ComboBoxEx control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**COMBOBOXEXITEM**](/windows/win32/api/commctrl/ns-commctrl-comboboxexitema) structure that contains the item information to be set. When the message is sent, the **mask** member of the structure must be set to indicate which attributes are valid and the **iItem** member must specify the zero-based index of the item to be modified. Setting the **iItem** member to -1 will modify the item displayed in the edit control.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **CBEM\_SETITEMW** (Unicode) and **CBEM\_SETITEMA** (ANSI)<br/>                 |



 

 





