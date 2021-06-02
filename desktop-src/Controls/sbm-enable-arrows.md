---
title: SBM_ENABLE_ARROWS message (Winuser.h)
description: An application sends the SBM\_ENABLE\_ARROWS message to enable or disable one or both arrows of a scroll bar control.
ms.assetid: 9646826a-3a7c-490b-822d-7511e4ef2262
keywords:
- SBM_ENABLE_ARROWS message Windows Controls
topic_type:
- apiref
api_name:
- SBM_ENABLE_ARROWS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SBM\_ENABLE\_ARROWS message

An application sends the **SBM\_ENABLE\_ARROWS** message to enable or disable one or both arrows of a scroll bar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies whether the scroll bar arrows are enabled or disabled and indicates which arrows are enabled or disabled. This parameter can be one of the following values.



| Value                                                                                                                                                                   | Meaning                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <span id="ESB_DISABLE_BOTH"></span><span id="esb_disable_both"></span><dl> <dt>**ESB\_DISABLE\_BOTH**</dt> </dl> | Disables both arrows on a scroll bar.<br/>                                                           |
| <span id="ESB_DISABLE_DOWN"></span><span id="esb_disable_down"></span><dl> <dt>**ESB\_DISABLE\_DOWN**</dt> </dl> | Disables the down arrow on a vertical scroll bar.<br/>                                               |
| <span id="ESB_DISABLE_LTUP"></span><span id="esb_disable_ltup"></span><dl> <dt>**ESB\_DISABLE\_LTUP**</dt> </dl> | Disables the left arrow on a horizontal scroll bar or the up arrow on a vertical scroll bar.<br/>    |
| <span id="ESB_DISABLE_LEFT"></span><span id="esb_disable_left"></span><dl> <dt>**ESB\_DISABLE\_LEFT**</dt> </dl> | Disables the left arrow on a horizontal scroll bar.<br/>                                             |
| <span id="ESB_DISABLE_RTDN"></span><span id="esb_disable_rtdn"></span><dl> <dt>**ESB\_DISABLE\_RTDN**</dt> </dl> | Disables the right arrow on a horizontal scroll bar or the down arrow on a vertical scroll bar.<br/> |
| <span id="ESB_DISABLE_UP"></span><span id="esb_disable_up"></span><dl> <dt>**ESB\_DISABLE\_UP**</dt> </dl>       | Disables the up arrow on a vertical scroll bar.<br/>                                                 |
| <span id="ESB_ENABLE_BOTH"></span><span id="esb_enable_both"></span><dl> <dt>**ESB\_ENABLE\_BOTH**</dt> </dl>    | Enables both arrows on a scroll bar.<br/>                                                            |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If the message succeeds, the return value is **TRUE**; otherwise, it is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





