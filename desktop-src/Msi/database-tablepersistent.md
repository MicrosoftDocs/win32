---
description: The TablePersistent property of the Database object returns the persistence state of the table as one of the following parameters.
ms.assetid: c395e99c-5cdc-4d7b-ac55-a79d4e1477dc
title: Database.TablePersistent property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.TablePersistent
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.TablePersistent property

The **TablePersistent** property of the [**Database**](database-object.md) object returns the persistence state of the table as one of the following parameters.



| Table state               | Value | Description                    |
|---------------------------|-------|--------------------------------|
| msiEvaluateConditionFalse | 0     | Table is temporary.            |
| msiEvaluateConditionTrue  | 1     | Table is persistent.           |
| msiEvaluateConditionNone  | 2     | Table is not in the database.  |
| msiEvaluateConditionError | 3     | Invalid or missing table name. |



 

This property is read-only.

## Syntax


```JScript
propVal = Database.TablePersistent
```



## Property value

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



 

 




