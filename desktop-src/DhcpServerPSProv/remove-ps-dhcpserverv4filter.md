---
title: Remove method of the PS\_DhcpServerv4Filter class
description: Deletes the specified MAC address or MAC address pattern from allow list or deny list of the Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 800d61a7-85d8-4cfb-ba90-9613d69140b1
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv4Filter class
- PS_DhcpServerv4Filter class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Filter.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DhcpServerv4Filter class

Deletes the specified MAC address or MAC address pattern from allow list or deny list of the Server.

## Syntax


```mof
uint32 Remove(
  [in]  string             ComputerName,
  [in]  boolean            PassThru,
  [in]  string             MacAddress[],
  [out] DhcpServerv4Filter cmdletOutput[]
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

*MacAddress* \[in\]
</dt> <dd>

MAC Address(es) which are to be deleted from the allow or deny filter

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Filter**](dhcpserverv4filter.md) class.

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

[**PS\_DhcpServerv4Filter**](ps-dhcpserverv4filter.md)
</dt> </dl>

 

 





