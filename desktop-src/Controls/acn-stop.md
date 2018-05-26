---
title: ACN\_STOP notification code
description: Notifies the parent window of an animation control that the associated AVI clip has stopped playing. This notification code is sent in the form of a WM\_COMMAND message.
ms.assetid: 2f21a2ec-975f-4592-8b21-956bd5311ef4
keywords:
- ACN_STOP notification code Windows Controls
topic_type:
- apiref
api_name:
- ACN_STOP
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

# ACN\_STOP notification code

Notifies the parent window of an animation control that the associated AVI clip has stopped playing. This notification code is sent in the form of a [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
ACN_STOP     

    WPARAM wParam;
    LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) contains the animation control's identifier. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

An **HWND** that specifies the handle to the animation control.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





