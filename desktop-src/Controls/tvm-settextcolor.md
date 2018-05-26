---
title: TVM\_SETTEXTCOLOR message
description: Sets the text color of the control. You can send this message explicitly or by using the TreeView\_SetTextColor macro.
ms.assetid: eb57dfd5-3e7b-4cda-a659-be9e03470a44
keywords:
- TVM_SETTEXTCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETTEXTCOLOR
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

# TVM\_SETTEXTCOLOR message

Sets the text color of the control. You can send this message explicitly or by using the [**TreeView\_SetTextColor**](/windows/win32/Commctrl/nf-commctrl-treeview_settextcolor?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

[**COLORREF**](https://msdn.microsoft.com/library/windows/desktop/dd183449) value that contains the new text color. If this argument is -1, the control will revert to using the system color for the text color.

</dd> </dl>

## Return value

Returns a **COLORREF** value that represents the previous text color. If this value is -1, the control was using the system color for the text color.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_GETTEXTCOLOR**](tvm-gettextcolor.md)
</dt> </dl>

 

 





