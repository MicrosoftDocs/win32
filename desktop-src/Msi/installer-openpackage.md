---
description: The OpenPackage method of the Installer object opens an installer package for use with functions that access the product database and install engine, returning an Session object.
ms.assetid: 22b03bde-29ae-4dd4-a41c-d55b3a4f424c
title: Installer.OpenPackage method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.OpenPackage
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.OpenPackage method

The **OpenPackage** method of the [**Installer**](installer-object.md) object opens an installer package for use with functions that access the product database and install engine, returning an [**Session**](session-object.md) object.

## Syntax


```JScript
Installer.OpenPackage(
  packagePath,
  options
)
```



## Parameters

<dl> <dt>

*packagePath* 
</dt> <dd>

Required string containing the path name of the package.

</dd> <dt>

*options* 
</dt> <dd>

An optional integer value that specifies whether or not **OpenPackage** should ignore the current computer state when creating the Session object. No value or a value of 0 for options defaults to the original behavior. When options is 1, the **OpenPackage** Method ignores the current computer state when opening the package. A value of 1 prevents changes to the current computer state. For more information, see [**MsiOpenPackageEx**](/windows/desktop/api/Msi/nf-msi-msiopenpackageexa).

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The **OpenPackage** method can accept the database handle directly instead of the string for the package path.

Note that only one [**Session**](session-object.md) object can be opened by a single process. **OpenPackage** cannot be used in a custom action because the active installation is the only session allowed.

A safe [**Session**](session-object.md) object ignores the current computer state when opening the package and prevents changes to the current computer state. For more information, see [**MsiOpenPackageEx**](/windows/desktop/api/Msi/nf-msi-msiopenpackageexa).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




