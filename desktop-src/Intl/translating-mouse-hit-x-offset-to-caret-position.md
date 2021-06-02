---
description: Conventionally, the user can select caret position (cp) by clicking either the trailing half of character &\#0034;cp-1&\#0034; or the leading half of character &\#0034;cp&\#0034;.
ms.assetid: 36b6ff00-7ea8-40e5-90f7-917cef117d4a
title: Translating Mouse Hit X Offset to Caret Position
ms.topic: article
ms.date: 05/31/2018
---

# Translating Mouse Hit X Offset to Caret Position

Conventionally, the user can select caret position (cp) by clicking either the trailing half of character "cp-1" or the leading half of character "cp". An application can implement the translation of mouse hit x offset to caret position as follows:


```C++
int iCharPos;
int iCaretPos;
int fTrailing;
ScriptXtoCP(iMouseX, cChars, cGlyphs, pwLogClust, psva, piAdvance, psa,
            &iCharPos, &fTrailing);
iCaretPos = iCharPos + fTrailing;
```



For scripts that snap the caret to cluster boundaries, a call to [**ScriptXtoCP**](/windows/desktop/api/Usp10/nf-usp10-scriptxtocp) returns with *fTrailing* set to either 0 or the width of the cluster in code points.

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 



