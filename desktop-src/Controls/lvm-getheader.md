---
title: LVM\_GETHEADER message
description: Gets the handle to the header control used by the list-view control. You can send this message explicitly or use the ListView\_GetHeader macro.
ms.assetid: 4708b493-4449-4844-bf0d-e6969bcf0246
keywords:
- LVM_GETHEADER message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETHEADER
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

# LVM\_GETHEADER message

Gets the handle to the header control used by the list-view control. You can send this message explicitly or use the [**ListView\_GetHeader**](/windows/win32/Commctrl/nf-commctrl-listview_getheader?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the header control.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





