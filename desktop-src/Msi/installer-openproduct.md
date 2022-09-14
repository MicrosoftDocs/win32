---
description: The OpenProduct method of the Installer object opens an installer package for an installed product using the product code and returns a Session object.
ms.assetid: f09c4795-19e1-4474-b7ca-68ef650b69d5
title: Installer.OpenProduct method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.OpenProduct
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.OpenProduct method

The **OpenProduct** method of the [**Installer**](installer-object.md) object opens an installer package for an installed product using the product code and returns a [**Session**](session-object.md) object.

## Syntax


```JScript
Installer.OpenProduct(
  productCode
)
```



## Parameters

<dl> <dt>

*productCode* 
</dt> <dd>

Required string containing the unique product code (a [GUID](guid.md)) or an activation descriptor written by the installer.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Note that only one [**Session**](session-object.md) object can be opened by a single process. **OpenProduct** cannot be used in a custom action because the active installation is the only session allowed.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




