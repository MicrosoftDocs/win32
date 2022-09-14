---
description: The AddSource method of the Installer object adds a source to the list of valid network sources in the sourcelist.
ms.assetid: e24c8484-fe84-4f97-9c06-c063bb7c6810
title: Installer.AddSource method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.AddSource
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.AddSource method

The **AddSource** method of the [**Installer**](installer-object.md) object adds a source to the list of valid network sources in the sourcelist.

## Syntax


```JScript
Installer.AddSource(
  Product,
  User,
  Source
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

</dd> <dt>

*Source* 
</dt> <dd>

Pointer to the string specifying the source.

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

[**MsiSourceListAddSource**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourcea)
</dt> <dt>

[source resiliency](source-resiliency.md)
</dt> </dl>

 

 




