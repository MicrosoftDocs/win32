---
title: ICatalogRead interface
description: Stateless object, does fetch action based on catalog object passed in
ms.assetid: 1f25d0dc-bd4d-45f9-b58a-e5d706b2ed43
keywords:
- ICatalogRead interface HelpAPI
- ICatalogRead interface HelpAPI , described
topic_type:
- apiref
api_name:
- ICatalogRead
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ICatalogRead interface

Stateless object, does fetch action based on catalog object passed in

## Members

The **ICatalogRead** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ICatalogRead** also has these types of members:

-   [Methods](#methods)

### Methods

The **ICatalogRead** interface has these methods.



| Method                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                            |
|:--------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetIndexedTopic**](icatalogread-getindexedtopic.md)                         | method GetIndexedTopic - returns a data stream containing the XHTML data for a topic identified by its topic id in an open catalog<br/>                                                                                                                                                                                                                                          |
| [**GetIndexedTopicDetails**](icatalogread-getindexedtopicdetails.md)           | method GetIndexedTopicDetails - returns an ITopic interface containing the details of a topic identified by its topic id in an open catalog<br/>                                                                                                                                                                                                                                 |
| [**GetKeywords**](icatalogread-getkeywords.md)                                 | method GetKeywords - returns an IKeywordCollection of all of the keywords in the catalog<br/>                                                                                                                                                                                                                                                                                    |
| [**GetLinkedAsset**](icatalogread-getlinkedasset.md)                           | method GetLinkedAsset - returns a data stream containing the requested asset. Asset is identified by its package name and file path within the package within the currently open catalog<br/>                                                                                                                                                                                    |
| [**GetSearchResults**](icatalogread-getsearchresults.md)                       | method GetSearchResults - returns an ITopicCollection for a given query within a catalog. filter is a collection of key/value pairs to refine the search results. Supports paging.<br/>                                                                                                                                                                                          |
| [**GetTableOfContents**](icatalogread-gettableofcontents.md)                   | method GetTableOfContents - returns an ITopicCollection of ToC data. ToC is from the starting point of the topic id and matching the topic locale and topic version (to support multiple locale and versions in a catalog). The return detail can be one of four levels (Children of the topicId, Siblings of the topicId, Ancestors of the topicId, or all ToC Root Nodes)<br/> |
| [**GetTopicDetailsForF1Keyword**](icatalogread-gettopicdetailsforf1keyword.md) | method GetTopicDetailsForF1Keyword - returns an ITopic interface containing the matching topic for the F1 keyword. F1 keywords consists of an array of prioritized F1 keywords<br/>                                                                                                                                                                                              |
| [**GetTopicForF1Keyword**](icatalogread-gettopicforf1keyword.md)               | method GetTopicForF1Keyword - returns a stream containing the matching topic for the F1 keyword in XHTML format. F1 keywords consists of an array of prioritized F1 keywords<br/>                                                                                                                                                                                                |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



 

 





