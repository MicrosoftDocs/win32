---
title: Remove method of the PS\_DhcpServerv6Class class
description: Deletes an IPv6 vendor class or user class from a DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '813d50ed-69f1-461b-a126-2097e5df4927'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_DhcpServerv6Class class", "PS_DhcpServerv6Class class, Remove method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Class.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Remove method of the PS\_DhcpServerv6Class class

Deletes an IPv6 vendor class or user class from a DHCP Server.

## Syntax


```mof
uint32 Remove(
  [in]  boolean           PassThru,
  [in]  string            Type,
  [in]  string            Name[],
  [in]  string            ComputerName,
  [out] DhcpServerv6Class cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type of the class being deleted. Permissible values are Vendor or User.

<dt>

<span id="Vendor"></span><span id="vendor"></span><span id="VENDOR"></span>

**Vendor** ("Vendor")


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** ("User")


</dt> <dd></dd> </dl> </dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the vendor or user class to be deleted.

</dd> <dt>

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

 

 





