---
description: The ProvideQualifiedComponent method of the Installer object returns the full component path and performs any necessary installation. If necessary, this method prompts for the source and increments the usage count for the feature.
ms.assetid: 4f9a5094-1556-4d86-8b51-c8c3ce1cbed4
title: Installer.ProvideQualifiedComponent method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ProvideQualifiedComponent
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ProvideQualifiedComponent method

The **ProvideQualifiedComponent** method of the [**Installer**](installer-object.md) object returns the full component path and performs any necessary installation. If necessary, this method prompts for the source and increments the usage count for the feature.

## Syntax


```JScript
Installer.ProvideQualifiedComponent(
  Category,
  Qualifier,
  InstallMode
)
```



## Parameters

<dl> <dt>

*Category* 
</dt> <dd>

Specifies the component ID for the requested component. This may not be the GUID for the component itself but rather a server that provides the correct functionality, as in the ComponentId column of the [PublishComponent table](publishcomponent-table.md).

</dd> <dt>

*Qualifier* 
</dt> <dd>

Specifies a qualifier into a list of advertising components (from [PublishComponent table](publishcomponent-table.md)).

</dd> <dt>

*InstallMode* 
</dt> <dd>

Defines the installation mode. This parameter can be one of the values shown in the following table.



| InstallMode                                                                                                                                                                                                                                                                                                                                                         | Meaning                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="msiInstallModeDefault"></span><span id="msiinstallmodedefault"></span><span id="MSIINSTALLMODEDEFAULT"></span><dl> <dt>**msiInstallModeDefault**</dt> <dt>0</dt> </dl>                                                                                 | Provides the component, performing any necessary installation.<br/>                                                                                                                                                           |
| <span id="msiInstallModeExisting"></span><span id="msiinstallmodeexisting"></span><span id="MSIINSTALLMODEEXISTING"></span><dl> <dt>**msiInstallModeExisting**</dt> <dt>–1</dt> </dl>                                                                            | Provides the component only if the feature exists; otherwise returns an empty string. This mode verifies the existence of the component's key file.<br/>                                                                      |
| <span id="msiInstallModeNoDetection"></span><span id="msiinstallmodenodetection"></span><span id="MSIINSTALLMODENODETECTION"></span><dl> <dt>**msiInstallModeNoDetection**</dt> <dt>–2</dt> </dl>                                                                | Provides the component only if the feature exists; otherwise returns an empty string. This mode only checks that the component is registered but does not verify the existence of the component's key file.<br/>              |
| <span id="msiInstallModeNoSourceResolution"></span><span id="msiinstallmodenosourceresolution"></span><span id="MSIINSTALLMODENOSOURCERESOLUTION"></span><dl> <dt>**msiInstallModeNoSourceResolution**</dt> <dt>–3</dt> </dl>                                    | Provides the component path only if the feature exists with an InstallState parameter of *msiInstallStateLocal*. This checks the component's registration but does not verify the existence of the component's key file.<br/> |
| <span id="combination_of_the_msiReinstallMode_flags"></span><span id="combination_of_the_msireinstallmode_flags"></span><span id="COMBINATION_OF_THE_MSIREINSTALLMODE_FLAGS"></span><dl> <dt>**combination of the msiReinstallMode flags**</dt> <dt> </dt> </dl> | Calls [**ReinstallFeature**](installer-reinstallfeature.md) to reinstall the feature using this parameter for the *ReinstallMode* parameter, and then provides the component.<br/>                                           |



 

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

[**MsiProvideQualifiedComponent**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponenta)
</dt> </dl>

 

 




