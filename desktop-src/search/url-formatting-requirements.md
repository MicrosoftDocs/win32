---
description: As of Windows 7, inconsistencies remain in the handling and parsing of URLs. This topic provides a limited guide to navigating inconsistencies in file URL formats.
ms.assetid: E9792368-517B-4FD7-A244-6C4B7F78B66E
title: URL Formatting Requirements
ms.topic: article
ms.date: 05/31/2018
---

# URL Formatting Requirements

As of Windows 7, inconsistencies remain in the handling and parsing of URLs. This topic provides a limited guide to navigating inconsistencies in file URL formats.

This topic is organized as follows:

-   [URL Formats in Use](#url-formats-in-use)
-   [Slash Direction, Trailing Star, and Trailing Slash Sensitivity](#slash-direction-trailing-star-and-trailing-slash-sensitivity)
-   [URL Formats by API and Query](#url-formats-by-api-and-query)
-   [Related topics](#related-topics)

## URL Formats in Use

Third-party protocols are responsible for defining their URL format and defining queries in a manner that conforms to their standard. For example, Microsoft Outlook supports folder names with arbitrary characters, including those that are illegal in URLs such as the `"?"` character. The MAPI protocol handler does its own URL-encoding of its URLs. Hence, the index stores `"%3F"` instead of `"?"` , and Outlook must take this into account when creating queries.

The different formats are listed in the following table and are each assigned a letter identifier for referring to them later in this topic.



| ID  | Local file URL or remote | Example                     |
|-----|--------------------------|-----------------------------|
| A   | Local                    | file:///c:\\test\\example\\ |
| B   | Local                    | file:c:/test/example/       |
| C   | Local                    | c:\\test\\example\\         |
| D   | Remote                   | file:///\\\\server\\share\\ |
| E   | Remote                   | file://server/share/        |
| F   | Remote                   | \\\\server\\share\\         |



 

## Slash Direction, Trailing Star, and Trailing Slash Sensitivity

In Windows Search there is largely no sensitivity to slash direction. If the format `c:\test\example` is accepted, then c:/test/example is accepted as well. However, although [SCOPE](-search-sql-folderdepth.md) is generally insensitive to slash direction, it is sensitive to the slash direction in the case of remote URL format F. Hence, `Scope = '//server/share'` does not work.

The only API that is sensitive to trailing stars and distinguishes between `c:\test\ ` and `c:\test\*` is [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager). If there is an exclusion rule for `c:\test\*`, the URL directory `c:\test` itself will still be indexed. But if the exclusion URL is `c:\test\`, the URL directory `c:\test` itself will not be indexed.

There are two places where Windows Search is sensitive to trailing slashes: ItemUrl and Path queries. If there is a directory `c:\test`, Windows Search treats `c:\test\` differently from `c:\test` for predicates like `path = 'c:\test'` and `System.ItemUrl = 'c:\test'`. For example, the predicate `path='file:c:/test'` would match the directory `c:\test`, but `path='file:c:/test/'` would not, due to the trailing slash.

## URL Formats by API and Query

Local file URL formats accepted by selected APIs and queries are listed in the following table. The formats are associated with a letter (A through F), the meaning of which was denoted in the "[URL Formats in Use](#url-formats-in-use)" section earlier in this topic.



| API or query                                                                                                    | Format A | Format B | Format C |
|-----------------------------------------------------------------------------------------------------------------|----------|----------|----------|
| [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager)                                            | Y        | N        | Y        |
| [**IGatherNotifyInline::OnDataChange**](/previous-versions/windows/desktop/legacy/bb231472(v=vs.85))                           | Y        | Y        | Y        |
| [**ISearchCatalogManager::ReindexMatchingURLs**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-reindexmatchingurls)         | Y        | Y        | Y        |
| [**ISearchCatalogManager::ReindexSearchRoot**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-reindexsearchroot)             | Y        | N        | N        |
| [**ISearchCatalogManager2::PrioritizeMatchingURLs**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager2-prioritizematchingurls) | Y        | Y        | Y        |
| Scope=                                                                                                          | N        | Y        | Y        |
| Directory=                                                                                                      | N        | Y        | Y        |
| ItemUrl=                                                                                                        | N        | Y        | Y        |
| Path=                                                                                                           | N        | Y        | Y        |



 

Remote file URL formats accepted by selected queries are listed in the following table.



| Query                                                                                                           | Format D | Format E | Format F |
|-----------------------------------------------------------------------------------------------------------------|----------|----------|----------|
| [**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager)                                            | N/A      | N/A      | N/A      |
| [**IGatherNotifyInline::OnDataChange**](/previous-versions/windows/desktop/legacy/bb231472(v=vs.85))                           | N/A      | N/A      | N/A      |
| [**ISearchCatalogManager::ReindexMatchingURLs**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-reindexmatchingurls)         | N/A      | N/A      | N/A      |
| [**ISearchCatalogManager::ReindexSearchRoot**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager-reindexsearchroot)             | N/A      | N/A      | N/A      |
| [**ISearchCatalogManager2::PrioritizeMatchingURLs**](/windows/desktop/api/Searchapi/nf-searchapi-isearchcatalogmanager2-prioritizematchingurls) | N/A      | N/A      | N/A      |
| Scope=                                                                                                          | Y        | Y        | Y        |
| Directory=                                                                                                      | Y        | Y        | Y        |
| ItemUrl=                                                                                                        | Y        | Y        | Y        |
| Path=                                                                                                           | Y        | Y        | Y        |



 

## Related topics

<dl> <dt>

[What Is Included in the Index](-search-indexing-process-overview.md)
</dt> <dt>

[Indexing Process in Windows Search](-search-indexing-process-overview.md)
</dt> <dt>

[Querying Process in Windows Search](querying-process--windows-search-.md)
</dt> <dt>

[Notifications Process in Windows Search](-search-3x-wds-support.md)
</dt> </dl>

 

 
