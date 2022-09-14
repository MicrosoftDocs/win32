---
description: Understanding Internationalization
ms.assetid: 9147cd20-eeae-4ad4-8d51-ac1d68a4b2c5
title: Understanding Internationalization
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Internationalization

Developing internationalized software products requires not only the production of correct code, but also a design that permits the product to support many locales. Developers and their managers should be aware of the level of effort and attention to detail required to create world-ready applications, whether they deliver them as single binaries ready for use in many different markets, or as multiple binaries that are each specific to one locale. As a developer, make sure your management understands that internationalization involves more than just code development. Designing for internationalization at the beginning of your product cycle saves you time, money, and effort.

**Internationalization** is the creation of software that adapts to locales around the world. A **locale** is a collection of language-related user preferences. A locale is specified by the pairing of a language and a geographical region. For example, English (United States) and English (United Kingdom) are two different locales, as are English (Canada) and French (Canada).

Internationalized software has these attributes:

-   **World-readiness** covers design and implementation that separate locale-independent code from locale-dependent resources, and comprises two major areas:
    -   **Globalization** is the process of developing a program core with features and code design that are independent of language or locale. Instead, the design supports the input, display, and output of Unicode-supported language scripts, as well as data related to specific locales.
    -   **Localizability** is the design of the software code base and resources such that a program can be localized, as defined below, into different language editions without any changes to the source code. For example, string buffers in the code, and text boxes in the UI, must be large enough to accommodate longer text strings in languages such as German or Dutch.
-   **Localization** This involves translating and customizing a product for a specific market, and it is mainly about creating resource files rather than writing source code.

For example, using the National Language Support (NLS) supplied by the Microsoft Win32 API is a software development process that supports world-readiness, whereas modifying the UI elements, translating text, and standardizing terminology are localization steps usually performed by someone who is a language specialist, such as a translator. Even when your code development emphasizes world-readiness, you need to understand localization because your design decisions affect the work of the translator.

 

 



