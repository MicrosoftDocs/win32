---
title: TVM_GETSCROLLTIME message (Commctrl.h)
description: Retrieves the maximum scroll time for the tree-view control. You can send this message explicitly or by using the TreeView\_GetScrollTime macro.
ms.assetid: 992d1906-cda3-4ac7-ba90-c681c551ac2e
keywords:
- TVM_GETSCROLLTIME message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETSCROLLTIME
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETSCROLLTIME message

Retrieves the maximum scroll time for the tree-view control. You can send this message explicitly or by using the [**TreeView\_GetScrollTime**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getscrolltime) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the maximum scroll time, in milliseconds.

## Remarks

The maximum scroll time is the longest amount of time that a scroll operation can take. The scrolling will be adjusted so that the scroll will take place within the maximum scroll time. A scroll operation may take less time than the maximum.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_SETSCROLLTIME**](tvm-setscrolltime.md)
</dt> </dl>

 

 





