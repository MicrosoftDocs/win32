---
title: RemoveByIPAddress method of the PS\_DhcpServerv4Lease class
description: Deletes the specified IPv4 address lease record from the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ed5a833e-a149-41b0-b100-6fea530cc211
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByIPAddress method
- RemoveByIPAddress method, PS_DhcpServerv4Lease class
- PS_DhcpServerv4Lease class, RemoveByIPAddress method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Lease.RemoveByIPAddress
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveByIPAddress method of the PS\_DhcpServerv4Lease class

Deletes the specified IPv4 address lease record from the DHCP server.

## Syntax


```mof
uint32 RemoveByIPAddress(
  [in]  boolean           PassThru,
  [in]  string            ComputerName,
  [in]  string            IPAddress[],
  [out] DhcpServerv4Lease cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

IP address(es) whose lease records are to be deleted

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Lease**](dhcpserverv4lease.md) class.

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

[**PS\_DhcpServerv4Lease**](ps-dhcpserverv4lease.md)
</dt> </dl>

 

 





