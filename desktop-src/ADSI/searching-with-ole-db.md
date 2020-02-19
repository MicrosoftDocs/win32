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

Under the OLE DB implementation, a directory service is exposed as a Data Source object. Data Source objects are factories for session objects and support [IDBInitialize](https://msdn.microsoft.com/library/ms713706.aspx) to connect to the directory, [IDBCreateSession](https://msdn.microsoft.com/library/ms724076.aspx) to create the session object, [IDBProperties](https://msdn.microsoft.com/library/ms719607.aspx) to supply authentication data to the underlying namespace and supply the query command and [**IPersist**](https://msdn.microsoft.com/library/ms688695(v=VS.85).aspx) to save the data necessary to create the data source object to the underlying directory service.

**To perform an Active Directory query using OLE DB**

1.  Retrieve the [IDBInitialize](https://msdn.microsoft.com/library/ms713706.aspx) interface from the OLE DB provider. In the case of Active Directory, use the class identifier **CLSID\_ADsDSOObject**.
2.  Build a [DBPROP](https://msdn.microsoft.com/library/ms717970.aspx) array of connection data specifying user name and password.
3.  Query the [IDBInitialize](https://msdn.microsoft.com/library/ms713706.aspx) interface retrieved in Step 1 for the [IDBProperties](https://msdn.microsoft.com/library/ms719607.aspx) interface.
4.  Call the [IDBProperties::SetProperties](https://msdn.microsoft.com/library/ms723049.aspx) method passing in the [DBPROP](https://msdn.microsoft.com/library/ms717970.aspx) array created in Step 2.
5.  Call the [IDBInitialize::Initialize](https://msdn.microsoft.com/library/ms718026.aspx) method to establish the connection to the OLE DB provider; that is the Active Directory provider, in this case.
6.  Query the [IDBInitialize](https://msdn.microsoft.com/library/ms713706.aspx) interface for the [IDBCreateSession](https://msdn.microsoft.com/library/ms724076.aspx) interface.
7.  Call the [IDBCreateSession::CreateSession](https://msdn.microsoft.com/library/ms714942.aspx) method requesting a new interface of type [IDBCreateCommand](https://msdn.microsoft.com/library/ms711625.aspx).
8.  Call the [IDBCreateCommand::CreateCommand](https://msdn.microsoft.com/library/ms709772.aspx) method to create an [ICommandText](https://msdn.microsoft.com/library/ms714914.aspx) interface.
9.  Call the [ICommandText::SetCommandText](https://msdn.microsoft.com/library/ms709757.aspx) method. Pass in the preferred dialect and the actual query command text in that dialect. Either **DBGUID\_LDAPDialect** or **DBGUID\_DBSQL** may be used as the dialect.
10. Call [ICommand::Execute](https://msdn.microsoft.com/library/ms718095.aspx); an [IRowset](https://msdn.microsoft.com/library/ms720986.aspx) interface is returned which is the interface to the result set.
11. Query the [IRowset](https://msdn.microsoft.com/library/ms720986.aspx) interface for the [IColumnsInfo](https://msdn.microsoft.com/library/ms725401.aspx) interface.
12. Call the [IColumnsInfo::GetColumnInfo](https://msdn.microsoft.com/library/ms722704.aspx) method to retrieve column data about the result set.
13. Populate an array of [DBBINDING](https://msdn.microsoft.com/library/ms716845.aspx) structures, describing to the OLE DB provider how to expose the data types on a per-column basis to the application code. This step enables you to specify which TYPE is contained in a particular column. Also the offsets of the columns, relative to the returned row, are set here on a column-by-column basis.
14. Query the [IRowset](https://msdn.microsoft.com/library/ms720986.aspx) interface for the [IAccessor](https://msdn.microsoft.com/library/ms719672.aspx) interface.
15. Call the [IAccessor::CreateAccessor](https://msdn.microsoft.com/library/ms720969.aspx) method, which returns an array of accessor handles. This array is then used to access the rows of the result set.
16. Call [IRowset::GetNextRows](https://msdn.microsoft.com/library/ms709827.aspx) passing in the row handles, and number of rows to get.
17. Call [IRowset::GetData](https://msdn.microsoft.com/library/ms716988.aspx) passing in a row handle, from the set returned in Step 16. A raw pointer to the row is returned.

For more information about the search filter syntax, see [Search Filter Syntax](search-filter-syntax.md).

To read the unprocessed row data returned, use the [DBBINDING](https://msdn.microsoft.com/library/ms716845.aspx) structure, created in Step 13, compute the column offsets in the unprocessed data pointer returned in Step 17. Read the status portion of the column for a retrieval result on that column.

For more information and a code example that shows how to search Active Directory using the ADSI OLE DB provider, see [Example Code for Using OLE DB to Search Active Directory](example-code-for-using-ole-db-to-search-active-directory.md).

 

 




