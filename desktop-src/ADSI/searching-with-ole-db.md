---
title: Searching with OLE DB
description: For both Automation clients using ActiveX Data Objects (ADO) and all non-Automation clients, ADSI supplies an OLE DB provider that supports a subset of OLE DB query interfaces.
ms.assetid: f4e48b60-82dd-4c39-879b-0bc8f40747d2
ms.tgt_platform: multiple
keywords:
- Searching with OLE DB ADSI
- queries ADSI , searching with OLE DB
ms.topic: article
ms.date: 05/31/2018
---

# Searching with OLE DB

For both Automation clients using ActiveX Data Objects (ADO) and all non-Automation clients, ADSI supplies an OLE DB provider that supports a subset of OLE DB query interfaces. Client code that already uses OLE DB interfaces for queries can use the same interfaces to query directory services.

Under the OLE DB implementation, a directory service is exposed as a Data Source object. Data Source objects are factories for session objects and support [IDBInitialize](http://go.microsoft.com/fwlink/p/?linkid=83907) to connect to the directory, [IDBCreateSession](http://go.microsoft.com/fwlink/p/?linkid=83905) to create the session object, [IDBProperties](http://go.microsoft.com/fwlink/p/?linkid=83909) to supply authentication data to the underlying namespace and supply the query command and [**IPersist**](https://msdn.microsoft.com/en-us/library/ms688695(v=VS.85).aspx) to save the data necessary to create the data source object to the underlying directory service.

**To perform an Active Directory query using OLE DB**

1.  Retrieve the [IDBInitialize](http://go.microsoft.com/fwlink/p/?linkid=83907) interface from the OLE DB provider. In the case of Active Directory, use the class identifier **CLSID\_ADsDSOObject**.
2.  Build a [DBPROP](http://go.microsoft.com/fwlink/p/?linkid=83894) array of connection data specifying user name and password.
3.  Query the [IDBInitialize](http://go.microsoft.com/fwlink/p/?linkid=83907) interface retrieved in Step 1 for the [IDBProperties](http://go.microsoft.com/fwlink/p/?linkid=83909) interface.
4.  Call the [IDBProperties::SetProperties](http://go.microsoft.com/fwlink/p/?linkid=83908) method passing in the [DBPROP](http://go.microsoft.com/fwlink/p/?linkid=83894) array created in Step 2.
5.  Call the [IDBInitialize::Initialize](http://go.microsoft.com/fwlink/p/?linkid=83906) method to establish the connection to the OLE DB provider; that is the Active Directory provider, in this case.
6.  Query the [IDBInitialize](http://go.microsoft.com/fwlink/p/?linkid=83907) interface for the [IDBCreateSession](http://go.microsoft.com/fwlink/p/?linkid=83905) interface.
7.  Call the [IDBCreateSession::CreateSession](http://go.microsoft.com/fwlink/p/?linkid=83904) method requesting a new interface of type [IDBCreateCommand](http://go.microsoft.com/fwlink/p/?linkid=83902).
8.  Call the [IDBCreateCommand::CreateCommand](http://go.microsoft.com/fwlink/p/?linkid=83903) method to create an [ICommandText](http://go.microsoft.com/fwlink/p/?linkid=83901) interface.
9.  Call the [ICommandText::SetCommandText](http://go.microsoft.com/fwlink/p/?linkid=83900) method. Pass in the preferred dialect and the actual query command text in that dialect. Either **DBGUID\_LDAPDialect** or **DBGUID\_DBSQL** may be used as the dialect.
10. Call [ICommand::Execute](http://go.microsoft.com/fwlink/p/?linkid=83899); an [IRowset](http://go.microsoft.com/fwlink/p/?linkid=83912) interface is returned which is the interface to the result set.
11. Query the [IRowset](http://go.microsoft.com/fwlink/p/?linkid=83912) interface for the [IColumnsInfo](http://go.microsoft.com/fwlink/p/?linkid=83897) interface.
12. Call the [IColumnsInfo::GetColumnInfo](http://go.microsoft.com/fwlink/p/?linkid=83898) method to retrieve column data about the result set.
13. Populate an array of [DBBINDING](http://go.microsoft.com/fwlink/p/?linkid=83893) structures, describing to the OLE DB provider how to expose the data types on a per-column basis to the application code. This step enables you to specify which TYPE is contained in a particular column. Also the offsets of the columns, relative to the returned row, are set here on a column-by-column basis.
14. Query the [IRowset](http://go.microsoft.com/fwlink/p/?linkid=83912) interface for the [IAccessor](http://go.microsoft.com/fwlink/p/?linkid=83896) interface.
15. Call the [IAccessor::CreateAccessor](http://go.microsoft.com/fwlink/p/?linkid=83895) method, which returns an array of accessor handles. This array is then used to access the rows of the result set.
16. Call [IRowset::GetNextRows](http://go.microsoft.com/fwlink/p/?linkid=83911) passing in the row handles, and number of rows to get.
17. Call [IRowset::GetData](http://go.microsoft.com/fwlink/p/?linkid=83910) passing in a row handle, from the set returned in Step 16. A raw pointer to the row is returned.

For more information about the search filter syntax, see [Search Filter Syntax](search-filter-syntax.md).

To read the unprocessed row data returned, use the [DBBINDING](http://go.microsoft.com/fwlink/p/?linkid=83893) structure, created in Step 13, compute the column offsets in the unprocessed data pointer returned in Step 17. Read the status portion of the column for a retrieval result on that column.

For more information and a code example that shows how to search Active Directory using the ADSI OLE DB provider, see [Example Code for Using OLE DB to Search Active Directory](example-code-for-using-ole-db-to-search-active-directory.md).

 

 




