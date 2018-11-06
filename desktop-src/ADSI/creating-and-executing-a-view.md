---
title: Creating and Executing a View
description: You can create a view for data obtained from Active Directory. Be aware that only the view definition is stored in SQL Server, and not the actual result set. Therefore, you may get a different result when you invoke the view at a later time.
ms.assetid: c2892517-11e1-489f-a2f2-5118bccd605b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Executing a View

You can create a view for data obtained from Active Directory. Be aware that only the view definition is stored in SQL Server, and not the actual result set. Therefore, you may get a different result when you invoke the view at a later time.

The following code sample shows how to create a view.


```sql
CREATE VIEW viewADUsers 
AS
SELECT * FROM OpenQuery( ADSI,
    '<LDAP://DC=Fabrikam,DC=com>;(&(objectCategory=Person)(objectClass=user));name, adspath, title;subtree')
```



Use the following code to invoke a view.


```sql
SELECT * from viewADUsers
```



## Related topics

<dl> <dt>

[Creating a Heterogeneous Join between SQL Server and Active Directory](creating-a-heterogeneous-join-between-sql-server-and-active-directory.md)
</dt> </dl>

 

 




