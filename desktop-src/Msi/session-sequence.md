---
description: The Sequence method of the Session object opens a query on the specified table, ordering the actions by the numbers in the Sequence column.
ms.assetid: cde735b0-0b97-4c4f-adfc-f0321aafb012
title: Session.Sequence method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.Sequence
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.Sequence method

The **Sequence** method of the [**Session**](session-object.md) object opens a query on the specified table, ordering the actions by the numbers in the Sequence column. For each row fetched, the [**DoAction**](session-doaction.md) method is called, provided that any supplied condition expression does not evaluate to False. Returns an enumeration msiDoActionStatusEnum, as described in the [**DoAction**](session-doaction.md) method.

## Syntax


```JScript
Session.Sequence(
  table
)
```



## Parameters

<dl> <dt>

*table* 
</dt> <dd>

Required string name of the table to use for sequencing.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method is normally called internally by top-level actions.

An action sequence containing actions that update the system, such as the [InstallFiles](installfiles-action.md) and [WriteRegistryValues](writeregistryvalues-action.md) actions, cannot be run by calling the **Sequence** method. The exception to this rule is if the **Sequence** method is called from a custom action that is scheduled in the [InstallExecuteSequence table](installexecutesequence-table.md) between the [InstallInitialize](installinitialize-action.md) and [InstallFinalize actions](installfinalize-action.md). Actions that do not update the system, such as [AppSearch](appsearch-action.md) or [CostInitialize](costinitialize-action.md), can be called.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 




