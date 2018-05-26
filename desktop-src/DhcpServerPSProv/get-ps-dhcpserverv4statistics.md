---
title: Get method of the PS\_DhcpServerv4Statistics class
description: Gets DHCP Server statistics for IPv4.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 10025e44-ee2c-44ae-bc68-c9e79cbce6f2
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv4Statistics class
- PS_DhcpServerv4Statistics class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Statistics.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerv4Statistics class

Gets DHCP Server statistics for IPv4.

## Syntax


```mof
uint32 Get(
  [in]  string                 ComputerName,
  [out] DhcpServerv4Statistics cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Statistics**](dhcpserverv4statistics.md) class.

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

[**PS\_DhcpServerv4Statistics**](ps-dhcpserverv4statistics.md)
</dt> </dl>

 

 





