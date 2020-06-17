---
title: How to Use Font Binding in Rich Edit Controls
description: Microsoft Rich Edit 3.0 assigns a character set to plain-text characters depending on their context.
ms.assetid: 975B9C33-6766-4FF1-A93E-2169C140CEE9
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Font Binding in Rich Edit Controls

Microsoft Rich Edit 3.0 assigns a character set to plain-text characters depending on their context. Some examples are:

-   Greek characters are assigned **GREEK\_CHARSET**.
-   Hangul symbols are assigned **HANGUL\_CHARSET**.
-   Chinese characters are assigned **SHIFTJIS\_CHARSET** if kana characters are found nearby, or **GB2312\_CHARSET** if no kana are found nearby.
-   Non-neutral ANSI characters are assigned **ANSI\_CHARSET** in any event.

> [!Note]  
> The rich edit control uses Unicode internally, so this use of character sets differs from the original one used in font specifications. But the [**CHARFORMAT**](/windows/win32/api/richedit/ns-richedit-charformata) structure has a well-defined place for the character set.

 

Neutral characters like blanks and digits are assigned a character set depending on their context. For example, a blank surrounded by characters of the same character set gets that character set. Neutrals and digits used for bidirectional text are assigned character sets in a way that is based on the Unicode bidirectional algorithm.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use Font Binding in a Rich Edit Control

After character sets are assigned, Rich Edit scans the text around the insertion point forward and backward to find the nearest fonts that have been used for the character sets. If no font is found for a character set, Rich Edit uses the font chosen by the client for that character set. If the client hasn't specified a font for the character set, Rich Edit uses the default font for that character set. If the client wants some other font, the client can always change it, but this approach will work most of the time. The current default font choices are based on the following table. Note that the default fonts are set per-process, and there are separate lists for UI usage and for non-UI usage.



| Language                    | UI font name  | UI font size | non-UI font name | non-UI font size |
|-----------------------------|---------------|--------------|------------------|------------------|
| Western, CE, ME, Vietnamese | Tahoma        | 8            | Arial            | 10               |
| Japanese                    | MS UI Gothic  | 9            | MS P Gothic      | 10               |
| Korean                      | Gulim         | 9            | Gulim            | 9                |
| Simplified Chinese          | Simsun        | 9            | SimSun           | 10               |
| Traditional Chinese         | PMingLiU      | 9            | PMingLiU         | 9                |
| Thai                        | MS Sans Serif | 8            | Tahoma           | 14               |
| Symbols                     | Wingdings     | 8            | Wingdings        | 10               |
| Devanagari                  | Mangal        | 8            | Mangal           | 10               |
| Tamil                       | Latha         | 8            | Latha            | 10               |
| Georgian, Armenian          | Arial Unicode | 8            | Arial Unicode    | 10               |



 

Therefore, in the default font-binding table (entries have a character set, font name, and size), Rich Edit allows ANSI\_CHARSET to match several character sets, while the appropriate character set matches other fonts on a one-to-one basis. More precisely, rich edit uses the ANSI\_CHARSET choice whenever no other alternative is found. You will be able to specify a finer granularity than this; for example, assign a specific ARABIC\_CHARSET for Arabic runs, a specific Greek font for Greek runs, and so on. This finer granularity will also be used if a font with the desired character set stamp is found somewhere in the document before the area that is being font-bound.

Note that Rich Edit does not currently handle a missing glyph in a font that claims to support a character set but is incomplete. At display time in a complex script, Rich Edit does end up knowing that such a glyph is missing, but it does not cause the backing store to use a new font. Normally, the underlying font linking of the operating system will accomplish this.

## Remarks

**Rich Edit 4.1:** To set the default font for a script, call [**EM\_SETCHARFORMAT**](em-setcharformat.md) with [**CHARFORMAT2**](/windows/desktop/api/Richedit/ns-richedit-charformat2a), specifying values for the **yHeight**, **bCharSet**, **bPitchAndFamily**, **szFaceName**, and **lcid** members. Also, to get the default font for a specific code page, call [**EM\_GETCHARFORMAT**](em-getcharformat.md) with **CHARFORMAT2**, specifying values for the **bCharSet** and **lcid** members.

## Related topics

<dl> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




