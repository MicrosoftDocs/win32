---
title: TBN_GETBUTTONINFO notification code (Commctrl.h)
description: Retrieves toolbar customization information and notifies the toolbar's parent window of any changes being made to the toolbar. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 088527fe-5a38-4c35-ba68-d0cbfdee410c
keywords:
- TBN_GETBUTTONINFO notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_GETBUTTONINFO
- TBN_GETBUTTONINFOA
- TBN_GETBUTTONINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBN\_GETBUTTONINFO notification code

Retrieves toolbar customization information and notifies the toolbar's parent window of any changes being made to the toolbar. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_GETBUTTONINFO 

    lpnmtb = (LPNMTOOLBAR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTOOLBAR**](/windows/win32/api/commctrl/ns-commctrl-nmtoolbara) structure. The **iItem** member specifies a zero-based index that provides a count of the buttons the Customize Toolbar dialog box displays as both available and present on the toolbar. The **pszText** member specifies the address of the current button text, and **cchText** specifies its length in characters. The application should fill the structure with information about the button.

</dd> </dl>

## Return value

Returns **TRUE** if button information was copied to the specified structure, or **FALSE** otherwise.

## Remarks

The toolbar control allocates a buffer, and the receiver (parent window) must copy the text into that buffer. The **cchText** member contains the length of the buffer allocated by the toolbar when TBN\_GETBUTTONINFO is sent to the parent window.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TBN\_GETBUTTONINFOW** (Unicode) and **TBN\_GETBUTTONINFOA** (ANSI)<br/>       |



 

 





