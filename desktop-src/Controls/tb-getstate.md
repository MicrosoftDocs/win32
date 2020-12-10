---
title: TB_GETSTATE message (Commctrl.h)
description: Retrieves information about the state of the specified button in a toolbar, such as whether it is enabled, pressed, or checked.
ms.assetid: e8a9e1ff-506f-413b-8f8c-986c25bce736
keywords:
- TB_GETSTATE message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETSTATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETSTATE message

Retrieves information about the state of the specified button in a toolbar, such as whether it is enabled, pressed, or checked.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier of the button for which to retrieve information.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the button state information if successful, or -1 otherwise. The button state information can be a combination of the values listed in [**Toolbar Button States**](toolbar-button-states.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





