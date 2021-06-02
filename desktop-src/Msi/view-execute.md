---
description: The Execute method of the View object uses the question mark token to represent parameters in an SQL statement. For more information, see SQL Syntax. The values of these parameters are passed in as the corresponding fields of a parameter record.
ms.assetid: 4f2b2cb8-8f59-4e4a-ba09-6cb092ef81d6
title: View.Execute method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- View.Execute
api_type: 
- COM
api_location: 
- Msi.dll
---

# View.Execute method

The **Execute** method of the [**View**](view-object.md) object uses the question mark token to represent parameters in an SQL statement. For more information, see [SQL Syntax](sql-syntax.md). The values of these parameters are passed in as the corresponding fields of a parameter record.

## Syntax


```JScript
View.Execute(
  record
)
```



## Parameters

<dl> <dt>

*record* 
</dt> <dd>

Optional [**Record**](record-object.md) objects that contains the values that replace the parameter tokens (?) in the SQL query.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method must be called before any calls to the [**Fetch**](view-fetch.md) method.

If the SQL query specifies values with parameter markers (?), a record must be supplied that contains all of the replacement values, which must be in the same order and of the same data type as the parameter markers. When this method is used with INSERT and UPDATE queries, the question mark tokens must precede all the non-parameterized values.

For example, these queries are valid:

UPDATE {table-list} SET {column}= ? , {column}= {constant}

INSERT INTO {table} ({column-list}) VALUES (?, {constant-list})

However these queries are invalid:

UPDATE {table-list} SET {column}= {constant}, {column}=?

INSERT INTO {table} ({column-list}) VALUES ({constant-list}, ? )

If the method fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IView is defined as 000C109C-0000-0000-C000-000000000046<br/>                                                                                                                                                                                |



 

 




