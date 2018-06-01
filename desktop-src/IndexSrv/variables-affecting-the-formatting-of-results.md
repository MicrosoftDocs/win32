---
title: Variables Affecting the Formatting of Results
description: Variables Affecting the Formatting of Results
ms.assetid: 8c6a9cf3-3022-45d3-9fe6-5e80a37eb956
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Variables Affecting the Formatting of Results

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Some variables that can be set in the .idq file affect the formatting of data in the .htx file. The variable [CiLocale](https://www.bing.com/search?q=CiLocale) can be set to affect the formatting of dates, times, currency values, and floating-point numbers according to NLS conventions. If CiLocale is not set, the locale is set from the client's browser or the server's default locale, in order of priority.

To change the formatting of data types, modify format settings as needed in the **Regional Settings** in the system Control Panel.

A set of variables taken from the .idq file will be used to enclose and separate elements of column values that are vectors. Unlike all other variables set in the .idq file, these variables cannot be referred to explicitly in the .htx file:

-   [CiCurrencyVectorPrefix](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiCurrencyVectorSeparator](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiCurrencyVectorSuffix](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiDateVectorPrefix](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiDateVectorSeparator](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiDateVectorSuffix](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiNumberVectorPrefix](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiNumberVectorSeparator](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiNumberVectorSuffix](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiStringVectorPrefix](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiStringVectorSeparator](string-variables-useful-for-formatting-displayed-columns.md)
-   [CiStringVectorSuffix](string-variables-useful-for-formatting-displayed-columns.md)

 

 




