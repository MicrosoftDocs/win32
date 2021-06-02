---
description: The Database object accesses an installer database.
ms.assetid: 97765884-3e1c-486a-932c-6430b113fac8
title: Database object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database object

The **Database** object accesses an installer database.

The **Database** object is released when it is either taken out of scope or when the object variable associated with it is set to null. The [**Commit**](database-commit.md) method must be called before the **Database** object is released to write out all persistent changes. If the **Commit** method is not called, the installer performs an implicit rollback upon object destruction.

The client can use the following procedure for data access.

**To Query API Sequencing**

1.  Obtain a **Database** object by calling the [**OpenDatabase**](installer-opendatabase.md) or the [**Installer**](installer-object.md) object.
2.  Initiate a query using a SQL string by calling the [**OpenView**](database-openview.md) method of the **Database** object.
3.  Set query parameters in a [**Record**](record-object.md) object and execute the database query by calling the [**Execute**](view-execute.md) method of the [**View**](view-object.md) object. This produces a result that can be fetched or updated.
4.  Call the [**Fetch**](view-fetch.md) method of the [**View**](view-object.md) object repeatedly to return [**Record**](record-object.md) objects.
5.  Update database rows of a [**Record**](record-object.md) object obtained by the [**Fetch**](view-fetch.md) method using the [**Modify**](view-modify.md) method of the [**View**](view-object.md) object.
6.  Release the query and any unfetched records by calling the [**Close**](view-close.md) method of the [**View**](view-object.md) object.
7.  Persist any database updates by calling the [**Commit**](database-commit.md) method of the **Database** object.

## Members

The **Database** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Database** object has these methods.



| Method                                                                    | Description                                                                                                                                                               |
|:--------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ApplyTransform**](database-applytransform.md)                         | Applies the transform to this database.<br/>                                                                                                                        |
| [**Commit**](database-commit.md)                                         | Finalizes the persistent form of the database.<br/>                                                                                                                 |
| [**CreateTransformSummaryInfo**](database-createtransformsummaryinfo.md) | Creates and populates the summary information stream of an existing transform file.<br/>                                                                            |
| [**EnableUIPreview**](database-enableuipreview.md)                       | Facilitates the authoring of dialog boxes and billboards by providing the support needed to view user interface dialog boxes stored in the installer database.<br/> |
| [**Export**](database-export.md)                                         | Copies the structure and data from a specified table to a text archive file.<br/>                                                                                   |
| [**GenerateTransform**](database-generatetransform.md)                   | Creates a transform.<br/>                                                                                                                                           |
| [**Import**](database-import.md)                                         | Imports a database table from a text archive file.<br/>                                                                                                             |
| [**Merge**](database-merge.md)                                           | Merges the reference database with the base database.<br/>                                                                                                          |
| [**OpenView**](database-openview.md)                                     | Returns a [**View**](view-object.md) object representing the query specified by a SQL string.<br/>                                                                 |



 

### Properties

The **Database** object has these properties.



| Property                                                                               | Description                                                                                                                                                      |
|:---------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DatabaseState**](database-databasestate.md)<br/>                             | Returns the persistence state of the database.<br/>                                                                                                        |
| [**PrimaryKeys**](database-primarykeys.md)<br/>                                 | Returns a [**Record**](record-object.md) object containing the table name and the column names (comprising the primary keys).<br/>                        |
| [**SummaryInformation (Database Object)**](database-summaryinformation.md)<br/> | Returns a [**SummaryInfo**](summaryinfo-object.md) object that can be used to examine, update, and add properties to the summary information stream.<br/> |
| [**TablePersistent**](database-tablepersistent.md)<br/>                         | Returns the persistence state of the table.<br/>                                                                                                           |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



## See also

<dl> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




