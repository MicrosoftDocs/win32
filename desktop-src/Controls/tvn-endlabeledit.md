---
title: TVN\_ENDLABELEDIT notification code
description: Notifies a tree-view controls parent window about the end of label editing for an item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 82eb9fcd-de10-4efb-8501-78c5af5e089e
keywords:
- TVN_ENDLABELEDIT notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_ENDLABELEDIT
- TVN_ENDLABELEDITA
- TVN_ENDLABELEDITW
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

# TVN\_ENDLABELEDIT notification code

Notifies a tree-view control's parent window about the end of label editing for an item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_ENDLABELEDIT 

    ptvdi = (LPNMTVDISPINFO) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTVDISPINFO**](/windows/win32/Commctrl/ns-commctrl-tagtvdispinfoa?branch=master) structure. The **item** member of this structure is a [**TVITEM**](/windows/win32/Commctrl/ns-commctrl-tagtvitema?branch=master) structure whose **hItem**, **lParam**, and **pszText** members contain valid information about the item that was edited. If label editing was canceled, the **pszText** member of the **TVITEM** structure is **NULL**; otherwise, **pszText** is the address of the edited text.

</dd> </dl>

## Return value

If the **pszText** member is non-**NULL**, return **TRUE** to set the item's label to the edited text. Return **FALSE** to reject the edited text and revert to the original label.

## Remarks

If the **pszText** member is **NULL**, the return value is ignored.

If you specified the LPSTR\_TEXTCALLBACK value for this item and the **pszText** member is non-**NULL**, your TVN\_ENDLABELEDIT handler should copy the text from **pszText** to your local storage.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_ENDLABELEDITW** (Unicode) and **TVN\_ENDLABELEDITA** (ANSI)<br/>         |



 

 





