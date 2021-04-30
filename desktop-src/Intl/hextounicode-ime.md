---
description: Rich Edit 3.0 supports the HexToUnicode IME, which allows a user to convert between hexadecimal and Unicode characters by using hot keys in one of two ways.
ms.assetid: 4b8c4de4-9c1c-459c-a640-367e86a9b9cc
title: HexToUnicode IME
ms.topic: article
ms.date: 05/31/2018
---

# HexToUnicode IME

Rich Edit 3.0 supports the HexToUnicode IME, which allows a user to convert between hexadecimal and Unicode characters by using hot keys in one of two ways.

Using the first conversion method, the user types the character code in hexadecimal and then enters ALT+X. The IME replaces the hexadecimal digits preceding the insertion point with the Unicode character. If the current font does not support the character code, an appropriate font is chosen that does support it. To convert from Unicode to hexadecimal, the user enters SHIFT+ALT+X. This entry replaces the Unicode character that precedes the insertion point with the hexadecimal digits. In particular, this method allows the user to determine the character that is indicated by a "missing glyph" indicator. If the hexadecimal character code immediately follows some legitimate (noncharacter) hexadecimal characters, the user selects the specific digits to convert before typing ALT+X. A problem with this first method is that ALT+X is sometimes used as a key combination for the exit command (that is, eXit). For example, in Microsoft Office, this command only appears as an option of the **File** menu.

The second method of converting between hexadecimal and Unicode characters involves the number pad. Using this method, the user types ALT+NumPad numbers (with values greater than 255) to enter Unicode characters using decimal values. This method is not as useful as the first because the user cannot see what hexadecimal digits have been typed. Also, the user cannot correct the hexadecimal digits except by re-entering all the digits.

## Related topics

<dl> <dt>

[About Input Method Manager](about-input-method-manager.md)
</dt> </dl>

 

 



