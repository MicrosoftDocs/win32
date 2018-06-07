---
title: LVM\_SETBKIMAGE message
description: Sets the background image in a list-view control. You can send this message explicitly or by using the ListView\_SetBkImage macro.
ms.assetid: 8fdd363c-ac12-498b-80b7-aaa5741cfd76
keywords:
- LVM_SETBKIMAGE message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETBKIMAGE
- LVM_SETBKIMAGEA
- LVM_SETBKIMAGEW
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

# LVM\_SETBKIMAGE message

Sets the background image in a list-view control. You can send this message explicitly or by using the [**ListView\_SetBkImage**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setbkimage) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**LVBKIMAGE**](/windows/desktop/api/Commctrl/ns-commctrl-taglvbkimagea) structure that contains the new background image information.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise. Returns zero if the **ulFlags** member of the [**LVBKIMAGE**](/windows/desktop/api/Commctrl/ns-commctrl-taglvbkimagea) structure is **LVBKIF\_SOURCE\_NONE**.

## Remarks

Because the list-view control uses OLE COM to manipulate the background images, the calling application must call [**CoInitialize**](https://msdn.microsoft.com/library/windows/desktop/ms678543) or [**OleInitialize**](https://msdn.microsoft.com/library/windows/desktop/ms690134) before sending this message. It is best to call one of these functions when the application is initialized and call either [**CoUninitialize**](https://msdn.microsoft.com/library/windows/desktop/ms688715) or [**OleUninitialize**](https://msdn.microsoft.com/library/windows/desktop/ms691326) when the application is terminating.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_SETBKIMAGEW** (Unicode) and **LVM\_SETBKIMAGEA** (ANSI)<br/>             |



## See also

<dl> <dt>

[**LVM\_GETBKIMAGE**](lvm-getbkimage.md)
</dt> </dl>

 

 





