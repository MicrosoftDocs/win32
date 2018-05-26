---
title: LVM\_INSERTGROUPSORTED message
description: Inserts a group into an ordered list of groups.
ms.assetid: 8ad1660b-8b64-4f02-ac1b-b7edeeea38ab
keywords:
- LVM_INSERTGROUPSORTED message Windows Controls
topic_type:
- apiref
api_name:
- LVM_INSERTGROUPSORTED
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

# LVM\_INSERTGROUPSORTED message

Inserts a group into an ordered list of groups.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Pointer to an [**LVINSERTGROUPSORTED**](/windows/win32/Commctrl/ns-commctrl-taglvinsertgroupsorted?branch=master) structure that contains the group to insert.</dd> <dt>

*lParam* 
</dt> <dd>Must be **NULL**.</dd> </dl>

## Return value

The return value is not used.

## Remarks

The ordering of the list is based on the ID of the group. The order is defined by the application-defined ordering function, [**LVGroupCompare**](/windows/win32/Commctrl/?branch=master), that is passed in the [**LVINSERTGROUPSORTED**](/windows/win32/Commctrl/ns-commctrl-taglvinsertgroupsorted?branch=master) structure by the *wParam* parameter.

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**LVGroupCompare**](/windows/win32/Commctrl/?branch=master)
</dt> <dt>

[**LVINSERTGROUPSORTED**](/windows/win32/Commctrl/ns-commctrl-taglvinsertgroupsorted?branch=master)
</dt> </dl>

 

 





