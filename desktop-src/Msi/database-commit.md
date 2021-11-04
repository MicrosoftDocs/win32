---
description: The Commit method of the Database object finalizes the persistent form of the database.
ms.assetid: 39253ccd-08f1-4a6f-87cb-3678ae5221a4
title: Database.Commit method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.Commit
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.Commit method

The **Commit** method of the [**Database**](database-object.md) object finalizes the persistent form of the database. All persistent data is written to the writeable database, and no temporary columns or rows are written. This method has no effect on a database opened as read-only. This method can be called multiple times to save the current state of tables loaded into memory. When the database is finally closed, any changes made subsequent to the last **Commit** are rolled back. This method is normally called prior to shutdown when all database changes have been finalized.

## Syntax


```JScript
Database.Commit()
```



## Parameters

This method has no parameters.

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



 

 




