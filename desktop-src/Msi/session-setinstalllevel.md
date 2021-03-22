---
description: The SetInstallLevel method of the Session object sets the install level for the current installation to a specified value and recalculates the Select and Installed states for all features in the Feature table.
ms.assetid: d47f8025-d484-42c7-9808-5ee590a4d200
title: Session.SetInstallLevel method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.SetInstallLevel
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.SetInstallLevel method

The **SetInstallLevel** method of the [**Session**](session-object.md) object sets the install level for the current installation to a specified value and recalculates the Select and Installed states for all features in the Feature table. It also sets the Action state of each component in the [Component table](component-table.md) based on the new level.

## Syntax


```JScript
Session.SetInstallLevel(
  installLevel
)
```



## Parameters

<dl> <dt>

*installLevel* 
</dt> <dd>

Required requested new install level.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The [CostInitialize action](costinitialize-action.md) must be executed prior to calling **SetInstallLevel**.

If 0 is passed for the *installLevel* parameter, the current install level is not changed, but all features are still updated based on the current install level. For example, this functionality could be used by the Handler module to reset all selections back to their initial default states at any point in the UI selection process.

If the method fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




