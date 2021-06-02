---
description: The read-only ComponentClients property returns a StringList object enumerating the set of clients of a specified component.
ms.assetid: 47553360-298f-4be8-819d-18f4df96667c
title: Installer.ComponentClients property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ComponentClients
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ComponentClients property

The read-only **ComponentClients** property returns a [**StringList**](stringlist-object.md) object enumerating the set of clients of a specified component.

This property is read-only.

## Syntax


```JScript
propVal = Installer.ComponentClients
```



## Property value

A string GUID that represents the component code of the component. The component codes are specified in the ComponentId column of the [Component table](component-table.md).

## Remarks

To enumerate the component clients, an application may iterate through the [**StringList**](stringlist-object.md) object using a For Each construct. Because clients are not ordered, any new components has an arbitrary index. This means that the function may return clients in any order.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiEnumClients**](/windows/desktop/api/Msi/nf-msi-msienumclientsa)
</dt> </dl>

 

 




