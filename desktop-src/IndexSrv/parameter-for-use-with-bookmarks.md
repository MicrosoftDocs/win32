---
Description: Parameter for Use with Bookmarks
ms.assetid: c3f0af10-1c45-413b-bf08-55ed05c7f343
title: Parameter for Use with Bookmarks
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Parameter for Use with Bookmarks

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The CiBookmarkSkipCount variable (described in the following table) is used in conjunction with CiBookmark to set an offset from the previous page of the query. It cannot be set in the .idq file; it should be set as a form variable. See [HTML Extension Files](html-extension-files.md) for examples.

The following variable can be set as a CGI variable, for navigating between pages:



| Variable Name                                                                                                       | Meaning                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| <span id="_idxs_cibookmarkskipcount_var"></span><span id="_IDXS_CIBOOKMARKSKIPCOUNT_VAR"></span>CiBookmarkSkipCount | Signed number of rows to skip for the next page. Negative means “skip backward,” positive means “skip forward.” |



 

 

 



