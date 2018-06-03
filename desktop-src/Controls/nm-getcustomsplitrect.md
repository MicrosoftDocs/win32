---
title: NM\_GETCUSTOMSPLITRECT notification code
description: Sent by a button control to its parent to get measurements for the two rectangles of the split button. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: ce72778d-3cca-46a4-9d05-40954a18681d
keywords:
- NM_GETCUSTOMSPLITRECT notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_GETCUSTOMSPLITRECT
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

# NM\_GETCUSTOMSPLITRECT notification code

Sent by a button control to its parent to get measurements for the two rectangles of the split button. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_GETCUSTOMSPLITRECT
        
    nmCustomSplit = (NMCUSTOMSPLITRECTINFO *) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMCUSTOMSPLITRECTINFO**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmcustomsplitrectinfo) to receive bounding rectangles information. The **NMCUSTOMSPLITRECTINFO** structure is sent with the notification code as a request for the parent to provide measurements for the rectangles of the split button.

</dd> </dl>

## Return value

Return [**CDRF\_SKIPDEFAULT**](https://www.bing.com/search?q=**CDRF\_SKIPDEFAULT**) to tell the button control to use the values returned in the [**NMCUSTOMSPLITRECTINFO**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmcustomsplitrectinfo) structure; otherwise, return [**CDRF\_DODEFAULT**](https://www.bing.com/search?q=**CDRF\_DODEFAULT**).

## Remarks

This notification code is sent by a button control before it is drawn. The button must be of style [**BS\_SPLITBUTTON**](https://www.bing.com/search?q=**BS\_SPLITBUTTON**) or [**BS\_DEFSPLITBUTTON**](https://www.bing.com/search?q=**BS\_DEFSPLITBUTTON**). If the rectangles returned to the control in *lParam* are not valid, they are ignored.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





