---
title: Set method of the PS\_DhcpServerv4Failover class
description: Modifies the properties of an existing failover relationship.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3836f670-f01e-44d0-ba87-2f78412666be
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerv4Failover class
- PS_DhcpServerv4Failover class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Failover.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DhcpServerv4Failover class

Modifies the properties of an existing failover relationship.

## Syntax


```mof
uint32 Set(
  [in]  string               ComputerName,
  [in]  string               Name,
  [in]  boolean              AutoStateTransition,
  [in]  datetime             MaxClientLeadTime,
  [in]  string               SharedSecret,
  [in]  datetime             StateSwitchInterval,
  [in]  boolean              PartnerDown,
  [in]  boolean              Force,
  [in]  uint32               LoadBalancePercent,
  [in]  uint32               ReservePercent,
  [in]  boolean              PassThru,
  [in]  string               Mode,
  [out] DhcpServerv4Failover cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of failover relationship whose properties need to be modified.

</dd> <dt>

*AutoStateTransition* \[in\]
</dt> <dd>

Enable/Disable automatic state transition from COMMUNICATION INTERRUPTED state to PARTNER DOWN state based on expiry of the timer (Safe Period) while in COMMUNICATION INTERRUPTED state. Valid values are True, False. Default value is False; however, this will be set to True if safe period is specified.

</dd> <dt>

*MaxClientLeadTime* \[in\]
</dt> <dd>

Maximum Client Lead time for the failover relationship.

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Shared secret to be used for message authentication. To turn off message authentication, set the shared secret value to Null.

</dd> <dt>

*StateSwitchInterval* \[in\]
</dt> <dd>

Time interval for which the server should continue to operate in COMMUNICATION INTERRUPTED state before transitioning to PARTNER DOWN state.

</dd> <dt>

*PartnerDown* \[in\]
</dt> <dd>

Changes the state of the server from Communication Interrupted to Partner Down

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If shared secret is specified, user confirmation is sought since shared secret specified may be transferred in clear text transport in case of remote management.

</dd> <dt>

*LoadBalancePercent* \[in\]
</dt> <dd>

Percentage of DHCP client requests which should be served by the local server. The remaining requests would be served by the partner server.

</dd> <dt>

*ReservePercent* \[in\]
</dt> <dd>

Percentage of free IP address pool of the scope which should be reserved on the standby server. In case of a failover, IP addresses from this reserved pool on the standby server will be leased to new DHCP clients.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*Mode* \[in\]
</dt> <dd>

Mode of the failover relationship.

<dt>

<span id="HotStandby"></span><span id="hotstandby"></span><span id="HOTSTANDBY"></span>

**HotStandby** ("HotStandby")


</dt> <dd></dd> <dt>

<span id="LoadBalance"></span><span id="loadbalance"></span><span id="LOADBALANCE"></span>

**LoadBalance** ("LoadBalance")


</dt> <dd></dd> </dl>

**Windows Server 2012:** This parameter is supported beginning with Windows Server 2012 R2.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4Failover**](ps-dhcpserverv4failover.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4Failover**](ps-dhcpserverv4failover.md)
</dt> </dl>

 

 





