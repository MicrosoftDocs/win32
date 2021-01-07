---
description: The term &\#0034;language&\#0034; indicates a collection of properties used in spoken and written communication.
ms.assetid: 8214c00d-4ec6-4597-8088-7819a160f0dc
title: Locales and Languages
ms.topic: article
ms.date: 05/31/2018
---

# Locales and Languages

The term "language" indicates a collection of properties used in spoken and written communication. Each language has a language name and a language identifier that indicate the particular [code page](code-pages.md) (ANSI, DOS, Macintosh) used to represent the [geographical location](table-of-geographical-locations.md) for the language on the operating system. A neutral language is indicated by a name such as "en" for English. A more geographically specific language can be indicated by a name that includes both locale and country/region information. For example, the locale English (United States) has the language name "en-US".

A "locale" is a collection of language-related user preference information represented as a list of values. Windows XP supports more than 150 locales, and Windows Vista supports about 200. Each locale is defined by a language and a sort order, and has both a locale name and a locale identifier. An example of a locale name for German (Germany) is "de-DE\_phonebook".

Each operating system has at least one installed locale and often has many locales from which the user can select. Each locale has a variety of information associated with it, other than its name and identifier. Locale information types are described in [Locale Information Constants](locale-information-constants.md).

The operating system assigns a locale to each thread, initially assigning the "system default locale," defined by [LOCALE\_SYSTEM\_DEFAULT](locale-system-default.md). This locale is set when the operating system is installed or when the user selects it using the regional and language options portion of the Control Panel. When running a thread in a process belonging to the user, the operating system assigns the "user default locale" to the thread. This locale is defined by [LOCALE\_USER\_DEFAULT](locale-user-default.md). An application can override either default by using the [**SetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-setthreadlocale) function to explicitly set the locale for a thread.

Implementation of a language requires a corresponding locale. The operating system implements a neutral language by selecting the data for the locale associated with a specific version of the language, usually the most widespread locale.

Starting with Windows Vista, it is possible for a particular language to correspond to a supplemental locale, which is a type of custom locale. Since supplemental locales all share a single locale identifier, your applications should handle these locales and the corresponding languages by name instead of by identifier.

Language concepts are closely related to locale concepts, but the two terms are not interchangeable. As a general rule, functions related to the [Multilingual User Interface](multilingual-user-interface.md) deal with languages, while the NLS functions act upon locales.

The following topics are covered in this section:

-   [Custom Locales](custom-locales.md)
-   [Language Identifiers](language-identifiers.md)
-   [Language Names](language-names.md)
-   [Locale Identifiers](locale-identifiers.md)
-   [Locale Names](locale-names.md)
-   [Pseudo-Locales](pseudo-locales.md)

## Related topics

<dl> <dt>

[About National Language Support](about-national-language-support.md)
</dt> <dt>

[Code Pages](code-pages.md)
</dt> <dt>

[Locale Information Constants](locale-information-constants.md)
</dt> <dt>

[Multilingual User Interface](multilingual-user-interface.md)
</dt> <dt>

[Table of Geographical Locations](table-of-geographical-locations.md)
</dt> <dt>

[User Interface Language Management](user-interface-language-management.md)
</dt> <dt>

[**SetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-setthreadlocale)
</dt> </dl>

 

 



