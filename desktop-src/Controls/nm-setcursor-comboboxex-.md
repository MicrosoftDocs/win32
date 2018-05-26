---
title: NM\_SETCURSOR (ComboBoxEx) notification code
description: Notifies a ComboBoxEx controls parent window that the control is setting the cursor in response to a WM\_SETCURSOR message. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: a1c617fa-8eb2-444f-88d1-9913de7a42d1
keywords:
- NM_SETCURSOR (ComboBoxEx) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_SETCURSOR
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

# NM\_SETCURSOR (ComboBoxEx) notification code

Notifies a ComboBoxEx control's parent window that the control is setting the cursor in response to a [**WM\_SETCURSOR**](https://msdn.microsoft.com/library/windows/desktop/ms648382) message. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_SETCURSOR

    lpnmm = (LPNMMOUSE) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMMOUSE**](/windows/win32/Commctrl/ns-commctrl-tagnmmouse?branch=master) structure that contains additional information about this notification.

</dd> </dl>

## Return value

Return zero to enable the control to set the cursor or nonzero to prevent the control from setting the cursor.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





