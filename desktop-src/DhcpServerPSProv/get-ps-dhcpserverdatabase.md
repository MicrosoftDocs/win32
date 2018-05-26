---
title: Get method of the PS\_DhcpServerDatabase class
description: Gets the configuration parameters related to the database of the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 64674183-50f0-402e-afbe-2304a9c9a979
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerDatabase class
- PS_DhcpServerDatabase class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerDatabase.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerDatabase class

Gets the configuration parameters related to the database of the DHCP server.

## Syntax


```mof
uint32 Get(
  [in]  string             ComputerName,
  [out] DhcpServerDatabase cmdletOutput
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

An embedded instance of the [**DhcpServerDatabase**](dhcpserverdatabase.md) class.

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

[**PS\_DhcpServerDatabase**](ps-dhcpserverdatabase.md)
</dt> </dl>

 

 





