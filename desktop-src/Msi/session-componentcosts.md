---
description: The ComponentCosts property of the Session object returns a RecordList object enumerating the disk space per drive required to install a component.
ms.assetid: 9b1355f1-cc99-49d9-8187-07fba4804d1f
title: Session.ComponentCosts property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.ComponentCosts
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.ComponentCosts property

The ComponentCosts property of the [**Session**](session-object.md) object returns a [**RecordList**](recordlist-object.md) object enumerating the disk space per drive required to install a component. This information is used by the user interface to display the disk space required for all drives. The returned disk space costs are in multiples of 512 bytes.

The ComponentCosts property should only be used after the installer has completed [file costing](file-costing.md) and after the [CostFinalize action](costfinalize-action.md).

This property is read-only.

## Syntax


```JScript
propVal = Session.ComponentCosts
```



## Property value

## Remarks

To obtain the total cost, add the costs for all components plus the installer engine cost (Component = "").

ComponentCosts returns a [**RecordList object**](recordlist-object.md). Each record in the returned RecordList object has the following fields:



| Field | Description                                          |
|-------|------------------------------------------------------|
| 1     | Volume/Drive name                                    |
| 2     | Final disk space cost in multiples of 512 bytes.     |
| 3     | Temporary disk space cost in multiples of 512 bytes. |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




