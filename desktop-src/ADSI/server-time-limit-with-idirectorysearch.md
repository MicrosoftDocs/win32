---
title: Server Time Limit with IDirectorySearch
description: To avoid using all the CPU time and preventing other operations from running, specify the search time limit to a small value and then rerun the application later if it fails to generate the report.
ms.assetid: 0fd4d8a2-36fc-4179-aeee-1cd3f3996e19
ms.tgt_platform: multiple
keywords:
- Server Time Limit with IDirectorySearch ADSI
- ADSI, Searching, IDirectorySearch, Other Search Options, Server Time Limit
ms.topic: article
ms.date: 05/31/2018
---

# Server Time Limit with IDirectorySearch

When you request a search on a busy server, you may want to request that the server to restrict the search to a specified time limit. For example, you want to run an application to generate a weekly report on a server that is running near its capacity. To avoid using all the CPU time and preventing other operations from running, specify the search time limit to a small value and then rerun the application later if it fails to generate the report.

Some servers might impose their own administrative time limit. In these cases, if you specify a search time limit value greater than the administrative time limit, the server will ignore your specification and use its internal time limit value instead.

The default for the server time limit is no limit. To set a server time limit, set an **ADS\_SEARCHPREF\_TIME\_LIMIT** search option with an **ADSTYPE\_INTEGER** value that contains the server time limit, in seconds, in the [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) array passed to the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method. This operation is shown in the following code example. A server time limit of zero indicates no time limit.


```C++
ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_TIME_LIMIT;
SearchPref.vValue.dwType = ADSTYPE_INTEGER;
SearchPref.vValue.Integer = 10;
```



 

 




