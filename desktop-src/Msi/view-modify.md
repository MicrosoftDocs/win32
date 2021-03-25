---
description: The Modify method of the View object modifies a database row with a modified Record object obtained by the Fetch method.
ms.assetid: c3c500aa-070f-41d7-90f7-db979452d24f
title: View.Modify method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- View.Modify
api_type: 
- COM
api_location: 
- Msi.dll
---

# View.Modify method

The **Modify** method of the [**View**](view-object.md) object modifies a database row with a modified [**Record**](record-object.md) object obtained by the [**Fetch**](view-fetch.md) method.

## Syntax


```JScript
View.Modify(
  action,
  record
)
```



## Parameters

<dl> <dt>

*action* 
</dt> <dd>

Required action to be performed on the database row. This action is one of those shown in the following table.



| Action name                                                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="msiViewModifySeek"></span><span id="msiviewmodifyseek"></span><span id="MSIVIEWMODIFYSEEK"></span><dl> <dt>**msiViewModifySeek**</dt> <dt>–1</dt> </dl>                                            | Refreshes the information in the supplied record without changing the position in the result set and without affecting subsequent fetch operations. The record may then be used for subsequent Update, Delete, and Refresh. All primary key columns of the table must be in the query and the record must have at least as many fields as the query.Seek cannot be used with multitable queries. See the remarks. This mode cannot be used with a view containing joins.<br/>                                                                             |
| <span id="msiViewModifyRefresh"></span><span id="msiviewmodifyrefresh"></span><span id="MSIVIEWMODIFYREFRESH"></span><dl> <dt>**msiViewModifyRefresh**</dt> <dt>0</dt> </dl>                                 | Refreshes the information in the record. Must first call the [**Fetch**](view-fetch.md) method with the same record. Fails for a deleted row. Works with both read-write and read-only records.<br/>                                                                                                                                                                                                                                                                                                                                                     |
| <span id="msiViewModifyInsert"></span><span id="msiviewmodifyinsert"></span><span id="MSIVIEWMODIFYINSERT"></span><dl> <dt>**msiViewModifyInsert**</dt> <dt>1</dt> </dl>                                     | Inserts a record. Fails if a row with the same primary keys exists. Fails with a read-only database. This mode cannot be used with a view containing joins.<br/>                                                                                                                                                                                                                                                                                                                                                                                          |
| <span id="msiViewModifyUpdate"></span><span id="msiviewmodifyupdate"></span><span id="MSIVIEWMODIFYUPDATE"></span><dl> <dt>**msiViewModifyUpdate**</dt> <dt>2</dt> </dl>                                     | Updates an existing record. Non-primary keys only. Must first call the [**Fetch**](view-fetch.md) method with the same record. Fails with a deleted record. Works only with read-write records.<br/>                                                                                                                                                                                                                                                                                                                                                     |
| <span id="msiViewModifyAssign"></span><span id="msiviewmodifyassign"></span><span id="MSIVIEWMODIFYASSIGN"></span><dl> <dt>**msiViewModifyAssign**</dt> <dt>3</dt> </dl>                                     | Writes current data in the cursor to a table row. Updates record if the primary keys match an existing row and inserts if they do not match. Fails with a read-only database. This mode cannot be used with a view containing joins.<br/>                                                                                                                                                                                                                                                                                                                 |
| <span id="msiViewModifyReplace"></span><span id="msiviewmodifyreplace"></span><span id="MSIVIEWMODIFYREPLACE"></span><dl> <dt>**msiViewModifyReplace**</dt> <dt>4</dt> </dl>                                 | Updates or deletes and inserts a record into a table. Must first call the [**Fetch**](view-fetch.md) method with the same record. Updates record if the primary keys are unchanged. Deletes old row and inserts new if primary keys have changed. Fails with a read-only database. This mode cannot be used with a view containing joins.<br/>                                                                                                                                                                                                           |
| <span id="msiViewModifyMerge"></span><span id="msiviewmodifymerge"></span><span id="MSIVIEWMODIFYMERGE"></span><dl> <dt>**msiViewModifyMerge**</dt> <dt>5</dt> </dl>                                         | Inserts or validates a record in a table. Inserts if primary keys do not match any row and validates if there is a match. Fails if the record does not match the data in the table. Fails if there is a record with a duplicate key that is not identical. Works only with read-write records. This mode cannot be used with a view containing joins.<br/>                                                                                                                                                                                                |
| <span id="msiViewModifyDelete"></span><span id="msiviewmodifydelete"></span><span id="MSIVIEWMODIFYDELETE"></span><dl> <dt>**msiViewModifyDelete**</dt> <dt>6</dt> </dl>                                     | Removes a row from the table. Must first call the [**Fetch**](view-fetch.md) method with the same record. Fails if the row has been deleted. Works only with read-write records. This mode cannot be used with a view containing joins.<br/>                                                                                                                                                                                                                                                                                                             |
| <span id="msiViewModifyInsertTemporary"></span><span id="msiviewmodifyinserttemporary"></span><span id="MSIVIEWMODIFYINSERTTEMPORARY"></span><dl> <dt>**msiViewModifyInsertTemporary**</dt> <dt>7</dt> </dl> | Inserts a temporary record. The information is not persistent. Fails if a row with the same primary key exists. Works only with read-write records. This mode cannot be used with a view containing joins.<br/>                                                                                                                                                                                                                                                                                                                                           |
| <span id="msiViewModifyValidate"></span><span id="msiviewmodifyvalidate"></span><span id="MSIVIEWMODIFYVALIDATE"></span><dl> <dt>**msiViewModifyValidate**</dt> <dt>8</dt> </dl>                             | Validates a record. Does not validate across joins. Must first call the [**Fetch**](view-fetch.md) method with the same record. Obtain validation errors with [**GetError**](view-geterror.md) method. Works with read-write and read-only records. This mode cannot be used with a view containing joins.<br/>                                                                                                                                                                                                                                         |
| <span id="msiViewModifyValidateNew"></span><span id="msiviewmodifyvalidatenew"></span><span id="MSIVIEWMODIFYVALIDATENEW"></span><dl> <dt>**msiViewModifyValidateNew**</dt> <dt>9</dt> </dl>                 | Validates a new record. Does not validate across joins. Checks for duplicate keys. Obtains validation errors by calling [**GetError**](view-geterror.md) method. Requires calling [**MsiDatabase.OpenView**](database-openview.md) method with a modify value. Works with read-write and read-only records. This mode cannot be used with a view containing joins.<br/>                                                                                                                                                                                 |
| <span id="msiViewModifyValidateField"></span><span id="msiviewmodifyvalidatefield"></span><span id="MSIVIEWMODIFYVALIDATEFIELD"></span><dl> <dt>**msiViewModifyValidateField**</dt> <dt>10</dt> </dl>        | Validates fields of a fetched or new record. Can validate one or more fields of an incomplete record. Obtains validation errors by calling [**GetError**](view-geterror.md) method. Works with read-write and read-only records. This mode cannot be used with a view containing joins.<br/>                                                                                                                                                                                                                                                             |
| <span id="msiViewModifyValidateDelete"></span><span id="msiviewmodifyvalidatedelete"></span><span id="MSIVIEWMODIFYVALIDATEDELETE"></span><dl> <dt>**msiViewModifyValidateDelete**</dt> <dt>11</dt> </dl>    | Validates a record that will be deleted later. Must first call the [**Fetch**](view-fetch.md) method with the same record. Fails if another row refers to the primary keys of this row. Validation does not check for the existence of the primary keys of this row in properties or strings. Does not check if a column is a foreign key to multiple tables. Obtain validation errors by calling the [**GetError**](view-geterror.md) method. Works with read-write and read-only records. This mode cannot be used with a view containing joins.<br/> |



 

</dd> <dt>

*record* 
</dt> <dd>

Required. [**Record**](record-object.md) object obtained by the [**Fetch**](view-fetch.md) method with modified field data.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method must be called after the [**Execute**](view-execute.md) method.

To execute any SQL statement, a view must be created. However, a view that does not create a result set, such as CREATE TABLE or INSERT INTO, cannot be used with the **Modify** method to update tables though the view.

The msiViewModifyValidate, msiViewModifyValidateNew, msiViewModifyValidateField, and msiViewModifyValidateDelete values of the **Modify** method do not perform actual updates; they ensure that the data in the record is valid. Use of these actions requires that the database contain a [\_Validation table](-validation-table.md) .

You cannot fetch a record containing binary data from one database and then use that record to insert the data into a completely different database. To move binary data from one database to another, you should export the data to a file and then import it into the new database using the [**SetStream**](record-setstream.md) method of the [**Record**](record-object.md) object. This ensures that each database has its own copy of the binary data.

> [!Note]  
> Custom actions can only add, modify, or remove temporary rows, columns, or tables from a database. Custom actions cannot modify persistent data in a database, such as data that is a part of the database stored on disk. For more information, see [Accessing the Current Installer Session from Inside a Custom Action](accessing-the-current-installer-session-from-inside-a-custom-action.md).

 

If the method fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IView is defined as 000C109C-0000-0000-C000-000000000046<br/>                                                                                                                                                                                |



 

 




