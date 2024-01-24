---
title: SB_SETTIPTEXT message (Commctrl.h)
description: Sets the tooltip text for a part in a status bar. The status bar must have been created with the SBT\_TOOLTIPS style to enable tooltips.
ms.assetid: 8fc3cc00-9742-4861-b2c2-b8aa30f75aaa
keywords:
- SB_SETTIPTEXT message Windows Controls
topic_type:
- apiref
api_name:
- SB_SETTIPTEXT
- SB_SETTIPTEXTA
- SB_SETTIPTEXTW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_SETTIPTEXT message

Sets the tooltip text for a part in a status bar. The status bar must have been created with the [**SBT\_TOOLTIPS**](status-bar-styles.md) style to enable tooltips.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the part that will receive the tooltip text.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a character buffer that contains the new tooltip text.

</dd> </dl>

## Return value

The return value is not used.

## Remarks

This tooltip text is displayed in two situations:

-   When the corresponding pane in the status bar contains only an icon.
-   When the corresponding pane in the status bar contains text that is truncated due to the size of the pane.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **SB\_SETTIPTEXTW** (Unicode) and **SB\_SETTIPTEXTA** (ANSI)<br/>               |



 

 





