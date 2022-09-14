---
title: HDN_FILTERBTNCLICK notification code (Commctrl.h)
description: Notifies the header control's parent window when the filter button is clicked or in response to an HDM\_SETITEM message. This notification code sent in the form of a WM\_NOTIFY message.
ms.assetid: 36b85cdc-1022-4568-8891-0c919c850fd4
keywords:
- HDN_FILTERBTNCLICK notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_FILTERBTNCLICK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDN\_FILTERBTNCLICK notification code

Notifies the header control's parent window when the filter button is clicked or in response to an [**HDM\_SETITEM**](hdm-setitem.md) message. This notification code sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_FILTERBTNCLICK

    pNMHDFilterBtnClk = (LPNMHDFILTERBTNCLICK) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHDFILTERBTNCLICK**](/windows/win32/api/commctrl/ns-commctrl-nmhdfilterbtnclick) structure that contains information about the header control and the header filter button.

</dd> </dl>

## Return value

If you return **TRUE**, an [HDN\_FILTERCHANGE](hdn-filterchange.md) notification code will be sent to the header control's parent window. This notification code gives the parent window an opportunity to synchronize its user interface elements. Return **FALSE** if you do not want the notification sent.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**NMHDFILTERBTNCLICK**](/windows/win32/api/commctrl/ns-commctrl-nmhdfilterbtnclick)
</dt> </dl>

 

 





