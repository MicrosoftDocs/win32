---
Description: LOCALE\_NOUSEROVERRIDE
ms.assetid: ab68d16b-5e1e-4af3-b048-43975cded00a
title: LOCALE\_NOUSEROVERRIDE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LOCALE\_NOUSEROVERRIDE

> \[!Caution\]  
> Since LOCALE\_NOUSEROVERRIDE disables user preferences, its use is strongly discouraged. This constant does not guarantee data stability since [custom locales](custom-locales.md), service updates, different operating system versions, and other scenarios can change data in unexpected ways. For more information, see [Using Persistent Locale Data](using-persistent-locale-data.md).

 

No user override. In several functions, for example, [**GetLocaleInfo**](/windows/win32/Winnls/nf-winnls-getlocaleinfoa?branch=master) and [**GetLocaleInfoEx**](/windows/win32/Winnls/nf-winnls-getlocaleinfoex?branch=master), this constant causes the function to bypass any user override and use the system default value for any other constant specified in the function call. The information is retrieved from the locale database, even if the identifier indicates the current locale and the user has changed some of the values using the Control Panel, or if an application has changed these values by using [**SetLocaleInfo**](/windows/win32/Winnls/nf-winnls-setlocaleinfoa?branch=master). If this constant is not specified, any values that the user has configured from the Control Panel or that an application has configured using [**SetLocaleInfo**](/windows/win32/Winnls/nf-winnls-setlocaleinfoa?branch=master) take precedence over the database settings for the current system default locale.

 

 



