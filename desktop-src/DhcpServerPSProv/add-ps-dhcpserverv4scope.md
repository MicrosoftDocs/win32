---
title: Add method of the PS\_DhcpServerv4Scope class
description: Adds an IPv4 scope on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f1220e03-9d51-4c17-ae21-367036ec0c4e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DhcpServerv4Scope class", "PS_DhcpServerv4Scope class, Add method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Scope.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Add method of the PS\_DhcpServerv4Scope class

Adds an IPv4 scope on the server.

## Syntax


```mof
uint32 Add(
  [in]  string            ComputerName,
  [in]  string            StartRange,
  [in]  string            EndRange,
  [in]  string            Name,
  [in]  string            Description,
  [in]  string            State,
  [in]  string            SuperscopeName,
  [in]  uint32            MaxBootpClients,
  [in]  boolean           ActivatePolicies,
  [in]  boolean           PassThru,
  [in]  boolean           NapEnable,
  [in]  string            NapProfile,
  [in]  uint16            Delay,
  [in]  datetime          LeaseDuration,
  [in]  string            SubnetMask,
  [in]  string            Type,
  [out] DhcpServerv4Scope cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

Start IP address of the range within the subnet from which IP addresses should be leased by the server.

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

End IP address of the range within the subnet from which IP addresses should be leased by the server.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the IPv4 scope being added.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description string for the IPv4 scope being added.

</dd> <dt>

*State* \[in\]
</dt> <dd>

This specified if the scope should be created in active or inactive state. Valid values are {Active, Inactive}. Only an active scope will respond to client requests. Default value is Active

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="InActive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**InActive** ("InActive")


</dt> <dd></dd> </dl> </dd> <dt>

*SuperscopeName* \[in\]
</dt> <dd>

The name of the superscope to which the scope will be added.

</dd> <dt>

*MaxBootpClients* \[in\]
</dt> <dd>

If the scope type is specified as Both to allow for both DHCP and BOOTP clients, this parameter allows to specify the maximum number of bootp clients which should be leased an IP address from this scope.

</dd> <dt>

*ActivatePolicies* \[in\]
</dt> <dd>

This specifies if the policy enforcement is to be enabled/disabled on the scope being added. Default value is true (enabled).

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*NapEnable* \[in\]
</dt> <dd>

This parameter specifies whether NAP should be enabled for this scope or not. If NAP is enabled, DHCP server passes on the SoH (statement of health) received from the client to the NPS server. Based on the NAP profile set, NPS server determines the network access to be granted to the client.

</dd> <dt>

*NapProfile* \[in\]
</dt> <dd>

The NAP profile should be set only if NAP is enabled on the scope. The NAP profile refers to the MS Service Class which is a condition used in network policies on NPS.

</dd> <dt>

*Delay* \[in\]
</dt> <dd>

Specifies the number of milliseconds by which the server should wait before responding to the client requests. This should be configured if the scope is part of a split scope deployment and this server should act as a secondary server for the scope being added.

</dd> <dt>

*LeaseDuration* \[in\]
</dt> <dd>

The time interval for which an IP address should be leased to a client in this scope. This should be specified in the format day.hrs:mins:secs

</dd> <dt>

*SubnetMask* \[in\]
</dt> <dd>

The subnet mask for the scope specified in IP address format. For example: 255.255.255.0.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of clients to be serviced by the scope. Valid values are DHCP, BOOTP, BOTH.

<dt>

<span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span>

**Dhcp** ("Dhcp")


</dt> <dd></dd> <dt>

<span id="Bootp"></span><span id="bootp"></span><span id="BOOTP"></span>

**Bootp** ("Bootp")


</dt> <dd></dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

**Both** ("Both")


</dt> <dd></dd> </dl> </dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Scope**](dhcpserverv4scope.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4Scope**](ps-dhcpserverv4scope.md)
</dt> </dl>

 

 





