---
title: Enumerating Groups That Contain Many Members
description: Learn about enumerating Azure Active Directory groups that contain many members by using the incremental retrieval of data (range retrieval).
ms.assetid: 78f81b09-2223-4b74-b8d5-7a97494c0324
ms.tgt_platform: multiple
keywords:
- Enumerating Groups That Contain Many Members Active Directory
- groups Active Directory , enumerating groups with many members
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Groups That Contain Many Members

The members of a group are stored in a multi-value attribute called **member**. The **member** attribute can contain a large number of values. Enumerating members can be inefficient when the number of values in a multi-valued attribute becomes large. The server will also limit the maximum number of values that can be retrieved in a single query. This means that if a group may have more members than can be supplied by the server, the only way to enumerate all members is to use incremental retrieval of data, known as *range retrieval*.

Range retrieval involves requesting a limited number of attribute values in a single query. The number of values requested must be less than, or equal to, the maximum number of values supported by the server. To reduce the number of times the query must contact the server, the number of values requested should be as close, as possible, to this maximum. To enable an application to work correctly with all servers, a maximum number of 1000 should be used.

The version of the server that supplies the requested data determines the maximum number of values that can be retrieved in a single query. The following table lists the server version and the maximum number of values that can be retrieved in a single query.



| Server operating system version | Maximum values retrieved |
|---------------------------------|--------------------------|
| Windows 2000                    | 1000                     |
| Windows Server 2003             | 1500                     |



 

For more information about retrieving ranges of attribute values with ADSI, see [Attribute Range Retrieval](/windows/desktop/ADSI/attribute-range-retrieval).

For more information about retrieving ranges of attribute values with [System.DirectoryServices](/dotnet/api/system.directoryservices), see [Enumerating Members in a Large Group](https://msdn.microsoft.com/library/ms180907(v=VS.80).aspx).

 

 