---
title: WM_QUERYUISTATE message (Winuser.h)
description: An application sends the WM\_QUERYUISTATE message to retrieve the UI state for a window.
ms.assetid: 3a9e3477-b5d7-4c55-b6d4-8a479451fee8
keywords:
- WM_QUERYUISTATE message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_QUERYUISTATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_QUERYUISTATE message

An application sends the **WM\_QUERYUISTATE** message to retrieve the UI state for a window.


```C++
#define WM_QUERYUISTATE                 0x0129
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used and must be 0.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used and must be 0.

</dd> </dl>

## Return value

The return value is **NULL** if the focus indicators and the keyboard accelerators are visible. Otherwise, the return value can be one or more of the following values.



| Return code/value                                                                                                                                       | Description                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**UISF\_ACTIVE**</dt> <dt>0x4</dt> </dl>    | A control should be drawn in the style used for active controls.<br/> |
| <dl> <dt>**UISF\_HIDEACCEL**</dt> <dt>0x2</dt> </dl> | Keyboard accelerators are hidden.<br/>                                |
| <dl> <dt>**UISF\_HIDEFOCUS**</dt> <dt>0x1</dt> </dl> | Focus indicators are hidden.<br/>                                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**WM\_CHANGEUISTATE**](wm-changeuistate.md)
</dt> <dt>

[**WM\_UPDATEUISTATE**](wm-updateuistate.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Accelerators](keyboard-accelerators.md)
</dt> </dl>

 

 





