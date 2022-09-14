---
description: The OpenView method of the Database object returns a View object that represents the query specified by a SQL string.
ms.assetid: 6afb2fdb-0e6a-468f-8faf-e48d8d1960b6
title: Database.OpenView method (Certview.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.OpenView
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.OpenView method

The **OpenView** method of the [**Database**](database-object.md) object returns a [**View**](view-object.md) object that represents the query specified by a SQL string.

## Syntax


```JScript
Database.OpenView(
  sql
)
```



## Parameters

<dl> <dt>

*sql* 
</dt> <dd>

Required SQL query string.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

For information about SQL syntax implemented in the installer, see [SQL Syntax](sql-syntax.md).

If the method fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| Header<br/>  | <dl> <dt>Certview.h</dt> </dl>                                                                                                                                                                   |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



## See also

<dl> <dt>

[**Database**](database-object.md)
</dt> <dt>

[SQL Syntax](sql-syntax.md)
</dt> </dl>

 

 




