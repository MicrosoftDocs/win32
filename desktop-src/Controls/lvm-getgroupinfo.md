---
title: LVM_GETGROUPINFO message (Commctrl.h)
description: Gets group information.
ms.assetid: 72d84e0b-121e-473b-a34d-874234c598b6
keywords:
- LVM_GETGROUPINFO message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETGROUPINFO
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETGROUPINFO message

Gets group information.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>An ID that specifies the group whose information is retrieved.</dd> <dt>

*lParam* 
</dt> <dd>A pointer an <a href="/windows/win32/api/commctrl/ns-commctrl-lvgroup"><b>LVGROUP</b></a> structure that receives the retrieved information. Set the <b>cbSize</b> member of this structure to sizeof(LVGROUP). </dd> </dl>

## Return value

Returns the ID of the group if successful, or -1 otherwise.

## Remarks

Before attempting to retrieve the header for a group, first ensure that the group does not have the LBGS\_NOHEADER style.

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





