---
description: The composition string is the current text in the composition window.
ms.assetid: ab226567-f68d-4fa4-9ead-e9bfabde927e
title: Composition String
ms.topic: article
ms.date: 05/31/2018
---

# Composition String

The composition string is the current text in the composition window. This is the text that the IME converts to final characters. Each composition string consists of one or more "clauses". A clause is the smallest combination of characters that the IME can convert to a final character. To get and set the composition string, the application calls the [**ImmGetCompositionString**](/windows/desktop/api/Imm/nf-imm-immgetcompositionstringa) and [**ImmSetCompositionString**](/windows/desktop/api/Imm/nf-imm-immsetcompositionstringa) functions, respectively.

As the user enters text in the composition window, the IME tracks the status of the composition string. This status includes attribute information, clause information, typing information, and cursor position. The application can retrieve the composition status by using the [**ImmGetCompositionString**](/windows/desktop/api/Imm/nf-imm-immgetcompositionstringa) function.

Attribute information is rendered in an array of 8-bit values that specifies the status of characters in the composition string. All characters of one clause must have the same attribute. The array includes one value for each byte in the string, including one byte each for the lead and second bytes of any double-byte characters in the string. For each value in the array, bits 0 through 3 can be one combination of the following values.



| Value                      | Meaning                                                                                                   |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| ATTR\_INPUT                | Character being entered by the user. The IME has yet to convert this character.                           |
| ATTR\_INPUT\_ERROR         | An error character that the IME cannot convert. For example, the IME cannot put together some consonants. |
| ATTR\_TARGET\_CONVERTED    | Character selected by the user and then converted by the IME.                                             |
| ATTR\_CONVERTED            | Character that the IME has already converted.                                                             |
| ATTR\_TARGET\_NOTCONVERTED | Character being converted. The user has selected this character but the IME has not yet converted it.     |
| ATTR\_FIXEDCONVERTED       | Characters that the IME will no longer convert.                                                           |



 

All other values are reserved. In Japanese, any unconverted character having the ATTR\_INPUT attribute is a hiragana, katakana, or alphanumeric character. In Korean, this attribute represents a Hangul character that the IME has not yet converted. In Traditional Chinese and Simplified Chinese, each IME can limit its character within some range.

The clause information included in the composition string status is an array of 32-bit values that specifies the positions of the clauses in the composition string. The array includes one value for each clause and a final value that specifies the length of the full string. Each value in the array specifies the offset, in bytes, from the beginning of the string to the clause. The first value is always 0 because the first clause always starts at the beginning of the string. For example, if a string has two clauses, the clause information has three values: the first value is 0, the second value is the offset of the second clause, and the third value is the length of the string. For Unicode, the position of a clause is counted in Unicode characters, and the length of a string is the size in Unicode characters.

The typing information included in the composition string status is a null-terminated character string representing the characters that the user enters at the keyboard.

The cursor position included in the composition string status is a value indicating the position of the cursor relative to the characters in the composition string. The value is the offset, in bytes, from the beginning of the string. If this value is 0, the cursor is immediately before the first character in the string. If the value is equal to the length of the string, the cursor is immediately after the last character. If the value is 1, the cursor is not present. For Unicode, both position and length are measured in Unicode characters.

Your application can set the composition string or elements of the composition status by using the [**ImmSetCompositionString**](/windows/desktop/api/Imm/nf-imm-immsetcompositionstringa) function. To ensure that the composition window updates its appearance based on these changes, the function allows the application to send a notification message to the window. Applications that set a combination of composition status elements typically disable notifications for all but the last call to this function so that only one notification message is generated for the composition window.

Finally, the edit control supports two messages for changing the handling of composition strings by the IME. For more information, see [**EM\_GETIMESTATUS**](../controls/em-getimestatus.md) and [**EM\_SETIMESTATUS**](../controls/em-setimestatus.md). For more information on the edit control, see [Edit Control](../controls/edit-controls.md).

## Related topics

<dl> <dt>

[About Input Method Manager](about-input-method-manager.md)
</dt> </dl>

 

 
