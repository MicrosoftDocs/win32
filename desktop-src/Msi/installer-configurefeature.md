---
description: The ConfigureFeature method of the Installer object configures the installed state of a product feature.
ms.assetid: cc950951-3b43-4d86-9ff1-80aa2ccd11d5
title: Installer.ConfigureFeature method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ConfigureFeature
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ConfigureFeature method

The **ConfigureFeature** method of the [**Installer**](installer-object.md) object configures the installed state of a product feature.

## Syntax


```JScript
Installer.ConfigureFeature(
  Product,
  Feature,
  InstallState
)
```



## Parameters

<dl> <dt>

*Product* 
</dt> <dd>

Specifies the product code of the product.

</dd> <dt>

*Feature* 
</dt> <dd>

Specifies the feature ID of the feature to be configured.

</dd> <dt>

*InstallState* 
</dt> <dd>

Specifies the installation state for the feature. This parameter must be one of the following values.



| Value                                                                                                                                                                                                                                        | Meaning                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <span id="msiInstallStateAdvertised"></span><span id="msiinstallstateadvertised"></span><span id="MSIINSTALLSTATEADVERTISED"></span><dl> <dt>**msiInstallStateAdvertised**</dt> </dl> | The feature is advertised<br/>                         |
| <span id="msiInstallStateLocal"></span><span id="msiinstallstatelocal"></span><span id="MSIINSTALLSTATELOCAL"></span><dl> <dt>**msiInstallStateLocal**</dt> </dl>                     | The feature is installed locally.<br/>                 |
| <span id="msiInstallStateAbsent"></span><span id="msiinstallstateabsent"></span><span id="MSIINSTALLSTATEABSENT"></span><dl> <dt>**msiInstallStateAbsent**</dt> </dl>                 | The feature is uninstalled.<br/>                       |
| <span id="msiInstallStateSource"></span><span id="msiinstallstatesource"></span><span id="MSIINSTALLSTATESOURCE"></span><dl> <dt>**msiInstallStateSource**</dt> </dl>                 | The feature is installed to run from source.<br/>      |
| <span id="msiInstallStateDefault"></span><span id="msiinstallstatedefault"></span><span id="MSIINSTALLSTATEDEFAULT"></span><dl> <dt>**msiInstallStateDefault**</dt> </dl>             | The feature is installed to its default location.<br/> |



 

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

[**MsiConfigureFeature**](/windows/desktop/api/Msi/nf-msi-msiconfigurefeaturea)
</dt> <dt>

[Installation and Configuration Functions](installer-function-reference.md)
</dt> </dl>

 

 




