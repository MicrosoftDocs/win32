---
title: Get method of the PS\_DhcpServerv4Superscope class
description: Returns configuration of specified superscope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 02fb959f-3ad5-411f-a531-5d1111494a1a
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv4Superscope class
- PS_DhcpServerv4Superscope class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Superscope.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerv4Superscope class

Returns configuration of specified superscope.

## Syntax


```mof
uint32 Get(
  [in]  string                 SuperscopeName[],
  [in]  string                 ComputerName,
  [out] DhcpServerv4Superscope cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*SuperscopeName* \[in\]
</dt> <dd>

The names of the superscopes whose configuration needs to be retrieved.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Superscope**](dhcpserverv4superscope.md) class.

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

[**PS\_DhcpServerv4Superscope**](ps-dhcpserverv4superscope.md)
</dt> </dl>

 

 





