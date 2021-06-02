---
description: The Environment property of the Installer object is a read-write property that is the string value for an environment variable of the current process.
ms.assetid: f59a270f-9bd8-4d17-96e2-cb3c62a31cad
title: Installer.Environment property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.Environment
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.Environment property

The **Environment** property of the [**Installer**](installer-object.md) object is a read-write property that is the string value for an environment variable of the current process.

This property is read/write.

## Syntax


```JScript
propVal = Installer.Environment
Installer.Environment = propVal 
```



## Property value

The name of the environment variable to be read or written. This is case-insensitive.

## Remarks

Setting an environment variable with the **Environment** property only affects the active session. To make persistent changes to an environment variable, use the [Environment table](environment-table.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




