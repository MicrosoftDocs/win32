---
Description: 'The following are options for display and related processing of text to support fine typography effects or complex scripts: Text functionsEdit controlsRich edit controlsUniscribe'
ms.assetid: 337bc798-e75d-4389-8fea-577eb82a0ed5
title: Complex Script Processing
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Complex Script Processing

The following are options for display and related processing of text to support fine typography effects or complex scripts:

-   Text functions
-   Edit controls
-   Rich edit controls
-   Uniscribe

The options you choose depend on the following factors:

-   The type of text or scripts.
-   The implementation model, for example, the text layout and handling of line breaking by the application.
-   Update of an existing application versus creation of a new application.

In general, an application that does relatively simple script processing can choose any option for processing complex scripts. However, for the most complete control of complex script processing, Uniscribe is recommended.

## Complex Script Processing Using Text Functions

Applications that use mostly plain text, that is, text that uses the same typeface, weight, color, and so on, have traditionally written text and measured line lengths using standard text functions, such as [**TextOut**](https://msdn.microsoft.com/0c437ff8-3893-4dc3-827b-fa9ce4bcd7e6), [**ExtTextOut**](https://msdn.microsoft.com/74f8fcb8-8ad4-47f2-a330-fa56713bdb37), [**TabbedTextOut**](https://msdn.microsoft.com/1cb78a75-752d-4e06-afdf-cd797f209114), [**DrawText**](https://msdn.microsoft.com/fe412280-d797-4abd-8a29-107a9cd96145), and [**GetTextExtentExPoint**](https://msdn.microsoft.com/b873a059-5aa3-47d0-b109-7acd542c7d79). These functions support processing for complex scripts and fine typography effects. For more information, see [Fonts and Text](https://msdn.microsoft.com/9944baa9-8e50-40b9-9650-78b0b1d7643a).

In general, the standard text support is transparent to applications processing complex scripts. However, you should be aware of some specific rules to follow in writing applications that support fine typography and process complex scripts:

-   Your application should save characters in a buffer and display a whole line of text at one time instead of, for example, calling [**ExtTextOut**](https://msdn.microsoft.com/74f8fcb8-8ad4-47f2-a330-fa56713bdb37) on each character as it is typed in by the user. This mechanism allows the advanced text shaping modules to use context to reorder and generate [glyphs](uniscribe-glossary.md#glyph) correctly.
-   The application should use [**GetTextExtentExPoint**](https://msdn.microsoft.com/b873a059-5aa3-47d0-b109-7acd542c7d79) to determine line length, instead of computing line lengths from cached character widths, since the width of a glyph can vary by context.
-   The application should optionally add support for right-to-left reading order and right alignment.
-   The reordering and contextual processing required for complex scripts or fine typography requires a significant increase in processing over basic text display for simple scripts. Therefore, to avoid performance issues, your application should not process large amounts of text before displaying results and returning control to the user.

## Complex Script Processing Using Edit Controls

The standard Windows edit controls have been extended to support multilingual text and complex scripts. The extended support includes input and display, as well as correct cursor movement over character clusters, for example, in Thai and Devanagari scripts. For more information, see [Edit Controls](https://www.bing.com/search?q=Edit+Controls).

## Complex Script Processing Using Rich Edit Controls

Rich Edit 3.0 is a higher-level collection of interfaces that takes advantage of Uniscribe to insulate text layout applications from the complexities of certain scripts. Rich Edit is the simplest way for applications to display complex scripts even though their primary purpose is not necessarily text layout. Rich Edit provides fast, versatile editing of rich Unicode multilingual text and simple plain text. It includes extensive message and COM interfaces, text editing, formatting, line breaking, simple table layout, vertical text layout, bidirectional text layout, Indic and Thai support, an editing user interface much like Microsoft Word, and Text Object Model interfaces.

Along with the Rich Edit interfaces, applications can use the Rich Edit [**TextOut**](https://msdn.microsoft.com/0c437ff8-3893-4dc3-827b-fa9ce4bcd7e6) function to automatically parse, shape, position, and break lines. For more information, see [Rich Edit Controls](https://www.bing.com/search?q=Rich+Edit+Controls).

## Complex Script Processing Using Uniscribe

[Uniscribe](uniscribe.md) provides the most extensive support for processing of text involving fine typography effects and complex scripts. It supports the complex rules found in scripts such as Arabic, Devanagari, and Thai. It handles scripts written from right to left, such as Arabic and Hebrew, and supports the mixing of scripts. Uniscribe also exposes [OpenType](opentype-font-format.md) font features that can be used by applications to control fine typography effects. For more information, see [Processing Complex Scripts](processing-complex-scripts.md).

## Related topics

<dl> <dt>

[About Uniscribe](about-uniscribe.md)
</dt> <dt>

[Processing Complex Scripts](processing-complex-scripts.md)
</dt> </dl>

 

 



