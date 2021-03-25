---
description: The Count property is a read-only property that returns the number of items in the StringList object.
ms.assetid: aa85b8d9-344d-4f31-aa86-9e6497c07751
title: StringList.Count property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StringList.Count
api_type: 
- COM
api_location: 
- Msi.dll
---

# StringList.Count property

The **Count** property is a read-only property that returns the number of items in the [**StringList object**](stringlist-object.md).

This property is read-only.

## Syntax


```JScript
propVal = StringList.Count
```



## Property value

## Remarks

The client must verify that the [**StringList**](stringlist-object.md) object exists and is not empty before referencing the **Count** property.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IStringList is defined as 000C1095-0000-0000-C000-000000000046<br/>                                                                                                                                                                          |



 

 




