---
description: Renames a switch team.
ms.assetid: 62f6ac51-0388-4182-b258-ce8e31f36a69
title: Rename method of the MSFT\_NetSwitchTeam class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSwitchTeam.Rename
api_type: 
- COM
api_location: 
- NetSwitchTeamCim.dll
ROBOTS: INDEX,FOLLOW
---

# Rename method of the MSFT\_NetSwitchTeam class

Renames a switch team.

## Syntax


```mof
uint32 Rename(
  [in] string Name,
  [in] string NewName
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The current name of a switch team.

</dd> <dt>

*NewName* \[in\]
</dt> <dd>

The new name to give to the switch team.

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

 

 




