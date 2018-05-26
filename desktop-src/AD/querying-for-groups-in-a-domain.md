---
title: Querying for Groups in a Domain
description: Groups can be placed in any container or organizational unit in a domain as well as the root of the domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 338a93dd-445d-4f74-a6d6-e5c8ba2e765e
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Querying for Groups in a Domain AD
- Groups AD , Querying for Groups in a Domain
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Querying for Groups in a Domain

Groups can be placed in any container or organizational unit in a domain as well as the root of the domain. Groups may not always be in one container. Therefore, it is necessary to search the entire domain to find all groups in the domain.

To search for all groups in a domain, set the search start point to the root of the domain, set the search scope to subtree and search for all objects that have an [**objectClass**](https://msdn.microsoft.com/library/ms679012) value of "group".

If groups that contain particular [**ADS\_GROUP\_TYPE\_ENUM**](https://msdn.microsoft.com/library/aa772263) values must be found, the **LDAP\_MATCHING\_RULE\_BIT\_AND** matching rule operator can be used to search for groups that have particular bits set in the [**groupType**](https://msdn.microsoft.com/library/ms675935) attribute. For more information about using matching rules, see [Search Filter Syntax](https://msdn.microsoft.com/library/aa746475).

For more information and a code example that shows how to search for groups in a domain, see [Example Code for Searching for Groups in a Domain](example-code-for-performing-a-query-in-a-domain.md).

 

 




