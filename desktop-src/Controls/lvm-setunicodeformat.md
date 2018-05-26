---
title: LVM\_SETUNICODEFORMAT message
description: Sets the UNICODE character format flag for the control.
ms.assetid: e332ae88-821f-4341-a98d-59d8a01a126f
keywords:
- LVM_SETUNICODEFORMAT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETUNICODEFORMAT
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

# LVM\_SETUNICODEFORMAT message

Sets the UNICODE character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control. You can send this message explicitly or use the [**ListView\_SetUnicodeFormat**](/windows/win32/Commctrl/nf-commctrl-listview_setunicodeformat?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Determines the character set that is used by the control. If this value is nonzero, the control will use Unicode characters. If this value is zero, the control will use ANSI characters.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the previous Unicode format flag for the control.

## Remarks

See the remarks for [**CCM\_SETUNICODEFORMAT**](ccm-setunicodeformat.md) for a discussion of this message.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**LVM\_GETUNICODEFORMAT**](lvm-getunicodeformat.md)
</dt> </dl>

 

 





