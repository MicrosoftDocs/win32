---
title: Getting Browsers to Recognize Different Languages
description: Getting Browsers to Recognize Different Languages
ms.assetid: faabc494-8524-45c0-8800-5e563524d682
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting Browsers to Recognize Different Languages

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

If you set [CiLocale](variables-in-forms-and-in-idq-files.md#-idxs-cilocale-var) in your .idq files, you can override the locale sent from a browser. The Web browser sends its locale through the HTTP\_ACCEPT\_LANGUAGE variable. To find a list of recognized locale codes, see [Valid Locale Identifiers](valid-locale-identifiers.md).

Instead of overriding the locale sent by a browser, you may want to use the locale sent by a browser that is querying text in variety of languages. For example, given a single HTML page, one query could be for German text (CiLocale=De) and another could be for Spanish text (CiLocale=Es). If CiLocale is not found in the .idq file the locale sent by the Web browser is used. If no locale is sent by the browser, Indexing Service uses the locale of the web server.

The following table shows examples of three types of settings. Each setting specifies a different source from which the value of CiLocale is taken:



| CiLocale Setting in .Idq | Value Source                              |
|--------------------------|-------------------------------------------|
| CiLocale=En-US           | Web site (set in the .idq file)           |
| CiLocale=%CiLocale%      | HTML page (set in the query form)         |
| CiLocale=                | Web browser (from HTTP\_ACCEPT\_LANGUAGE) |



 

 

 




