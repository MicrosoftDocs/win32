---
title: Add method of the PS\_DhcpServerv4MulticastScope class
description: Adds a Multicast Scope on the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4d49426f-24c0-4009-b057-de2fc01337c7
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerv4MulticastScope class
- PS_DhcpServerv4MulticastScope class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastScope.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_DhcpServerv4MulticastScope class

Adds a Multicast Scope on the DHCP Server.

## Syntax


```mof
uint32 Add(
  [in]  string                     ComputerName,
  [in]  string                     Name,
  [in]  string                     StartRange,
  [in]  string                     EndRange,
  [in]  string                     Description,
  [in]  string                     State = Active,
  [in]  datetime                   LeaseDuration,
  [in]  boolean                    PassThru,
  [in]  uint32                     Ttl,
  [in]  datetime                   ExpiryTime,
  [out] DhcpServerv4MulticastScope cmdletOutput
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

Name of multicast scope.

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

Starting address of the range for the Scope.

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

Ending address of the range for the Scope

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description of the Scope.

The default value is.

<dl><span id="Null"></span><span id="null"></span><span id="NULL"></span><dt>

**Null**
</dt> </dl> </dd> <dt>

*State* \[in\]
</dt> <dd>

Scope state.

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** ("Inactive")


</dt> <dd></dd> </dl> </dd> <dt>

*LeaseDuration* \[in\]
</dt> <dd>

Lease duration. Default value is 30 days

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*Ttl* \[in\]
</dt> <dd>

Number of routers through which multicast traffic passes through. Default value is 32

</dd> <dt>

*ExpiryTime* \[in\]
</dt> <dd>

Expiry time for the multicast scope. default value is infinite

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4MulticastScope**](dhcpserverv4multicastscope.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4MulticastScope**](ps-dhcpserverv4multicastscope.md)
</dt> </dl>

 

 





