---
title: ADO SQL Ranging Dialect
description: When using the ActiveX Directory Objects (ADO), using the SQL dialect, single quotation marks (') must be used around the attribute and range specifier.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '0453aa9e-ed35-45ff-a728-e854bf0bb353'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["ADO SQL Ranging Dialect ADSI"]
---

# ADO SQL Ranging Dialect

When using the ActiveX Directory Objects (ADO), using the SQL dialect, single quotation marks (') must be used around the attribute and range specifier. The following is an example of the ADO SQL dialect.


```sql
Command.CommandText = "select Name, 'member;Range=0-50' from 'LDAP://CN=Group1,DC=Fabrikam,DC=Com' where objectCategory='group'"
```



 

 




