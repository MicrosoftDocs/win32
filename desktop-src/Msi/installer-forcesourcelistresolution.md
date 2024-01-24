---
description: The ForceSourceListResolution method of the Installer object forces the Windows Installer to search the source list for a valid product source.
ms.assetid: d5097331-8cf5-494f-9e88-bcffcad3fe5d
title: Installer.ForceSourceListResolution method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ForceSourceListResolution
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ForceSourceListResolution method

The **ForceSourceListResolution** method of the [**Installer**](installer-object.md) object forces the installer to search the source list for a valid product source the next time a source is needed, such as when the installer performs an installation or a reinstallation, or when it needs the path for a component set to run from source.

## Syntax


```JScript
Installer.ForceSourceListResolution(
  Product,
  User
)
```



## Parameters

<dl> <dt>

*Product* 
</dt> <dd>

Specifies the product code.

</dd> <dt>

*User* 
</dt> <dd>

User name for per-user installation; null or empty string for per-machine installation.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiSourceListForceResolution**](/windows/desktop/api/Msi/nf-msi-msisourcelistforceresolutiona)
</dt> <dt>

[Source Resiliency](source-resiliency.md)
</dt> </dl>

 

 




