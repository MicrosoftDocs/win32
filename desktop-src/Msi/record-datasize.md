---
description: The DataSize property of the Record object is a read-only property that returns the size of the data for the designated field.
ms.assetid: 6f89321e-bdb2-4c18-bdf8-01dea38b47c9
title: Record.DataSize property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Record.DataSize
api_type: 
- COM
api_location: 
- Msi.dll
---

# Record.DataSize property

The **DataSize** property of the [**Record**](record-object.md) object is a read-only property that returns the size of the data for the designated field. If the data is a stream, the stream length in bytes is returned. If the data is a string, the string length without Null is returned. If the data is an integer, the value 4 is returned (indicating the size of the integer). If the data is Null, 0 is returned.

This property is read-only.

## Syntax


```JScript
propVal = Record.DataSize
```



## Property value

Required field number of the value within the record, 1-based.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IRecord is defined as 000C1093-0000-0000-C000-000000000046<br/>                                                                                                                                                                              |



 

 




