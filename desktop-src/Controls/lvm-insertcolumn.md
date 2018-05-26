---
title: LVM\_INSERTCOLUMN message
description: Inserts a new column in a list-view control. You can send this message explicitly or by using the ListView\_InsertColumn macro.
ms.assetid: 1326e38e-bb45-4d0d-b5bc-ec684b3b92ef
keywords:
- LVM_INSERTCOLUMN message Windows Controls
topic_type:
- apiref
api_name:
- LVM_INSERTCOLUMN
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

# LVM\_INSERTCOLUMN message

Inserts a new column in a list-view control. You can send this message explicitly or by using the [**ListView\_InsertColumn**](/windows/win32/Commctrl/nf-commctrl-listview_insertcolumn?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the new column.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVCOLUMN**](/windows/win32/Commctrl/ns-commctrl-taglvcolumna?branch=master) structure that contains the attributes of the new column.

</dd> </dl>

## Return value

Returns the index of the new column if successful, or -1 otherwise.

## Remarks

Columns are visible only in report (details) view.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





