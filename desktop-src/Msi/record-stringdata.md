---
description: The StringData property of the Record object is a read-write property that transfers string data in to or out of a specified field within the record. If an integer or object has been stored, its string value is returned.
ms.assetid: ffa163eb-41b3-47ae-b01d-39a3890990a3
title: Record.StringData property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Record.StringData
api_type: 
- COM
api_location: 
- Msi.dll
---

# Record.StringData property

The **StringData** property of the [**Record**](record-object.md) object is a read-write property that transfers string data in to or out of a specified field within the record. If an integer or object has been stored, its string value is returned.

This property is read/write.

## Syntax


```JScript
propVal = Record.StringData
Record.StringData = propVal 
```



## Property value

Required field number of the value within the record, 1-based.

## Remarks

The returned value of a nonexistent field is an empty string. To set a record string field to null, use either an empty variant or an empty string. Attempting to store a value in a nonexistent field causes an error.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IRecord is defined as 000C1093-0000-0000-C000-000000000046<br/>                                                                                                                                                                              |



 

 




