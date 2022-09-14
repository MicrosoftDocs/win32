---
title: Using ADO for Range Retrieval
description: If an automation language is used, the ActiveX Directory Objects (ADO) should be used to retrieve a range of property values.When using ADO for range retrieval, there is one problem that must be specifically addressed.
ms.assetid: ca06169d-7de7-4552-aa7d-e9427353e49e
ms.tgt_platform: multiple
keywords:
- Using ADO for Range Retrieval ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Using ADO for Range Retrieval

If an automation language is used, the ActiveX Directory Objects (ADO) should be used to retrieve a range of property values.

When using ADO for range retrieval, there is one problem that must be specifically addressed. When querying for the final group of property values, the ADO object will retrieve zero objects, even though more remain. To retrieve the remaining values, use the range wildcard '\*'. For example, if a group contains 150 members, member values 0-100 can be retrieved normally using ranged retrieval. If range 101-200 is then requested, the ADO object will return zero objects. At this point, it is necessary to modify the query to request range 101-\*. This will retrieve values from 101 to 150. For more information and a code example, see [Example Code for Using Ranging to Retrieve Members of a Group](example-code-for-using-ranging-to-retrieve-members-of-a-group.md).

For more information about using ADO for range retrieval, see:

-   [ADO LDAP Ranging Dialect](ado-ldap-ranging-dialect.md)
-   [ADO SQL Ranging Dialect](ado-sql-ranging-dialect.md)
-   [Example Code for Using Ranging to Retrieve Members of a Group](example-code-for-using-ranging-to-retrieve-members-of-a-group.md)

 

 




