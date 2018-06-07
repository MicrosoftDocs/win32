---
title: TBN\_DRAGOUT notification code
description: Sent by a toolbar control when the user clicks a button and then moves the cursor off the button. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 3566ad60-9744-494f-bb02-d30b41d06351
keywords:
- TBN_DRAGOUT notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_DRAGOUT
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

# TBN\_DRAGOUT notification code

Sent by a toolbar control when the user clicks a button and then moves the cursor off the button. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_DRAGOUT

    lpnmtb = (LPNMTOOLBAR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTOOLBAR**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmtoolbara) structure that contains information about this notification code. For this notification code, only the **hdr** and **iItem** members of this structure are valid. The **iItem** member of this structure contains the command identifier of the button being dragged.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

This notification code allows an application to implement drag-and-drop functionality for toolbar buttons. When processing this notification code, the application will begin the drag-and-drop operation.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





