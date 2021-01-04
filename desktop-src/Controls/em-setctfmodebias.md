---
title: EM_SETCTFMODEBIAS message (Richedit.h)
description: Sets the Text Services Framework (TSF) mode bias for a rich edit control.
ms.assetid: 17e3aac8-2ba8-4c06-bfd6-e118cfb82529
keywords:
- EM_SETCTFMODEBIAS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETCTFMODEBIAS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETCTFMODEBIAS message

Sets the Text Services Framework (TSF) mode bias for a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Mode bias value. This can be one of the following values.



| Value                                                                                                                                                                                                                     | Meaning                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="CTFMODEBIAS_DEFAULT"></span><span id="ctfmodebias_default"></span><dl> <dt>**CTFMODEBIAS\_DEFAULT**</dt> </dl>                                           | There is no mode bias.<br/>                             |
| <span id="CTFMODEBIAS_FILENAME"></span><span id="ctfmodebias_filename"></span><dl> <dt>**CTFMODEBIAS\_FILENAME**</dt> </dl>                                        | The bias is to a filename.<br/>                         |
| <span id="CTFMODEBIAS_NAME"></span><span id="ctfmodebias_name"></span><dl> <dt>**CTFMODEBIAS\_NAME**</dt> </dl>                                                    | The bias is to a name.<br/>                             |
| <span id="CTFMODEBIAS_READING"></span><span id="ctfmodebias_reading"></span><dl> <dt>**CTFMODEBIAS\_READING**</dt> </dl>                                           | The bias is to the reading.<br/>                        |
| <span id="CTFMODEBIAS_DATETIME"></span><span id="ctfmodebias_datetime"></span><dl> <dt>**CTFMODEBIAS\_DATETIME**</dt> </dl>                                        | The bias is to a date or time.<br/>                     |
| <span id="CTFMODEBIAS_CONVERSATION"></span><span id="ctfmodebias_conversation"></span><dl> <dt>**CTFMODEBIAS\_CONVERSATION**</dt> </dl>                            | The bias is to a conversation.<br/>                     |
| <span id="CTFMODEBIAS_NUMERIC"></span><span id="ctfmodebias_numeric"></span><dl> <dt>**CTFMODEBIAS\_NUMERIC**</dt> </dl>                                           | The bias is to a number.<br/>                           |
| <span id="CTFMODEBIAS_HIRAGANA"></span><span id="ctfmodebias_hiragana"></span><dl> <dt>**CTFMODEBIAS\_HIRAGANA**</dt> </dl>                                        | The bias is to hiragana strings.<br/>                   |
| <span id="CTFMODEBIAS_KATAKANA"></span><span id="ctfmodebias_katakana"></span><dl> <dt>**CTFMODEBIAS\_KATAKANA**</dt> </dl>                                        | The bias is to katakana strings.<br/>                   |
| <span id="CTFMODEBIAS_HANGUL"></span><span id="ctfmodebias_hangul"></span><dl> <dt>**CTFMODEBIAS\_HANGUL**</dt> </dl>                                              | The bias is to Hangul characters.<br/>                  |
| <span id="CTFMODEBIAS_HALFWIDTHKATAKANA"></span><span id="ctfmodebias_halfwidthkatakana"></span><dl> <dt>**CTFMODEBIAS\_HALFWIDTHKATAKANA**</dt> </dl>             | The bias is to half-width katakana strings.<br/>        |
| <span id="CTFMODEBIAS_FULLWIDTHALPHANUMERIC"></span><span id="ctfmodebias_fullwidthalphanumeric"></span><dl> <dt>**CTFMODEBIAS\_FULLWIDTHALPHANUMERIC**</dt> </dl> | The bias is to full-width alphanumeric characters.<br/> |
| <span id="CTFMODEBIAS_HALFWIDTHALPHANUMERIC"></span><span id="ctfmodebias_halfwidthalphanumeric"></span><dl> <dt>**CTFMODEBIAS\_HALFWIDTHALPHANUMERIC**</dt> </dl> | The bias is to half-width alphanumeric characters.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

If successful, the return value is the new TSF mode bias value. If unsuccessful, the return value is the old TSF mode bias value.

## Remarks

When a Microsoft Rich Edit application uses TSF, it can select the TSF mode bias. This message sets the criteria by which an alternative choice appears at the top of the list for selection.

To set the mode bias for the Input Method Editor (IME), use [**EM\_SETIMEMODEBIAS**](em-setimemodebias.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_GETCTFMODEBIAS**](em-getctfmodebias.md)
</dt> <dt>

[**EM\_SETIMEMODEBIAS**](em-setimemodebias.md)
</dt> </dl>

 

 





