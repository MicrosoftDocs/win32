---
title: Remove method of the PS\_DhcpServerv4Class class
description: Deletes an IPv4 vendor class or user class from a DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1e1fd7b4-03b2-4d22-a609-fb11642a1e4e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_DhcpServerv4Class class", "PS_DhcpServerv4Class class, Remove method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Class.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Remove method of the PS\_DhcpServerv4Class class

Deletes an IPv4 vendor class or user class from a DHCP Server.

## Syntax


```mof
uint32 Remove(
  [in]  string            ComputerName,
  [in]  string            Name[],
  [in]  string            Type,
  [in]  boolean           PassThru,
  [out] DhcpServerv4Class cmdletOutput[]
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

Name(s) of the class to be deleted.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type of the class being deleted. Valid values for this parameter are Vendor and User.

<dt>

<span id="Vendor"></span><span id="vendor"></span><span id="VENDOR"></span>

**Vendor** ("Vendor")


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** ("User")


</dt> <dd></dd> </dl> </dd> <dt>

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

 

 





