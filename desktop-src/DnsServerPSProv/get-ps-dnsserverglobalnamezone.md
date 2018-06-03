---
title: Get method of the PS\_DnsServerGlobalNameZone class
description: Retrieves Global Name Zone parameters.
audience: developer
ms.assetid: c340e712-5638-4020-b126-37465e900297
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerGlobalNameZone class
- PS_DnsServerGlobalNameZone class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerGlobalNameZone.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerGlobalNameZone class

Retrieves Global Name Zone parameters.

## Syntax


```mof
uint32 Get(
  [in]  string                  ComputerName,
  [out] DnsServerGlobalNameZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerGlobalNameZone**](dnsserverglobalnamezone.md) class.

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

[**PS\_DnsServerGlobalNameZone**](ps-dnsserverglobalnamezone.md)
</dt> </dl>

 

 





