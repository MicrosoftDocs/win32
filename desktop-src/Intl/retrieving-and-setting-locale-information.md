---
description: Retrieving and Setting Locale Information
ms.assetid: 7675f826-76be-4361-a82c-9573040a7e72
title: Retrieving and Setting Locale Information
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving and Setting Locale Information

The application must be able to retrieve and set specific information about available [locales and languages](locales-and-languages.md). Each element of locale information, such as the name of a particular day of the week or the character used as a decimal separator, has a corresponding constant. The available constants are defined in [Locale Information Constants](locale-information-constants.md).

Your application always stores and manipulates locale information as a null-terminated string. No binary data is allowed, and any numeric values must be specified as text. Each type of information has a particular format. Also, several types are linked together so that changing one type changes the value of the other type as well.

To retrieve locale information, the application calls [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) or [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) with the constant that corresponds to the required information. The application can call [**SetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-setlocaleinfoa) to set an item of locale information.

> [!Note]  
> Although a [locale identifier](locale-identifiers.md) might be supported, it is not available for use by an application unless the corresponding locale is also installed.

 

Since most locale information constants are mutually exclusive, only one type of information can be handled at a time. The exceptions to this rule are [LOCALE\_USE\_CP\_ACP](locale-use-cp-acp.md), [LOCALE\_RETURN\_NUMBER](locale-return-constants.md), and [LOCALE\_NOUSEROVERRIDE](locale-nouseroverride.md), which can be combined with other constants using a binary OR.

> [!Caution]  
> Use of LOCALE\_NOUSEROVERRIDE is strongly discouraged as it disables user preferences.

 

Like a number of applications, for example Microsoft Active Directory, your application can maintain its strings in a sortable database. For more information, see [Handling Sorting in Your Applications](handling-sorting-in-your-applications.md).

## Related topics

<dl> <dt>

[Using National Language Support](using-national-language-support.md)
</dt> <dt>

[Locale Information Constants](locale-information-constants.md)
</dt> <dt>

[Handling Sorting in Your Applications](handling-sorting-in-your-applications.md)
</dt> <dt>

[Working with Custom Locales](working-with-custom-locales.md)
</dt> </dl>

 

 



