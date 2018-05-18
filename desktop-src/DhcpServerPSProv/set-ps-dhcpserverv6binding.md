---
title: Set method of the PS\_DhcpServerv6Binding class
description: Binds or unbinds the DHCP server from the specified IPv6 interface on the system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '57d5133d-a3b3-47f9-9c68-1da614340231'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DhcpServerv6Binding class", "PS_DhcpServerv6Binding class, Set method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Binding.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Set method of the PS\_DhcpServerv6Binding class

Binds or unbinds the DHCP server from the specified IPv6 interface on the system.

## Syntax


```mof
uint32 Set(
  [in]  string              ComputerName,
  [in]  boolean             BindingState,
  [in]  string              InterfaceAlias[],
  [in]  boolean             PassThru,
  [out] DhcpServerv6Binding cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*BindingState* \[in\]
</dt> <dd>

Binding state of the interface (true or false).

</dd> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

IPv6 interface of the system.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Binding**](dhcpserverv6binding.md) class.

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

[**PS\_DhcpServerv6Binding**](ps-dhcpserverv6binding.md)
</dt> </dl>

 

 





