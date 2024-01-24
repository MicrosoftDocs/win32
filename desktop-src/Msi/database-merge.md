---
description: The Merge method of the Database object merges the reference database with the base database.
ms.assetid: 777060cf-c672-49d5-a1a8-8674fdc4bde4
title: Database.Merge method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.Merge
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.Merge method

The **Merge** method of the [**Database**](database-object.md) object merges the reference database with the base database.

## Syntax


```JScript
Database.Merge(
  reference,
  errorTable
)
```



## Parameters

<dl> <dt>

*reference* 
</dt> <dd>

The required [**Database**](database-object.md) object to be merged into the database.

</dd> <dt>

*errorTable* 
</dt> <dd>

An optional name of a table to contain the names of the tables containing merge conflicts, the number of conflicting rows within the table, and a reference to the table with the merge conflict.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The [**MsiDatabaseMerge**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasemergea) function and the **Merge** method of the [**Database**](database-object.md) object cannot be used to merge a module included within an installation package. They should not be used to merge [Merge Modules](merge-modules.md) into a Windows Installer package. To include a merge module in an installation package, authors of installation packages should follow the guidelines that are described in the [Applying Merge Modules](applying-merge-modules.md) topic.

The **Merge** method does not copy over embedded [cabinet files](cabinet-files.md) or [embedded transforms](embedded-transforms.md) from the reference database into the target database. Embedded data streams that are listed in the [Binary Table](binary-table.md) or [Icon Table](icon-table.md) are copied from the reference database to the target database. Storages embedded in the reference database are not copied to the target database.

If no table is provided, the general error message provides the number of tables containing merge conflicts. Any table can be passed in, but all other columns must be nullable because the operation to update the [Error Table](error-table.md) fails if a column is not nullable. A newly created table can be passed in as well because the **Merge** method automatically creates the columns it uses if merge conflicts are found. Two columns are used to present merge conflicts. The first column is the table name and the primary key column. The second column is the number of rows of that table that have merge failures.

If tables of the same name in both databases do not match in the number of primary keys, the column types, the number of columns, or the column names, the **Merge** method fails and posts an error message stating what occurred.

For the Error table to remain, the error handler must commit the database to which the Error table belongs. However, this commit should be done after using the third column to obtain the references to those tables where merge conflicts occurred.

If the method fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



 

 




