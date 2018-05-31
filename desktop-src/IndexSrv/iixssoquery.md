---
title: IixssoQuery interface
description: The Query object of Indexing Service supports methods and properties that allow you to formulate a query and define an ActiveX Data Objects (ADO) recordset to manage and display the results of the query.
ms.assetid: 9cd79cd0-eff9-4e8f-a4a2-48d182aae668
keywords:
- IixssoQuery interface Indexing Service
- IixssoQuery interface Indexing Service , described
topic_type:
- apiref
api_name:
- IixssoQuery
- IixssoQuery.OnStartPage
- IixssoQuery.StartHit
- IixssoQuery.get_StartHit
- IixssoQuery.put_StartHit
- IixssoQuery.ResourceUseFactor
- IixssoQuery.get_ResourceUseFactor
- IixssoQuery.put_ResourceUseFactor
api_location:
- Ixsso.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IixssoQuery interface

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

The Query object of Indexing Service supports methods and properties that allow you to formulate a query and define an ActiveX Data Objects (ADO) recordset to manage and display the results of the query.

The programmatic identifier (ProgID) for the query object is the literal value IXSSO.Query.2. The version-independent ProgID is IXSSO.Query.

## Members

The **IixssoQuery** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IixssoQuery** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IixssoQuery** interface has these methods.



| Method                                                 | Description                                                                                               |
|:-------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**AddScopeToQuery**](iixssoquery-addscopetoquery.md) | Adds a search path to a query.<br/>                                                                 |
| [**CreateRecordset**](iixssoquery-createrecordset.md) | Execute the query, creating an OLE DB results table or an Microsoft ActiveX Directory Object. <br/> |
| [**DefineColumn**](iixssoquery-definecolumn.md)       | Defines a column to be used in the query.<br/>                                                      |
| **OnStartPage**                                        | Reserved for internal use.<br/>                                                                     |
| [**QueryToURL**](iixssoquery-querytourl.md)           | Creates the query string portion of a URL from the the internal state of the query properties.<br/> |
| [**Reset**](iixssoquery-reset.md)                     | Clears the state of the query object.<br/>                                                          |
| [**SetQueryFromURL**](iixssoquery-setqueryfromurl.md) | Sets Query and other properties from the query string.<br/>                                         |



 

### Properties

The **IixssoQuery** interface has these properties.



| Property                                                            | Access type           | Description                                                                                                                     |
|:--------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| [**AllowEnumeration**](iixssoquery-allowenumeration.md)<br/> | Read/write<br/> | Indicates whether enumeration is allowed.<br/>                                                                            |
| [**Catalog**](iixssoquery-catalog.md)<br/>                   | Read/write<br/> | The index catalog name.<br/>                                                                                              |
| [**CiFlags**](iixssoquery-ciflags.md)<br/>                   | Read-only<br/>  | The flags. This is a deprecated property; use [**AddScopeToQuery**](iixssoquery-addscopetoquery.md) instead.<br/>        |
| [**CiScope**](iixssoquery-ciscope.md)<br/>                   | Read-only<br/>  | The catalog path. This is a deprecated property; use [**AddScopeToQuery**](iixssoquery-addscopetoquery.md) instead.<br/> |
| [**CodePage**](iixssoquery-codepage.md)<br/>                 | Read/write<br/> | The character set code page.<br/>                                                                                         |
| [**Columns**](iixssoquery-columns.md)<br/>                   | Read/write<br/> | The list of columns available for OLE DB recordset retrieval for query results.<br/>                                      |
| [**Dialect**](iixssoquery-dialect.md)<br/>                   | Read/write<br/> | The query language version.<br/>                                                                                          |
| [**GroupBy**](iixssoquery-groupby.md)<br/>                   | Read/write<br/> | The choice for grouping.<br/>                                                                                             |
| [**LocaleID**](iixssoquery-localeid.md)<br/>                 | Read/write<br/> | The language locale ID (LCID) to be used when executing the query.<br/>                                                   |
| [**MaxRecords**](iixssoquery-maxrecords.md)<br/>             | Read/write<br/> | The maximum number of records to be retrieved.<br/>                                                                       |
| [**OptimizeFor**](iixssoquery-optimizefor.md)<br/>           | Read/write<br/> | Controls whether queries are optimized for better performance or for a greater number of hits.<br/>                       |
| [**OutOfDate**](iixssoquery-outofdate.md)<br/>               | Read-only<br/>  | Indicates whether the content index is out of date.<br/>                                                                  |
| [**Query**](iixssoquery-query.md)<br/>                       | Read/write<br/> | The query string, also known as the restriction.<br/>                                                                     |
| [**QueryIncomplete**](iixssoquery-queryincomplete.md)<br/>   | Read-only<br/>  | Indicates whether the query could be resolved using the Content Index.<br/>                                               |
| [**QueryTimedOut**](iixssoquery-querytimedout.md)<br/>       | Read-only<br/>  | Indicates whether the query exceeded time limit for execution.<br/>                                                       |
| **ResourceUseFactor**<br/>                                    | Read/write<br/> | Reserved for internal use.<br/>                                                                                           |
| [**SortBy**](iixssoquery-sortby.md)<br/>                     | Read/write<br/> | The choice for sorting.<br/>                                                                                              |
| **StartHit**<br/>                                             | Read/write<br/> | Reserved for internal use.<br/>                                                                                           |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



 

 





