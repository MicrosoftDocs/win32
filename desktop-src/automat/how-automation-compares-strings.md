---
title: How Automation Compares Strings
description: Describes the string comparison rules applied by Automation.
ms.assetid: 9c2709a8-f726-4bd3-98e0-6db069fb712a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How Automation Compares Strings

This appendix describes how Automation compares strings. These comparisons are important when creating applications that support national language accents and digraphs. The information in this appendix applies to the following:

-   [**CreateStdDispatch**](/windows/previous-versions/OleAuto/nf-oleauto-createstddispatch?branch=master)

-   [**DispGetIDsOfNames**](/windows/previous-versions/OleAuto/nf-oleauto-dispgetidsofnames?branch=master)

-   [**ITypeLib::FindName**](/windows/previous-versions/oaidl/nf-oaidl-itypelib-findname?branch=master)

-   [**IDispatch::GetIDsOfNames**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-getidsofnames?branch=master)

-   Using MIDL

When comparing strings, Automation components use the following rules:

-   Comparisons are sensitive to locale, based on the string's locale identifier (LCID). A string must have an LCID that is supported by the application or type library. For more information about locales and LCIDs, see [Locales](https://msdn.microsoft.com/library/windows/desktop/dd318716) and [Language Identifier Constants and Strings](https://msdn.microsoft.com/library/windows/desktop/dd318693).

-   Accent characters are ignored. For example, the "á" string compares the same as "a".

-   Case is ignored. For example, the string "A" compares the same as "a".

-   Comparisons are sensitive to digraphs. For example, the "Æ" string is not the same as "AE".

-   For Japanese, Korean, and Chinese locales, [**ITypeLib::FindName**](/windows/previous-versions/oaidl/nf-oaidl-itypelib-findname?branch=master) and [**IDispatch::GetIDsOfNames**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-getidsofnames?branch=master) ignore width and kanatype.

## Related topics

<dl> <dt>

[Appendices](appendices.md)
</dt> <dt>

[Automation Programming Reference](automation-programming-reference.md)
</dt> </dl>

 

 




