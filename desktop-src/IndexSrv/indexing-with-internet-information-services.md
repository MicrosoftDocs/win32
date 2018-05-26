---
title: Indexing with Internet Information Services
description: Indexing with Internet Information Services
ms.assetid: 2523b97c-dc9d-4d47-b075-34988556c082
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Indexing with Internet Information Services

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service provides search capabilities to websites hosted with Internet Information Services (IIS). With Indexing Service, you can provide searchable access to both intranet and Internet websites. You can index remote computers and multiple web servers.

The default set of filters provided with Indexing Services includes a filter for HTML documents. However, you can also provide Web-based searches of any documents that Indexing Service is able to filter, including Microsoft Office documents. Indexing Service supports a set of document properties for webpages, making it possible to search for webpages by date of creation or author, or by their content.

Indexing with IIS involves these main tasks, which are described in this section:

-   Setting up a Web catalog
-   Creating a query page
-   Processing an index query from a query page
-   Formatting and displaying query results
-   Administering the index

For more information, see [Best Practices](best-practices.md).

### Setting Up a Web Catalog

Before you can index content on the web server, you must create a Web catalog for Indexing Service. Use the Microsoft Management Console (MMC) in Microsoft to carry out this task. You will find Indexing Service under the Server Applications and Services node in the Computer Management tree.

There are various tasks specific to setting up a Web catalog on IIS:

-   [Listing Virtual Roots](listing-virtual-roots.md)
-   [Setting Up a Remote Virtual Root](setting-up-a-remote-virtual-root.md)
-   [Indexing Remote Computers](indexing-remote-computers.md)
-   [Logging Queries](logging-queries.md)
-   [Putting Security Features to Work](putting-security-features-to-work.md)
-   [List of Property Names for a Web Catalog](list-of-property-names-for-a-web-catalog.md)

### Creating a Query Page

You must also provide a user interface to submit search requests for those who browse your website. Indexing Service supports several ways to create query pages, including Internet Data Query (.idq) files and Active Server Pages (.asp). For more information, see [Creating Query Forms](creating-query-forms.md).

### Processing Index Queries

After users of your website submit their search requests through your query page, your site must process the queries. This involves taking the information supplied to the query page and constructing an Indexing Service query to run. For more information, see [Query Languages for Indexing Service](query-languages-for-indexing-service.md).

### Formatting Query Results

After Indexing Service returns the results of the query, your website must format the data and display it in a webpage. Indexing Service supports various ways to display query results, including HTML extension (.htx) files and Active Server Pages (.asp) files. For more information, see [HTML Extension Files](html-extension-files.md) and [Formatting Results in an Active Server Pages File](formatting-results-in-an-active-server-pages-file.md).

In addition to listing webpages that match a query, Indexing Service can also highlight the search text when showing a webpage found by the query. For more information, see [Highlighting Search Hits](highlighting-search-hits.md).

### Administering the Index

You can administer your website index with the MMC or create your own administration interface. You can develop Active Server Pages (.asp) or Internet Data Administration (.ida) files. These kinds of administration front ends are very easy to customize and accessible through any computer that can browse the website. For more information, see [Creating Administration Forms](creating-administration-forms.md).

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 




