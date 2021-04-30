---
description: The FeatureCost property of the Session object returns the total amount of disk space (in units of 512 bytes) required by the specified feature and its parent features (up to the root of the Feature table).
ms.assetid: 5df9912a-2722-41c8-991b-256a009e85df
title: Session.FeatureCost property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.FeatureCost
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.FeatureCost property

The **FeatureCost** property of the [**Session**](session-object.md) object returns the total amount of disk space (in units of 512 bytes) required by the specified feature and its parent features (up to the root of the Feature table). For each feature, the total cost is made up of the disk costs attributed to every component linked to the feature.

This property is read-only.

## Syntax


```JScript
propVal = Session.FeatureCost
```



## Property value

## Remarks

If the property fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




