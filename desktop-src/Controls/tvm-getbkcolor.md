---
title: TVM\_GETBKCOLOR message
description: Retrieves the current background color of the control. You can send this message explicitly or by using the TreeView\_GetBkColor macro.
ms.assetid: 1b9eea90-54cd-47b9-befa-ec0128a0230f
keywords:
- TVM_GETBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETBKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TVM\_GETBKCOLOR message

Retrieves the current background color of the control. You can send this message explicitly or by using the [**TreeView\_GetBkColor**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getbkcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a [**COLORREF**](https://msdn.microsoft.com/library/windows/desktop/dd183449) value that represents the current background color. If this value is -1, the control is using the system color for the background color.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_SETBKCOLOR**](tvm-setbkcolor.md)
</dt> </dl>

 

 





