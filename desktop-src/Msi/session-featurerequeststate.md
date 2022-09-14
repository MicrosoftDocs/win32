---
description: The FeatureRequestState property is a read-write property of the Session object.
ms.assetid: ba19603b-ac81-4a8b-81ca-ad5f28974599
title: Session.FeatureRequestState property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.FeatureRequestState
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.FeatureRequestState property

The **FeatureRequestState** property is a read-write property of the [**Session**](session-object.md) object. It can be used to obtain the current action state of a feature or to request a change in the action of a feature and its subfeatures. The feature must be named in the [Feature](feature-table.md) table. If a change to the action state of a feature is requested, the action state of all components of the changed feature may be changed as well. The action state of components shared by more than one feature will be changed as appropriate based on the new feature action state (see Remarks). The **FeatureRequestState** property can also be used to configure all features at once by specifying the keyword ALL instead of a specific feature name.

This property is read/write.

## Syntax


```JScript
propVal = Session.FeatureRequestState
Session.FeatureRequestState = propVal 
```



## Property value

Required string that specifies the name of the feature to be configured. To set all features to a desired request state, use the reserved case-insensitive word: ALL.

## Remarks

The [**SetInstallLevel**](session-setinstalllevel.md) method must be called before calling **FeatureRequestState**.

If the current state of the feature is being requested, the **FeatureRequestState** property returns one of the following values.



| Selection state name         | Meaning                                                               |
|------------------------------|-----------------------------------------------------------------------|
| msiInstallStateUnknown = -1  | No action is taken for the feature. This is equivalent to null.       |
| msiInstallStateAdvertised =1 | Feature is to be advertised.                                          |
| msiInstallStateAbsent = 2    | Feature is to be removed.                                             |
| msiInstallStateLocal = 3     | Feature is to be installed as run-local.                              |
| msiInstallStateSource = 4    | Feature is to be installed as run-from-source.                        |
| msiInstallStateDefault = 5   | Feature is to be reinstalled with the feature's current action state. |



 

For example, the following obtains the current state of "MyFeature" from a VBScript custom action.


```VB
Dim iRequestState
iRequestState = Session.FeatureRequestState("MyFeature")
```



If the state of the feature is being configured, the **FeatureRequestState** property should be set to one of the following values.



| Selection state name          | Meaning                                 |
|-------------------------------|-----------------------------------------|
| msiInstallStateAdvertised = 1 | Advertise the feature.                  |
| msiInstallStateAbsent = 2     | Remove the feature.                     |
| msiInstallStateLocal = 3      | Install the feature as run-local.       |
| msiInstallStateSource = 4     | Install the feature as run-from-source. |



 

For example, the following requests from a VBScript custom action that "MyFeature" be installed to run locally on the computer.


```VB
Session.FeatureRequestState("MyFeature")=3
```



When **FeatureRequestState** is called, the installer attempts to set the action state of each component tied to the specified feature to the specified state, as best as possible. However, there are common situations when the request cannot be fully honored. For example, if a feature is tied to two components, Component A and Component B, through the [FeatureComponents](featurecomponents-table.md) table and Component A has the **msidbComponentAttributesLocalOnly** attribute and component B has the **msidbComponentAttributesSourceOnly** attribute. In this case, if **FeatureRequestState** is called with a requested state of either msiInstallStateLocal or msiInstallStateSource, the request cannot be honored for both components. In this case, both components can be turned on with Component A set to msiInstallStateLocal and Component B set to msiInstallStateSource.

If more than one feature is linked to a single component, the final action state of that component is determined as follows: If at least one feature calls for the component to be installed locally, it is installed msiInstallStateLocal. If at least one feature calls for the component to be run from the source media, it is installed msiInstallStateSource. If at least one feature calls for the removal of the component, the action state is msiInstallStateAbsent. For more information on how features are selected for installation, see the [Feature](feature-table.md) table.

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

[Feature](feature-table.md)
</dt> </dl>

 

 




