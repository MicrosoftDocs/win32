---
title: Get method of the PS\_DhcpServerv4FilterList class
description: Gets the status (enabled/disabled) of the allow and deny filter lists set on the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 00cbdc39-d29d-4558-b36f-f7974852e379
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv4FilterList class
- PS_DhcpServerv4FilterList class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4FilterList.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerv4FilterList class

Gets the status (enabled/disabled) of the allow and deny filter lists set on the DHCP Server.

## Syntax


```mof
uint32 Get(
  [in]  string                 ComputerName,
  [out] DhcpServerv4FilterList cmdletOutput
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

An embedded instance of the [**DhcpServerv4FilterList**](dhcpserverv4filterlist.md) class.

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

[**PS\_DhcpServerv4FilterList**](ps-dhcpserverv4filterlist.md)
</dt> </dl>

 

 





