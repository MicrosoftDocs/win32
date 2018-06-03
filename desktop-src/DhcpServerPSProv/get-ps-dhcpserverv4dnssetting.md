---
title: Get method of the PS\_DhcpServerv4DnsSetting class
description: Gets the DNS Update settings configured for a specific scope or reservation or server level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 162babdc-2bc6-4707-bada-4124d4d0e731
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv4DnsSetting class
- PS_DhcpServerv4DnsSetting class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4DnsSetting.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerv4DnsSetting class

Gets the DNS Update settings configured for a specific scope or reservation or server level.

## Syntax


```mof
uint32 Get(
  [in]  string                 IPAddress,
  [in]  string                 ScopeId,
  [in]  string                 ComputerName,
  [in]  string                 PolicyName,
  [out] DhcpServerv4DnsSetting cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

IP address of the reservation for which the DNS update settings are to be retrieved

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier ( in IPv4 address format) for which the DNS update settings are to be retrieved

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PolicyName* \[in\]
</dt> <dd>

Specifies the policy for which DNS settings are to be modified.

**Windows Server 2012:** This parameter is supported beginning with Windows Server 2012 R2.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4DnsSetting**](dhcpserverv4dnssetting.md) object.

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

[**PS\_DhcpServerv4DnsSetting**](ps-dhcpserverv4dnssetting.md)
</dt> </dl>

 

 





