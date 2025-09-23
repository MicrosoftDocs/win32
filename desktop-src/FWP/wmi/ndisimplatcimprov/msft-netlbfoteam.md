---
description: Represents an Lbfo team.
ms.assetid: aeae6c5a-9264-4488-90f7-94b6dc12a2ef
title: MSFT\_NetLbfoTeam class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetLbfoTeam
- MSFT_NetLbfoTeam.TeamingMode
- MSFT_NetLbfoTeam.LoadBalancingAlgorithm
- MSFT_NetLbfoTeam.Status
api_type: 
- DllExport
api_location: 
- NdisIMPlatCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetLbfoTeam class

Represents an Lbfo team.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("MsNetImPlatform")]
class MSFT_NetLbfoTeam : MSFT_NetImPlatTeam
{
  uint32 TeamingMode;
  uint32 LoadBalancingAlgorithm;
  uint32 Status;
};
```

## Members

The **MSFT\_NetLbfoTeam** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetLbfoTeam** class has these methods.



| Method                                    | Description                |
|:------------------------------------------|:---------------------------|
| [**Rename**](rename-msft-netlbfoteam.md) | Renames a team.<br/> |



 

### Properties

The **MSFT\_NetLbfoTeam** class has these properties.

<dl> <dt>

**LoadBalancingAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The load balancing algorithm for all providers.

<dl> <dt>

<span id="TransportPorts"></span><span id="transportports"></span><span id="TRANSPORTPORTS"></span>**TransportPorts** (0)
</dt> <dt>

<span id="IPAddresses"></span><span id="ipaddresses"></span><span id="IPADDRESSES"></span>**IPAddresses** (2)
</dt> <dt>

<span id="MacAddresses"></span><span id="macaddresses"></span><span id="MACADDRESSES"></span>**MacAddresses** (3)
</dt> <dt>

<span id="HyperVPort"></span><span id="hypervport"></span><span id="HYPERVPORT"></span>**HyperVPort** (4)
</dt> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>**Dynamic** (5)
</dt> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current operational status of the team.

<dl> <dt>

<span id="Up"></span><span id="up"></span><span id="UP"></span>**Up** (0)
</dt> <dt>

<span id="Down"></span><span id="down"></span><span id="DOWN"></span>**Down** (1)
</dt> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (2)
</dt> </dl>

</dd> <dt>

**TeamingMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The teaming mode value for all providers.

<dl> <dt>

<span id="Static"></span><span id="static"></span><span id="STATIC"></span>**Static** (0)
</dt> <dt>

<span id="SwitchIndependent"></span><span id="switchindependent"></span><span id="SWITCHINDEPENDENT"></span>**SwitchIndependent** (1)
</dt> <dt>

<span id="Lacp"></span><span id="lacp"></span><span id="LACP"></span>**Lacp** (2)
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



 

 




