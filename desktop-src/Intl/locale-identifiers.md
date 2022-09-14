---
description: Each locale has a unique identifier, a 32-bit value that consists of a language identifier and a sort order identifier.
ms.assetid: ea45b0e5-7df7-47fb-8dad-fccfbe53fec0
title: Locale Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Locale Identifiers

Each [locale](locales-and-languages.md) has a unique identifier, a 32-bit value that consists of a [language identifier](language-identifiers.md) and a [sort order identifier](sort-order-identifiers.md). The locale identifier is a standard international numeric abbreviation and has the components necessary to uniquely identify one of the installed operating system-defined locales. NLS supports both predefined locale identifiers and custom identifiers.

> [!Note]  
> Locale names can be used with functions introduced in Windows Vista that take a [locale name](locale-names.md) as a parameter, instead of a locale identifier. For more information, see [Calling the "Locale Name" Functions](calling-the--locale-name--functions.md). Use of locale names instead of locale identifiers is always preferable.

 

The following illustration shows the format of the bits in a locale identifier.

``` syntax
+-------------+---------+-------------------------+
|   Reserved  | Sort ID |      Language ID        |
+-------------+---------+-------------------------+
31         20 19     16 15                      0   bit
```

## Predefined Locale Identifiers

The predefined locale identifiers supported by NLS are defined in the [National Language Support (NLS) API Reference](/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c).

NLS uses the following locale information constants to represent locale identifiers.

-   [LOCALE\_SLANGUAGE](locale-slanguage.md) or [LOCALE\_SLOCALIZEDLANGUAGENAME](locale-slocalized-constants.md)
-   [LOCALE\_SNAME](locale-sname.md)
-   [LOCALE\_SSCRIPTS](locale-sscripts.md)
-   [LOCALE\_IDEFAULTANSICODEPAGE](locale-idefault-constants.md)

## Custom Locale Identifiers

**Windows Vista:** NLS supports the custom locale identifiers represented by the following locale information constants.

-   [LOCALE\_CUSTOM\_DEFAULT](locale-custom-constants.md)
-   [LOCALE\_CUSTOM\_UI\_DEFAULT](locale-custom-constants.md)
-   [LOCALE\_CUSTOM\_UNSPECIFIED](locale-custom-constants.md)

## Building a Locale

You can use the Locale Builder utility provided by NLS to build locales. For more information, see [Microsoft Locale Builder](https://www.microsoft.com/download/details.aspx?id=41158).

Your application can construct a locale identifier using the [**MAKELCID**](/windows/desktop/api/Winnt/nf-winnt-makelcid) macro. Alternatively it can use one of the default identifiers corresponding to the constants listed below.

-   [LOCALE\_INVARIANT](locale-invariant.md)
-   [LOCALE\_SYSTEM\_DEFAULT](locale-system-default.md)
-   [LOCALE\_USER\_DEFAULT](locale-user-default.md)

## Retrieval of Locale Identifiers

An application can retrieve the current locale identifiers by using the [**GetSystemDefaultLCID**](/windows/desktop/api/Winnls/nf-winnls-getsystemdefaultlcid) and [**GetUserDefaultLCID**](/windows/desktop/api/Winnls/nf-winnls-getuserdefaultlcid) functions. Each thread can set and retrieve its own locale with [**SetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-setthreadlocale) and [**GetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-getthreadlocale).

## Related topics

<dl> <dt>

[Locales and Languages](locales-and-languages.md)
</dt> <dt>

[Language Identifiers](language-identifiers.md)
</dt> <dt>

[Locale Names](locale-names.md)
</dt> <dt>

[Sort Order Identifiers](sort-order-identifiers.md)
</dt> <dt>

[**MAKELCID**](/windows/desktop/api/Winnt/nf-winnt-makelcid)
</dt> </dl>

 

 
