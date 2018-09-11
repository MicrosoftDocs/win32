---
title: LVM_GETBKIMAGE message
description: Gets the background image in a list-view control. You can send this message explicitly or by using the ListView\_GetBkImage macro.
ms.assetid: db0e8f31-746a-4a16-b689-68da696e3657
keywords:
- LVM_GETBKIMAGE message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETBKIMAGE
- LVM_GETBKIMAGEA
- LVM_GETBKIMAGEW
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

# LVM\_GETBKIMAGE message

Gets the background image in a list-view control. You can send this message explicitly or by using the [**ListView\_GetBkImage**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getbkimage) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**LVBKIMAGE**](/windows/desktop/api/Commctrl/ns-commctrl-taglvbkimagea) structure that will receive the background image information.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_GETBKIMAGEW** (Unicode) and **LVM\_GETBKIMAGEA** (ANSI)<br/>             |



## See also

<dl> <dt>

[**LVM\_SETBKIMAGE**](lvm-setbkimage.md)
</dt> </dl>

 

 





