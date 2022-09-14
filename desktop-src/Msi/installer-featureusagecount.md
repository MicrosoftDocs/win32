---
description: The FeatureUsageCount property is a read-only property that returns the number of times the feature has been used.
ms.assetid: 70171e22-d73a-4718-a360-df9d1722761b
title: Installer.FeatureUsageCount property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.FeatureUsageCount
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.FeatureUsageCount property

The **FeatureUsageCount** property is a read-only property that returns the number of times the feature has been used.

This property is read-only.

## Syntax


```JScript
propVal = Installer.FeatureUsageCount
```



## Property value

## Remarks

Use of the [**UseFeature**](installer-usefeature.md), [**ProvideComponent**](installer-providecomponent.md) or [**ProvideQualifiedComponent**](installer-providequalifiedcomponent.md) methods or their API equivalents on the specified feature increments this property.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiGetFeatureUsage**](/windows/desktop/api/Msi/nf-msi-msigetfeatureusagea)
</dt> </dl>

 

 




