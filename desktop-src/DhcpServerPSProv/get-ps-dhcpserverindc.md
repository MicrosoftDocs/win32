---
title: Get method of the PS\_DhcpServerInDC class
description: Retrieve the list of authorized DHCP servers from AD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f5098393-a4b1-42a8-8d82-8240f951f60b
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerInDC class
- PS_DhcpServerInDC class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerInDC.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerInDC class

Retrieve the list of authorized DHCP servers from AD.

## Syntax


```mof
uint32 Get(
  [out] DhcpServerInDC cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerInDC**](dhcpserverindc.md) object.

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

[**PS\_DhcpServerInDC**](ps-dhcpserverindc.md)
</dt> </dl>

 

 





