---
description: The Property property of the UIPreview object is a read-write property that represents the string value of a named installer property, or, if it is prefixed with a percent sign (%), the value of a system environment variable for the current process.
ms.assetid: 92900426-8fb5-4a94-a982-438267ad756e
title: UIPreview.Property property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UIPreview.Property
api_type: 
- COM
api_location: 
- Msi.dll
---

# UIPreview.Property property

The **Property** property of the [**UIPreview**](uipreview-object.md) object is a read-write property that represents the string value of a named installer property, or, if it is prefixed with a percent sign (%), the value of a system environment variable for the current process. This is exposed to allow proper display of dialog boxes that are dependent upon property values. Either string or integer values may be supplied. A nonexistent property or environment variable is equivalent to its value being null.

This property is read/write.

## Syntax


```JScript
propVal = UIPreview.Property
UIPreview.Property = propVal 
```



## Property value

Required case-sensitive name of a property, or a case-insensitive name of an environment variable prefixed by a percent sign (%).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IUIPreview is defined as 000C109A-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




