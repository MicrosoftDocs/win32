---
description: End-user-defined characters (EUDC) in double-byte character sets (DBCSs) and private use area (PUA) characters in Unicode are custom characters.
ms.assetid: e76ea1ed-5962-440a-a722-b59b314babd6
title: End-User-Defined and Private Use Area Characters
ms.topic: article
ms.date: 05/31/2018
---

# End-User-Defined and Private Use Area Characters

End-user-defined characters (EUDC) in [double-byte character sets](double-byte-character-sets.md) (DBCSs) and private use area (PUA) characters in [Unicode](unicode.md) are custom characters. They can be defined and implemented either by an end user or by another party, such as an equipment manufacturer, a user group, a government body, or a font design company. Their use enables users to form names and other words using characters that are not available in standard screen and printer fonts.

The EUDC and PUA characters can be assigned differently, or not assigned at all, on different computers. Some code pages have extensions that reuse the EUDC range, and these extensions can conflict with each other. In other cases, a manufacturer might provide a custom set of characters in one of these ranges. Additionally, user groups can attempt to provide additional characters in the PUA. Different combinations of these cases can cause conflict. When creating applications that rely on EUDC or PUA characters, you should keep in mind the conflicting interpretations of an individual code point.

The following topics discuss the fonts that support EUDCs, and access and management for these characters:

-   [Character Sets and Fonts](character-sets-and-fonts.md)
-   [EUDC Registry Entries](eudc-registry-entries.md)

## Related topics

<dl> <dt>

[About Unicode and Character Sets](about-unicode-and-character-sets.md)
</dt> </dl>

 

 



