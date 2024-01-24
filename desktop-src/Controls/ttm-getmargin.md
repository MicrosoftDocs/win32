---
title: TTM_GETMARGIN message (Commctrl.h)
description: Retrieves the top, left, bottom, and right margins set for a tooltip window. A margin is the distance, in pixels, between the tooltip window border and the text contained within the tooltip window.
ms.assetid: c33ee1de-5fbd-4c7e-a703-576c2ffd3052
keywords:
- TTM_GETMARGIN message Windows Controls
topic_type:
- apiref
api_name:
- TTM_GETMARGIN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_GETMARGIN message

Retrieves the top, left, bottom, and right margins set for a tooltip window. A margin is the distance, in pixels, between the tooltip window border and the text contained within the tooltip window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that will receive the margin information. The members of the **RECT** structure do not define a bounding rectangle. For the purpose of this message, the structure members are interpreted as follows:



| Value                                                                                                                                   | Meaning                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <span id="top"></span><span id="TOP"></span><dl> <dt>**top**</dt> </dl>          | Distance between top border and top of tooltip text, in pixels.<br/>         |
| <span id="left"></span><span id="LEFT"></span><dl> <dt>**left**</dt> </dl>       | Distance between left border and left end of tooltip text, in pixels.<br/>   |
| <span id="bottom"></span><span id="BOTTOM"></span><dl> <dt>**bottom**</dt> </dl> | Distance between bottom border and bottom of tooltip text, in pixels.<br/>   |
| <span id="right"></span><span id="RIGHT"></span><dl> <dt>**right**</dt> </dl>    | Distance between right border and right end of tooltip text, in pixels.<br/> |



 

</dd> </dl>

## Return value

The return value for this message is not used.

## Remarks

All four margins default to zero when you create the tooltip control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TTM\_SETMARGIN**](ttm-setmargin.md)
</dt> </dl>

 

