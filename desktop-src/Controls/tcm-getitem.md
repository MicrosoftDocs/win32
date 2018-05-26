---
title: TCM\_GETITEM message
description: Retrieves information about a tab in a tab control. You can send this message explicitly or by using the TabCtrl\_GetItem macro.
ms.assetid: 41774f14-c4e9-4c98-bc25-3522b2125ed5
keywords:
- TCM_GETITEM message Windows Controls
topic_type:
- apiref
api_name:
- TCM_GETITEM
- TCM_GETITEMA
- TCM_GETITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TCM\_GETITEM message

Retrieves information about a tab in a tab control. You can send this message explicitly or by using the [**TabCtrl\_GetItem**](/windows/win32/Commctrl/nf-commctrl-tabctrl_getitem?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the tab.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TCITEM**](/windows/win32/Commctrl/ns-commctrl-tagtcitema?branch=master) structure that specifies the information to retrieve and receives information about the tab. When the message is sent, the **mask** member specifies which attributes to return. If the **mask** member specifies the TCIF\_TEXT value, the **pszText** member must contain the address of the buffer that receives the item text, and the **cchTextMax** member must specify the size of the buffer.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

If the TCIF\_TEXT flag is set in the **mask** member of the [**TCITEM**](/windows/win32/Commctrl/ns-commctrl-tagtcitema?branch=master) structure, the control may change the **pszText** member of the structure to point to the new text instead of filling the buffer with the requested text. The control may set the **pszText** member to **NULL** to indicate that no text is associated with the item.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TCM\_GETITEMW** (Unicode) and **TCM\_GETITEMA** (ANSI)<br/>                   |



 

 





