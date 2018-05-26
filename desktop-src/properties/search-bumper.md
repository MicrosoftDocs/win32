---
Description: .
ms.assetid: 8a025bee-65e1-40a7-a269-72a93aca827b
title: Search
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Search

## In this section



| Topic                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [System.Search.AutoSummary](properties.props_system_search_autosummary)<br/>                                         | An automated search system summary of the full text contents of a document, displayed in the search results view in **Search Explorer**. Use this property only when consuming the values in an application, not when providing values to a property handler.<br/>                                                                                                     |
| [System.Search.ContainerHash](properties.props_system_search_containerhash)<br/>                                     | The hash code used to identify attachments to be deleted based on a common container url.<br/>                                                                                                                                                                                                                                                                         |
| [System.Search.Contents](properties.props_system_search_contents)<br/>                                               | The contents of the item. <br/>                                                                                                                                                                                                                                                                                                                                        |
| [System.Search.EntryID](properties.props_system_search_entryid)<br/>                                                 | The entry ID for an item within a given catalog in the Windows Search Index.<br/>                                                                                                                                                                                                                                                                                      |
| [System.Search.ExtendedProperties](properties.props_system_search_extendedproperties)<br/>                           |                                                                                                                                                                                                                                                                                                                                                                              |
| [System.Search.GatherTime](properties.props_system_search_gathertime)<br/>                                           | The Datetime value representing the time when the Windows Search Gatherer process last pushed properties of this document to the Windows Search Gatherer Plugins.<br/>                                                                                                                                                                                                 |
| [System.Search.HitCount](properties.props_system_search_hitcount)<br/>                                               | When using CONTAINS over the Windows Search Index, this is the number of matches of the term. If there are multiple CONTAINS, an AND computes the minimal number of hits, and an OR computes the maximal number of hits.<br/>                                                                                                                                          |
| [System.Search.IsClosedDirectory](properties.props_system_search_iscloseddirectory)<br/>                             | Emitted as **TRUE** by a container item to indicate that its child items do not need to be enumerated by an indexer if the container item has not changed since the last incremental index verification crawl. This contributes to the optimization of indexer performance.<br/>                                                                                       |
| [System.Search.IsFullyContained](properties.props_system_search_isfullycontained)<br/>                               | Emitted as **TRUE** by all child items of a container (such as an e-mail or a compressed file with a .zip name extension) that emits [System.Search.IsClosedDirectory](shell.props_System_Search_IsClosedDirectory) as **TRUE**. This ensures that the child items are included in the search index.<br/>                                                              |
| [System.Search.QueryFocusedSummary](properties.props_system_search_queryfocusedsummary)<br/>                         | The query-focused summary of the document.<br/>                                                                                                                                                                                                                                                                                                                        |
| [System.Search.QueryFocusedSummaryWithFallback](properties.props_system_search_queryfocusedsummarywithfallback)<br/> | The query-focused summary of the document. If none is available, the AutoSummary is returned.<br/>                                                                                                                                                                                                                                                                     |
| [System.Search.QueryPropertyHits](props-system-search-querypropertyhits.md)<br/>                                    | Contains the list of matched properties from a query.<br/>                                                                                                                                                                                                                                                                                                             |
| [System.Search.Rank](properties.props_system_search_rank)<br/>                                                       | Relevance rank of row, with a range from 0-1000. <br/>                                                                                                                                                                                                                                                                                                                 |
| [System.Search.Store](properties.props_system_search_store)<br/>                                                     | The identifier for the protocol handler that produced the item. For example, MAPI, CSC, FILE, and so on.<br/>                                                                                                                                                                                                                                                          |
| [System.Search.UrlToIndex](properties.props_system_search_urltoindex)<br/>                                           | Emitted by a container [**IFilter**](search._search_IFilter) for each child URL within the container. The children are eventually crawled by the indexer if they are within scope.<br/>                                                                                                                                                                                |
| [System.Search.UrlToIndexWithModificationTime](properties.props_system_search_urltoindexwithmodificationtime)<br/>   | This property is the same as [**System.Search.UrlToIndex**](props-system-search-urltoindex.md) except that it includes the time that the URL was last modified. This is an optimization for the indexer so that it does not have to call back into the protocol handler to ask for this information to determine whether the content needs to be indexed again. <br/> |



 

 

 




