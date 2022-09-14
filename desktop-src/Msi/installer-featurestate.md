---
description: The read-only FeatureState property returns the installed state of a feature.
ms.assetid: a3d30296-191e-4446-b5b1-a92f8991926a
title: Installer.FeatureState property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.FeatureState
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.FeatureState property

The read-only **FeatureState** property returns the installed state of a feature.

This property is read-only.

## Syntax


```JScript
propVal = Installer.FeatureState
```



## Property value

## Remarks

This property returns one of the following values.



| Value                     | Description                                      |
|---------------------------|--------------------------------------------------|
| msiInstallStateAbsent     | The feature is not installed.                    |
| msiInstallStateAdvertised | The feature is advertised.                       |
| msiInstallStateLocal      | The feature is installed to run locally.         |
| msiInstallStateSource     | The feature is installed to run from source.     |
| msiInstallStateInvalidArg | An invalid parameter was passed to the function. |
| msiInstallStateUnknown    | The product code or feature ID is unknown.       |
| msiInstallStateBadConfig  | The configuration data is corrupt.               |



 

 

The **FeatureState** property does not validate that the feature is accessible.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiQueryFeatureState**](/windows/desktop/api/Msi/nf-msi-msiqueryfeaturestatea)
</dt> </dl>

 

 




