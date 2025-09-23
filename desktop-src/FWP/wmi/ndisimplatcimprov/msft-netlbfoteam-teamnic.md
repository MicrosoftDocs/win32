---
description: Represents an association between an Lbfo Team and its TeamNics.
ms.assetid: 8a2bccf8-36f7-4ea7-80d7-5dd3aabba141
title: MSFT\_NetLbfoTeam\_TeamNic class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetLbfoTeam_TeamNic
- MSFT_NetLbfoTeam_TeamNic.GroupComponent
- MSFT_NetLbfoTeam_TeamNic.PartComponent
api_type: 
- DllExport
api_location: 
- NdisIMPlatCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetLbfoTeam\_TeamNic class

Represents an association between an Lbfo Team and its TeamNics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MsNetImPlatform")]
class MSFT_NetLbfoTeam_TeamNic : CIM_Component
{
  MSFT_NetLbfoTeam    REF GroupComponent;
  MSFT_NetLbfoTeamNic REF PartComponent;
};
```

## Members

The **MSFT\_NetLbfoTeam\_TeamNic** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetLbfoTeam\_TeamNic** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetLbfoTeam**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The LbfoTeam associated with the LbfoTeamNic.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetLbfoTeamNic**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The LbfoTeamNic associated with the LbfoTeam.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>MsNetImPlatform.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NdisIMPlatCim.dll</dt> </dl>   |



 

 




