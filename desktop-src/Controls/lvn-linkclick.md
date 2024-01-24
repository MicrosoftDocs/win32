---
title: LVN_LINKCLICK notification code (Commctrl.h)
description: Notifies a list-view control's parent window that a link has been clicked on. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: de8f40d6-b79e-4324-af67-9a3c0915609d
keywords:
- LVN_LINKCLICK notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_LINKCLICK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_LINKCLICK notification code

Notifies a list-view control's parent window that a link has been clicked on. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_LINKCLICK
        
    pLinkInfo = (NMLVLINK*) lParam;         
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLVLINK**](/windows/win32/api/commctrl/ns-commctrl-nmlvlink) structure. The identifier of the group containing the link is in the **iSubItem** member.

</dd> </dl>

## Return value

No return value.

## Remarks

The following example shows how an application might respond to this notification code in its [**WM\_NOTIFY**](wm-notify.md) message handler. The example toggles the collapsed state of the group and sets the appropriate link text.

``` syntax
case LVN_LINKCLICK:
{
    NMLVLINK* pLinkInfo = (NMLVLINK*)lParam;
    HWND hList = pLinkInfo->hdr.hwndFrom;
    LVGROUP groupInfo;
    groupInfo.cbSize = sizeof(groupInfo);
    groupInfo.mask = LVGF_TASK;
    int groupIndex = pLinkInfo->iSubItem;
    if (ListView_GetGroupState(hList, groupIndex, LVGS_COLLAPSED))
    {
        ListView_SetGroupState(hList, groupIndex, LVGS_COLLAPSED, 0);
        groupInfo.pszTask = L"Hide";
    }
    else
    {
        ListView_SetGroupState(hList, groupIndex, LVGS_COLLAPSED, LVGS_COLLAPSED);
        groupInfo.pszTask = L"Show";
     }
      ListView_SetGroupInfo(hList, groupIndex, &groupInfo);
      break;
}
```

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





