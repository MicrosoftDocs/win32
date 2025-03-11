---
description: Represents an association between an Lbfo team and its members.
ms.assetid: 15a01c4a-b666-45b6-adcf-7fed46bbb748
title: MSFT\_NetLbfoTeam\_TeamMember class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetLbfoTeam_TeamMember
- MSFT_NetLbfoTeam_TeamMember.GroupComponent
- MSFT_NetLbfoTeam_TeamMember.PartComponent
api_type: 
- DllExport
api_location: 
- NdisIMPlatCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetLbfoTeam\_TeamMember class

Represents an association between an Lbfo team and its members.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MsNetImPlatform")]
class MSFT_NetLbfoTeam_TeamMember : CIM_Component
{
  MSFT_NetLbfoTeam       REF GroupComponent;
  MSFT_NetLbfoTeamMember REF PartComponent;
};
```

## Members

The **MSFT\_NetLbfoTeam\_TeamMember** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetLbfoTeam\_TeamMember** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetLbfoTeam**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The LbfoTeam associated with the LbfoTeamMember.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetLbfoTeamMember**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The LbfoTeamMember associated with the LbfoTeam.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>MsNetImPlatform.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NdisIMPlatCim.dll</dt> </dl>   |



 

 




