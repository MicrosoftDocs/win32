---
title: ADO LDAP Ranging Dialect
description: When using ActiveX Directory Objects (ADO) with the LDAP dialect, the attribute and range specifier do not require quotation marks.
ms.assetid: adda9cf7-6588-48ee-85e2-fddbaf28807b
ms.tgt_platform: multiple
keywords:
- ADO LDAP Ranging Dialect ADSI
ms.topic: article
ms.date: 05/31/2018
---

# ADO LDAP Ranging Dialect

When using ActiveX Directory Objects (ADO) with the LDAP dialect, the attribute and range specifier do not require quotation marks.

The following is an example of the ADO LDAP dialect.


```C++
Command.Text = "<LDAP://CN=NewGroup,DC=Fabrikam,DC=Com>;(objectCategory=group);name,member;Range=51-*;base"
```



 

 




