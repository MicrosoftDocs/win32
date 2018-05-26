---
title: TCM\_GETCURSEL message
description: Determines the currently selected tab in a tab control. You can send this message explicitly or by using the TabCtrl\_GetCurSel macro.
ms.assetid: 1caa7fad-da5a-4b26-8e78-12110c126691
keywords:
- TCM_GETCURSEL message Windows Controls
topic_type:
- apiref
api_name:
- TCM_GETCURSEL
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

# TCM\_GETCURSEL message

Determines the currently selected tab in a tab control. You can send this message explicitly or by using the [**TabCtrl\_GetCurSel**](/windows/win32/Commctrl/nf-commctrl-tabctrl_getcursel?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the index of the selected tab if successful, or -1 if no tab is selected.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





