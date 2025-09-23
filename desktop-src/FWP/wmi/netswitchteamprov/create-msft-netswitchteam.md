---
description: Creates a new switch team with initial members.
ms.assetid: a95bd48e-0bde-4706-8e08-32776cf85b78
title: Create method of the MSFT\_NetSwitchTeam class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSwitchTeam.Create
api_type: 
- COM
api_location: 
- NetSwitchTeamCim.dll
ROBOTS: INDEX,FOLLOW
---

# Create method of the MSFT\_NetSwitchTeam class

Creates a new switch team with initial members.

## Syntax


```mof
uint32 Create(
  [in] string Name,
  [in] string TeamMembers[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the switch team to create.

</dd> <dt>

*TeamMembers* \[in\]
</dt> <dd>

An array that contains the names of the initial members of the new switch team.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>NetSwitchTeam.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>NetSwitchTeamCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetSwitchTeam**](msft-netswitchteam.md)
</dt> </dl>

 

 




