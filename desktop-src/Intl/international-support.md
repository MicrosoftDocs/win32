---
description: This section describes the technologies in Windows that enable you to support the many cultures and written languages of the international marketplace in your C or C++ based Microsoft Win32 application.
ms.assetid: 90dbbd70-3609-4c12-bdc1-7fa222c96f67
title: Internationalization for Windows Applications
ms.topic: article
ms.date: 05/31/2018
---

# Internationalization for Windows Applications

(Formerly titled "International Support")

This section describes the technologies in Windows that enable you to support the many cultures and written languages of the international marketplace in your C or C++ based Microsoft Win32 application.

Windows has become an essential platform for customers worldwide. International users expect solutions that are adapted to their languages and regions around the world. In this section, you will find the information you need to develop multilanguage, multicultural, and multi-site solutions. The international support built into Windows empowers you to implement many scenarios with less engineering overhead than ever before.

The development of world-ready applications requires the use of many services and tools. Windows contains features that enable you to develop solutions that:

- Support the different language-specific and locale-specific needs of users around the world (including specialized text support, sorting behavior, date and time formatting, and keyboard layouts). (For more information, see [National Language Support Knowledge Center](./national-language-support-reference.md).)
- Are globalized (can be deployed worldwide from a single binary image) and can be localized (able to be adapted for specific local markets). (For more information, see [Multilingual User Interface](./multilingual-user-interface.md).)
- Display international fonts and text, and allow users to specify the font they want. (For more information, see [Script and Font Support in Windows](/globalization/input/font-support).)
- Permit the user to enter complex characters and symbols with a standard keyboard.
- Provide support for many different written languages through Unicode and traditional character sets.
- Discover the language input by a user, and tailor the user experience provided by your application. (For more information, see [Writing World-Ready Applications in Windows: Extended Linguistic Services in Windows](./using-extended-linguistic-services.md).)

## In this Section

The following international support technologies are documented in this section. They are listed with some key scenarios for which they can be used.

- [Getting Started with International Windows Development](getting-started-with-international-development.md)

    Describes how to get started creating world-ready applications, and provides a tutorial illustrating a common task in writing global software.

    Common Scenarios:

    - Determine a path to take to learn how to develop international software.
    - Discover the internationalization technologies available in the Microsoft Windows Software Development Kit (SDK).
    - Follow a tutorial that takes an existing monolingual application and adds support for additional languages.

- [Globalization Services](globalization-services.md)

    Describes [Extended Linguistic Services (ELS)](extended-linguistic-services.md), which enable you to discover the language in which text and user input is written, and [National Language Support (NLS)](national-language-support.md), which enables an application to use locale information to display culture-sensitive information (such as time, dates, and currency) and properly sort strings.

    Common Scenarios:

    - Discover the language of the user's input, so that help content can be displayed in an understandable language.
    - Discover the script used in text that is to be displayed. If it is Simplified or Traditional Chinese, offer the user the option to have the text transliterated from one to the other.
    - Permit the user to select a locale (a collection of language-related user preference information).
    - Display times, dates, calendar information, currency, and many other culture-dependent objects in appropriate languages and formats.
    - Sort strings into the order expected by the user of a given locale.

- [Input Method Manager](input-method-manager.md)

    Describes the technology used by an application to communicate with an input method editor (IME). The IME allows computer users to enter complex characters and symbols by using a standard keyboard.

    Common Scenario:

    - Permit the user to use a standard keyboard to enter Japanese kanji characters.

- [International Fonts and Text Display](international-fonts-and-text-display.md)

    Describes the support provided by the Windows platform for international fonts, international text, and fine typography.

    Common Scenarios:

    - Allow the user to select international fonts based on character set.
    - Display international text.
    - Process complex scripts, including bidirectional rendering, contextual shaping, and ligatures (Uniscribe).
    - Allow a high degree of control for fine typography (Uniscribe).

- [Multilingual User Interface](multilingual-user-interface.md)

    Describes how applications can separate language-dependent resources from language-neutral code for supported user interface languages.

    Common Scenarios:

    - Create regional or worldwide single deployment images of an application.
    - Localize a solution by updating application resources with no change to application source code.
    - Permit users to switch from one UI language to another at run time.

- [Unicode and Character Sets](unicode-and-character-sets.md)

    Describes how applications can take advantage of Unicode, the worldwide character-encoding standard that uses 16-bit code values to represent all the characters used in modern computing, including technical symbols and special characters used in publishing.

    Common Scenarios:

    - Support the many different languages of the international marketplace through Unicode.
    - Convert Unicode characters to and from other character sets, when necessary.

- [Security Considerations: International Features](security-considerations--international-features.md)

    Provides information about security considerations related to international development support features.

    The security information pertains to all scenarios.

## Related International Technologies

International development support is also available for applications written in managed code. If you are developing for the .NET Framework, you will need some or all of these:

- The [System.Globalization Namespace](/dotnet/api/system.globalization) contains classes that define culture-related information and provide advanced globalization functions.
- The [System.Text Namespace](/dotnet/api/system.text) contains classes that represent character encodings, convert blocks of characters, and manipulate and format String objects.
