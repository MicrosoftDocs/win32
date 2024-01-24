---
description: This topic provides actions to take to create code that supports multiple markets. Consider these statements as a guide during code design, and as metrics when you evaluate the builds.
ms.assetid: cf2ac58e-7fc3-4635-8b82-586a0732b2a3
title: Internationalization Checklist
ms.topic: article
ms.date: 05/31/2018
---

# Internationalization Checklist

This topic provides actions to take to create code that supports multiple markets. Consider these statements as a guide during code design, and as metrics when you evaluate the builds.

-   Create program specifications that account for international considerations from the outset.
    -   Design icons and bitmaps to be meaningful and not offensive in your target markets, and to not contain text.
    -   Design menus and dialog boxes to leave room for text expansion. For example, English strings often expand by 40% when translated into German or Dutch.
    -   Do not use slang or culturally-specific references in UI elements or messages.
    -   Create shortcut key combinations that are accessible on international keyboards. For example, avoid using punctuation character keys as shortcut keys because they are not always found on international keyboards or easily produced by the user. For examples of keyboard layouts, see [Windows Keyboard Layouts](https://msdn.microsoft.com/goglobal/bb964651.aspx).
    -   Consider local laws affecting feature designs, such as requirements that government entities purchase software that supports multiple official languages.
    -   Develop third-party agreements that support your organization's international UI standards and design decisions.
    -   Use consistent terminology in user interface strings that must be translated.

<!-- -->

-   Create code that is independent of locale.
    -   Don't concatenate strings to form sentences.
    -   Don't use a given string variable in more than one context, such as reusing a sentence fragment in different messages and prompts, because such strings may not be easy to translate.
    -   Document strings using comments to provide context for translators, and clearly mark strings or characters that should not be localized.
    -   Don't use hard-coded character constants, numeric constants, screen positions, filenames, or pathnames that presume a particular language.
    -   Make buffers large enough to hold translated strings.
    -   Allow the input of data with formats that vary by locale, such as dates, times, and currencies.
    -   Use paper size, envelope size, and other defaults that are appropriate to a given locale.
    -   Ensure that each language edition can read documents created by the other editions.
    -   Provide support for locale-specific hardware, if necessary.
    -   Configure features that don't apply to international markets as implementation options that can be disabled easily.

<!-- -->

-   Create code that takes advantage of international functionality offered by Microsoft Windows.
    -   Use international information carried by the system (National Language Support).
    -   Use system functions for sorting, case conversion, and string mapping.
    -   Use generic text layout functions.
    -   Respond to changes to international settings in Control Panel.
    -   Handle the WM\_INPUTLANGCHANGEREQUEST message.
    -   Support input method editors, vertical text, and line-breaking rules in East Asian editions.

<!-- -->

-   Compile all international editions of the program from one set of source files.
    -   Minimize or eliminate mechanisms that require code to be recompiled for different language editions.
    -   Store localizable items, such as strings and icons, in Windows resource files.
    -   Store documents in all language editions using the same file format.

<!-- -->

-   Support different character sets, not just the Latin 1 code page, number 1252.
    -   Program supports network environments in which computers run operating systems with different default code pages.
    -   Use GetCPInfoEx to retrieve lead-byte ranges for East Asian code pages.
    -   Parse double-byte characters in East Asian–language applications unless the code is based on Unicode.
    -   Support Unicode or conversion between Unicode and the local code page.
    -   Don't assume that all characters are 8-bit or 16-bit.
    -   Use generic data types and generic function prototypes.
    -   Use the font charset property, which calls EnumFontFamiliesEx and the ChooseFont common dialog function.
    -   Display and print text using the fonts that are appropriate for the locale.

<!-- -->

-   Test the international features of the program.
    -   Translated text should meet the standards of native speakers.
    -   Dialog boxes should resize properly, and text should be hyphenated appropriately, when different languages are displayed.
    -   Dialog boxes, status bars, toolbars, and menus should fit on the screen and read legibly when the display is set at different resolutions, for all translated languages.
    -   Menu and dialog-box accelerators should be unique.
    -   Users should be able to type characters from non-European scripts into documents, dialog boxes, and filenames.
    -   Users should be able to cut, paste, save, and print characters from non-European scripts successfully.
    -   Sorting and case conversion should be accurate for different locales.
    -   The application should work correctly on localized editions of Windows.

 

 



