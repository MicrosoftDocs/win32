---
title: Set method of the PS\_DhcpServerv4Class class
description: Modifies an IPv4 vendor class or user class on the DHCP Server with specified parameters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4f70cb6f-aec6-43b1-897a-875fdb0a4148'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DhcpServerv4Class class", "PS_DhcpServerv4Class class, Set method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Class.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Set method of the PS\_DhcpServerv4Class class

Modifies an IPv4 vendor class or user class on the DHCP Server with specified parameters.

## Syntax


```mof
uint32 Set(
  [in]  string            Name,
  [in]  string            Type,
  [in]  string            Data,
  [in]  string            Description,
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [out] DhcpServerv4Class cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the user or vendor class being modified

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type of the class being modified. Valid values are Vendor, User.

<dt>

<span id="Vendor"></span><span id="vendor"></span><span id="VENDOR"></span>

**Vendor** ("Vendor")


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** ("User")


</dt> <dd></dd> </dl> </dd> <dt>

*Data* \[in\]
</dt> <dd>

Data for the specified vendor or user class. This is the actual value expected to be present in the request from the client belonging to this vendor or user class.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description string to be set on the vendor or user class.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4Class**](dhcpserverv4class.md) object.

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

[**PS\_DhcpServerv4Class**](ps-dhcpserverv4class.md)
</dt> </dl>

 

 





