---
title: TB\_INSERTBUTTON message
description: Inserts a button in a toolbar.
ms.assetid: 6be27817-5d86-4649-bd63-173845197763
keywords:
- TB_INSERTBUTTON message Windows Controls
topic_type:
- apiref
api_name:
- TB_INSERTBUTTON
- TB_INSERTBUTTONA
- TB_INSERTBUTTONW
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

# TB\_INSERTBUTTON message

Inserts a button in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of a button. The message inserts the new button to the left of this button.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TBBUTTON**](/windows/win32/Commctrl/ns-commctrl-_tbbutton?branch=master) structure containing information about the button to insert.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TB\_INSERTBUTTONW** (Unicode) and **TB\_INSERTBUTTONA** (ANSI)<br/>           |



 

 





