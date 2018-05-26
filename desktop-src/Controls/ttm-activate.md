---
title: TTM\_ACTIVATE message
description: Activates or deactivates a tooltip control.
ms.assetid: f37da001-748c-4c51-bb32-dc49031ff2fb
keywords:
- TTM_ACTIVATE message Windows Controls
topic_type:
- apiref
api_name:
- TTM_ACTIVATE
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

# TTM\_ACTIVATE message

Activates or deactivates a tooltip control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Activation flag. If this parameter is **TRUE**, the tooltip control is activated. If it is **FALSE**, the tooltip control is deactivated.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





