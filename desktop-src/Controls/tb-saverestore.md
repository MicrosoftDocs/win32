---
title: TB_SAVERESTORE message (Commctrl.h)
description: Send this message to initiate saving or restoring a toolbar state.
ms.assetid: 59f51d07-cd08-4d6f-9d19-614064ba6f20
keywords:
- TB_SAVERESTORE message Windows Controls
topic_type:
- apiref
api_name:
- TB_SAVERESTORE
- TB_SAVERESTOREA
- TB_SAVERESTOREW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SAVERESTORE message

Send this message to initiate saving or restoring a toolbar state.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Save or restore flag. If this parameter is **TRUE**, the information is saved. If it is **FALSE**, the information is restored.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TBSAVEPARAMS**](/windows/win32/api/commctrl/ns-commctrl-tbsaveparamsa) structure that specifies the registry key, subkey, and value name for the toolbar state information.

</dd> </dl>

## Return value

No return value.

## Remarks

For version 4.72 and earlier, to use this message to save or restore a toolbar, the parent window of the toolbar control must implement a handler for the [TBN\_GETBUTTONINFO](tbn-getbuttoninfo.md) notification code. The toolbar issues this notification to retrieve information about each button as it is restored.

Version 5.80 includes a new save/restore option. At the beginning of the process, and as each button is saved or restored, your application will receive a [TBN\_SAVE](tbn-save.md) or [TBN\_RESTORE](tbn-restore.md) notification. To use this option, you must implement notification handlers to provide the Shell with the bitmap and state information it needs to successfully save or restore the toolbar state.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TB\_SAVERESTOREW** (Unicode) and **TB\_SAVERESTOREA** (ANSI)<br/>             |



 

 





