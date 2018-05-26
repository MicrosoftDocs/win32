---
title: Set method of the PS\_DhcpServerv4Binding class
description: Binds or unbinds the DHCP server from the specified IPv4 interface on the system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c4ec9ce1-fdb4-4ed2-9614-7a822ff8436f
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerv4Binding class
- PS_DhcpServerv4Binding class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Binding.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DhcpServerv4Binding class

Binds or unbinds the DHCP server from the specified IPv4 interface on the system.

## Syntax


```mof
uint32 Set(
  [in]  string              ComputerName,
  [in]  string              InterfaceAlias[],
  [in]  boolean             BindingState,
  [in]  boolean             PassThru,
  [out] DhcpServerv4Binding cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

Name(s) of the interface in the system

</dd> <dt>

*BindingState* \[in\]
</dt> <dd>

Binding state of the interface. Can be set to true or false

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4Binding**](dhcpserverv4binding.md) object.

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

[**PS\_DhcpServerv4Binding**](ps-dhcpserverv4binding.md)
</dt> </dl>

 

 





