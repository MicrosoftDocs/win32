---
Description: Using Indexing Service with Web Servers
ms.assetid: 2d7fd5ec-0e5b-4f08-85a6-541e9394fac4
title: Using Indexing Service with Web Servers
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Indexing Service with Web Servers

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This section consists of the following topics.

-   [Indexing with Internet Information Services](indexing-with-internet-information-services.md)
-   [Creating Query Forms](creating-query-forms.md)
-   [Creating Administration Forms](creating-administration-forms.md)
-   [Highlighting Search Hits](highlighting-search-hits.md)
-   [Error Messages and Error Pages](error-messages-and-error-pages.md)
-   [Web Server Samples](web-server-samples.md)

Indexing Service is well suited for querying and indexing Web content. It integrates with Internet Information Services (IIS) to provide low-maintenance indexing and querying of sites hosted on the web server.

To provide search features on a web server, you must first configure Indexing Service to identify the searchable Web content. Then you develop a search page, either as an Active Server Page (ASP) or as a static query form. After developing the query form, you must develop a webpage for displaying query results. This results page could be the same ASP used for the query form, an .htx file, or another webpage. Indexing Service then returns the search results in a webpage you create. You can also provide hit-highlighting so that readers can see the location of the text they are searching for in the pages found by the query.

In addition to querying, you can develop webpages to administer the content index on the web server. These administration forms make it possible to create a custom, Web-based administration interface for Indexing Service.

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 



