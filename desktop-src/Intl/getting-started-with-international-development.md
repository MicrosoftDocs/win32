---
description: This topic helps you get started creating world-ready applications, by specifying prerequisites, summarizing technologies, and introducing a getting-started tutorial.
ms.assetid: 80c10bc2-b7e3-4f24-8bac-826149a376c7
title: Getting Started with International Windows Development
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with International Windows Development

This topic helps you get started creating world-ready applications, by specifying prerequisites, summarizing technologies, and introducing a getting-started tutorial.

## Getting Started

If you write applications for users in a single locale, those applications can be successful even if you design them with locale-specific assumptions, such as presenting dates in a particular format, or sorting strings in a particular sequence. But now you have to ensure that your applications can be used in multiple countries, by users who have different languages and different cultures. To succeed in multiple locales, the applications need to adjust to the locale in which they run. This flexibility is important whether you add it to an existing application, or you design it into a new application.

This section helps you get started in international development. It presents links to topics that provide prerequisite overviews of internationalization. It summarizes the technologies that the SDK offers for support of worldwide customers. Finally, this section provides a sample application that solves a problem that you often encounter when writing global software.

## Prerequisites

You should become familiar with the issues that arise in developing international software for Windows. Start with these overviews.

-   [Understanding Internationalization](understanding-internationalization.md) explains the added difficulty of developing world-ready applications, and defines key terms.
-   The [Get World-Ready](https://msdn.microsoft.com/goglobal/bb895995.aspx) topic leads you to guidelines and best practices that you can skim through or delve into as needed.
-   The [Internationalization Checklist](internationalization-checklist.md) summarizes the actions you should take to create a world-ready application.
-   Security is always an issue in software development, but you need to consider additional issues when developing international software. Take a look at [Security Considerations: International Features](security-considerations--international-features.md).

Also be aware of the more extensive articles that can be found at the [Go Global Developer Center](https://msdn.microsoft.com/globalization/mt613165) in the [Globalization Step-by-Step](https://msdn.microsoft.com/globalization/mt642951) section. As you develop international software, you will want to consult the additional overviews and detailed articles that can be found there.

## Learning Paths

The path you follow next in learning to create international software depends on the scenarios you face. The following scenarios are based on those introduced in the main section topic, [Internationalization for Windows Applications](international-support.md).

-   **Create applications that can be deployed to multiple regions in multiple languages.**

    The challenge is to develop an application that does not have to be rewritten for each language or culture.

    -   Read the article [Understanding Multilingual User Interface (MUI)](./about-multilingual-user-interface.md).
    -   Explore the documentation for [Multilingual User Interface](multilingual-user-interface.md).
    -   Get started with the [Hello MUI](#the-hello-mui-application) application.

-   **Support the input and display of different languages, character sets, and fonts.**

    Your application may need to support multiple character sets, support complex scripts (such as those used to represent Hebrew, Arabic, Thai, and Indic languages), permit the user to select from international fonts, or allow the user to enter characters and symbols, such as Japanese kanji, for other languages by using a standard keyboard.

    -   Read the articles:

        -   [Script and Font Support in Windows](https://msdn.microsoft.com/globalization/mt791278)
        -   [Input Language: Keyboards and IMEs](https://msdn.microsoft.com/globalization/mt662332)

    -   Explore the documentation for:

        -   [Unicode and Character Sets](unicode-and-character-sets.md)
        -   [International Fonts and Text Display](international-fonts-and-text-display.md)
        -   [Input Method Manager](input-method-manager.md)

-   **Display culture-dependent objects in appropriate formats.**

    International applications should use locale settings to properly sort strings, and to display culture-sensitive information, such as time, dates, and currency.

    -   Explore the [National Language Support Knowledge Center](./national-language-support-reference.md).
    -   Examine the documentation for [National Language Support (NLS)](national-language-support.md).

-   **Discover the language or script used by the user, and apply it to the other services of the application.**

    If your application can determine the language in which text and user input is written, it can display content such as prompts or help in an understandable language.

    -   Read the article [Writing World-Ready Applications in Windows: Extended Linguistic Services in Windows](./using-extended-linguistic-services.md).
    -   Explore the documentation for [Extended Linguistic Services (ELS)](extended-linguistic-services.md).

## Internationalization Technologies in the SDK

The International Development Support section of the SDK provides technologies that permit the application to enumerate languages, locales, and locale-specific formats. You can use them in Microsoft Win32 applications that you write in C or C++ .

The [Extended Linguistic Services](extended-linguistic-services.md) offer Microsoft-patented technology for the identification of languages and scripts in text. Your application can determine the services available based on category as well as on input and output language, script, and content type.

[International Fonts and Text Display](international-fonts-and-text-display.md) provides information about international fonts, complex scripts and glyphs, and the fine rendering of typography on the Windows platform.

[Input Method Manager (IMM)](input-method-manager.md) is a technology that helps the application receive input from Input Method Editor (IME) software, which in turn allows the entry of characters and symbols, such as Japanese kanji, for other languages by using a standard keyboard.

## The Hello MUI Application

A common task in international development begins with a monolingual application that you must make world-ready. You need to add support for additional languages, but in a way that does not require that you rewrite the code for each new language or culture.

This task provides the opportunity to present a tutorial that takes you step-by-step through the creation of a Hello MUI application, making use of the [Multilingual User Interface (MUI)](multilingual-user-interface.md) resource model and associated support provided in Windows.

The tutorial adopts the concept of the familiar Hello World application, demonstrating the use of MUI to build a basic multilingual application.

You can begin the Hello MUI tutorial at [Adding Multilingual User Interface Support to an Application](creating-a-multilingual-user-interface-application.md).

 

 
