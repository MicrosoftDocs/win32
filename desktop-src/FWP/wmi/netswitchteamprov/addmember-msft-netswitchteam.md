---
description: Adds a new member to an existing switch team.
ms.assetid: c5e5ff83-b115-4caa-8271-8e0efb64aeb8
title: AddMember method of the MSFT\_NetSwitchTeam class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSwitchTeam.AddMember
api_type: 
- COM
api_location: 
- NetSwitchTeamCim.dll
ROBOTS: INDEX,FOLLOW
---

# AddMember method of the MSFT\_NetSwitchTeam class

Adds a new member to an existing switch team.

## Syntax


```mof
uint32 AddMember(
  [in] string Name,
  [in] string Team
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the member to add.

</dd> <dt>

*Team* \[in\]
</dt> <dd>

The switch team in which to add the member.

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

 

 




