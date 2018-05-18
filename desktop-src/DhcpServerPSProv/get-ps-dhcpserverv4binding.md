---
title: Get method of the PS\_DhcpServerv4Binding class
description: Gets all IPv4 interfaces in the system to which the DHCP Server is bound to.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a17bf561-7a51-4f1a-b6e8-e6b14da7b3e8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv4Binding class", "PS_DhcpServerv4Binding class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Binding.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv4Binding class

Gets all IPv4 interfaces in the system to which the DHCP Server is bound to.

## Syntax


```mof
uint32 Get(
  [in]  string              ComputerName,
  [out] DhcpServerv4Binding cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4Binding**](dhcpserverv4binding.md) object.

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

[**PS\_DhcpServerv4Binding**](ps-dhcpserverv4binding.md)
</dt> </dl>

 

 





