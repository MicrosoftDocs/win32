---
description: The ConfigureProduct method of the Installer object installs or uninstalls a product.
ms.assetid: 1215a03f-6c96-4416-881f-0071c1b3c5df
title: Installer.ConfigureProduct method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ConfigureProduct
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ConfigureProduct method

The **ConfigureProduct** method of the [**Installer**](installer-object.md) object installs or uninstalls a product.

## Syntax


```JScript
Installer.ConfigureProduct(
  Product,
  InstallLevel,
  InstallState
)
```



## Parameters

<dl> <dt>

*Product* 
</dt> <dd>

Specifies the product code of the product.

</dd> <dt>

*InstallLevel* 
</dt> <dd>

Specifies the default installation configuration of the product. The InstallLevel parameter is ignored and all features are installed if the InstallState parameter is set to any other value than msiInstallStateDefault.

This parameter must be either 0 (install using authored feature levels), 65535 (install all features), or a value between 0 and 65535 to install a subset of available features.

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

## Remarks

The **ConfigureProduct** method displays the user interface using current settings. User interface settings can be changed by modifying the [**UILevel property (Installer object)**](installer-uilevel.md) before calling the **ConfigureProduct** method.

If the *InstallState* parameter is set to any other value than msiInstallStateDefault, the *InstallLevel* parameter is ignored and all features of the product are installed. Use the [**ConfigureFeature**](installer-configurefeature.md) method to control the installation of individual features when the *InstallState* parameter is not set to msiInstallStateDefault.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiConfigureProduct**](/windows/desktop/api/Msi/nf-msi-msiconfigureproducta)
</dt> <dt>

[Installation and Configuration Functions](installer-function-reference.md)
</dt> </dl>

 

 




