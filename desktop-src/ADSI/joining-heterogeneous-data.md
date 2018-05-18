---
title: Joining Heterogeneous Data
description: Typical organizations store data in multiple heterogeneous databases. Human Resources data may be stored in SQL Server, while account management data is stored in the directory. Other data may be stored in proprietary formats.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '45281b42-5cb2-42f9-9c7c-f3e3174b0f9d'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# Joining Heterogeneous Data

Typical organizations store data in multiple heterogeneous databases. Human Resources data may be stored in SQL Server, while account management data is stored in the directory. Other data may be stored in proprietary formats.

With, SQL Server 7.0, ADSI, and the OLE DB Provider, it is possible to join data from Active Directory to data in SQL Server and create a view of the joined data.

**To join Active Directory Data with SQL Server Data**

1.  Run the **SQL Query Analyzer** (Start \| Programs \| Microsoft SQL Server 7.0)
2.  Log on to the SQL Server computer.
3.  Execute the following line (by highlighting it and pressing CTRL+E):

    ```sql
    EXEC sp_addlinkedserver 'ADSI', 'Active Directory Service Interfaces', 
    'ADSDSOObject', 'adsdatasource'
    GO
    ```

    

    In this line, the arguments for the [sp\_addlinkedserver](http://go.microsoft.com/fwlink/p/?linkid=83926) System Stored Procedure are as follows:

    -   " ADSI" is the **server** argument, which will be the name of this linked server.
    -   "Active Directory Services" is the **srvproduct** argument, which is the name of the OLE DB data source that you are adding as a linked server.
    -   "ADSDSOObject" is the **provider\_name** argument and indicates you are using the OLE DB Provider.
    -   "adsdatasource" is the **data\_source argument**, which is the name of the data source as interpreted by the OLE DB Provider.

    You can now use the linked server to access Active Directory from SQL Server.

4.  The next example performs a query using the [OPENQUERY](http://go.microsoft.com/fwlink/p/?linkid=83923) statement. This statement has two arguments: ADSI, which is the name of the linked server that you just created, and a query statement. The query statement contains the following items:

    -   The [SELECT](http://go.microsoft.com/fwlink/p/?linkid=83924) statement contains the list of data that will be obtained from the directory service. You will need to use the LDAP display name to indicate which data you are searching for.
    -   The [FROM](http://go.microsoft.com/fwlink/p/?linkid=83922) statement contains the name of the linked directory server where this information will be obtained from.
    -   The [WHERE](http://go.microsoft.com/fwlink/p/?linkid=83927) statement provides the search conditions. In this example, it is searching for users.

    Type and execute:

    ```sql
    SELECT * FROM OPENQUERY( ADSI, 
        'SELECT name, adsPath 
         FROM 'LDAP://DC=Fabrikam,DC=com' 
         WHERE objectCategory = 'Person' AND objectClass= 'user'')
    ```

    

    You can also use the ADSI [LDAP dialect](ldap-dialect.md). For example:

    ```sql
    SELECT * FROM OPENQUERY(ADSI,
        '<LDAP://DC=Fabrikam,DC=COM>;(&amp;(objectCategory=Person)(objectClass=user));name, adspath;subtree')
    ```

    

    In the previous example, the LDAP query has four parts:

    -   "&lt;LDAP://DC=Fabrikam,DC=COM&gt;" is the distinguished name of the directory server to search.
    -   "(&(objectCategory=Person)(objectClass=user))" is the LDAP search filter (see [Search Filter Syntax](search-filter-syntax.md)).
    -   "name, adspath" are the names (using the LDAP display name format) of the attributes to retrieve.
    -   "subtree" indicates the [scope](scope-of-query.md) of the search.

## Related topics

<dl> <dt>

[Creating and Executing a View](creating-and-executing-a-view.md)
</dt> </dl>

 

 




