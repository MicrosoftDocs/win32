---
title: Clear method of the PS\_DnsServerCache class
description: Clears the settings of a DNS server cache.
audience: developer
ms.assetid: 'cbe476ad-dfbc-4863-8808-3526a53d4540'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Clear method", "Clear method, PS_DnsServerCache class", "PS_DnsServerCache class, Clear method"]
topic_type:
- apiref
api_name:
- PS_DnsServerCache.Clear
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Clear method of the PS\_DnsServerCache class

Clears the settings of a DNS server cache.

## Syntax


```mof
uint32 Clear(
  [in] string  ComputerName,
  [in] boolean Force,
  [in] string  CacheScope
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The remote computer on which to execute the command.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**true** to override the default confirmation before performing the operation; otherwise, **false**.

</dd> <dt>

*CacheScope* \[in\]
</dt> <dd>

The scope name of the cache settings.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

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

 

 





