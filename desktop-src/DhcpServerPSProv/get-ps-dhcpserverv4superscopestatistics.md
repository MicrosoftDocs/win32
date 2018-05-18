---
title: Get method of the PS\_DhcpServerv4SuperscopeStatistics class
description: Retrieves superscope statistics for the specified super scopes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'da4638c0-1b92-4552-ab0f-b3993c9285ec'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv4SuperscopeStatistics class", "PS_DhcpServerv4SuperscopeStatistics class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4SuperscopeStatistics.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv4SuperscopeStatistics class

Retrieves superscope statistics for the specified super scopes.

## Syntax


```mof
uint32 Get(
  [in]  string                           ComputerName,
  [in]  string                           Name[],
  [out] DhcpServerv4SuperscopeStatistics cmdletOutput[]
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

Names of the superscopes. Retrieves statistics for all superscopes if the *Name* parameter is not specified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4SuperscopeStatistics**](dhcpserverv4superscopestatistics.md) class.

</dd> </dl>

## Return value

Scope address utilization percentage

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4SuperscopeStatistics**](ps-dhcpserverv4superscopestatistics.md)
</dt> </dl>

 

 





