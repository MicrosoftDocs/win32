---
title: TCN_GETOBJECT notification code (Commctrl.h)
description: Sent by a tab control when it has the TCS\_EX\_REGISTERDROP extended style and an object is dragged over a tab item in the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 0beddabe-0e97-4fe7-bcf7-adaba0d72dfe
keywords:
- TCN_GETOBJECT notification code Windows Controls
topic_type:
- apiref
api_name:
- TCN_GETOBJECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCN\_GETOBJECT notification code

Sent by a tab control when it has the [**TCS\_EX\_REGISTERDROP**](tab-control-extended-styles.md) extended style and an object is dragged over a tab item in the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TCN_GETOBJECT

    lpnmon = (LPNMOBJECTNOTIFY) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMOBJECTNOTIFY**](/windows/win32/api/commctrl/ns-commctrl-nmobjectnotify) structure that contains information about the tab item the object is dragged over and receives data the application returns in response to this message.

</dd> </dl>

## Return value

The application processing this notification code must return zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





