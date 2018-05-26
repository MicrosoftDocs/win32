---
title: PSN\_HELP notification code
description: Notifies a page that the user has clicked the Help button. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 4ad2c608-8caa-44c6-845d-4c0c1bd80763
keywords:
- PSN_HELP notification code Windows Controls
topic_type:
- apiref
api_name:
- PSN_HELP
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PSN\_HELP notification code

Notifies a page that the user has clicked the Help button. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
PSN_HELP 

    lppsn = (LPPSHNOTIFY) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**PSHNOTIFY**](/windows/win32/Prsht/ns-prsht-_pshnotify?branch=master) structure that contains information about the notification code. This structure contains an [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure as its first member, **hdr**. The **hwndFrom** member of this **NMHDR** structure contains the handle to the property sheet. The **lParam** member of the **PSHNOTIFY** structure does not contain any information.

</dd> </dl>

## Return value

No return value.

## Remarks

An application should display Help information for the page.

> [!Note]  
> This notification code is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/win32/Prsht/ns-prsht-_propsheetheadera_v2?branch=master)).

 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





