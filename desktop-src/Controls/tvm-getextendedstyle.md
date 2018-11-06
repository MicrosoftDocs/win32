---
title: TVM_GETEXTENDEDSTYLE message
description: Retrieves the extended style for a tree-view control. Send this message explicitly or by using the TreeView\_GetExtendedStyle macro.
ms.assetid: adc74cc5-e741-4966-bf49-a4b0c67e645a
keywords:
- TVM_GETEXTENDEDSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETEXTENDEDSTYLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# TVM\_GETEXTENDEDSTYLE message

Retrieves the extended style for a tree-view control. Send this message explicitly or by using the [**TreeView\_GetExtendedStyle**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getextendedstyle) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the value of extended style.For more information on styles, see [Tree-View Control Extended Styles](tree-view-control-window-extended-styles.md).

## Remarks

The extended styles for a tree-view control have nothing to do with the extended styles used with function [**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680) or function [**SetWindowLong**](https://msdn.microsoft.com/library/windows/desktop/ms633591).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





