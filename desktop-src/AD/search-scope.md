---
title: Specifying the Search Scope
description: You can specify the scope of a search as either a base, one-level, or subtree search.
ms.assetid: b02354c2-7b95-4911-8ae3-4a261d3ca2d3
ms.tgt_platform: multiple
keywords:
- Specifying the Search Scope AD
- Active Directory,searching,specifying the search scope
ms.topic: article
ms.date: 05/31/2018
---

# Specifying the Search Scope

You can specify the scope of a search as either a base, one-level, or subtree search. Use the **ADS\_SEARCHPREF\_SEARCH\_SCOPE** flag with the values of the [**ADS\_SCOPEENUM**](/windows/win32/api/iads/ne-iads-ads_scopeenum) enumeration to specify the search scope. The following list includes descriptions of the search types:

-   **Base**. A base search limits the search to the base object. The maximum number of objects returned is always one. This search is useful to verify the existence of an object for retrieving group membership. For example, if you have an object distinguished name, and you must verify the object's existence based on the path, you can use a one-level search. If the search fails, you can assume that the object may have been renamed or moved to a different location, or you were given the wrong information about the object. Be aware that you should store the globally unique identifier (GUID) of the object instead of the distinguished name, if you wish to revisit an object. The GUID will always reference the same object, regardless of where the object is located within the directory hierarchy.
-   **One-level**. A one-level search is restricted to the immediate children of a base object, but excludes the base object itself. This setting can perform a targeted search for immediate child objects of a parent object. For example, consider a parent object P1 and its immediate children: C1, C2, and C3. A one-level search evaluates C1, C2, and C3 against the search criteria, but does not evaluate P1. Use a one-level search to enumerate all children of an object. An [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) enumeration translates to a one-level search.
-   **Subtree**. A subtree search (or a deep search) includes all child objects as well as the base object. You can request the LDAP provider to chase referrals to other LDAP directory services, including other directory domains or forests.

 

 