---
title: RBN\_AUTOBREAK message
description: Notifies a rebar's parent that a break will appear in the bar. The parent determines whether to make the break. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: b7a63027-6cfa-4d5a-9ea6-fdd8b4fb6864
keywords:
- RBN_AUTOBREAK message Windows Controls
topic_type:
- apiref
api_name:
- RBN_AUTOBREAK
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

# RBN\_AUTOBREAK message

Notifies a [rebar's](rebar-controls.md) parent that a break will appear in the bar. The parent determines whether to make the break. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
RBN_AUTOBREAK

    pnmRebarAutoBreak = (LPNMREBARAUTOBREAK) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**NMREBARAUTOBREAK**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmrebarautobreak) structure that contains information about the notification code.

</dd> </dl>

## Return value

The return value for this notification is not used.

## Remarks

The value in the **fAutoBreak** member of the [**NMREBARAUTOBREAK**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmrebarautobreak) structure indicates whether a break should occur in the rebar.

To use this notification code, specify Comctl32.dll version 6 in the manifest. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





