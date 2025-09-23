---
description: Represents a NetAdapter that is a Team NIC for an Lbfo Team.
ms.assetid: 9a229e8f-33c1-4714-8312-ee14f86c6c71
title: MSFT\_NetLbfoTeamNic class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetLbfoTeamNic
- MSFT_NetLbfoTeamNic.VlanID
- MSFT_NetLbfoTeamNic.Primary
- MSFT_NetLbfoTeamNic.Default
api_type: 
- DllExport
api_location: 
- NdisIMPlatCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetLbfoTeamNic class

Represents a NetAdapter that is a Team NIC for an Lbfo Team.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MsNetImPlatform")]
class MSFT_NetLbfoTeamNic : MSFT_NetImPlatAdapter
{
  uint32  VlanID;
  boolean Primary;
  boolean Default;
};
```

## Members

The **MSFT\_NetLbfoTeamNic** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetLbfoTeamNic** class has these properties.

<dl> <dt>

**Default**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the TeamNic is the default TeamNic.

</dd> <dt>

**Primary**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the TeamNic is the primary TeamNic.

</dd> <dt>

**VlanID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

VlanID of the TeamNic.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>MsNetImPlatform.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NdisIMPlatCim.dll</dt> </dl>   |



 

 




