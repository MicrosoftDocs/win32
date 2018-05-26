---
title: LVM\_GETBKIMAGE message
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LVM\_GETBKIMAGE message

Gets the background image in a list-view control. You can send this message explicitly or by using the [**ListView\_GetBkImage**](/windows/win32/Commctrl/nf-commctrl-listview_getbkimage?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**LVBKIMAGE**](/windows/win32/Commctrl/ns-commctrl-taglvbkimagea?branch=master) structure that will receive the background image information.

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

 

 





