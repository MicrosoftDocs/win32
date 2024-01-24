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



| Value                                                                                                                                                                                    | Meaning                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <span id="TO_ADVANCEDTYPOGRAPHY_"></span><span id="to_advancedtypography_"></span><dl> <dt>**TO\_ADVANCEDTYPOGRAPHY** </dt> </dl> | Advanced line breaking and line formatting is turned on. <br/>                    |
| <span id="TO_SIMPLELINEBREAK"></span><span id="to_simplelinebreak"></span><dl> <dt>**TO\_SIMPLELINEBREAK**</dt> </dl>             | Faster line breaking for simple text (requires **TO\_ADVANCEDTYPOGRAPHY**). <br/> |



 

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

 

 





