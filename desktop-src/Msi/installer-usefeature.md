---
description: The UseFeature method of the Installer object increments the usage count for a particular feature and returns the installation state for that feature. This method should be used to indicate an application's intent to use a feature.
ms.assetid: c9ea812c-2f95-4ba4-ad8e-b96f7fc14bb1
title: Installer.UseFeature method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.UseFeature
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.UseFeature method

The **UseFeature** method of the [**Installer**](installer-object.md) object increments the usage count for a particular feature and returns the installation state for that feature. This method should be used to indicate an application's intent to use a feature.

## Syntax


```JScript
Installer.UseFeature(
  Product,
  Feature,
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

Identifies the feature to be used.

</dd> <dt>

*InstallMode* 
</dt> <dd>

This parameter must be *msiInstallModeNoDetection*.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The **UseFeature** method should only be used on features known to be published. The application should determine the status of the feature by calling either the [**FeatureState**](installer-featurestate.md) property or [**Features**](installer-features.md) property or their API equivalents.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiUseFeatureEx**](/windows/desktop/api/Msi/nf-msi-msiusefeatureexa)
</dt> </dl>

 

 




