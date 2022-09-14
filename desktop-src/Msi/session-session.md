---
description: The Property property of the Session object is a read-write property that represents the string value of a named installer property, as maintained by the Session object.
ms.assetid: 15ce8264-2573-428c-98d9-690cfaae5144
title: Session.Property property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.Property
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.Property property

The **Property** property of the [**Session**](session-object.md) object is a read-write property that represents the string value of a named installer property, as maintained by the **Session** object in the in-memory Property table, or, if it is prefixed with a percent sign (%), the value of a system environment variable for the current process. Either string or integer values may be supplied. A non-existent property or environment variable is equivalent to its value being Null.

This property is read/write.

## Syntax


```JScript
propVal = Session.Property
Session.Property = propVal 
```



## Property value

Required case-sensitive name of a property, or a case-insensitive name of an environment variable prefixed by a percent sign (%).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




