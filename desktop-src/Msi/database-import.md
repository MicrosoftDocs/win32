---
description: The Import method of the Database object imports a database table from a text archive files, dropping any existing table.
ms.assetid: 9ecc31d9-bccd-48cc-b205-9ce70aaf638a
title: Database.Import method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.Import
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.Import method

The **Import** method of the [**Database**](database-object.md) object imports a database table from a [text archive files](text-archive-files.md), dropping any existing table.

## Syntax


```JScript
Database.Import(
  path,
  file
)
```



## Parameters

<dl> <dt>

*path* 
</dt> <dd>

Required folder where the text file is present.

</dd> <dt>

*file* 
</dt> <dd>

Required name of the file to be imported. This does not include the folder, as that must be set in the path object. The table name is specified within the file.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If the method fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



## See also

<dl> <dt>

[**Database**](database-object.md)
</dt> <dt>

[**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta)
</dt> </dl>

 

 




