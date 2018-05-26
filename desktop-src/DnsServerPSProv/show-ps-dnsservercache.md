---
title: Show method of the PS\_DnsServerCache class
description: Dumps a DNS server cache.
audience: developer
ms.assetid: cf8d9c84-db0f-4387-a773-05292968bdf3
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Show method
- Show method, PS_DnsServerCache class
- PS_DnsServerCache class, Show method
topic_type:
- apiref
api_name:
- PS_DnsServerCache.Show
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Show method of the PS\_DnsServerCache class

Dumps a DNS server cache.

## Syntax


```mof
uint32 Show(
  [in]  string                  ComputerName,
  [in]  string                  CacheScope,
  [out] DnsServerResourceRecord cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The remote computer on which to execute the command.

</dd> <dt>

*CacheScope* \[in\]
</dt> <dd>

The scope name of the cache to clear.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, this parameter contains an instance of the current object.

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

[**PS\_DnsServerCache**](ps-dnsservercache.md)
</dt> </dl>

 

 





