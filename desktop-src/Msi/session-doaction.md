---
description: The DoAction method of the Session object executes the action function corresponding to the name supplied.
ms.assetid: 6cff1cf1-1c8f-4c43-a687-e927e8573e55
title: Session.DoAction method (Photoacquire.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.DoAction
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.DoAction method

The **DoAction** method of the [**Session**](session-object.md) object executes the action function corresponding to the name supplied. If a Null action name is supplied, the engine uses the uppercase value of the [ACTION property](action.md) as the action to perform. If no property value is defined, the default action is performed, currently defined as INSTALL. This method returns an integer enumeration.

## Syntax


```JScript
Session.DoAction(
  action
)
```



## Parameters

<dl> <dt>

*action* 
</dt> <dd>

Required string name of the action to execute. Case-sensitive.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Actions that update the system, such as the [InstallFiles](installfiles-action.md) and [WriteRegistryValues](writeregistryvalues-action.md) actions, cannot be run by calling the **DoAction** method. The exception to this rule is if the **DoAction** method is called from a custom action that is scheduled in the [InstallExecuteSequence table](installexecutesequence-table.md) between the [InstallInitialize](installinitialize-action.md) and [InstallFinalize actions](installfinalize-action.md). Actions that do not update the system, such as [AppSearch](appsearch-action.md) or [CostInitialize](costinitialize-action.md), can be called.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| Header<br/>  | <dl> <dt>Photoacquire.h</dt> </dl>                                                                                                                                                               |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




