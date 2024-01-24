---
description: In unidirectional text, the caret position has no ambiguity because the leading edge of a character is at the same place as the trailing edge of the previous character.
ms.assetid: 3bebb329-3dd7-4b2e-8ff3-878aaf337a2c
title: Displaying the Caret in Bidirectional Strings
ms.topic: article
ms.date: 05/31/2018
---

# Displaying the Caret in Bidirectional Strings

In unidirectional text, the caret position has no ambiguity because the leading edge of a character is at the same place as the trailing edge of the previous character. However, in bidirectional text, the caret position between runs of opposing direction is ambiguous. For example, in the left-to-right paragraph "hellosalaam", the last letter of "hello" immediately precedes the first letter of "salaam". The best position in which to display the caret depends on whether it is considered to follow the "o" of "hello" or to precede the "s" of "salaam".

Uniscribe uses the caret positioning conventions shown in the next table.



| Situation       | Visual caret placement                       |
|-----------------|----------------------------------------------|
| Typing          | Trailing edge of last character typed.       |
| Pasting         | Trailing edge of last character pasted.      |
| Caret advancing | Trailing edge of last character passed over. |
| Caret retiring  | Leading edge of last character passed over.  |
| Home            | Leading edge of line.                        |
| End             | Trailing edge of line.                       |



 

The caret can be positioned as shown in the following example:


```C++
if (fAdvancing) {
    ScriptCPtoX(
        iCharPos - 1, TRUE, 
        cChars, cGlyphs, &wLogClust, &sva, &iAdvance, &sa, &iCaretX
        );
} else {
    ScriptCPtoX(
        iCharPos, FALSE, 
        cChars, cGlyphs, &wLogClust, &sva, &iAdvance, &sa, &iCaretX
        );
}
```



Positioning of the caret can be simpler, as shown below, given an *fAdvancing* value restricted to **TRUE** or **FALSE**:


```C++
ScriptCPtoX(
    iCharPos - fAdvancing, fAdvancing, 
    cChars, cGlyphs, &wLogClust, &sva, &iAdvance, &sa, &iCaretX
    );
```



[**ScriptCPtoX**](/windows/desktop/api/Usp10/nf-usp10-scriptcptox) handles out-of-range positions logically. It returns the leading edge of the run for *iCharPos* <0, and the trailing edge of the run for *iCharPos* >= length. For more information, see [Managing Caret Placement and Hit Testing](managing-caret-placement-and-hit-testing.md)

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 



