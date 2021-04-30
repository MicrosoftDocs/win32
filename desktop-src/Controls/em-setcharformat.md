---
title: EM_SETCHARFORMAT message (Richedit.h)
description: Sets character formatting in a rich edit control.
ms.assetid: 5e7a545d-4ca4-4dc6-badb-584c11194982
keywords:
- EM_SETCHARFORMAT message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETCHARFORMAT
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETCHARFORMAT message

Sets character formatting in a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Character formatting that applies to the control. If this parameter is zero, the default character format is set. Otherwise, it can be one of the following values.



| Value                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SCF_ALL"></span><span id="scf_all"></span><dl> <dt>**SCF\_ALL**</dt> </dl>                                     | Applies the formatting to all text in the control. Not valid with **SCF\_SELECTION** or **SCF\_WORD**.<br/>                                                                                                                                                                                         |
| <span id="SCF_ASSOCIATEFONT"></span><span id="scf_associatefont"></span><dl> <dt>**SCF\_ASSOCIATEFONT**</dt> </dl>       | **RichEdit 4.1:** Associates a font to a given script, thus changing the default font for that script. To specify the font, use the following members of [**CHARFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-charformat2a): **yHeight**, **bCharSet**, **bPitchAndFamily**, **szFaceName**, and **lcid**.<br/>                     |
| <span id="SCF_ASSOCIATEFONT2"></span><span id="scf_associatefont2"></span><dl> <dt>**SCF\_ASSOCIATEFONT2**</dt> </dl>    | **RichEdit 4.1:** Associates a surrogate (plane-2) font to a given script, thus changing the default font for that script. To specify the font, use the following members of [**CHARFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-charformat2a): **yHeight**, **bCharSet**, **bPitchAndFamily**, **szFaceName**, and **lcid**.<br/> |
| <span id="SCF_CHARREPFROMLCID"></span><span id="scf_charrepfromlcid"></span><dl> <dt>**SCF\_CHARREPFROMLCID**</dt> </dl> | Gets the character repertoire from the LCID.<br/>                                                                                                                                                                                                                                                   |
| <span id="SCF_DEFAULT"></span><span id="scf_default"></span><dl> <dt>**SCF\_DEFAULT**</dt> </dl>                         | **RichEdit 4.1:** Sets the default font for the control. <br/>                                                                                                                                                                                                                                      |
| <span id="SPF_DONTSETDEFAULT"></span><span id="spf_dontsetdefault"></span><dl> <dt>**SPF\_DONTSETDEFAULT**</dt> </dl>    | Prevents setting the default paragraph format when the rich edit control is empty.<br/>                                                                                                                                                                                                             |
| <span id="SCF_NOKBUPDATE"></span><span id="scf_nokbupdate"></span><dl> <dt>**SCF\_NOKBUPDATE**</dt> </dl>                | **RichEdit 4.1:** Prevents keyboard switching to match the font. For example, if an Arabic font is set, normally the automatic keyboard feature for Bidi languages changes the keyboard to an Arabic keyboard.<br/>                                                                                 |
| <span id="SCF_SELECTION"></span><span id="scf_selection"></span><dl> <dt>**SCF\_SELECTION**</dt> </dl>                   | Applies the formatting to the current selection. If the selection is empty, the character formatting is applied to the insertion point, and the new character format is in effect only until the insertion point changes.<br/>                                                                      |
| <span id="SPF_SETDEFAULT"></span><span id="spf_setdefault"></span><dl> <dt>**SPF\_SETDEFAULT**</dt> </dl>                | Sets the default paragraph formatting attributes.<br/>                                                                                                                                                                                                                                              |
| <span id="SCF_SMARTFONT"></span><span id="scf_smartfont"></span><dl> <dt>**SCF\_SMARTFONT**</dt> </dl>                   | Apply the font only if it can handle script.<br/>                                                                                                                                                                                                                                                   |
| <span id="SCF_USEUIRULES"></span><span id="scf_useuirules"></span><dl> <dt>**SCF\_USEUIRULES**</dt> </dl>                | **RichEdit 4.1:** Used with **SCF\_SELECTION**. Indicates that format came from a toolbar or other UI tool, so UI formatting rules should be used instead of literal formatting.<br/>                                                                                                               |
| <span id="SCF_WORD"></span><span id="scf_word"></span><dl> <dt>**SCF\_WORD**</dt> </dl>                                  | Applies the formatting to the selected word or words. If the selection is empty but the insertion point is inside a word, the formatting is applied to the word. The **SCF\_WORD** value must be used in conjunction with the **SCF\_SELECTION** value.<br/>                                        |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**CHARFORMAT**](/windows/win32/api/richedit/ns-richedit-charformata) structure specifying the character formatting to use. Only the formatting attributes specified by the **dwMask** member are changed.

Microsoft Rich Edit 2.0 and later: This parameter can be a pointer to a [**CHARFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-charformat2a) structure, which is an extension of the [**CHARFORMAT**](/windows/win32/api/richedit/ns-richedit-charformata) structure. Before sending the **EM\_SETCHARFORMAT** message, set the structure's **cbSize** member to `sizeof(CHARFORMAT)` or `sizeof(CHARFORMAT2)` indicate which version of the structure is being used.

The **szFaceName** and **bCharSet** members may be overruled when invalid for characters, for example: Arial on kanji characters.

</dd> </dl>

## Return value

If the operation succeeds, the return value is a nonzero value.

If the operation fails, the return value is zero.

## Remarks

If this message is sent more than once with the same parameters, the effect on the text is toggled. That is, sending the message once produces the effect, sending the message twice cancels the effect, and so forth.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CHARFORMAT**](/windows/win32/api/richedit/ns-richedit-charformata)
</dt> <dt>

[**CHARFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-charformat2a)
</dt> </dl>

 

 





