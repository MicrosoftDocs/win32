---
description: Represents an association between a switch team and its members.
ms.assetid: 47dab3d6-030b-410a-8042-03c772f07ba9
title: MSFT\_NetSwitchTeam\_TeamMember class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSwitchTeam_TeamMember
- MSFT_NetSwitchTeam_TeamMember.TeamOfTheMember
- MSFT_NetSwitchTeam_TeamMember.MemberOfTheTeam
api_type: 
- DllExport
api_location: 
- NetSwitchTeamCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetSwitchTeam\_TeamMember class

Represents an association between a switch team and its members.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetSwitchTeam")]
class MSFT_NetSwitchTeam_TeamMember
{
  MSFT_NetSwitchTeam       REF TeamOfTheMember;
  MSFT_NetSwitchTeamMember REF MemberOfTheTeam;
};
```

## Members

The **MSFT\_NetSwitchTeam\_TeamMember** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetSwitchTeam\_TeamMember** class has these properties.

<dl> <dt>

**MemberOfTheTeam**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetSwitchTeamMember**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The switch team member associated with the switch team.

</dd> <dt>

**TeamOfTheMember**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetSwitchTeam**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The switch team associated with the switch team member.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>NetSwitchTeam.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>NetSwitchTeamCim.dll</dt> </dl> |



 

 




