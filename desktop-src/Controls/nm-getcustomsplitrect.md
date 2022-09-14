---
title: NM_GETCUSTOMSPLITRECT notification code (Commctrl.h)
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
ms.topic: reference
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

A pointer to an [**NMCUSTOMSPLITRECTINFO**](/windows/win32/api/commctrl/ns-commctrl-nmcustomsplitrectinfo) to receive bounding rectangles information. The **NMCUSTOMSPLITRECTINFO** structure is sent with the notification code as a request for the parent to provide measurements for the rectangles of the split button.

</dd> </dl>

## Return value

Return [**CDRF\_SKIPDEFAULT**](cdrf-constants.md) to tell the button control to use the values returned in the [**NMCUSTOMSPLITRECTINFO**](/windows/win32/api/commctrl/ns-commctrl-nmcustomsplitrectinfo) structure; otherwise, return [**CDRF\_DODEFAULT**](cdrf-constants.md).

## Remarks

This notification code is sent by a button control before it is drawn. The button must be of style [**BS\_SPLITBUTTON**](button-styles.md) or [**BS\_DEFSPLITBUTTON**](button-styles.md). If the rectangles returned to the control in *lParam* are not valid, they are ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





