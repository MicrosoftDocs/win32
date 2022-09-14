---
title: TTN_LINKCLICK notification code (Commctrl.h)
description: Sent when a text link inside a balloon tooltip is clicked. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: d3e76431-5b5f-4d67-8528-db21fd939917
keywords:
- TTN_LINKCLICK notification code Windows Controls
topic_type:
- apiref
api_name:
- TTN_LINKCLICK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTN\_LINKCLICK notification code

Sent when a text link inside a balloon tooltip is clicked. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TTN_LINKCLICK
```



## Parameters

This notification code has no parameters.

## Return value

Return value not used.

## Remarks

Following is an example of when this notification is sent. Assume that your balloon tooltip contains the following text, "This is a <A>link</A>". When "link" is clicked, the tooltip control sends a TTN\_LINKCLICK notification code.

> [!Note]  
> To use this notification code, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





