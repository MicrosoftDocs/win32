---
title: Get method of the PS\_DhcpServerv4Class class
description: Retrieves an IPv4 vendor or user class from the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7b3779d5-7522-473e-9c62-5c93fbcce29a
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv4Class class
- PS_DhcpServerv4Class class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Class.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerv4Class class

Retrieves an IPv4 vendor or user class from the DHCP Server.

## Syntax


```mof
uint32 Get(
  [in]  string            Name[],
  [in]  string            Type,
  [in]  string            ComputerName,
  [out] DhcpServerv4Class cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the vendor or user class to be retrieved.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type of the class. Valid values are Vendor, User.

<dt>

<span id="Vendor"></span><span id="vendor"></span><span id="VENDOR"></span>

**Vendor** ("Vendor")


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** ("User")


</dt> <dd></dd> </dl> </dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4Class**](dhcpserverv4class.md) object.

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

[**PS\_DhcpServerv4Class**](ps-dhcpserverv4class.md)
</dt> </dl>

 

 





