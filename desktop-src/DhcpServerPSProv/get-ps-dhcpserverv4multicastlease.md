---
title: Get method of the PS\_DhcpServerv4MulticastLease class
description: Gets multicast leases corresponding to the specified scope name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 43c9c973-4ed7-40bf-bb46-6b821904124a
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv4MulticastLease class
- PS_DhcpServerv4MulticastLease class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastLease.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerv4MulticastLease class

Gets multicast leases corresponding to the specified scope name

## Syntax


```mof
uint32 Get(
  [in]  string                     ComputerName,
  [in]  string                     Name[],
  [out] DhcpServerv4MulticastLease cmdletOutput[]
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

Name of multicast scope

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4MulticastLease**](dhcpserverv4multicastlease.md) class.

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

[**PS\_DhcpServerv4MulticastLease**](ps-dhcpserverv4multicastlease.md)
</dt> </dl>

 

 





