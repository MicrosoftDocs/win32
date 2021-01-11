---
description: These values are used with the ImmGetConversionStatus and ImmSetConversionStatus functions.
ms.assetid: 24b12936-7dfc-4c8d-970c-d8354ad46d1d
title: IME Sentence Mode Values
ms.topic: article
ms.date: 05/31/2018
---

# IME Sentence Mode Values

These values are used with the [**ImmGetConversionStatus**](/windows/desktop/api/Imm/nf-imm-immgetconversionstatus) and [**ImmSetConversionStatus**](/windows/desktop/api/Imm/nf-imm-immsetconversionstatus) functions.



| Constant                  | Definition                                                                 |
|---------------------------|----------------------------------------------------------------------------|
| IME\_SMODE\_AUTOMATIC     | The IME carries out conversion processing in automatic mode.               |
| IME\_SMODE\_NONE          | No information for sentence.                                               |
| IME\_SMODE\_PHRASEPREDICT | The IME uses phrase information to predict the next character.             |
| IME\_SMODE\_PLURALCLAUSE  | The IME uses plural clause information to carry out conversion processing. |
| IME\_SMODE\_SINGLECONVERT | The IME carries out conversion processing in single-character mode.        |
| IME\_SMODE\_CONVERSATION  | The IME uses conversation mode. This is useful for chat applications.      |



 

Bits 16 through 31 are reserved for IME use.

 

 



