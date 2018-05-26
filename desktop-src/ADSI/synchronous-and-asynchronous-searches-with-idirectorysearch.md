---
title: Synchronous and Asynchronous Searches with IDirectorySearch
description: When you perform a search using the IDirectorySearch interface, the IDirectorySearch ExecuteSearch method does not send the search request to the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c4387202-22a0-497a-af0a-20aa8ede905d
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Synchronous and Asynchronous Searches with IDirectorySearch ADSI
- ADSI, Searching, IDirectorySearch, Other Search Options, Synchronous and Asynchronous Searches
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Synchronous and Asynchronous Searches with IDirectorySearch

When you perform a search using the [**IDirectorySearch**](/windows/win32/Iads/nn-iads-idirectorysearch?branch=master) interface, the [**IDirectorySearch::ExecuteSearch**](/windows/win32/Iads/nf-iads-idirectorysearch-executesearch?branch=master) method does not send the search request to the server. This method only saves the search parameters. The search request is actually sent when you call [**IDirectorySearch::GetFirstRow**](/windows/win32/Iads/nf-iads-idirectorysearch-getfirstrow?branch=master) or [**IDirectorySearch::GetNextRow**](/windows/win32/Iads/nf-iads-idirectorysearch-getnextrow?branch=master).

For Active Directory searches, the primary difference between synchronous and asynchronous is when the first row of the result is returned, that is, when the first [**GetFirstRow**](/windows/win32/Iads/nf-iads-idirectorysearch-getfirstrow?branch=master) or [**GetNextRow**](/windows/win32/Iads/nf-iads-idirectorysearch-getnextrow?branch=master) call returns.

In a synchronous search, if paging is not enabled, the first row is returned when the server has constructed and returned the entire result set to the client. If paging is enabled, the first row is returned when the first page of the result set is returned.

In an asynchronous search, if paging is not enabled, the first row is returned when the server has constructed the first row of the result set. If paging is enabled, the first row is returned when the first page of the result set is returned.

The default search type is synchronous. To specify an asynchronous search, set an **ADS\_SEARCHPREF\_ASYNCHRONOUS** search option with an **ADSTYPE\_BOOLEAN** value of **TRUE** in the [**ADS\_SEARCHPREF\_INFO**](/windows/win32/Iads/ns-iads-ads_searchpref_info?branch=master) array passed to the [**IDirectorySearch::SetSearchPreference**](/windows/win32/Iads/nf-iads-idirectorysearch-setsearchpreference?branch=master) method. This operation is shown in the following code example.


```C++
ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_ASYNCHRONOUS;
SearchPref.vValue.dwType = ADSTYPE_BOOLEAN;
SearchPref.vValue.Boolean = TRUE;
```



 

 




