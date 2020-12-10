---
title: EM_GETIMEPROPERTY message (Richedit.h)
description: Retrieves the property and capabilities of the Input Method Editor (IME) associated with the current input locale.
ms.assetid: 0cbe52d4-c3e7-40bd-a6f6-da0a11056976
keywords:
- EM_GETIMEPROPERTY message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETIMEPROPERTY
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETIMEPROPERTY message

Retrieves the property and capabilities of the Input Method Editor (IME) associated with the current input locale.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the type of property information to retrieve. This parameter can be one of the following values.



| Value                                                                                                                                                                     | Meaning                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <span id="IGP_PROPERTY"></span><span id="igp_property"></span><dl> <dt>**IGP\_PROPERTY**</dt> </dl>                | Property information.<br/>                                                         |
| <span id="IGP_CONVERSION"></span><span id="igp_conversion"></span><dl> <dt>**IGP\_CONVERSION**</dt> </dl>          | Conversion capabilities. <br/>                                                     |
| <span id="IGP_SENTENCE"></span><span id="igp_sentence"></span><dl> <dt>**IGP\_SENTENCE**</dt> </dl>                | Sentence mode capabilities. <br/>                                                  |
| <span id="IGP_UI"></span><span id="igp_ui"></span><dl> <dt>**IGP\_UI**</dt> </dl>                                  | User interface capabilities. <br/>                                                 |
| <span id="IGP_SETCOMPSTR"></span><span id="igp_setcompstr"></span><dl> <dt>**IGP\_SETCOMPSTR**</dt> </dl>          | Composition string capabilities. <br/>                                             |
| <span id="IGP_SELECT"></span><span id="igp_select"></span><dl> <dt>**IGP\_SELECT**</dt> </dl>                      | Selection inheritance capabilities. <br/>                                          |
| <span id="IGP_GETIMEVERSION"></span><span id="igp_getimeversion"></span><dl> <dt>**IGP\_GETIMEVERSION**</dt> </dl> | Retrieves the system version number for which the specified IME was created. <br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

Returns the property or capability value, depending on the value of the *lParam* parameter. For more information, see the Remarks.

## Remarks

If *wParam* is IGP\_PROPERTY, it returns one or more of the following values.



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IME\_PROP\_AT\_CARET                | If set, conversion window is at the caret position. If clear, the window is near caret position.                                                                                                                                                                  |
| IME\_PROP\_SPECIAL\_UI              | If set, IME has a nonstandard user interface. The application should not draw in the IME window.                                                                                                                                                                  |
| IME\_PROP\_CANDLIST\_START\_FROM\_1 | If set, strings in the candidate list are numbered starting at 1. If clear, strings start at zero.                                                                                                                                                                |
| IME\_PROP\_UNICODE                  | If set, the IME is viewed as a UnicodeIME. The system and the IME will communicate through the UnicodeIME interface. If clear, IME will use the ANSI interface to communicate with the system.                                                                    |
| IME\_PROP\_COMPLETE\_ON\_UNSELECT   | If set, conversion window is at the caret position. If clear, the window is near caret position.                                                                                                                                                                  |
| IME\_PROP\_ACCEPT\_WIDE\_VKEY       | If set, the IME processes the injected Unicode that came from the [**SendInput**](/windows/desktop/api/winuser/nf-winuser-sendinput) function by using VK\_PACKET. If clear, the IME might not process the injected Unicode, and the injected Unicode might be sent to the application directly. |



 

If *wParam* is IGP\_UI, it returns one or more of the following values.



| Requirement | Value |
|-----------------|-------------------------------------------------------------------------------------------------------|
| UI\_CAP\_2700   | Supports text escapement values of 0 or 2700. For more information, see **lfEscapement**.             |
| UI\_CAP\_ROT90  | Supports text escapement values of 0, 900, 1800, or 2700. For more information, see **lfEscapement**. |
| UI\_CAP\_ROTANY | Supports any text escapement value. For more information, see **lfEscapement**.                       |



 

If *wParam* is IGP\_SETCOMPSTR, it returns one or more of the following values.



| Requirement | Value |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCS\_CAP\_COMPSTR            | Can create the composition string by calling the [**ImmSetCompositionString**](/windows/desktop/api/imm/nf-imm-immsetcompositionstringa) function with the SCS\_SETSTR value.                                                      |
| SCS\_CAP\_MAKEREAD           | Can create the reading string from corresponding composition string when using the [**ImmSetCompositionString**](/windows/desktop/api/imm/nf-imm-immsetcompositionstringa) function with SCS\_SETSTR and without setting *lpRead*. |
| SCS\_CAP\_SETRECONVERTSTRING | This IME can support reconversion. Use [**ImmSetCompositionString**](/windows/desktop/api/imm/nf-imm-immsetcompositionstringa) to do the reconversion.                                                                             |



 

If *wParam* is IGP\_SELECT, it returns one or more of the following values.



| Requirement | Value |
|-----------------------|------------------------------------------------------|
| SELECT\_CAP\_CONVMODE | Inherits conversion mode when a new IME is selected. |
| SELECT\_CAP\_SENTENCE | Inherits sentence mode when a new IME is selected.   |



 

If *wParam* is IGP\_GETIMEVERSION, it returns one or more of the following values.



| Requirement | Value |
|--------------|---------------------------------------------|
| IMEVER\_0310 | The IME was created for Windows 3.1.        |
| IMEVER\_0400 | The IME was created for Windows 95 or later |



 

This message is similar to [**ImmGetProperty**](/windows/desktop/api/imm/nf-imm-immgetproperty), except that it uses the current input locale. The application should call [**EM\_ISIME**](em-isime.md) before calling this function.

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

[**EM\_ISIME**](em-isime.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**ImmGetProperty**](/windows/desktop/api/imm/nf-imm-immgetproperty)
</dt> </dl>

 

