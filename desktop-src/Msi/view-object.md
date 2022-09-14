---
description: The View object represents a result set obtained when processing a query using the OpenView method of the Database object.
ms.assetid: 'd9d6583a-1cf3-4c33-a851-83e862e2338e'
title: View object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- View
api_type: 
- COM
api_location: 
- Msi.dll
---

# View object

The **View** object represents a result set obtained when processing a query using the [**OpenView**](database-openview.md) method of the [**Database**](database-object.md) object. Before any data can be transferred, the query must be executed using the [**Execute**](view-execute.md) method, passing to it all replaceable parameters designated within the SQL query string. The query may be executed again, with different parameters if needed, but only after freeing the result set either by fetching all the records or by calling the [**Close**](view-close.md) method.

## Members

The **View** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **View** object has these methods.



| Method                            | Description                                                                                                                                                                     |
|:----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Close**](view-close.md)       | Terminates query execution and releases database resources.<br/>                                                                                                          |
| [**Execute**](view-execute.md)   | Uses the question mark token to represent parameters in a SQL query. The values of these parameters are passed in as the corresponding fields of a parameter record.<br/> |
| [**Fetch**](view-fetch.md)       | Returns a [**Record**](record-object.md) object containing the requested column data if more rows are available in the result set, otherwise, it returns null.<br/>      |
| [**GetError**](view-geterror.md) | Returns the Validation error and column name for which the error occurred.<br/>                                                                                           |
| [**Modify**](view-modify.md)     | Modifies a database row with a modified [**Record**](record-object.md) object obtained by the [**Fetch**](view-fetch.md) method.<br/>                                   |



 

### Properties

The **View** object has these properties.



| Property                                         | Description                                                                                                                           |
|:-------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| [**ColumnInfo**](view-columninfo.md)<br/> | Returns a [**Record**](record-object.md) object containing the requested information about each column in the result set.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IView is defined as 000C109C-0000-0000-C000-000000000046<br/>                                                                                                                                                                                |



## See also

<dl> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




