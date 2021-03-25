---
description: The FeatureCurrentState property of the Session object is a read-only property that returns the current installed state of the designated feature. For state values, see the FeatureRequestState property.
ms.assetid: c4c325dc-6e7e-4009-8707-952c04574170
title: Session.FeatureCurrentState property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.FeatureCurrentState
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.FeatureCurrentState property

The **FeatureCurrentState** property of the [**Session**](session-object.md) object is a read-only property that returns the current installed state of the designated feature. For state values, see the [**FeatureRequestState**](session-featurerequeststate.md) property.

This property is read-only.

## Syntax


```JScript
propVal = Session.FeatureCurrentState
```



## Property value

Required string name of the requested feature, and a primary key into the [Feature table](feature-table.md).

## Remarks

If the property fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



## See also

<dl> <dt>

[**Session**](session-object.md)
</dt> <dt>

[**FeatureRequestState property**](session-featurerequeststate.md)
</dt> </dl>

 

 




