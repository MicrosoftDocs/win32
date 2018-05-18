---
title: Get method of the PS\_DhcpServerv4Filter class
description: Gets the list of all MAC addresses from the allow or deny list on the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ff1af7bc-4731-497f-861e-e84448d74949'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv4Filter class", "PS_DhcpServerv4Filter class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Filter.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv4Filter class

Gets the list of all MAC addresses from the allow or deny list on the DHCP Server.

## Syntax


```mof
uint32 Get(
  [in]  string             List,
  [in]  string             ComputerName,
  [out] DhcpServerv4Filter cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*List* \[in\]
</dt> <dd>

The list from which the MAC address(es) are to be retrieved. Valid values are Allow, Deny.

<dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>

**Allow** ("Allow")


</dt> <dd></dd> <dt>

<span id="Deny"></span><span id="deny"></span><span id="DENY"></span>

**Deny** ("Deny")


</dt> <dd></dd> </dl> </dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Filter**](dhcpserverv4filter.md) class.

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

[**PS\_DhcpServerv4Filter**](ps-dhcpserverv4filter.md)
</dt> </dl>

 

 





