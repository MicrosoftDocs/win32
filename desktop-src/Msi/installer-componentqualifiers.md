---
description: The ComponentQualifiers property is a read-only property that returns a StringList object enumerating the set of registered qualifiers for the specified component.
ms.assetid: 49b16c9a-ce84-42ff-af1d-f4ecf7dbe23a
title: Installer.ComponentQualifiers property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ComponentQualifiers
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ComponentQualifiers property

The **ComponentQualifiers** property is a read-only property that returns a [**StringList**](stringlist-object.md) object enumerating the set of registered qualifiers for the specified component.

This property is read-only.

## Syntax


```JScript
propVal = Installer.ComponentQualifiers
```



## Property value

A string GUID that represents the category of [component](publishcomponent-table.md).

## Remarks

To enumerate qualifiers the application iterates through the [**StringList**](stringlist-object.md) object using a For Each construct. Because qualifiers are not ordered, any new qualifier has an arbitrary index, meaning the function can return qualifiers in any order.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiEnumComponentQualifiers**](/windows/desktop/api/Msi/nf-msi-msienumcomponentqualifiersa)
</dt> </dl>

 

 




