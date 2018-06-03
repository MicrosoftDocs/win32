---
title: Get method of the PS\_DhcpServerv4MulticastScopeStatistics class
description: Retrieves multicast scope statistics corresponding to specified multicast scope name(s).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f7976969-125e-4881-9c83-5b9d26a61075
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv4MulticastScopeStatistics class
- PS_DhcpServerv4MulticastScopeStatistics class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastScopeStatistics.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerv4MulticastScopeStatistics class

Retrieves multicast scope statistics corresponding to specified multicast scope name(s).

## Syntax


```mof
uint32 Get(
  [in]  string                               ComputerName,
  [in]  string                               Name[],
  [out] DhcpServerv4MulticastScopeStatistics cmdletOutput[]
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

An array of multicast scope names. Retrieves statistics for all multicast scopes if no name is specified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4MulticastScopeStatistics**](dhcpserverv4multicastscopestatistics.md) class.

</dd> </dl>

## Return value

Scope address utilization percentage.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4MulticastScopeStatistics**](ps-dhcpserverv4multicastscopestatistics.md)
</dt> </dl>

 

 





