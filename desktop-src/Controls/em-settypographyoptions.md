---
title: EM_SETTYPOGRAPHYOPTIONS message (Richedit.h)
description: Sets the current state of the typography options of a rich edit control.
ms.assetid: 000e72a6-3f8c-4735-8190-3ac06a2206ac
keywords:
- EM_SETTYPOGRAPHYOPTIONS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETTYPOGRAPHYOPTIONS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETTYPOGRAPHYOPTIONS message

Sets the current state of the typography options of a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies one or both of the following values.



| Value | Meaning |
|---|---|
| **TO\_ADVANCEDTYPOGRAPHY**<br>`0x0001` | Advanced line breaking and line formatting is turned on. |
| **TO\_SIMPLELINEBREAK**<br>`0x0002` | Faster line breaking for simple text (requires **TO\_ADVANCEDTYPOGRAPHY**). |
| **TO\_DISABLECUSTOMTEXTOUT**<br>`0x0004` | ??? |
| **TO\_ADVANCEDLAYOUT**<br>`0x0008` | ??? |
| **TO\_DEFAULTCOLOREMOJI**<br>`0x1000` | Enable the display of colored emoji (requires **TO\_DISPLAYFONTCOLOR**). |
| **TO\_DISPLAYFONTCOLOR**<br>`0x200` | Enable the display of colored fonts. |

</dd> <dt>

*lParam* 
</dt> <dd>

A mask consisting of one or more of the flags in *wParam*. Only the flags that are set in this mask will be set or cleared. This allows a single flag to be set or cleared without reading the current flag states.

</dd> </dl>

## Return value

Returns **TRUE** if *wParam* is valid, otherwise **FALSE**.

## Remarks

Advanced line breaking is turned on automatically by the rich edit control when needed, such as for handling complex scripts like Arabic and Hebrew, and for mathematics. It s also needed for justified paragraphs, hyphenation, and other typographic features.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Rich Edit 3.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETTYPOGRAPHYOPTIONS**](em-gettypographyoptions.md)
</dt> </dl>

 

 





