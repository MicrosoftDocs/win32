---
title: TB\_HIDEBUTTON message
description: Hides or shows the specified button in a toolbar.
ms.assetid: 57941a40-279a-426e-baf9-115429c62839
keywords:
- TB_HIDEBUTTON message Windows Controls
topic_type:
- apiref
api_name:
- TB_HIDEBUTTON
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

# TB\_HIDEBUTTON message

Hides or shows the specified button in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier of the button to hide or show.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) is a **BOOL** that indicates whether to hide or show the specified button. If **TRUE**, the button is hidden. If **FALSE**, the button is shown.

The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) must be zero.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





