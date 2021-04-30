---
description: The Item property is a read-only property that returns a string in the StringList Object collection.
ms.assetid: 5c654927-41cf-4e47-9d4f-76524f8bbc97
title: StringList.Item property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StringList.Item
api_type: 
- COM
api_location: 
- Msi.dll
---

# StringList.Item property

The **Item** property is a read-only property that returns a string in the [**StringList Object**](stringlist-object.md) collection.

This property is read-only.

## Syntax


```JScript
propVal = StringList.Item
```



## Property value

Index number of the item with the collection of strings. This parameter is required.

## Remarks

The client must verify that the [**StringList Object**](stringlist-object.md) exists and is not empty before referencing the **Item** property.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IStringList is defined as 000C1095-0000-0000-C000-000000000046<br/>                                                                                                                                                                          |



 

 




