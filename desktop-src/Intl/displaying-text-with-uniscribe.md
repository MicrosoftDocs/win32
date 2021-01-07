---
description: Your applications can use Uniscribe API functions to support typography and the display and editing of international text. Uniscribe uses the paragraph as the unit for text display, and the Uniscribe functionality must be used for the entire paragraph.
ms.assetid: e1adc567-0445-4deb-8634-25653f82127c
title: Displaying Text with Uniscribe
ms.topic: article
ms.date: 05/31/2018
---

# Displaying Text with Uniscribe

Your applications can use Uniscribe API functions to support typography and the display and editing of international text. Uniscribe uses the paragraph as the unit for text display, and the Uniscribe functionality must be used for the entire paragraph.

When using Uniscribe for display of text, an application must go through a formatting ("layout") process, typically using Uniscribe. The application divides a text paragraph into strings of characters with the same style, called "runs". The style is determined by the particular implementation, but typically includes such attributes as font, size, and color. In defining runs, the application can also apply other information, such as language and locale data maintained for use with lexical tools. For example, an application might treat as a separate run a passage in a primarily English text that is rendered in French.

Once it has determined the runs for all paragraphs, the application divides each paragraph into strings that have the same script and direction ("items"). The application applies the item information to produce runs that are unique in script and direction and fall entirely within a single item ("ranges").

The breakdown of an item into ranges is somewhat arbitrary, although a range should consist of one or more consecutive script-defined, indivisible character groupings, called "clusters." For European languages, a cluster typically corresponds to a single code page character or Unicode code point, and consists of a single [glyph](uniscribe-glossary.md). However, in languages such as Thai, a cluster is a grouping of glyphs and corresponds to multiple consecutive characters or code points. For example, a Thai cluster might contain a consonant, a vowel, and a tone mark. So that it does not break clusters, the application typically should either use the longest ranges it can or use its own lexical information to break between ranges in places that are not in the middle of a cluster.

When it has identified the clusters in each range, the application must determine the size of each cluster. It uses Uniscribe to sum the clusters to determine the size of each range. Then the application sums the sizes of the ranges until they overflow a line, that is, reach the margin. The range that overflows the line is divided between the current line and the next line. For each line, the application builds a map from visual position to logical position for each range. Then the application shapes the code points for each range into glyphs, which it can subsequently position and render.

An application does text layout only one time. Afterwards, it either saves the glyphs and positions for display purposes or it generates them each time it displays the text, with the tradeoff being speed versus memory. A typical application implements the layout process once, then generates the glyphs and positions each time it displays the text.

An application that uses [complex scripts](uniscribe-glossary.md) has the following problems with a simple approach to layout and display.

-   The width of a complex script character depends on its context. It is not possible to save the widths in simple tables.
-   Breaking between words in scripts such as Thai requires dictionary support. For example, no separator character is used between Thai words.
-   Arabic, Hebrew, Persian, Urdu, and other [bidirectional text](uniscribe-glossary.md) languages require reordering before display.
-   Some form of font association is often required to easily use complex scripts.

The fact that Uniscribe uses the paragraph as the display unit helps the application deal adequately with these complex script issues.

> [!Note]  
> Uniscribe must be used for an entire paragraph, even if sections of the paragraph are not complex scripts.

 

As shown in the following table, Uniscribe version 1.6 or greater supports several functions that take advantage of OpenType tags. They can be substituted for the corresponding regular Uniscribe functions. Generally your applications should work entirely with functions from one set or the other and should not attempt to "mix and match" functions.



| Regular Uniscribe function             | Equivalent OpenType function                           |
|----------------------------------------|--------------------------------------------------------|
| [**ScriptItemize**](/windows/desktop/api/Usp10/nf-usp10-scriptitemize) | [**ScriptItemizeOpenType**](/windows/desktop/api/usp10/nf-usp10-scriptitemizeopentype) |
| [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape)     | [**ScriptShapeOpenType**](/windows/desktop/api/Usp10/nf-usp10-scriptshapeopentype)     |
| [**ScriptPlace**](/windows/desktop/api/Usp10/nf-usp10-scriptplace)     | [**ScriptPlaceOpenType**](/windows/desktop/api/Usp10/nf-usp10-scriptplaceopentype)     |



 

## Lay Out Text Using Uniscribe

Your application can use the following steps to lay out out a text paragraph with Uniscribe. This procedure assumes that the application has already divided the paragraph into runs.

1.  Call [**ScriptRecordDigitSubstitution**](/windows/desktop/api/Usp10/nf-usp10-scriptrecorddigitsubstitution) only when starting or when receiving a [**WM\_SETTINGCHANGE**](../winmsg/wm-settingchange.md) message.
2.  (Optional) Call [**ScriptIsComplex**](/windows/desktop/api/Usp10/nf-usp10-scriptiscomplex) to determine if the paragraph requires complex processing.
3.  (Optional) If using Uniscribe to handle bidirectional text and/or digit substitution, call [**ScriptApplyDigitSubstitution**](/windows/desktop/api/Usp10/nf-usp10-scriptapplydigitsubstitution) to prepare the [**SCRIPT\_CONTROL**](/windows/win32/api/usp10/ns-usp10-script_control) and [**SCRIPT\_STATE**](/windows/win32/api/usp10/ns-usp10-script_state) structures as inputs to [**ScriptItemize**](/windows/desktop/api/Usp10/nf-usp10-scriptitemize). If skipping this step, but still requiring digit substitution, substitute national digits for Unicode U+0030 through U+0039 (European digits). For information about digit substitution, see [Digit Shapes](digit-shapes.md).
4.  Call [**ScriptItemize**](/windows/desktop/api/Usp10/nf-usp10-scriptitemize) to divide the paragraph into items. If not using Uniscribe for digit substitution and the bidirectional order is known, for example, because of the keyboard layout used to enter the character, call **ScriptItemize**. In the call, provide null pointers for the [**SCRIPT\_CONTROL**](/windows/win32/api/usp10/ns-usp10-script_control) and [**SCRIPT\_STATE**](/windows/win32/api/usp10/ns-usp10-script_state) structures. This technique generates items by use of the shaping engine only, and the items can be reordered using the engine information.
    > [!Note]  
    > Typically, applications that work only with left-to-right scripts and without any digit substitution should pass null pointers for the [**SCRIPT\_CONTROL**](/windows/win32/api/usp10/ns-usp10-script_control) and [**SCRIPT\_STATE**](/windows/win32/api/usp10/ns-usp10-script_state) structures.

     

5.  Merge the item information with the run information to produce ranges.
6.  Call [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) to identify clusters and generate glyphs.
7.  If [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) returns the code USP\_E\_SCRIPT\_NOT\_IN\_FONT or S\_OK with the output containing missing glyphs, select characters from a different font. Either substitute another font or disable shaping by setting the **eScript** member of the [**SCRIPT\_ANALYSIS**](/windows/win32/api/usp10/ns-usp10-script_analysis) structure passed to **ScriptShape** to SCRIPT\_UNDEFINED. For more information, see [Using Font Fallback](using-font-fallback.md).
8.  Call [**ScriptPlace**](/windows/desktop/api/Usp10/nf-usp10-scriptplace) to generate [advance widths](uniscribe-glossary.md) and x and y positions for the glyphs in each successive range. This is the first step for which text size becomes a consideration.
9.  Sum the range sizes until the line overflows.
10. Break the range on a word boundary by using the **fSoftBreak** and **fWhiteSpace** members in the logical attributes. To break a single character cluster off the run, use the information returned by calling [**ScriptBreak**](/windows/desktop/api/Usp10/nf-usp10-scriptbreak).
    > [!Note]  
    > Decide if the first code point of a range should be a word break point because the last character of the previous range requires it. For example, if one range ends in a comma, consider the first character of the next range to be a word break point.

     

11. Repeat steps 6 through 10 for each line in the paragraph. However, if breaking the last run on the line, call [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) to reshape the remaining part of the run as the first run on the next line.

## Display Text Using Uniscribe

Your application can use the following steps to display a text paragraph. This procedure assumes that the application has already laid out the text and has not saved the glyphs and positions from the layout process. If speed is a concern, the application can save the glyphs and positions from the layout procedure and start at step 2 in the display procedure.

> [!Note]  
> The application can omit step 2 if the text contains no characters from right-to-left scripts, contains no bidirectional control characters, and uses a left-to-right base embedding level.

 

1.  For each run, do the following:
    1.  If the style has changed since the last run, update the handle to the device context by releasing and getting it again.
    2.  Call [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) to generate glyphs for the run.
    3.  Call [**ScriptPlace**](/windows/desktop/api/Usp10/nf-usp10-scriptplace) to generate an advance width and an x,y offset for each glyph.
2.  Do the following to establish the correct visual order for the runs in the line:
    1.  Extract an array of bidirectional [embedding levels](uniscribe-glossary.md), one per range. The embedding level is given by (SCRIPT\_ITEM) si.(SCRIPT\_ANALYSIS) a. (SCRIPT\_STATE) s.uBidiLevel.
    2.  Pass this array to [**ScriptLayout**](/windows/desktop/api/Usp10/nf-usp10-scriptlayout) to generate a map of visual positions to logical positions.
3.  (Optional) To justify the text, either call [**ScriptJustify**](/windows/desktop/api/Usp10/nf-usp10-scriptjustify) or use specialized knowledge of the text.
4.  Use the visual-to-logical map to display the runs in visual order. Starting at the left end of the line, call [**ScriptTextOut**](/windows/desktop/api/Usp10/nf-usp10-scripttextout) to display the run given by the first entry in the map. For each subsequent entry in the map, call **ScriptTextOut** to display the indicated run to the right of the previously displayed run.

    If omitting step 2, start at the left end of the line and call [**ScriptTextOut**](/windows/desktop/api/Usp10/nf-usp10-scripttextout) to display the first logical run, and then to display each logical run to the right of the previous run.

5.  Repeat the steps above for all lines in the paragraph.

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 
