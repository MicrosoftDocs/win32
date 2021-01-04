---
title: CBEM_GETITEM message (Commctrl.h)
description: Gets item information for a given ComboBoxEx item.
ms.assetid: 2df07ae8-fa84-487c-a4a7-90244dfdb40e
keywords:
- CBEM_GETITEM message Windows Controls
topic_type:
- apiref
api_name:
- CBEM_GETITEM
- CBEM_GETITEMA
- CBEM_GETITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CBEM\_GETITEM message

Gets item information for a given ComboBoxEx item.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**COMBOBOXEXITEM**](/windows/win32/api/commctrl/ns-commctrl-comboboxexitema) structure that receives the item information.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

When the message is sent, the **iItem** and **mask** members of the structure must be set to indicate the index of the target item and the type of information to be retrieved. Other members are set as needed. For example, to retrieve text, you must set the CBEIF\_TEXT flag in **mask**, and assign a value to **cchTextMax**. Setting the **iItem** member to -1 will retrieve the item displayed in the edit control.

If the CBEIF\_TEXT flag is set in the **mask** member of the [**COMBOBOXEXITEM**](/windows/win32/api/commctrl/ns-commctrl-comboboxexitema) structure, the control may change the **pszText** member of the structure to point to the new text instead of filling the buffer with the requested text. Applications should not assume that the text will always be placed in the requested buffer.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **CBEM\_GETITEMW** (Unicode) and **CBEM\_GETITEMA** (ANSI)<br/>                 |



 

 





