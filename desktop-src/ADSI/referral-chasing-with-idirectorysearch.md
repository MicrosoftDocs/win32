---
title: Referral Chasing with IDirectorySearch
description: A referral is the mechanism that a directory server uses to direct a client to another server when it does not contain sufficient data about the object requested by a query.
ms.assetid: ef97eafd-5227-4dd7-9f8a-6b4591261f79
ms.tgt_platform: multiple
keywords:
- Referral Chasing with IDirectorySearch ADSI
- ADSI, Searching, IDirectorySearch, Other Search Options, Referral Chasing
ms.topic: article
ms.date: 05/31/2018
---

# Referral Chasing with IDirectorySearch

A referral is the mechanism that a directory server uses to direct a client to another server when it does not contain sufficient data about the object requested by a query.

In a one-level or subtree search, referrals are returned for known, immediately subordinate domain, schema, or configuration containers only; that is, child domains that are direct descendants. For more information, see [Search Scope](/windows/desktop/AD/search-scope).

In a directory, not all data is available on a single server, rather, it is distributed over several different servers across the network. If the servers share the data that other servers can provide, they can provide referrals to a client when a requested query cannot be resolved on the originating server. For example, when a client asks Server A to query a user object (U), then A can suggest that the client continue the search on Server B if U does not reside on A, but is identified to be on B. The client has the choice to pursue the referral or not. Referrals free the client from having to possess previous knowledge of the capability of each server, but the client must specify the type of referrals a server should perform.

To enable or disable referral chasing, set an **ADS\_SEARCHPREF\_CHASE\_REFERRALS** search option with an **ADSTYPE\_INTEGER** value that contains one of the [**ADS\_CHASE\_REFERRALS\_ENUM**](/windows/win32/api/iads/ne-iads-ads_chase_referrals_enum) enumeration values in the [**ADS\_SEARCHPREF\_INFO**](/windows/desktop/api/Iads/ns-iads-ads_searchpref_info) array passed to the [**IDirectorySearch::SetSearchPreference**](/windows/desktop/api/Iads/nf-iads-idirectorysearch-setsearchpreference) method.

The following code example shows how to enable chase referrals.


```C++
ADS_SEARCHPREF_INFO SearchPref;
SearchPref.dwSearchPref = ADS_SEARCHPREF_CHASE_REFERRALS;
SearchPref.vValue.dwType = ADSTYPE_INTEGER;
SearchPref.vValue.Integer = ADS_CHASE_REFERRALS_ALWAYS;
```



For more information about referrals in Active Directory, see [Referrals](/windows/desktop/AD/referrals).

 

 