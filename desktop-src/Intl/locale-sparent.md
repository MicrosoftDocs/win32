---
description: LOCALE\_SPARENT
ms.assetid: 3fa0bc36-7577-4b5a-b557-8ac42e8594a8
title: LOCALE_SPARENT
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_SPARENT

**Windows Vista and later:** Fallback locale, used by the resource loader. The maximum number of characters allowed for this string is 85, including a terminating null character.

Locales have a hierarchy in which the parent of a specific locale is a neutral locale. A specific locale is associated with both a language and a country/region, while a neutral locale is associated with a language but is not associated with any country/region. The parent locale is used to decide the first fallback to be tried when a resource for a specific locale is not available. For example, the parent locale for "en-US" (0x0409) is "en" (0x0009). When a resource is not available for the specific "en-US" locale, the resource loader falls back to use the resource that is available for the neutral "en" locale. See [User Interface Language Management](user-interface-language-management.md) for further details of the resource loader fallback strategy.

This pattern is consistent for predefined locales. However, the parent locale is not determined by any manipulation of the locale name. That is, [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) and [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) do not parse a string such as "en-US" to get the value "en". Instead, they look at the stored locale data. For predefined locales, the value follows the expected pattern, in which the parent of a specific locale is the corresponding neutral locale and the parent of a neutral locale is the invariant locale. While it is recommended that custom locales follow a similar strategy in terms of defining their parent locale, this is not enforced. The application implementing a custom locale can specify a less obviously appropriate parent.

> [!Note]  
> Since none of the functions described in [Calling the "Locale Name" Functions](calling-the--locale-name--functions.md) accept neutral locales as inputs, this LOCALE\_SPARENT data is of very limited use. In particular, neither [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) nor [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) accepts neutral locales as inputs.

 

 

 



