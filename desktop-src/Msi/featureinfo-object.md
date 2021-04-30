---
description: The FeatureInfo object contains information regarding the targeted feature and is created from the Session object using the FeatureInfo Method.
ms.assetid: c9c96799-22c7-4e74-947b-3b8d31ebc1f1
title: FeatureInfo object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FeatureInfo
api_type: 
- COM
api_location: 
- Msi.dll
---

# FeatureInfo object

The **FeatureInfo** object contains information regarding the targeted feature and is created from the [**Session**](session-object.md) object using the [**FeatureInfo**](session-featureinfo.md) Method.

## Members

The **FeatureInfo** object has these types of members:

-   [Properties](#properties)

### Properties

The **FeatureInfo** object has these properties.



| Property                                                  | Access type           | Description                                                                                 |
|:----------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------|
| [**Attributes**](featureinfo-attributes.md)<br/>   | Read/write<br/> | Returns the value for the feature in the Attributes column of the Feature table.<br/> |
| [**Description**](featureinfo-description.md)<br/> |                       | Returns the description of the feature.<br/>                                          |
| [**Title**](featureinfo-title.md)<br/>             | Read-only<br/>  | Returns the title of the feature.<br/>                                                |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IFeatureInfo is defined as 000C109F-0000-0000-C000-000000000046<br/>                                                                                                                                                                         |



## See also

<dl> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




