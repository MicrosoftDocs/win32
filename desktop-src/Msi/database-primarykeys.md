---
description: The PrimaryKeys property of the Database object returns a Record object containing the table name in field 0 and the column names (comprising the primary keys) in succeeding fields corresponding to their column numbers.
ms.assetid: 9aeafda4-65b8-4469-a391-eb25ca72459d
title: Database.PrimaryKeys property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.PrimaryKeys
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.PrimaryKeys property

The **PrimaryKeys** property of the [**Database**](database-object.md) object returns a [**Record**](record-object.md) object containing the table name in field 0 and the column names (comprising the primary keys) in succeeding fields corresponding to their column numbers. The field count of the record is the count of primary key columns.

This property is read-only.

## Syntax


```JScript
propVal = Database.PrimaryKeys
```



## Property value

Required name of an existing table. An error is generated if the table does not exist.

## Remarks

The **PrimaryKeys** property cannot be used with the [\_Tables table](-tables-table.md) or the [\_Columns table](-columns-table.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



 

 




