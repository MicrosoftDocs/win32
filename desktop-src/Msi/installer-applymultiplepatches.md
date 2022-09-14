---
description: The ApplyMultiplePatches method applies one or more patches to products that are eligible to receive the patch. The method sets the PATCH property.
ms.assetid: 40c40e2c-60ef-4492-a4ab-0bb6b874fe80
title: Installer.ApplyMultiplePatches method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ApplyMultiplePatches
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ApplyMultiplePatches method

The **ApplyMultiplePatches** method applies one or more patches to products that are eligible to receive the patch. The method sets the [**PATCH**](patch.md) property.

## Syntax


```JScript
Installer.ApplyMultiplePatches(
  PatchPackagesList,
  Product,
  szPropertiesList
)
```



## Parameters

<dl> <dt>

*PatchPackagesList* 
</dt> <dd>

A string that contains a semicolon-delimited list of the paths to patch files. For example: ""c:\\sus\\download\\cache\\Office\\sp1.msp; c:\\sus\\download\\cache\\Office\\QFE1.msp;c:\\sus\\download\\cache\\Office\\QFEn.msp""

</dd> <dt>

*Product* 
</dt> <dd>

This parameter provides the [**ProductCode**](productcode.md) of the product being patched. This parameter is optional. When this parameter is null, the patches are applied to all products that are eligible to receive these patches.

</dd> <dt>

*szPropertiesList* 
</dt> <dd>

A null-terminated string that specifies command-line property settings. This parameter is optional. See [About Properties](about-properties.md) and [Setting Public Property Values on the Command Line](setting-public-property-values-on-the-command-line.md). These properties are shared by all target products.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003 or Windows XP.<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                    |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                                         |



## See also

<dl> <dt>

[About Properties](about-properties.md)
</dt> <dt>

[**ProductCode**](productcode.md)
</dt> <dt>

[**PATCH**](patch.md)
</dt> <dt>

[Setting Public Property Values on the Command Line](setting-public-property-values-on-the-command-line.md)
</dt> <dt>

[**MsiApplyMultiplePatches**](/windows/desktop/api/Msi/nf-msi-msiapplymultiplepatchesa)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




