---
title: Get method of the PS\_DnsServerCache class
description: Retrieves the settings of a DNS server cache.
audience: developer
ms.assetid: 'f1b3b846-cf3b-4840-b10b-5ffa17d9fab3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DnsServerCache class", "PS_DnsServerCache class, Get method"]
topic_type:
- apiref
api_name:
- PS_DnsServerCache.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DnsServerCache class

Retrieves the settings of a DNS server cache.

## Syntax


```mof
uint32 Get(
  [in]  string         ComputerName,
  [out] DnsServerCache cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The remote computer on which to execute the command.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerCache**](dnsservercache.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerCache**](ps-dnsservercache.md)
</dt> </dl>

 

 





