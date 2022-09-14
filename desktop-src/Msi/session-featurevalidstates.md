---
description: The FeatureValidStates property of the Session object returns an integer representing bit flags with each relevant bit representing a valid installation state for the specified feature.
ms.assetid: 8a1f6911-b0a6-4fac-ba77-df4f1b7d15e2
title: Session.FeatureValidStates property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.FeatureValidStates
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.FeatureValidStates property

The **FeatureValidStates** property of the [**Session**](session-object.md) object returns an integer representing bit flags with each relevant bit representing a valid installation state for the specified feature.

This property is read-only.

## Syntax


```JScript
propVal = Session.FeatureValidStates
```



## Property value

Required string name of the feature item whose valid installation states are to be retrieved.

## Remarks

The return value is composed of bit flags as follows. Bit 0: if set, Local is a valid state. Bit 1: if set, Source is a valid state.

The **FeatureValidStates** property only succeeds after the installer has called the [CostInitialize](costinitialize-action.md) and [CostFinalize](costfinalize-action.md) actions.

**FeatureValidStates** determines state validity by querying all components that are linked to the specified feature without taking into account the current installed state of any component.

The possible valid states for a feature are determined as follows:

-   If the feature does not contain components, both INSTALLSTATE\_LOCAL and INSTALLSTATE\_SOURCE are valid states for the feature.
-   If at least one component of the feature has an attribute of msidbComponentAttributesLocalOnly or msidbComponentAttributesOptional, INSTALLSTATE\_LOCAL is a valid state for the feature.
-   If at least one component of the feature has an attribute of msidbComponentAttributesSourceOnly or msidbComponentAttributesOptional, INSTALLSTATE\_SOURCE is a valid state for the feature.
-   If a file of a component belonging to the feature is patched or from a compressed source, then INSTALLSTATE\_SOURCE is not included as a valid state for the feature.
-   INSTALLSTATE\_ADVERTISE is not a valid state if the feature disallows advertisement (msidbFeatureAttributesDisallowAdvertise) or the feature requires platform support for advertisement (msidbFeatureAttributesNoUnsupportedAdvertise) and the platform does not support it.
-   INSTALLSTATE\_ABSENT is a valid state for the feature if its attributes do not include msidbFeatureAttributesUIDisallowAbsent.
-   Valid states for child features marked to follow the parent feature (msidbFeatureAttributesFollowParent) are based upon the parent feature's action or installed state.

If the property fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




