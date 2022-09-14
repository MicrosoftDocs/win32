---
title: Querying for Groups in a Domain
description: Groups can be placed in any container or organizational unit in a domain as well as the root of the domain.
ms.assetid: 338a93dd-445d-4f74-a6d6-e5c8ba2e765e
ms.tgt_platform: multiple
keywords:
- Querying for Groups in a Domain AD
- Groups AD , Querying for Groups in a Domain
ms.topic: article
ms.date: 05/31/2018
---

# Querying for Groups in a Domain

Groups can be placed in any container or organizational unit in a domain as well as the root of the domain. Groups may not always be in one container. Therefore, it is necessary to search the entire domain to find all groups in the domain.

To search for all groups in a domain, set the search start point to the root of the domain, set the search scope to subtree and search for all objects that have an [**objectClass**](/windows/desktop/ADSchema/a-objectclass) value of "group".

If groups that contain particular [**ADS\_GROUP\_TYPE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_group_type_enum) values must be found, the **LDAP\_MATCHING\_RULE\_BIT\_AND** matching rule operator can be used to search for groups that have particular bits set in the [**groupType**](/windows/desktop/ADSchema/a-grouptype) attribute. For more information about using matching rules, see [Search Filter Syntax](/windows/desktop/ADSI/search-filter-syntax).

For more information and a code example that shows how to search for groups in a domain, see [Example Code for Searching for Groups in a Domain](example-code-for-performing-a-query-in-a-domain.md).

 

 