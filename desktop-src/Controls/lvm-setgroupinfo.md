---
title: LVM\_SETGROUPINFO message
description: Sets group information.
ms.assetid: f79bd235-e2de-4055-be3e-76eb2744e1ee
keywords:
- LVM_SETGROUPINFO message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETGROUPINFO
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LVM\_SETGROUPINFO message

Sets group information.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>ID that specifies the group whose information is to be set.</dd> <dt>

*lParam* 
</dt> <dd>Pointer to an [**LVGROUP**](/windows/desktop/api/Commctrl/ns-commctrl-taglvgroup) structure that contains the information to set.</dd> </dl>

## Return value

Returns the ID of the group if successful, or -1 otherwise.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





