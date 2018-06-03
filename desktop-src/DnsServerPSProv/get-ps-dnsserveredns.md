---
title: Get method of the PS\_DnsServerEDns class
description: Retrieves DNS Sever EDns settings.
audience: developer
ms.assetid: 60eca66d-640d-4475-9ca1-d22da4106718
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerEDns class
- PS_DnsServerEDns class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerEDns.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerEDns class

Retrieves DNS Sever EDns settings.

## Syntax


```mof
uint32 Get(
  [in]  string        ComputerName,
  [out] DnsServerEDns cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerEDns**](dnsserveredns.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerEDns**](ps-dnsserveredns.md)
</dt> </dl>

 

 





