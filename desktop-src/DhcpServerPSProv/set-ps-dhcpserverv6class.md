---
title: Set method of the PS\_DhcpServerv6Class class
description: Modifies the properties of an IPv6 vendor or user class on the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '20b51d2e-6e85-4674-a8e4-19ce8d103a0b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DhcpServerv6Class class", "PS_DhcpServerv6Class class, Set method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Class.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Set method of the PS\_DhcpServerv6Class class

Modifies the properties of an IPv6 vendor or user class on the DHCP Server.

## Syntax


```mof
uint32 Set(
  [in]  string            ComputerName,
  [in]  string            Description,
  [in]  uint32            VendorId,
  [in]  string            Data,
  [in]  string            Type,
  [in]  string            Name,
  [in]  boolean           PassThru,
  [out] DhcpServerv6Class cmdletOutput
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

Description string to be set on the class being modified.

</dd> <dt>

*VendorId* \[in\]
</dt> <dd>

Enterprise number of the vendor class.

</dd> <dt>

*Data* \[in\]
</dt> <dd>

Data for the specified vendor or user class. This is the actual value expected to be present in the request from the client belonging to this vendor class.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type of the class - valid values are Vendor and User.

<dt>

<span id="Vendor"></span><span id="vendor"></span><span id="VENDOR"></span>

**Vendor** ("Vendor")


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** ("User")


</dt> <dd></dd> </dl> </dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of vendor or user class to be modified.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

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

 

 





