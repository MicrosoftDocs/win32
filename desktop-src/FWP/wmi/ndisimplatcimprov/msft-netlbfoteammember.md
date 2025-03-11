---
description: Represents members of an Lbfo team.
ms.assetid: d483e2c5-53cc-48b5-99fc-6f7e33095391
title: MSFT\_NetLbfoTeamMember class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetLbfoTeamMember
- MSFT_NetLbfoTeamMember.AdministrativeMode
- MSFT_NetLbfoTeamMember.OperationalMode
api_type: 
- DllExport
api_location: 
- NdisIMPlatCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetLbfoTeamMember class

Represents members of an Lbfo team.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MsNetImPlatform")]
class MSFT_NetLbfoTeamMember : MSFT_NetImPlatAdapter
{
  uint32 AdministrativeMode;
  uint32 OperationalMode;
};
```

## Members

The **MSFT\_NetLbfoTeamMember** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetLbfoTeamMember** class has these properties.

<dl> <dt>

**AdministrativeMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Administrative role of this member in the team.

<dl> <dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>**Active** (0)
</dt> <dt>

<span id="Standby"></span><span id="standby"></span><span id="STANDBY"></span>**Standby** (1)
</dt> </dl>

</dd> <dt>

**OperationalMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current operational mode of this member in the team.

<dl> <dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>**Active** (0)
</dt> <dt>

<span id="Standby"></span><span id="standby"></span><span id="STANDBY"></span>**Standby** (1)
</dt> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>**Failed** (4096)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>MsNetImPlatform.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NdisIMPlatCim.dll</dt> </dl>   |



 

 




