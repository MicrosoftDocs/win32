---
title: Asynchronous Searches
description: Enabling asynchronous (async) search results in a call to GetFirstRow or the first call to GetNextRow blocks until the first entry is returned from the server.
ms.assetid: f80e2c62-71c5-4a05-bd17-465962be3c2d
ms.tgt_platform: multiple
keywords:
- Asynchronous Searches ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Searches

Enabling asynchronous (async) search results in a call to **GetFirstRow** or the first call to **GetNextRow** blocks until the first entry is returned from the server. That is, if the search on the server requires much time, the first few results are returned quickly. This can help when populating a list box with search results. Search results are displayed as they are returned.

If async is disabled, the first call to **GetFirstRow** or **GetNextRow** will block until the server computes the entire result set and returns. Only then is the first row returned. This is not recommended if the result set is expected to be large.

If both paging and async are enabled, the first call to **GetFirstRow** or **GetNextRow** will block until the server generates and sends the first page of results. If a reasonable page size was set, results will appear immediately. More importantly, if the search results are expected to be very large, and you search for a particular entry, it is not required that you request more results from the server after you have found the entries that interest you.

A paged async search provides fine control of a search. This is useful if the search results may be very large and require extensive time from the server.

For more information about using asynchronous searches with a specific search interface, see:

-   [Synchronous and Asynchronous Searches with IDirectorySearch](synchronous-and-asynchronous-searches-with-idirectorysearch.md)
-   [Searching with ActiveX Data Objects](searching-with-activex-data-objects-ado.md)
-   [Searching with OLE DB](searching-with-ole-db.md)

 

 




