---
description: This is the IntegerData property of the Record object. This read-write property transfers 32-bit integer data in to or out of a specified field within the record. If a field value cannot be converted to an integer, msiDatabaseNullInteger is returned.
ms.assetid: abc291cd-31ba-409f-b010-8b3a71cbdc77
title: Record.IntegerData property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Record.IntegerData
api_type: 
- COM
api_location: 
- Msi.dll
---

# Record.IntegerData property

This is the **IntegerData** property of the [**Record**](record-object.md) object. This read-write property transfers 32-bit integer data in to or out of a specified field within the record. If a field value cannot be converted to an integer, msiDatabaseNullInteger is returned.

This property is read/write.

## Syntax


```JScript
propVal = Record.IntegerData
Record.IntegerData = propVal 
```



## Property value

Required field number of the value within the record, 1-based.

## Remarks

To set a record integer field to null, use msiDatabaseNullInteger. The returned value of a nonexistent field is msiDatabaseNullInteger. Attempting to store a value in a nonexistent field causes an error.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IRecord is defined as 000C1093-0000-0000-C000-000000000046<br/>                                                                                                                                                                              |



 

 




