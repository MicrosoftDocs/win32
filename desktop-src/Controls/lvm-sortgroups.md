---
title: LVM_SORTGROUPS message (Commctrl.h)
description: Uses an application-defined comparison function to sort groups by ID within a list-view control.
ms.assetid: 553e96d6-a982-4482-8fba-ef11a74fb82e
keywords:
- LVM_SORTGROUPS message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SORTGROUPS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SORTGROUPS message

Uses an application-defined comparison function to sort groups by ID within a list-view control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Pointer to an application-defined comparison function, <a href="/windows/desktop/api/commctrl/nc-commctrl-pfnlvgroupcompare">LVGroupCompare</a>.</dd> <dt>

*lParam* 
</dt> <dd>Void pointer to the application-defined information.</dd> </dl>

## Return value

Returns 1 if successful, or 0 otherwise.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**LVGroupCompare**](/windows/win32/api/commctrl/nc-commctrl-pfnlvgroupcompare)
</dt> </dl>

