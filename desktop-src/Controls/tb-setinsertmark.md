---
title: TB\_SETINSERTMARK message
description: Sets the current insertion mark for the toolbar.
ms.assetid: 9a576fca-89cf-4db5-9840-35bfa56af89e
keywords:
- TB_SETINSERTMARK message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETINSERTMARK
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

# TB\_SETINSERTMARK message

Sets the current insertion mark for the toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TBINSERTMARK**](/windows/win32/Commctrl/ns-commctrl-tbinsertmark?branch=master) structure that contains the insertion mark.

</dd> </dl>

## Return value

The return value for this message is not used.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TB\_GETINSERTMARK**](tb-getinsertmark.md)
</dt> </dl>

 

 





