---
title: AddByLoadBalance method of the PS\_DhcpServerv4Failover class
description: Adds a new IPv4 failover relationship on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12e28e12-72d3-483e-8444-5b6ff257ef29
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByLoadBalance method
- AddByLoadBalance method, PS_DhcpServerv4Failover class
- PS_DhcpServerv4Failover class, AddByLoadBalance method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Failover.AddByLoadBalance
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByLoadBalance method of the PS\_DhcpServerv4Failover class

Adds a new IPv4 failover relationship on the server.

## Syntax


```mof
uint32 AddByLoadBalance(
  [in]  string               ComputerName,
  [in]  string               Name,
  [in]  string               PartnerServer,
  [in]  string               ScopeId[],
  [in]  datetime             MaxClientLeadTime,
  [in]  boolean              AutoStateTransition,
  [in]  datetime             StateSwitchInterval,
  [in]  boolean              Force,
  [in]  string               SharedSecret,
  [in]  boolean              PassThru,
  [in]  uint32               LoadBalancePercent,
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

Name of the failover relationship to be created

</dd> <dt>

*PartnerServer* \[in\]
</dt> <dd>

IP address or hostname of the partner server

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifiers (in IPv4 address format) which are to be added to the failover relationship.

</dd> <dt>

*MaxClientLeadTime* \[in\]
</dt> <dd>

Maximum Client Lead time for the failover relationship. Default is 1 hour.

</dd> <dt>

*AutoStateTransition* \[in\]
</dt> <dd>

Enable/Disable automatic state transition from COMMUNICATION INTERRUPTED state to PARTNER DOWN state based on expiry of the timer (Safe Period) while in COMMUNICATION INTERRUPTED state. Valid values are True, False. Default value is False. However, this will be set to True if safe period is specified.

</dd> <dt>

*StateSwitchInterval* \[in\]
</dt> <dd>

Time interval for which the server should continue to operate in COMMUNICATION INTERRUPTED state before transitioning to PARTNER DOWN state

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If shared secret is specified, user confirmation is sought since shared secret specified may be transferred in clear text transport in case of remote management.

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Shared secret to be used for message digest authentication. If not specified, message digest authentication is turned off.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*LoadBalancePercent* \[in\]
</dt> <dd>

Percentage of DHCP client requests which should be served by the local server. The remaining requests would be served by the partner server. Default is 50%.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4Failover**](dhcpserverv4failover.md) object.

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

 

 





