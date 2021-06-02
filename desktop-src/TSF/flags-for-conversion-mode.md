---
title: Flags for Conversion Mode (Ctffunc.h)
description: The following flags are used as a value of GUID\_COMPARTMENT\_KEYBOARD\_INPUTMODE\_CONVERSION. This is equivalent with IME\_CMODE values for IMM32.
ms.assetid: 6e545af5-5fdb-49de-b24e-aaee82b51326
keywords:
- Flags for Conversion Mode Text Services Framework
topic_type:
- apiref
api_name:
- Flags for Conversion Mode
api_location:
- Ctffunc.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Flags for Conversion Mode

The following flags are used as a value of [GUID\_COMPARTMENT\_KEYBOARD\_INPUTMODE\_CONVERSION](predefined-compartments.md). This is equivalent with [IME\_CMODE](../intl/ime-conversion-mode-values.md) values for IMM32.



| Flag                             | Value  | Description                                                     |
|----------------------------------|--------|-----------------------------------------------------------------|
| TF\_CONVERSIONMODE\_ALPHANUMERIC | 0x0000 | Set to 1 if ALPHANUMERIC mode.                                  |
| TF\_CONVERSIONMODE\_NATIVE       | 0x0001 | Set to 1 if NATIVE mode; 0 if ALPHANUMERIC mode.                |
| TF\_CONVERSIONMODE\_KATAKANA     | 0x0002 | Set to 1 if KATAKANA mode; 0 if HIRAGANA mode.                  |
| TF\_CONVERSIONMODE\_FULLSHAPE    | 0x0008 | Set to 1 if full shape mode; 0 if half shape mode.              |
| TF\_CONVERSIONMODE\_ROMAN        | 0x0010 | Set to 1 to prevent processing of conversions by IME; 0 if not. |
| TF\_CONVERSIONMODE\_CHARCODE     | 0x0020 | Set to 1 if character code input mode; 0 if not.                |
| TF\_CONVERSIONMODE\_SOFTKEYBOARD | 0x0080 | Set to 1 if Soft Keyboard mode; 0 if not.                       |
| TF\_CONVERSIONMODE\_NOCONVERSION | 0x0100 | Set to 1 to prevent processing of conversions by IME; 0 if not. |
| TF\_CONVERSIONMODE\_SYMBOL       | 0x0400 | Set to 1 if SYMBOL conversion mode; 0 if not.                   |
| TF\_CONVERSIONMODE\_FIXED        | 0x0800 | Set to 1 if fixed conversion mode; 0 if not.                    |



 

The following values are used as a value of [GUID\_COMPARTMENT\_KEYBOARD\_INPUTMODE\_SENTENCE](predefined-compartments.md). This is equivalent with [IME\_SMODE](../intl/ime-composition-string-values.md) values for IMM32.



| Flag                            | Value  | Description                                                                |
|---------------------------------|--------|----------------------------------------------------------------------------|
| TF\_SENTENCEMODE\_NONE          | 0x0000 | No information for sentence.                                               |
| TF\_SENTENCEMODE\_PLAURALCLAUSE | 0x0001 | The IME uses plural clause information to carry out conversion processing. |
| TF\_SENTENCEMODE\_SINGLECONVERT | 0x0002 | The IME carries out conversion processing in single-character mode.        |
| TF\_SENTENCEMODE\_AUTOMATIC     | 0x0004 | The IME carries out conversion processing in automatic mode.               |
| TF\_SENTENCEMODE\_PHRASEPREDICT | 0x0008 | The IME uses phrase information to predict the next character.             |
| TF\_SENTENCEMODE\_CONVERSATION  | 0x0010 | The IME uses conversation mode. This is useful for chat applications.      |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 onWindows NT 4.0,Windows 2000 ProfessionalandWindows MeWindows 98<br/>   |
| Header<br/>                   | <dl> <dt>Ctffunc.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Ctffunc.idl</dt> </dl> |



## See also

<dl> <dt>

[Predefined Compartments](predefined-compartments.md)
</dt> </dl>

 

