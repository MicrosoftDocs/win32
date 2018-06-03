---
title: Help API Reference
description: The Help API enables opening help catalogs and retrieving help content items such as indexed help topics (XHTML, HTML)non-indexed imagesCSS filesJavaScriptaudio/video elements.
ms.assetid: 0F12204C-0451-4883-B28B-15C2312147B2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Help API Reference

The Help API enables opening help catalogs and retrieving help content items such as:

-   indexed help topics (XHTML, HTML)
-   non-indexed images
-   CSS files
-   JavaScript
-   audio/video elements

## In this section



| Topic                                                             | Description                                                                              |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [**ICatalog**](icatalog.md)<br/>                           | State object, holds open catalog and all info about catalog<br/>                   |
| [**ICatalogRead**](icatalogread.md)<br/>                   | Stateless object, does fetch action based on catalog object passed in<br/>         |
| [**ICatalogReadWriteLock**](icatalogreadwritelock.md)<br/> | Catalog lock state object, holds catalog lock and all info about catalog lock<br/> |
| [**IHelpFilter**](ihelpfilter.md)<br/>                     | Collection of filter criteria name/value pairs<br/>                                |
| [**IHelpKeyValuePair**](ihelpkeyvaluepair.md)<br/>         | Key/value pair for IHelpFilter objects<br/>                                        |
| [**IKeyword**](ikeyword.md)<br/>                           | Help Keyword interface, contains methods to retrieve keyword information<br/>      |
| [**IKeywordCollection**](ikeywordcollection.md)<br/>       | Collection of IKeyword interfaces<br/>                                             |
| [**ITopic**](itopic.md)<br/>                               | Help topic interface, contains methods to retrieve topic information<br/>          |
| [**ITopicCollection**](itopiccollection.md)<br/>           | Collection of ITopics<br/>                                                         |
| [**IndexException**](indexexception.md)<br/>               | An interface that inherits from the **IDispatch** interface.<br/>                  |



 

 

 





