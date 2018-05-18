---
title: How Automation Compares Strings
description: Describes the string comparison rules applied by Automation.
ms.assetid: '9c2709a8-f726-4bd3-98e0-6db069fb712a'
---

# How Automation Compares Strings

This appendix describes how Automation compares strings. These comparisons are important when creating applications that support national language accents and digraphs. The information in this appendix applies to the following:

-   [**CreateStdDispatch**](createstddispatch.md)

-   [**DispGetIDsOfNames**](dispgetidsofnames.md)

-   [**ITypeLib::FindName**](itypelib-findname.md)

-   [**IDispatch::GetIDsOfNames**](idispatch-getidsofnames.md)

-   Using MIDL

When comparing strings, Automation components use the following rules:

-   Comparisons are sensitive to locale, based on the string's locale identifier (LCID). A string must have an LCID that is supported by the application or type library. For more information about locales and LCIDs, see [Locales](https://msdn.microsoft.com/library/windows/desktop/dd318716) and [Language Identifier Constants and Strings](https://msdn.microsoft.com/library/windows/desktop/dd318693).

-   Accent characters are ignored. For example, the "á" string compares the same as "a".

-   Case is ignored. For example, the string "A" compares the same as "a".

-   Comparisons are sensitive to digraphs. For example, the "Æ" string is not the same as "AE".

-   For Japanese, Korean, and Chinese locales, [**ITypeLib::FindName**](itypelib-findname.md) and [**IDispatch::GetIDsOfNames**](idispatch-getidsofnames.md) ignore width and kanatype.

## Related topics

<dl> <dt>

[Appendices](appendices.md)
</dt> <dt>

[Automation Programming Reference](automation-programming-reference.md)
</dt> </dl>

 

 




