---
title: EM_GETEDITSTYLE message (Richedit.h)
description: Retrieves the current edit style flags.
ms.assetid: 568e51a4-0767-4a59-bf34-bc0281b5fe65
keywords:
- EM_GETEDITSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETEDITSTYLE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETEDITSTYLE message

Retrieves the current edit style flags.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

Returns the current edit style flags, which can include one or more of the following values:




| Return code | Description | 
|-------------|-------------|
| <dl><dt><strong>SES_BEEPONMAXTEXT</strong></dt></dl> | Rich Edit will call the system beeper if the user attempts to enter more than the maximum characters.<br /> | 
| <dl><dt><strong>SES_BIDI</strong></dt></dl> | Turns on bidirectional processing. This is automatically turned on by Rich Edit if any of the following window styles are active: <a href="/windows/desktop/winmsg/extended-window-styles"><strong>WS_EX_RIGHT</strong></a>, <a href="/windows/desktop/winmsg/extended-window-styles"><strong>WS_EX_RTLREADING</strong></a>, <a href="/windows/desktop/winmsg/extended-window-styles"><strong>WS_EX_LEFTSCROLLBAR</strong></a>. However, this setting is useful for handling these window styles when using a custom implementation of <a href="/windows/desktop/api/Textserv/nl-textserv-itexthost"><strong>ITextHost</strong></a> (default: 0).<br /> | 
| <dl><dt><strong>SES_CTFALLOWEMBED</strong></dt></dl> | <strong>Windows XP with SP1</strong>: Allow embedded objects to be inserted using TSF (default: 0).<br /> | 
| <dl><dt><strong>SES_CTFALLOWPROOFING</strong></dt></dl> | <strong>Windows XP with SP1</strong>: Allows TSF proofing tips (default: 0).<br /> | 
| <dl><dt><strong>SES_CTFALLOWSMARTTAG</strong></dt></dl> | <strong>Windows XP with SP1</strong>: Allows TSF SmartTag tips (default: 0).<br /> | 
| <dl><dt><strong>SES_CTFNOLOCK</strong></dt></dl> | <strong>Windows 8</strong>: Do not allow the TSF lock read/write access. This pauses TSF input. <br /> | 
| <dl><dt><strong>SES_DEFAULTLATINLIGA</strong></dt></dl> | <strong>Windows 8</strong>: Fonts with an fi ligature are displayed with default OpenType features resulting in improved typography (default: 0). <br /> | 
| <dl><dt><strong>SES_DRAFTMODE</strong></dt></dl> | <strong>Windows XP with SP1</strong>: Use draft mode fonts to display text. Draft mode is an accessibility option where the control displays the text with a single font; the font is determined by the system setting for the font used in message boxes. For example, accessible users may read text easier if it is uniform, rather than a mix of fonts and styles (default: 0). <br /> | 
| <dl><dt><strong>SES_EMULATE10</strong></dt></dl> | <strong>Windows 8</strong>: Emulate RichEdit 1.0 behavior. <br /><blockquote>[!Note]<br />If you really want this behavior, use the Windows riched32.dll instead of riched20.dll or msftedit.dll. Riched32.dll had more functionality.</blockquote><br /> | 
| <dl><dt><strong>SES_EMULATESYSEDIT</strong></dt></dl> | When this bit is on, rich edit attempts to emulate the system edit control (default: 0).<br /> | 
| <dl><dt><strong>SES_EXTENDBACKCOLOR</strong></dt></dl> | Extends the background color all the way to the edges of the client rectangle (default: 0).<br /> | 
| <dl><dt><strong>SES_HIDEGRIDLINES</strong></dt></dl> | <strong>Windows XP with SP1</strong>: If the width of table gridlines is zero, gridlines are not displayed. This is equivalent to the hide gridlines feature in Word's table menu (default: 0).<br /> | 
| <dl><dt><strong>SES_HYPERLINKTOOLTIPS</strong></dt></dl> | <strong>Windows 8</strong>: When the cursor is over a link, display a tooltip with the target link address (default: 0). <br /> | 
| <dl><dt><strong>SES_LOGICALCARET</strong></dt></dl> | <strong>Windows 8</strong>: Provide logical caret information instead of a caret bitmap as described in <a href="/windows/desktop/api/Textserv/nf-textserv-itexthost-txsetcaretpos"><strong>ITextHost::TxSetCaretPos</strong></a> (default: 0). <br /> | 
| <dl><dt><strong>SES_LOWERCASE</strong></dt></dl> | Converts all input characters to lowercase (default: 0).<br /> | 
| <dl><dt><strong>SES_MAPCPS</strong></dt></dl> | Obsolete. Do not use.<br /> | 
| <dl><dt><strong>SES_MULTISELECT</strong></dt></dl> | <strong>Windows 8</strong>: Enable multiselection with individual mouse selections made while the Ctrl key is pressed (default: 0). <br /> | 
| <dl><dt><strong>SES_NOEALINEHEIGHTADJUST</strong></dt></dl> | <strong>Windows 8</strong>: Do not adjust line height for East Asian text (default: 0 which adjusts the line height by 15%). <br /> | 
| <dl><dt><strong>SES_NOFOCUSLINKNOTIFY</strong></dt></dl> | Sends <a href="en-link.md">EN_LINK</a> notification from links that do not have focus.<br /> | 
| <dl><dt><strong>SES_NOIME</strong></dt></dl> | Disallows IMEs for this instance of the rich edit control (default: 0).<br /> | 
| <dl><dt><strong>SES_NOINPUTSEQUENCECHK</strong></dt></dl> | When this bit is on, rich edit does not verify the sequence of typed text. Some languages (such as Thai and Vietnamese) require verifying the input sequence order before submitting it to the backing store (default: 0).<br /> | 
| <dl><dt><strong>SES_SCROLLONKILLFOCUS</strong></dt></dl> | When KillFocus occurs, scroll to the beginning of the text (character position equal to 0) (default: 0).<br /> | 
| <dl><dt><strong>SES_SMARTDRAGDROP</strong></dt></dl> | <strong>Windows 8</strong>: Add or delete a space according to the context when dropping text (default: 0). <br /> | 
| <dl><dt><strong>SES_USECRLF</strong></dt></dl> | Obsolete. Do not use.<br /> | 
| <dl><dt><strong>SES_WORDDRAGDROP</strong></dt></dl> | <strong>Windows 8</strong>: If word select is active, ensure that the drop location is at a word boundary (default: 0). <br /> | 
| <dl><dt><strong>SES_UPPERCASE</strong></dt></dl> | Converts all input characters to uppercase (default: 0).<br /> | 
| <dl><dt><strong>SES_USEAIMM</strong></dt></dl> | Uses the Active IMM input method component that ships with Internet Explorer 4.0 or later (default: 0).<br /> | 
| <dl><dt><strong>SES_USEATFONT</strong></dt></dl> | <strong>Windows XP with SP1</strong>: Uses an @ font, which is designed for vertical text; this is used with the <a href="rich-edit-control-styles.md"><strong>ES_VERTICAL</strong></a> window style. The name of an @ font begins with the @ symbol, for example, "@Batang" (default: 0, but is automatically turned on for vertical text layout). <br /> | 
| <dl><dt><strong>SES_USECTF</strong></dt></dl> | <strong>Windows XP with SP1</strong>: Turns on TSF support. (default: 0)<br /> | 
| <dl><dt><strong>SES_XLTCRCRLFTOCR</strong></dt></dl> | Turns on translation of CRCRLFs to CRs. When this bit is on and a file is read in, all instances of CRCRLF will be converted to hard CRs internally. This will affect the text wrapping. Note that if such a file is saved as plain text, the CRs will be replaced by CRLFs. This is the .txt standard for plain text (default: 0, which deletes CRCRLFs on input). <br /> | 




 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Rich Edit 3.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETEDITSTYLE**](em-seteditstyle.md)
</dt> </dl>

 

