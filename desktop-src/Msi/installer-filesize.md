---
description: The FileSize method of the Installer object uses Win32 API calls to return the size of the file specified in Path.
ms.assetid: d7119e5e-9315-4b20-a904-bc1104f3a4e4
title: Installer.FileSize method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.FileSize
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.FileSize method

The **FileSize** method of the [**Installer**](installer-object.md) object uses Win32 API calls to return the size of the file specified in *Path*.

## Syntax


```JScript
Installer.FileSize(
  Path
)
```



## Parameters

<dl> <dt>

*Path* 
</dt> <dd>

Required string containing the path to the file.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




