---
title: TBN_DELETINGBUTTON message (Commctrl.h)
description: Sent by a toolbar control when a button is about to be deleted. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 08116071-36d6-456b-88f9-62a22cdb7ed9
keywords:
- TBN_DELETINGBUTTON message Windows Controls
topic_type:
- apiref
api_name:
- TBN_DELETINGBUTTON
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBN\_DELETINGBUTTON message

Sent by a toolbar control when a button is about to be deleted. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
 TBN_DELETINGBUTTON 

    lpnmtb = (LPNMTOOLBAR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTOOLBAR**](/windows/win32/api/commctrl/ns-commctrl-nmtoolbara) structure that contains information about the button being deleted. For this notification code, only the **hdr** and **iItem** members of this structure are valid. The **iItem** member of this structure contains the command identifier of the button being deleted.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





