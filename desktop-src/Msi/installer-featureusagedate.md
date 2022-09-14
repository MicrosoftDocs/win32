---
description: The FeatureUsageDate property is a read-only property that returns the date the specified feature was last used.
ms.assetid: 444e54b2-94e7-44ea-8d7b-eeac984e3715
title: Installer.FeatureUsageDate property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.FeatureUsageDate
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.FeatureUsageDate property

The **FeatureUsageDate** property is a read-only property that returns the date the specified feature was last used.

This property is read-only.

## Syntax


```JScript
propVal = Installer.FeatureUsageDate
```



## Property value

## Remarks

Use of the [**UseFeature**](installer-usefeature.md), [**ProvideComponent**](installer-providecomponent.md) or [**ProvideQualifiedComponent**](installer-providequalifiedcomponent.md) methods or their API equivalents on the specified feature sets this property.

The date is in the MS-DOS date format as shown in the following table.



| Bits | Contents                                            |
|------|-----------------------------------------------------|
| 0-4  | Day of the month (1-31)                             |
| 5-8  | Month (1 = January, 2 = February, and so on)        |
| 9-15 | Year offset from 1980 (add 1980 to get actual year) |



 

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

 

 




