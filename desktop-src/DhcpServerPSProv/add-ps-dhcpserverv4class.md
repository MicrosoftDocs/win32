---
title: Add method of the PS\_DhcpServerv4Class class
description: Adds an IPv4 vendor or user class to the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b4aef412-fd84-4951-8ce1-28a6704e059c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DhcpServerv4Class class", "PS_DhcpServerv4Class class, Add method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Class.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Add method of the PS\_DhcpServerv4Class class

Adds an IPv4 vendor or user class to the DHCP Server.

## Syntax


```mof
uint32 Add(
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

Name of the vendor or user class to be added

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type of the class - valid values are Vendor and User

<dt>

<span id="Vendor"></span><span id="vendor"></span><span id="VENDOR"></span>

**Vendor** ("Vendor")


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** ("User")


</dt> <dd></dd> </dl> </dd> <dt>

*Data* \[in\]
</dt> <dd>

Data of the specified vendor or user class. This is the value expected in the DHCP request from the client which belongs to this vendor or user class.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description string for the class being added

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

 

 





