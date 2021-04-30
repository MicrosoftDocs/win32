---
description: The ProvideComponent method of the Installer object returns the full component path and performs any necessary installation.
ms.assetid: 2bf09515-6f65-4712-89c1-01c43c1ce27c
title: Installer.ProvideComponent method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ProvideComponent
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ProvideComponent method

The **ProvideComponent** method of the [**Installer**](installer-object.md) object returns the full component path and performs any necessary installation. If necessary, the **ProvideComponent** method of the [**Installer**](installer-object.md) object prompts for the source and increments the usage count for the feature.

## Syntax


```JScript
Installer.ProvideComponent(
  Product,
  Feature,
  Component,
  InstallMode
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

Specifies the feature ID of the feature containing the component.

</dd> <dt>

*Component* 
</dt> <dd>

Specifies the component code.

</dd> <dt>

*InstallMode* 
</dt> <dd>

Defines the installation mode. This parameter can be one of the values shown in the following table.



| Name                                                                                                                                                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="msiInstallModeDefault"></span><span id="msiinstallmodedefault"></span><span id="MSIINSTALLMODEDEFAULT"></span><dl> <dt>**msiInstallModeDefault**</dt> <dt>0</dt> </dl>                                                                                | Provides the component path, performing any installation, if necessary.<br/>                                                                                                                                                  |
| <span id="msiInstallModeExisting"></span><span id="msiinstallmodeexisting"></span><span id="MSIINSTALLMODEEXISTING"></span><dl> <dt>**msiInstallModeExisting**</dt> <dt>–1</dt> </dl>                                                                           | Provides the component path only if the feature exists; otherwise, returns an empty string. This mode verifies the existence of the component's key file.<br/>                                                                |
| <span id="msiInstallModeNoDetection"></span><span id="msiinstallmodenodetection"></span><span id="MSIINSTALLMODENODETECTION"></span><dl> <dt>**msiInstallModeNoDetection**</dt> <dt>–2</dt> </dl>                                                               | Provides the component path only if the feature exists. Otherwise, returns an empty string. This mode checks the component's registration but does not verify the existence of the component's key file.<br/>                 |
| <span id="msiInstallModeNoSourceResolution"></span><span id="msiinstallmodenosourceresolution"></span><span id="MSIINSTALLMODENOSOURCERESOLUTION"></span><dl> <dt>**msiInstallModeNoSourceResolution**</dt> <dt>–3</dt> </dl>                                   | Provides the component path only if the feature exists with an InstallState parameter of *msiInstallStateLocal*. This checks the component's registration but does not verify the existence of the component's key file.<br/> |
| <span id="combination_of_the_msiReinstallMode_flags"></span><span id="combination_of_the_msireinstallmode_flags"></span><span id="COMBINATION_OF_THE_MSIREINSTALLMODE_FLAGS"></span><dl> <dt>**combination of the msiReinstallMode flags**</dt> <dt></dt> </dl> | Calls [**ReinstallFeature**](installer-reinstallfeature.md) to reinstall the feature using this parameter for the *ReinstallMode* parameter, and then provides the component.<br/>                                           |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The **ProvideComponent** method combines the functionality of [**UseFeature**](installer-usefeature.md), [**ConfigureFeature**](installer-configurefeature.md), and [**ComponentPath**](installer-componentpath.md). The **ProvideComponent** method simplifies the calling sequence, but it also increments the usage count and should be used with caution to prevent inaccurate usage counts. The **ProvideComponent** method also provides less flexibility than a series of individual calls to the methods and properties previously mentioned.

If the application is recovering from an unexpected situation, the application has probably already called [**UseFeature**](installer-usefeature.md) and incremented the usage count. In this case, the application should avoid incrementing the usage count by calling the [**ConfigureFeature**](installer-configurefeature.md) method instead of the **ProvideComponent** method.

The msiInstallModeExisting option cannot be used in combination with msiReinstallMode flags.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiProvideComponent**](/windows/desktop/api/Msi/nf-msi-msiprovidecomponenta)
</dt> </dl>

 

 




