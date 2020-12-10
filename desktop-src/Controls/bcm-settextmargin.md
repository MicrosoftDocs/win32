---
title: BCM_SETTEXTMARGIN message (Commctrl.h)
description: The BCM\_SETTEXTMARGIN message sets the margins for drawing text in a button control.
ms.assetid: 0798b1c5-7db4-46c6-8881-4c847abc7460
keywords:
- BCM_SETTEXTMARGIN message Windows Controls
topic_type:
- apiref
api_name:
- BCM_SETTEXTMARGIN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BCM\_SETTEXTMARGIN message

The **BCM\_SETTEXTMARGIN** message sets the margins for drawing text in a button control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure that specifies the margins to use for drawing text.

</dd> </dl>

## Return value

If the message succeeds, it returns **TRUE**. Otherwise it returns **FALSE**.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**Button\_SetTextMargin**](/windows/desktop/api/Commctrl/nf-commctrl-button_settextmargin)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Buttons](buttons.md)
</dt> </dl>

 

