---
title: Distributed Query
description: Because ADSI is an OLE DB Provider, it can participate in Distributed Query introduced in Microsoft SQL Server 7.0.
ms.assetid: 0a93ec2e-397a-47f7-b00c-f0f9aaa06de6
ms.tgt_platform: multiple
keywords:
- queries ADSI , distributed query
ms.topic: article
ms.date: 05/31/2018
---

# Distributed Query

Because ADSI is an OLE DB Provider, it can participate in Distributed Query introduced in Microsoft SQL Server 7.0. The following are possible scenarios:

-   Joining Active Directory objects with SQL Server data.
-   Updating SQL data from Active Directory objects.
-   Creating three-way or four-way joins with other OLE DB Providers. For example, Index Server, SQL Server, and Active Directory.

The OLE DB Provider supports two command dialects, LDAP and SQL, to access the directory service and return results in a tabular form that can be queried with SQL Server distributed queries.

**To start the SQL Query Analyzer**

1.  First, open the [SQL Query Analyzer](https://msdn.microsoft.com/library/Aa216983.aspx) on the SQL Server that is linked to the directory service (see Creating a Linked Server).
2.  Run the **SQL Query Analyzer** (Start \| Programs \| Microsoft SQL Server 7.0)
3.  Log on to the SQL Server computer.
4.  Enter the SQL Query into the Editor pane of the query window.
5.  Execute the query by pressing F5.

The following sections provide more detail:

-   [Creating a Linked Server](#creating-a-linked-server)
-   [Creating a SQL Server Authenticated Login](#creating-a-sql-server-authenticated-login)
-   [Querying the Directory Service](#querying-the-directory-service)

## Creating a Linked Server

To set up a distributed join on a Windows 2000 Server directory service, create a linked server. To do this, set up ADSI mapping by using the [sp\_addlinkedserver](https://msdn.microsoft.com/library/Aa259589.aspx) System Stored Procedure. This procedure links a name to an OLE DB Provider name.

In the following example, note that there are several arguments used with the [sp\_addlinkedserver](https://msdn.microsoft.com/library/Aa259589.aspx) System Stored Procedure:

-   "ADSI" is the **server** argument and will be the name of this linked server.
-   "Active Directory Services 2.5" is the **srvproduct** argument, which is the name of the OLE DB data source that you are adding as a linked server.
-   "ADSDSOObject" is the **provider\_name** argument.
-   "adsdatasource" is the **data\_source** argument, which is the name of the data source as interpreted by the OLE DB Provider.

The [EXEC](https://msdn.microsoft.com/library/Aa258848.aspx) command is used to execute System Stored Procedures.


```sql
EXEC sp_addlinkedserver 'ADSI', 'Active Directory Services 2.5', 
'ADSDSOObject', 'adsdatasource'
GO
```



For Windows-authenticated logins, the self-mapping is sufficient to access the directory with SQL Server Security Delegation. Because the self-mapping is created by default for linked servers created through [sp\_addlinkedserver](https://msdn.microsoft.com/library/Aa259589.aspx), no other login mapping is necessary.

For SQL Server–authenticated logins, you can configure suitable logins and passwords for connecting to the directory service by using the [sp\_addlinkedsrvlogin](https://msdn.microsoft.com/library/Aa259581.aspx) System Stored Procedure.

> [!Note]  
> When possible, use Windows Authentication.

 

## Creating a SQL Server Authenticated Login

If you prefer to use a SQL Server–authenticated login rather than Windows Authentication, add a login to the linked server (see the previous section). To do this, use the [sp\_addlinkedsrvlogin](https://msdn.microsoft.com/library/Aa259581.aspx) System Stored Procedure.

In the following example, there are several arguments that are used with the [sp\_addlinkedsrvlogin](https://msdn.microsoft.com/library/Aa259581.aspx) System Stored Procedure:

-   "ADSI" is the **rmtsvrname** argument, which is the name of the linked server created in the previous example.
-   "Fabrikam\\Administrator" is the **locallogin** argument, which is the login on the local server and can be the SQL Server login or a Windows NT user.
-   "CN=Administrator,OU=Sales,DC=activeds,DC=Fabrikam,DC=com" is the **rmtuser** argument, which is the user name that you use to connect because **useself** is **false**.
-   "secret\*\*2000" is the **rmtpassword**, which is the password associated to **rmtuser**

The [EXEC](https://msdn.microsoft.com/library/Aa258848.aspx) command is used to execute System Stored Procedures.


```sql
EXEC sp_addlinkedsrvlogin 'ADSI', false, 'Fabrikam\Administrator', 
'CN=Administrator,OU=Sales,DC=activeds,DC=Fabrikam,DC=com', 'secret**2000'
```



## Querying the Directory Service

After you have created a linked server, use an [OPENQUERY](https://msdn.microsoft.com/library/Aa276848.aspx) statement to send a query to the Directory Service. The following SQL query creates a virtual table to hold your query results by using the [CREATE VIEW](https://msdn.microsoft.com/library/Aa258253.aspx) statement. The view that is created is named "viewADContacts".

The first [SELECT](https://msdn.microsoft.com/library/Aa259187.aspx) statement defines the information that is being queried from the directory service and maps it to a column in the table. Information surrounded by brackets indicates the data that is put into the virtual table. The information that is not in brackets indicates the data that is retrieved from the directory service. Notice that the information that is being retrieved from the directory service must be referenced by its LDAP display name.

The next statement is the [OPENQUERY](https://msdn.microsoft.com/library/Aa276848.aspx) statement. This statement has two arguments: ADSI, which is the name of the linked server that you created, and a query statement. The query statement contains the following items:

-   The [SELECT](https://msdn.microsoft.com/library/Aa259187.aspx) statement contains the list of data that will be obtained from the directory service. You will need to use the LDAP display name to indicate which data you are searching for.
-   The [FROM](https://msdn.microsoft.com/library/Aa258869.aspx) statement contains the name of the linked directory server where this information will be obtained from.
-   The [WHERE](https://msdn.microsoft.com/library/Aa260674.aspx) statement provides the search conditions. In this example, it is searching for contacts.

The final [SELECT](https://msdn.microsoft.com/library/Aa259187.aspx) statement is used to pick up results from the view to display.


```sql
CREATE VIEW viewADContacts
AS
SELECT  [Name], sn [Last Name], street [Street], l [City], st [State]
FROM OPENQUERY( ADSI, 
     'SELECT name, sn, street, l, st
      FROM 'LDAP:// OU=Sales,DC=activeds,DC=Fabrikam,DC=Com'
      WHERE objectCategory='Person' AND 
      objectClass = 'contact'')
GO
SELECT * FROM viewADContacts
```



 

 




