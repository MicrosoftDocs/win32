---
title: Retrieving Large Results Sets
description: When there is the possibility that the result set that will be returned will contain more than 1000 items, you must use a paged search.
ms.assetid: 1439d6b8-50dd-4d37-bcc9-dd0f63af865f
ms.tgt_platform: multiple
keywords:
- Retrieving Large Results Sets ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Large Results Sets

When there is the possibility that the result set that will be returned will contain more than 1000 items, you must use a paged search. Searches of Active Directory performed without paging are limited to returning a maximum of the first 1000 records. With a paged search, the result set is presented as individual pages, each containing a predetermined number of result entries. With this type of search, new pages of result entries are returned until the end of the result set is reached.

By default, the server that responds to a query request completely calculates a result set before returning data. In a large result set, this requires server memory as the result set is acquired, and network bandwidth when the large result is returned. Setting a page size allows the server to send the data in pages as the pages are being built. The client then caches this data and provides a cursor to the application level code. Paging is set by defining how many rows the server calculates before the data is returned over the network to the client.

Paged searching offers benefits to both the client and the server. For example, the client can be more responsive in presenting the results to end users. This is especially relevant for graphical user interface tools that can display data while another thread concurrently receives more data from the server.

When you set up your query, if you specify a sort order for your result set, then the server must completely calculate the result set before returning the data to the client, which impacts the response time for the query.

On the server side, paged searching makes the operation scalable. For example, if one hundred clients issue search requests simultaneously and, on the average, each client is returned two hundred objects, if page size is not specified, the server must have sufficient memory to hold the complete result set of 20,000 entries. Alternately, if each client specified a page size of ten objects, the memory requirements on the server would be reduced by a factor of 20.

> [!Note]  
> Not all directory services support paged searches. Active Directory implements page size architecture.

 

Many directory servers specify an Administrative Limit for the maximum number of objects they can return if a client does not specify the page size. When the Administrative Limit is reached, ADSI generates the **ERROR\_DS\_ADMIN\_LIMIT\_EXCEEDED** Win32 error.

On the client side, a paged search allows a client to stop the operation while it is still in progress. By contrast, in a non-paged search, the client is blocked until the data is completely returned, or an error occurs. This could impact network performance if the result set turns out to be larger and takes more time than expected.

On behalf of the client, ADSI handles the page size transparently. The client does not have to count the number of objects in progress. ADSI encapsulates the server interaction for the client. From the client perspective, the search returns a complete result set.

For more information about using the search time out option with a specific search interface, see:

-   [Paging with IDirectorySearch](paging-with-idirectorysearch.md)
-   [Searching with ActiveX Data Objects](searching-with-activex-data-objects-ado.md)
-   [Searching with OLE DB](searching-with-ole-db.md)

A paged search is transparent to your application because ADSI automatically continues to retrieve additional pages of results until it reaches the end of the result set or the end of the time limit that you set. When you use a paged search, the size limit does not override page size. Size limit can only be used when you retrieve a result set that contains fewer than 1000 entries.

 

 




