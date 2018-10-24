---
title: TCN_SELCHANGING notification code
description: Notifies a tab control's parent window that the currently selected tab is about to change. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: ec7b1bd3-8932-4418-9eed-ecb7c748e4dd
keywords:
- TCN_SELCHANGING notification code Windows Controls
topic_type:
- apiref
api_name:
- TCN_SELCHANGING
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TCN\_SELCHANGING notification code

Notifies a tab control's parent window that the currently selected tab is about to change. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TCN_SELCHANGING 

    lpnmhdr = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-_nmhdr) structure that contains additional information about this notification.

</dd> </dl>

## Return value

Returns **TRUE** to prevent the selection from changing, or **FALSE** to allow the selection to change.

## Remarks

To determine the currently selected tab, use the [**TabCtrl\_GetCurSel**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_getcursel) macro.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[TCN\_SELCHANGE](tcn-selchange.md)
</dt> </dl>

 

 





