---
description: The FeatureInfo method of the Session object returns a FeatureInfo object containing descriptive information for the specified feature.
ms.assetid: f5391fd4-984e-44cc-8b6c-fd97834e0674
title: Session.FeatureInfo method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.FeatureInfo
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.FeatureInfo method

The **FeatureInfo** method of the [**Session**](session-object.md) object returns a **FeatureInfo** object containing descriptive information for the specified feature.

## Syntax


```JScript
Session.FeatureInfo(
  Feature
)
```



## Parameters

<dl> <dt>

*Feature* 
</dt> <dd>

Identifies the feature of interest.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



## See also

<dl> <dt>

[**MsiGetFeatureInfo**](/windows/desktop/api/Msi/nf-msi-msigetfeatureinfoa)
</dt> </dl>

 

 




