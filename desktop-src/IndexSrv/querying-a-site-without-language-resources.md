---
title: Querying a Site Without Language Resources
description: Querying a Site Without Language Resources
ms.assetid: 6374a9f5-2fd2-43b8-ae4a-1acaa9bf253d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying a Site Without Language Resources

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service ships with several languages, which you can install on your site during setup. For a list of these languages, see the Indexing Service webpage. For instructions about setting up Indexing Service and choosing the languages you want to install, see [Getting Started](getting-started.md) and [Language Resources](language-resources.md).

If a site does not have a particular language resource installed, Indexing Service sends you results in the format for the locale set for the system. But if you query the same site and specify [CiLocale](https://www.bing.com/search?q=CiLocale) for the document, the results are returned with the CiLocale setting Neutral.

For example, suppose a site in the United States has some documents in Russian. The site has a [CiLocale](https://www.bing.com/search?q=CiLocale) value of US, for American English. If you query that site for all documents in Russian and you specify the CiLocale value as RU, Indexing Service displays the documents in Russian. If you sent your query without specifying CiLocale, Indexing Service borrows the system CiLocale (US), and you would not be able to read the results.

 

 




