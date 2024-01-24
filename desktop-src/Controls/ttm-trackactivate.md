---
title: TTM_TRACKACTIVATE message (Commctrl.h)
description: Activates or deactivates a tracking tooltip.
ms.assetid: 6cf43377-a772-4749-81c4-a685998092e5
keywords:
- TTM_TRACKACTIVATE message Windows Controls
topic_type:
- apiref
api_name:
- TTM_TRACKACTIVATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_TRACKACTIVATE message

Activates or deactivates a tracking tooltip.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value specifying whether tracking is being activated or deactivated. This value can be one of the following:



| Value                                                                                                                                | Meaning                         |
|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Activate tracking.<br/>   |
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Deactivate tracking.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure that identifies the tool to which this message applies. The **hwnd** and **uId** members identify the tool, and the **cbSize** member specifies the size of the structure. All other members are ignored.

</dd> </dl>

## Return value

The return value for this message is not used.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TTM\_TRACKPOSITION**](ttm-trackposition.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Using Tooltip Controls](using-tooltip-contro.md)
</dt> </dl>

 

 





