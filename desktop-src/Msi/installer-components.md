---
description: The read-only Components property returns a StringList object enumerating the set of installed components for all products.
ms.assetid: 'c84e4329-428a-440a-bd65-097588a86932'
title: Installer.Components property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.Components
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.Components property

The read-only **Components** property returns a [**StringList**](stringlist-object.md) object enumerating the set of installed components for all products.

This property is read-only.

## Syntax


```JScript
propVal = Installer.Components
```



## Property value

## Remarks

To enumerate the components, an application can iterate through the [**StringList**](stringlist-object.md) object using a For Each construct. Because components are not ordered, any new components has an arbitrary index. This means that the function can return components in any order.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiEnumComponents**](/windows/desktop/api/Msi/nf-msi-msienumcomponentsa)
</dt> </dl>

 

 




