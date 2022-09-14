---
title: LVN_GETDISPINFO notification code (Commctrl.h)
description: Sent by a list-view control to its parent window. It is a request for the parent window to provide information needed to display or sort a list-view item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 04310e39-69bc-45d7-958c-00452279d7a9
keywords:
- LVN_GETDISPINFO notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_GETDISPINFO
- LVN_GETDISPINFOA
- LVN_GETDISPINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_GETDISPINFO notification code

Sent by a list-view control to its parent window. It is a request for the parent window to provide information needed to display or sort a list-view item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_GETDISPINFO
        
    pdi = (NMLVDISPINFO*) lParam
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLVDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmlvdispinfoa) structure. On input, the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure contained in this structure specifies the type of information required and identifies the item or subitem of interest. Use the **LVITEM** structure to return the requested information to the control. If your message handler sets the LVIF\_DI\_SETITEM flag in the **mask** member of the **LVITEM** structure, the list-view control stores the requested information and will not ask for it again.

</dd> </dl>

## Return value

No return value.

## Remarks

The notification receiver casts *lParam* to retrieve the [**NMLVDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmlvdispinfoa) structure. The *wParam* parameter contains the notification code.

A list-view control sends the **LVN\_GETDISPINFO** notification code to retrieve item information that is stored by the application rather than the control. The information can be text or icon information for an item. It can also be item state information. See the [**LVM\_SETCALLBACKMASK**](lvm-setcallbackmask.md) message for more information on implementing item state on a callback basis.

For more information on list-view callbacks, see [Callback Items and the Callback Mask](list-view-controls-overview.md).

## Examples

The following example shows how this notification code might be handled to set the text in the columns of a list view. The data for each item is held in the following structure.


```C++
 typedef struct tagPETINFO
{
    TCHAR szName[50];
    TCHAR szBreed[50];
    TCHAR szGender[7];
    TCHAR szPrice[20];
    GroupIds iGroup;
} PETINFO;
            
```



The following is from the WM\_NOTIFY handler in the dialog procedure.


```C++
    case WM_NOTIFY:
        switch (((LPNMHDR) lParam)->code)
        {
        case LVN_GETDISPINFO:
            {
                NMLVDISPINFO* plvdi = (NMLVDISPINFO*)lParam;    
                switch (plvdi->item.iSubItem)
                {
                case 0:
                    // rgPetInfo is an array of PETINFO structures.
                    plvdi->item.pszText = rgPetInfo[plvdi->item.iItem].szName;
                    break;

                case 1:
                    plvdi->item.pszText = rgPetInfo[plvdi->item.iItem].szBreed;
                    break;

                case 2:
                    plvdi->item.pszText = rgPetInfo[plvdi->item.iItem].szGender;
                    break;

                case 3:
                    plvdi->item.pszText = rgPetInfo[plvdi->item.iItem].szPrice;
                    break;

                default:
                    break;
                }
                return TRUE;
            }
      // More notifications...
      }
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVN\_GETDISPINFOW** (Unicode) and **LVN\_GETDISPINFOA** (ANSI)<br/>           |



## See also

<dl> <dt>

[**LVN\_SETDISPINFO**](lvn-setdispinfo.md)
</dt> </dl>

 

 





