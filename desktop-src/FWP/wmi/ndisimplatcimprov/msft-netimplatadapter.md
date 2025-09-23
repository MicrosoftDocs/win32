---
description: Represents Network Adapters used in IM Platform, ie. the members and team NICs.
ms.assetid: d01301a0-0df4-427a-8275-82f80157cbac
title: MSFT\_NetImPlatAdapter class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetImPlatAdapter
- MSFT_NetImPlatAdapter.InstanceID
- MSFT_NetImPlatAdapter.Name
- MSFT_NetImPlatAdapter.InterfaceDescription
- MSFT_NetImPlatAdapter.Team
- MSFT_NetImPlatAdapter.TransmitLinkSpeed
- MSFT_NetImPlatAdapter.ReceiveLinkSpeed
- MSFT_NetImPlatAdapter.FailureReason
api_type: 
- DllExport
api_location: 
- NdisIMPlatCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetImPlatAdapter class

Represents Network Adapters used in IM Platform, ie. the members and team NICs.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, ClassVersion("10")]
class MSFT_NetImPlatAdapter : CIM_EnabledLogicalElement
{
  string InstanceID;
  string Name;
  string InterfaceDescription;
  string Team;
  uint64 TransmitLinkSpeed;
  uint64 ReceiveLinkSpeed;
  uint32 FailureReason;
};
```

## Members

The **MSFT\_NetImPlatAdapter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetImPlatAdapter** class has these properties.

<dl> <dt>

**FailureReason**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The failure reason.

<dl> <dt>

<span id="NoFailure"></span><span id="nofailure"></span><span id="NOFAILURE"></span>**NoFailure** (0)
</dt> <dt>

<span id="AdministrativeDecision"></span><span id="administrativedecision"></span><span id="ADMINISTRATIVEDECISION"></span>**AdministrativeDecision** (1)
</dt> <dt>

<span id="PhysicalMediaDisconnected"></span><span id="physicalmediadisconnected"></span><span id="PHYSICALMEDIADISCONNECTED"></span>**PhysicalMediaDisconnected** (3)
</dt> <dt>

<span id="WaitingForStableConnectivity"></span><span id="waitingforstableconnectivity"></span><span id="WAITINGFORSTABLECONNECTIVITY"></span>**WaitingForStableConnectivity** (4)
</dt> <dt>

<span id="LacpNegotiationIssue"></span><span id="lacpnegotiationissue"></span><span id="LACPNEGOTIATIONISSUE"></span>**LacpNegotiationIssue** (5)
</dt> <dt>

<span id="NicNotPresent"></span><span id="nicnotpresent"></span><span id="NICNOTPRESENT"></span>**NicNotPresent** (6)
</dt> <dt>

<span id="UnknownFailure"></span><span id="unknownfailure"></span><span id="UNKNOWNFAILURE"></span>**UnknownFailure** (7)
</dt> <dt>

<span id="VirtualSwitchLacksExternalConnectivity"></span><span id="virtualswitchlacksexternalconnectivity"></span><span id="VIRTUALSWITCHLACKSEXTERNALCONNECTIVITY"></span>**VirtualSwitchLacksExternalConnectivity** (9)
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The NetCfgInstanceId of this adapter.

</dd> <dt>

**InterfaceDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The description of the member adapter.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (1024)
</dt> </dl>

The alias of the member adapter.

</dd> <dt>

**ReceiveLinkSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The receive speed of the adapter.

</dd> <dt>

**Team**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the team this belongs to.

</dd> <dt>

**TransmitLinkSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The transmission speed of the adapter.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>MsNetImPlatform.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NdisIMPlatCim.dll</dt> </dl>   |



 

 




