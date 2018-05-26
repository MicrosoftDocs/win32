---
title: SetByWithRange method of the PS\_DhcpServerv4Scope class
description: Sets the properties of an existing IPv4 Scope on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2cb3f50c-f883-4753-89bc-7cc64d220fca
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByWithRange method
- SetByWithRange method, PS_DhcpServerv4Scope class
- PS_DhcpServerv4Scope class, SetByWithRange method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Scope.SetByWithRange
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByWithRange method of the PS\_DhcpServerv4Scope class

Sets the properties of an existing IPv4 Scope on the server.

## Syntax


```mof
uint32 SetByWithRange(
  [in]  boolean           ActivatePolicies,
  [in]  boolean           PassThru,
  [in]  string            ScopeId,
  [in]  string            Name,
  [in]  string            State,
  [in]  datetime          LeaseDuration,
  [in]  uint16            Delay,
  [in]  boolean           NapEnable,
  [in]  string            SuperscopeName,
  [in]  uint32            MaxBootpClients,
  [in]  string            NapProfile,
  [in]  string            StartRange,
  [in]  string            EndRange,
  [in]  string            Description,
  [in]  string            Type,
  [in]  string            ComputerName,
  [out] DhcpServerv4Scope cmdletOutput
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

If **true**, passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) whose properties are being set

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name to be set for the scope

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

*LeaseDuration* \[in\]
</dt> <dd>

Duration of the IPv4 address lease to be given for the clients of this scope

</dd> <dt>

*Delay* \[in\]
</dt> <dd>

Time in milliseconds by which the server should delay sending a response to clients. This setting should be used on the secondary server in a split scope configuration.

</dd> <dt>

*NapEnable* \[in\]
</dt> <dd>

Enable/Disable NAP for the scope. Valid values are True, False.

</dd> <dt>

*SuperscopeName* \[in\]
</dt> <dd>

Name of the superscope to which this scope is to be added.

</dd> <dt>

*MaxBootpClients* \[in\]
</dt> <dd>

If the scope supports both types of clients (Bootp, Dhcp), maximum number of bootp clients to be permitted to get an IP address lease from the scope.

</dd> <dt>

*NapProfile* \[in\]
</dt> <dd>

If NAP is enabled for the scope, the name of the NAP profile to be used for clients in the scope. The NAP profile refers to the MS Service Class which is a condition used in network policies on NPS.

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

Start address of the IPv4 range to be set for the scope. If a new IP range is being set, the previously set IP range of the scope is discarded.

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

End address of the IPv4 range to be set for the scope. If a new IP range is being set, the previously set IP range of the scope is discarded.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description to be set for the scope

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

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Scope**](dhcpserverv4scope.md) class.

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

[**PS\_DhcpServerv4Scope**](ps-dhcpserverv4scope.md)
</dt> </dl>

 

 





