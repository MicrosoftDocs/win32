---
title: LVM\_GETTILEVIEWINFO message
description: Retrieves information about a list-view control in tile view.
ms.assetid: 114990c0-a150-49d8-80e7-b084c648ac34
keywords:
- LVM_GETTILEVIEWINFO message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETTILEVIEWINFO
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

# LVM\_GETTILEVIEWINFO message

Retrieves information about a list-view control in tile view.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Pointer to an [**LVTILEVIEWINFO**](/windows/win32/Commctrl/ns-commctrl-taglvtileviewinfo?branch=master) structure that receives the retrieved information.</dd> </dl>

## Return value

Return value not used.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





