---
title: Set method of the PS\_DhcpServerv4MulticastScope class
description: Modifies the specified properties of a Multicast Scope on the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '843e9396-c6c1-48bb-b82e-bea8973dd1aa'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DhcpServerv4MulticastScope class", "PS_DhcpServerv4MulticastScope class, Set method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastScope.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Set method of the PS\_DhcpServerv4MulticastScope class

Modifies the specified properties of a Multicast Scope on the DHCP Server.

## Syntax


```mof
uint32 Set(
  [in]  string                     ComputerName,
  [in]  string                     Description,
  [in]  string                     EndRange,
  [in]  datetime                   LeaseDuration,
  [in]  string                     Name,
  [in]  boolean                    PassThru,
  [in]  string                     StartRange,
  [in]  string                     State = Active,
  [in]  uint32                     Ttl,
  [in]  string                     NewName,
  [in]  datetime                   ExpiryTime,
  [out] DhcpServerv4MulticastScope cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description of the Scope. Default value is Null

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

Ending address of the range for the Scope

</dd> <dt>

*LeaseDuration* \[in\]
</dt> <dd>

Lease duration. Default value is 30 days

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of multicast scope.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

Starting address of the range for the Scope.

</dd> <dt>

*State* \[in\]
</dt> <dd>

Scope state valid values are Active, Inactive. Default value is Active

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** ("Inactive")


</dt> <dd></dd> </dl> </dd> <dt>

*Ttl* \[in\]
</dt> <dd>

Number of routers through which multicast traffic passes.

</dd> <dt>

*NewName* \[in\]
</dt> <dd>

New name to be assigned to the multicast scope

</dd> <dt>

*ExpiryTime* \[in\]
</dt> <dd>

Expiry time of the scope default value is infinite

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4MulticastScope**](dhcpserverv4multicastscope.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4MulticastScope**](ps-dhcpserverv4multicastscope.md)
</dt> </dl>

 

 





