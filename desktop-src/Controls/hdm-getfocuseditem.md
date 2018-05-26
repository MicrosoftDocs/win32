---
title: HDM\_GETFOCUSEDITEM message
description: Gets the item in a header control that has the focus. Send this message explicitly or by using the Header\_GetFocusedItem macro.
ms.assetid: 9ad8e497-6f81-4226-b138-d1101f2fd8b3
keywords:
- HDM_GETFOCUSEDITEM message Windows Controls
topic_type:
- apiref
api_name:
- HDM_GETFOCUSEDITEM
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

# HDM\_GETFOCUSEDITEM message

Gets the item in a header control that has the focus. Send this message explicitly or by using the [**Header\_GetFocusedItem**](/windows/win32/Commctrl/nf-commctrl-header_getfocuseditem?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Not used. Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Not used. Must be zero.</dd> </dl>

## Return value

Returns the index of the item in focus.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[About Header Controls](header-controls.md)
</dt> </dl>

 

 





