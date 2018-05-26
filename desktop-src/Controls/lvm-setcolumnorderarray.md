---
title: LVM\_SETCOLUMNORDERARRAY message
description: Sets the left-to-right order of columns in a list-view control. You can send this message explicitly or use the ListView\_SetColumnOrderArray macro.
ms.assetid: 9b491832-42cc-4262-8f6c-23cbc2c889bf
keywords:
- LVM_SETCOLUMNORDERARRAY message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETCOLUMNORDERARRAY
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

# LVM\_SETCOLUMNORDERARRAY message

Sets the left-to-right order of columns in a list-view control. You can send this message explicitly or use the [**ListView\_SetColumnOrderArray**](/windows/win32/Commctrl/nf-commctrl-listview_setcolumnorderarray?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Size, in elements, of the buffer at *lParam*.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an array that specifies the order in which columns should be displayed, from left to right. For example, if the contents of the array are {2,0,1}, the control displays column 2, column 0, and column 1 in that order.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





