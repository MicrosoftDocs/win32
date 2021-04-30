---
description: The FileVersion method of the Installer object returns the version string or language string of the path specified in Path using the format in which the installer expects to find them in the database.
ms.assetid: 387cf269-5a7a-476b-811e-d576da1c752f
title: Installer.FileVersion method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.FileVersion
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.FileVersion method

The **FileVersion** method of the [**Installer**](installer-object.md) object returns the version string or language string of the path specified in *Path* using the format in which the installer expects to find them in the database. For versions, this is a string in "\#.\#.\#.\#" format. For language, this is the decimal language ID.

## Syntax


```JScript
Installer.FileVersion(
  Path,
  Language
)
```



## Parameters

<dl> <dt>

*Path* 
</dt> <dd>

Required string containing the path to the file.

</dd> <dt>

*Language* 
</dt> <dd>

Flag for designating whether the returned value is a language ID or version string. TRUE returns the language, FALSE returns the version. This parameter is optional, with a default value of FALSE.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




