---
title: Remove method of the PS\_DhcpServerv4MulticastLease class
description: Deletes one or more multicast scope leases corresponding to the specified multicast scope or specified IP addresses.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1f037792-7056-47f2-8ec1-5604e5c9527e
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv4MulticastLease class
- PS_DhcpServerv4MulticastLease class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastLease.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DhcpServerv4MulticastLease class

Deletes one or more multicast scope leases corresponding to the specified multicast scope or specified IP addresses

## Syntax


```mof
uint32 Remove(
  [in]  string                     ComputerName,
  [in]  boolean                    PassThru,
  [in]  string                     Name,
  [in]  string                     IPAddress[],
  [out] DhcpServerv4MulticastLease cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the multicast scope from which to remove the IP address exclusion range

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

An array of IP addresses to be deleted

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

 

 





