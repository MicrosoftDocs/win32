---
title: RemoveByPrefix method of the PS\_DhcpServerv6Reservation class
description: Deletes the IPv6 reservation(s) from the specified scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8e1a4936-937c-414d-8fd0-34979021e7c9
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByPrefix method
- RemoveByPrefix method, PS_DhcpServerv6Reservation class
- PS_DhcpServerv6Reservation class, RemoveByPrefix method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Reservation.RemoveByPrefix
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveByPrefix method of the PS\_DhcpServerv6Reservation class

Deletes the IPv6 reservation(s) from the specified scope.

## Syntax


```mof
uint32 RemoveByPrefix(
  [in]  string                  Prefix,
  [in]  string                  ComputerName,
  [in]  boolean                 PassThru,
  [out] DhcpServerv6Reservation cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Prefix* \[in\]
</dt> <dd>

IPv6 subnet prefix of the scope from which leases are to be deleted.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Reservation**](dhcpserverv6reservation.md) class.

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

[**PS\_DhcpServerv6Reservation**](ps-dhcpserverv6reservation.md)
</dt> </dl>

 

 





