---
title: SetByWithoutRange method of the PS\_DhcpServerv4Scope class
description: Sets the properties of an existing IPv4 Scope on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e24c30d3-123e-42fb-97c1-ebb1ae4b0f2f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByWithoutRange method", "SetByWithoutRange method, PS_DhcpServerv4Scope class", "PS_DhcpServerv4Scope class, SetByWithoutRange method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Scope.SetByWithoutRange
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# SetByWithoutRange method of the PS\_DhcpServerv4Scope class

Sets the properties of an existing IPv4 Scope on the server.

## Syntax


```mof
uint32 SetByWithoutRange(
  [in]  boolean           ActivatePolicies,
  [in]  boolean           PassThru,
  [in]  string            Type,
  [in]  string            ScopeId,
  [in]  string            Description,
  [in]  datetime          LeaseDuration,
  [in]  string            Name,
  [in]  boolean           NapEnable,
  [in]  string            NapProfile,
  [in]  uint16            Delay,
  [in]  string            State,
  [in]  string            SuperscopeName,
  [in]  string            ComputerName,
  [in]  uint32            MaxBootpClients,
  [out] DhcpServerv4Scope cmdletOutput
);
```



## Parameters

<dl> <dt>

*ActivatePolicies* \[in\]
</dt> <dd>

This specifies if the policy enforcement is to be enabled/disabled on the scope. Valid values are True, False.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type of the scope. Valid values are DHCP, BOOTP and BOTH. The type of the scope determines if the server will respond to only DHCP client requests, only BOOTP client requests or Both types of clients.

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

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) whose properties are being set

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description to be set for the scope

</dd> <dt>

*LeaseDuration* \[in\]
</dt> <dd>

Duration of the IPv4 address lease to be given for the clients of this scope

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name to be set for the scope

</dd> <dt>

*NapEnable* \[in\]
</dt> <dd>

Enable/Disable NAP for the scope. Valid values are True, False.

</dd> <dt>

*NapProfile* \[in\]
</dt> <dd>

If NAP is enabled for the scope, the name of the NAP profile to be used for clients in the scope. The NAP profile refers to the MS Service Class which is a condition used in network policies on NPS.

</dd> <dt>

*Delay* \[in\]
</dt> <dd>

Time in milliseconds by which the server should delay sending a response to clients. This setting should be used on the secondary server in a split scope configuration.

</dd> <dt>

*State* \[in\]
</dt> <dd>

State of the scope. Valid values are Active and InActive.

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="InActive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**InActive** ("InActive")


</dt> <dd></dd> </dl> </dd> <dt>

*SuperscopeName* \[in\]
</dt> <dd>

Name of the superscope to which this scope is to be added.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*MaxBootpClients* \[in\]
</dt> <dd>

If the scope supports both types of clients (Bootp, Dhcp), maximum number of bootp clients to be permitted to get an IP address lease from the scope.

</dd> <dt>

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

 

 





