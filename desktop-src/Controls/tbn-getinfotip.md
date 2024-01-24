---
title: TBN_GETINFOTIP notification code (Commctrl.h)
description: Retrieves infotip information for a toolbar item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 877de60c-f6e1-440a-81f0-d66ab443c985
keywords:
- TBN_GETINFOTIP notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_GETINFOTIP
- TBN_GETINFOTIPA
- TBN_GETINFOTIPW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBN\_GETINFOTIP notification code

Retrieves infotip information for a toolbar item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_GETINFOTIP

    lptbgit = (LPNMTBGETINFOTIP) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTBGETINFOTIP**](/windows/win32/api/commctrl/ns-commctrl-nmtbgetinfotipa) structure that contains item information and receives infotip information.

</dd> </dl>

## Return value

The return value is ignored by the control.

## Remarks

The infotip support in the toolbar allows the toolbar to display tooltips for items that are as large as INFOTIPSIZE characters. If this notification code is not processed, the toolbar will use the item's text for the infotip.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TBN\_GETINFOTIPW** (Unicode) and **TBN\_GETINFOTIPA** (ANSI)<br/>             |



 

 





