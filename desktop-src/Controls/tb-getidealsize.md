---
title: TB_GETIDEALSIZE message (Commctrl.h)
description: Gets the ideal size of the toolbar.
ms.assetid: d3b5ea4d-fd80-4f07-be4f-89b53a8bdf4d
keywords:
- TB_GETIDEALSIZE message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETIDEALSIZE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETIDEALSIZE message

Gets the ideal size of the toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>A **BOOL** that indicates whether to retrieve the ideal height or width of the toolbar. Use **TRUE** to retrieve the ideal height, **FALSE** to retrieve the ideal width.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**SIZE**](/windows/win32/api/windef/ns-windef-size) structure that receives the height or width at which all buttons would be displayed. If *wParam* is **TRUE**, only the **cy** member (height) is valid. If *wParam* is **FALSE**, only the **cx** member (width) is valid.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

