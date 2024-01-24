---
title: EM_GETLANGOPTIONS message (Richedit.h)
description: Gets a rich edit control's option settings for Input Method Editor (IME) and Asian language support.
ms.assetid: 9fd9d27c-7713-454e-b49f-8ecdba848d2e
keywords:
- EM_GETLANGOPTIONS message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETLANGOPTIONS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETLANGOPTIONS message

Gets a rich edit control's option settings for Input Method Editor (IME) and Asian language support.

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

Returns the IME and Asian language settings, which can be zero or more of the following values.



| Return code                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**IMF\_AUTOFONT**</dt> </dl>                    | If this flag is set, the control automatically changes fonts when the user explicitly changes to a different keyboard layout. It is useful to turn off **IMF\_AUTOFONT** for universal Unicode fonts. This option is turned on by default (1).<br/>                                                                                                                                                                     |
| <dl> <dt>**IMF\_AUTOFONTSIZEADJUST**</dt> </dl>          | If this flag is set, the control scales font-bound font sizes from insertion point size according to script. For example, Asian fonts are slightly larger than Western ones. This option is turned on by default (1).<br/>                                                                                                                                                                                              |
| <dl> <dt>**IMF\_AUTOKEYBOARD**</dt> </dl>                | If this flag is set, the control automatically changes the keyboard layout when the user explicitly changes to a different font, or when the user explicitly changes the insertion point to a new location in the text. Will be turned on automatically for bidirectional controls. For all other controls, it is turned off by default. This option is turned off by default (0).<br/>                                 |
| <dl> <dt>**IMF\_DISABLEAUTOBIDIAUTOKEYBOARD**</dt> </dl> | **Windows 8**: If this flag is set, the control uses language neutral logic for automatic keyboard switching. This option is turned off by default (0).<br/>                                                                                                                                                                                                                                                            |
| <dl> <dt>**IMF\_DUALFONT**</dt> </dl>                    | If this flag is set, the control uses dual-font mode. Used for Asian language support. The control uses an English font for ASCII text and a Asian font for Asian text. This option is turned on by default (1).<br/>                                                                                                                                                                                                   |
| <dl> <dt>**IMF\_IMEALWAYSSENDNOTIFY**</dt> </dl>         | This flag controls how the rich edit control notifies the client during IME composition: <br/> 0: No [EN\_CHANGE](en-change.md) or [EN\_SELCHANGE](en-selchange.md) notifications during undetermined state. Send notification when the final string comes in. This is the default.<br/> 1: Send [EN\_CHANGE](en-change.md) and [EN\_SELCHANGE](en-selchange.md) events during undetermined state.<br/> |
| <dl> <dt>**IMF\_IMECANCELCOMPLETE**</dt> </dl>           | This flag determines how the control uses the composition string of an IME if the user cancels it. If this flag is set, the control discards the composition string. If this flag is not set, the control uses the composition string as the result string. This option is turned off by default (0).<br/>                                                                                                              |
| <dl> <dt>**IMF\_NOIMPLICITLANG**</dt> </dl>              | **Windows 8**: If this flag is set, disable stamping keyboard input with the keyboard language and ensuring that non-East Asian language IDss are compatible with the character repertoire. This option is turned off by default (0). <br/>                                                                                                                                                                             |
| <dl> <dt>**IMF\_NOKBDLIDFIXUP**</dt> </dl>               | **Windows 8**: If this flag is set, the rich edit control disables stamping keyboard language on an empty control. This option is turned off by default (0).<br/>                                                                                                                                                                                                                                                       |
| <dl> <dt>**IMF\_SPELLCHECKING**</dt> </dl>               | **Windows 8**: If this flag is set, the rich edit control turns on spell checking. This option is turned off by default (0). <br/>                                                                                                                                                                                                                                                                                      |
| <dl> <dt>**IMF\_TKBAUTOCORRECTION**</dt> </dl>           | **Windows 8**: If this flag is set, enable touch keyboard autocorrect. This option is turned off by default (0). <br/>                                                                                                                                                                                                                                                                                                  |
| <dl> <dt>**IMF\_TKBPREDICTION**</dt> </dl>               | **Windows 10**: Ignored.<br/> **Windows 8**: If this flag is set, the rich edit control enables touch keyboard prediction. This option is turned off by default (0). <br/>                                                                                                                                                                                                                                        |
| <dl> <dt>**IMF\_UIFONTS**</dt> </dl>                     | Use user-interface default fonts. This option is turned off by default (0).<br/>                                                                                                                                                                                                                                                                                                                                        |



 

## Remarks

The **IMF\_AUTOFONT** flag is set by default. The **IMF\_AUTOKEYBOARD** and **IMF\_IMECANCELCOMPLETE** flags are cleared by default.

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

[**EM\_SETLANGOPTIONS**](em-setlangoptions.md)
</dt> <dt>

[**EM\_SETLIMITTEXT**](em-setlimittext.md)
</dt> </dl>

 

 





