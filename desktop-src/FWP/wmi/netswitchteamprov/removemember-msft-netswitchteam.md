---
description: Removes an existing member from a switch team.
ms.assetid: f7f26dcc-5ee9-4f88-93bd-1a7c1b5adcac
title: RemoveMember method of the MSFT\_NetSwitchTeam class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSwitchTeam.RemoveMember
api_type: 
- COM
api_location: 
- NetSwitchTeamCim.dll
ROBOTS: INDEX,FOLLOW
---

# RemoveMember method of the MSFT\_NetSwitchTeam class

Removes an existing member from a switch team.

## Syntax


```mof
uint32 RemoveMember(
  [in] string Name,
  [in] string Team
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the member to remove from the switch team.

</dd> <dt>

*Team* \[in\]
</dt> <dd>

The switch team in which to remove a member.

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

 

 




