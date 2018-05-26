---
title: RBN\_GETOBJECT notification code
description: Sent by a rebar control created with the RBS\_REGISTERDROP style when an object is dragged over a band in the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 057474c1-5f65-4290-973e-4366b760365a
keywords:
- RBN_GETOBJECT notification code Windows Controls
topic_type:
- apiref
api_name:
- RBN_GETOBJECT
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

# RBN\_GETOBJECT notification code

Sent by a rebar control created with the [**RBS\_REGISTERDROP**](rebar-control-styles.md#rbs-registerdrop) style when an object is dragged over a band in the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
RBN_GETOBJECT

    lpnmon = (LPNMOBJECTNOTIFY) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMOBJECTNOTIFY**](/windows/win32/Commctrl/ns-commctrl-tagnmobjectnotify?branch=master) structure that contains information about the band that the object is dragged over and also receives the data provided by the receiving application in response to this notification code.

</dd> </dl>

## Return value

The return value for this notification code must be zero.

## Remarks

To receive the RBN\_GETOBJECT notification code, initialize OLE with a call to [**OleInitialize**](https://msdn.microsoft.com/library/windows/desktop/ms690134) or [**CoInitialize**](https://msdn.microsoft.com/library/windows/desktop/ms678543).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





