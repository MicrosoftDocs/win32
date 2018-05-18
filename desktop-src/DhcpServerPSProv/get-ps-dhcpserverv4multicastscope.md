---
title: Get method of the PS\_DhcpServerv4MulticastScope class
description: Retrieves one or more multicast scope objects corresponding to the specified scope names.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '549b19eb-b24b-4075-abda-09ad785169c4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv4MulticastScope class", "PS_DhcpServerv4MulticastScope class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastScope.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv4MulticastScope class

Retrieves one or more multicast scope objects corresponding to the specified scope names.

## Syntax


```mof
uint32 Get(
  [in]  string                     ComputerName,
  [in]  string                     Name[],
  [out] DhcpServerv4MulticastScope cmdletOutput[]
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

One or more names of multicast scopes. If *Name* is not specified, the cmdlet gets all multicast scopes present on the DHCP server

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4MulticastScope**](dhcpserverv4multicastscope.md) class.

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

 

 





