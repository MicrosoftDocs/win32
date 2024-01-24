---
description: The Count property is a read-only property that returns the number of items in the RecordList object.
ms.assetid: df384d5c-931f-4a31-af55-d013f010e100
title: RecordList.Count property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RecordList.Count
api_type: 
- COM
api_location: 
- Msi.dll
---

# RecordList.Count property

The **Count** property is a read-only property that returns the number of items in the [**RecordList**](recordlist-object.md) object.

This property is read-only.

## Syntax


```JScript
propVal = RecordList.Count
```



## Property value

## Remarks

The client must verify that the [**RecordList**](recordlist-object.md) object exists and is not empty before referencing the Count property.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IRecordList is defined as 000C1096-0000-0000-C000-000000000046<br/>                                                                                                                                                                          |



 

 




