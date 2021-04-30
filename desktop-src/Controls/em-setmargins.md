---
title: EM_SETMARGINS message (Winuser.h)
description: Sets the widths of the left and right margins for an edit control. The message redraws the control to reflect the new margins. You can send this message to either an edit control or a rich edit control.
ms.assetid: 23eb6c9e-3cf9-4c90-b33e-8da84034b49b
keywords:
- EM_SETMARGINS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETMARGINS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETMARGINS message

Sets the widths of the left and right margins for an edit control. The message redraws the control to reflect the new margins. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The margins to set. This parameter can be one or more of the following values.



| Value                                                                                                                                                            | Meaning                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EC_LEFTMARGIN"></span><span id="ec_leftmargin"></span><dl> <dt>**EC\_LEFTMARGIN**</dt> </dl>    | Sets the left margin.<br/>                                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="EC_RIGHTMARGIN"></span><span id="ec_rightmargin"></span><dl> <dt>**EC\_RIGHTMARGIN**</dt> </dl> | Sets the right margin.<br/>                                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="EC_USEFONTINFO"></span><span id="ec_usefontinfo"></span><dl> <dt>**EC\_USEFONTINFO**</dt> </dl> | **Rich edit controls:** Sets the left and right margins to a narrow width calculated using the text metrics of the control's current font. If no font has been set for the control, the margins are set to zero. The *lParam* parameter is ignored. <br/> **Edit controls:** The **EC\_USEFONTINFO** value cannot be used in the *wParam* parameter. It can only be used in the *lParam* parameter.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the new width of the left margin, in pixels. This value is ignored if *wParam* does not include **EC\_LEFTMARGIN**.

**Edit controls and Rich Edit 3.0 and later:** The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) can specify the **EC\_USEFONTINFO** value to set the left margin to a narrow width calculated using the text metrics of the control's current font. If no font has been set for the control, the margin is set to zero.

The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the new width of the right margin, in pixels. This value is ignored if *wParam* does not include **EC\_RIGHTMARGIN**.

**Edit controls and Rich Edit 3.0 and later:** The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) can specify the **EC\_USEFONTINFO** value to set the right margin to a narrow width calculated using the text metrics of the control's current font. If no font has been set for the control, the margin is set to zero.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

**Edit controls:** You cannot use **EC\_USEFONTINFO** in the *wParam* parameter, but you can use it in the *lParam* parameter.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. All rich edit versions support the use of **EC\_USEFONTINFO** in the *wParam* parameter. However, only Microsoft Rich Edit 3.0 and later support the use of **EC\_USEFONTINFO** in the *lParam* parameter. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETMARGINS**](em-getmargins.md)
</dt> </dl>

 

