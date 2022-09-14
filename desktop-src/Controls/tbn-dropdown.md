---
title: TBN_DROPDOWN notification code (Commctrl.h)
description: Sent by a toolbar control when the user clicks a dropdown button. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 85360f74-4b43-4d0a-8c89-22b0741fe96a
keywords:
- TBN_DROPDOWN notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_DROPDOWN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBN\_DROPDOWN notification code

Sent by a toolbar control when the user clicks a dropdown button. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_DROPDOWN

    lpnmtb = (LPNMTOOLBAR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTOOLBAR**](/windows/win32/api/commctrl/ns-commctrl-nmtoolbara) structure that contains information about this notification code. For this notification code, only the **hdr** and **iItem** members of this structure are valid.

</dd> </dl>

## Return value

Returns one of the following values:



| Return code                                                                                          | Description                                                                       |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**TBDDRET\_DEFAULT**</dt> </dl>      | The drop-down was handled.<br/>                                             |
| <dl> <dt>**TBDDRET\_NODEFAULT**</dt> </dl>    | The drop-down was not handled.<br/>                                         |
| <dl> <dt>**TBDDRET\_TREATPRESSED**</dt> </dl> | The drop-down was handled, but treat the button like a regular button.<br/> |



 

## Remarks

> [!Note]  
> Dropdown buttons can be plain ([**BTNS\_DROPDOWN**](toolbar-control-and-button-styles.md) style), display an arrow next to the button image ([**BTNS\_WHOLEDROPDOWN**](toolbar-control-and-button-styles.md) style), or display an arrow that is separated from the image ([**TBSTYLE\_EX\_DRAWDDARROWS**](toolbar-extended-styles.md) style). If a separated arrow is used, TBN\_DROPDOWN is sent only if the user clicks the arrow portion of the button. If the user clicks the main part of the button, a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message with button's ID is sent, just as with a standard button. For the other two styles of dropdown button, TBN\_DROPDOWN is sent when the user clicks any part of the button.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

