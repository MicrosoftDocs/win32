---
title: DhcpServerv4Failover class
description: Dhcp Server v4 Failover.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 80af5edc-b450-45ea-ba07-ac2d3f8b6a4e
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4Failover class
- DhcpServerv4Failover class, described
topic_type:
- apiref
api_name:
- DhcpServerv4Failover
- DhcpServerv4Failover.Name
- DhcpServerv4Failover.PartnerServer
- DhcpServerv4Failover.Mode
- DhcpServerv4Failover.ServerRole
- DhcpServerv4Failover.LoadBalancePercent
- DhcpServerv4Failover.ReservePercent
- DhcpServerv4Failover.ScopeId
- DhcpServerv4Failover.MaxClientLeadTime
- DhcpServerv4Failover.AutoStateTransition
- DhcpServerv4Failover.StateSwitchInterval
- DhcpServerv4Failover.State
- DhcpServerv4Failover.EnableAuth
- DhcpServerv4Failover.PrimaryServerIP
- DhcpServerv4Failover.SecondaryServerIP
- DhcpServerv4Failover.PrimaryServerName
- DhcpServerv4Failover.SecondaryServerName
- DhcpServerv4Failover.ServerType
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv4Failover class

Dhcp Server v4 Failover.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4Failover
{
  string   Name;
  string   PartnerServer;
  string   Mode;
  string   ServerRole;
  uint32   LoadBalancePercent;
  uint32   ReservePercent;
  string   ScopeId[];
  Datetime MaxClientLeadTime;
  boolean  AutoStateTransition;
  Datetime StateSwitchInterval;
  string   State;
  boolean  EnableAuth;
  string   PrimaryServerIP;
  string   SecondaryServerIP;
  string   PrimaryServerName;
  string   SecondaryServerName;
  string   ServerType;
};
```

## Members

The **DhcpServerv4Failover** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4Failover** class has these properties.

<dl> <dt>

**AutoStateTransition**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enables or disables the automatic transition from CommunicationInterrupted state to PartnerDown state.

</dd> <dt>

**EnableAuth**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enables or disables the message authentication.

</dd> <dt>

**LoadBalancePercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If FailoverMode is LoadBalance, this is the percent of load distribution else NA.

</dd> <dt>

**MaxClientLeadTime**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum amount of time that a server can extend a client's binding lease over the lease time.

</dd> <dt>

**Mode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Mode of the Failover Relationship.

<dt>

<span id="HotStandby"></span><span id="hotstandby"></span><span id="HOTSTANDBY"></span>

**HotStandby** ("HotStandby")


</dt> <dd></dd> <dt>

<span id="LoadBalance"></span><span id="loadbalance"></span><span id="LOADBALANCE"></span>

**LoadBalance** ("LoadBalance")


</dt> <dd></dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name for the failover relationship.

</dd> <dt>

**PartnerServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

IP Address or host name of the partner server.

</dd> <dt>

**PrimaryServerIP**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IP address of Primary Server.

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**PrimaryServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of Primary Server.

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**ReservePercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **Mode** is HotStandby, this is the percent of addresses reserved on standby server.

</dd> <dt>

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

IP Addresses of one or more Scopes that are part of the failover relationship.

</dd> <dt>

**SecondaryServerIP**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IP addresses of Secondary Server.

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**SecondaryServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of Secondary Server.

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**ServerRole**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **Mode** is HotStandby, this is the role of this server.

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="Standby"></span><span id="standby"></span><span id="STANDBY"></span>

**Standby** ("Standby")


</dt> <dd></dd> </dl>

</dd> <dt>

**ServerType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if server is primary or secondary.

<dt>

<span id="PrimaryServer"></span><span id="primaryserver"></span><span id="PRIMARYSERVER"></span>

**PrimaryServer** ("PrimaryServer")


</dt> <dd></dd> <dt>

<span id="SecondaryServer"></span><span id="secondaryserver"></span><span id="SECONDARYSERVER"></span>

**SecondaryServer** ("SecondaryServer")


</dt> <dd></dd> </dl>

**Windows Server 2012:** This value is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Mode of the failover relationship.

<dt>

<span id="NoState"></span><span id="nostate"></span><span id="NOSTATE"></span>

**NoState** ("NoState")


</dt> <dd></dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

**Normal** ("Normal")


</dt> <dd></dd> <dt>

<span id="Init"></span><span id="init"></span><span id="INIT"></span>

**Init** ("Init")


</dt> <dd></dd> <dt>

<span id="CommunicationInterrupted"></span><span id="communicationinterrupted"></span><span id="COMMUNICATIONINTERRUPTED"></span>

**CommunicationInterrupted** ("CommunicationInterrupted")


</dt> <dd></dd> <dt>

<span id="PartnerDown"></span><span id="partnerdown"></span><span id="PARTNERDOWN"></span>

**PartnerDown** ("PartnerDown")


</dt> <dd></dd> <dt>

<span id="PotentialConflict"></span><span id="potentialconflict"></span><span id="POTENTIALCONFLICT"></span>

**PotentialConflict** ("PotentialConflict")


</dt> <dd></dd> <dt>

<span id="Startup"></span><span id="startup"></span><span id="STARTUP"></span>

**Startup** ("Startup")


</dt> <dd></dd> <dt>

<span id="ResolutionInterrupted"></span><span id="resolutioninterrupted"></span><span id="RESOLUTIONINTERRUPTED"></span>

**ResolutionInterrupted** ("ResolutionInterrupted")


</dt> <dd></dd> <dt>

<span id="ConflictDone"></span><span id="conflictdone"></span><span id="CONFLICTDONE"></span>

**ConflictDone** ("ConflictDone")


</dt> <dd></dd> <dt>

<span id="Recover"></span><span id="recover"></span><span id="RECOVER"></span>

**Recover** ("Recover")


</dt> <dd></dd> <dt>

<span id="RecoverWait"></span><span id="recoverwait"></span><span id="RECOVERWAIT"></span>

**RecoverWait** ("RecoverWait")


</dt> <dd></dd> <dt>

<span id="RecoverDone"></span><span id="recoverdone"></span><span id="RECOVERDONE"></span>

**RecoverDone** ("RecoverDone")


</dt> <dd></dd> </dl>

</dd> <dt>

**StateSwitchInterval**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Time period that the server will stay in CommunicationInterrupted state before auto transitioning into PartnerDown state.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





