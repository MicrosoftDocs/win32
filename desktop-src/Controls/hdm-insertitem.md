---
title: HDM\_INSERTITEM message
description: Inserts a new item into a header control. You can send this message explicitly or use the Header\_InsertItem macro.
ms.assetid: aececf32-090d-4cd4-a239-4435a322f72e
keywords:
- HDM_INSERTITEM message Windows Controls
topic_type:
- apiref
api_name:
- HDM_INSERTITEM
- HDM_INSERTITEMA
- HDM_INSERTITEMW
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

# HDM\_INSERTITEM message

Inserts a new item into a header control. You can send this message explicitly or use the [**Header\_InsertItem**](/windows/win32/Commctrl/nf-commctrl-header_insertitem?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The index of the item after which the new item is to be inserted. The new item is inserted at the end of the header control if *wParam* is greater than or equal to the number of items in the control. If *wParam* is zero, the new item is inserted at the beginning of the header control.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**HDITEM**](/windows/win32/Commctrl/ns-commctrl-_hd_itema?branch=master) structure that contains information about the new item.

</dd> </dl>

## Return value

Returns the index of the new item if successful, or -1 otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDM\_INSERTITEMW** (Unicode) and **HDM\_INSERTITEMA** (ANSI)<br/>             |



 

 





