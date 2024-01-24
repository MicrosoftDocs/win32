---
description: The DatabaseState property of the Database object is a read-only property.
ms.assetid: 0a466e53-4ff5-4b95-b754-1aac0af16805
title: Database.DatabaseState property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.DatabaseState
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.DatabaseState property

The **DatabaseState** property of the [**Database**](database-object.md) object is a read-only property.

This property returns the persistence state of the database as one of the following parameters.



| Database state        | Value | Description                                                                                                |
|-----------------------|-------|------------------------------------------------------------------------------------------------------------|
| msiDatabaseStateRead  | 0     | Database opens as read-only. Changes to persistent data are not permitted and temporary data is not saved. |
| msiDatabaseStateWrite | 1     | Database is fully operational for read and write.                                                          |



 

This property is read-only.

## Syntax


```JScript
propVal = Database.DatabaseState
```



## Property value

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



 

 




