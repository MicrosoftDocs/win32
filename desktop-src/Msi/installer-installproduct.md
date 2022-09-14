---
description: The InstallProduct method of the Installer object opens an installer package and initializes an install session.
ms.assetid: 6828ca34-3cf1-4738-882d-9ff1450f1014
title: Installer.InstallProduct method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.InstallProduct
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.InstallProduct method

The **InstallProduct** method of the [**Installer**](installer-object.md) object opens an installer package and initializes an install session.

## Syntax


```JScript
Installer.InstallProduct(
  packagePath,
  propertyValues
)
```



## Parameters

<dl> <dt>

*packagePath* 
</dt> <dd>

Required string containing the path to the install package.

</dd> <dt>

*propertyValues* 
</dt> <dd>

Optional string containing property=value pairs separated by white space.

To perform an administrative installation, include ACTION=ADMIN in *propertyValues*. For more information, see the [**ACTION**](action.md) property.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To completely remove a product, set REMOVE=ALL in *propertyValues*. For more information, see [**REMOVE**](remove.md) property.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




