---
title: Get method of the PS\_DhcpServerv6Class class
description: Gets the IPv6 vendor or user class from the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0b2f4a58-f390-4575-9cc7-88a62c853d76'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv6Class class", "PS_DhcpServerv6Class class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Class.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv6Class class

Gets the IPv6 vendor or user class from the DHCP Server.

## Syntax


```mof
uint32 Get(
  [in]  string            Name[],
  [in]  string            Type,
  [in]  string            ComputerName,
  [out] DhcpServerv6Class cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the vendor or user class which is to be retrieved

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

An embedded instance of the [**DhcpServerv6Class**](dhcpserverv6class.md) class.

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

[**PS\_DhcpServerv6Class**](ps-dhcpserverv6class.md)
</dt> </dl>

 

 





