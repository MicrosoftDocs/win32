---
title: Set method of the PS\_DnsServerCache class
description: Updates the settings of a DNS server cache.
audience: developer
ms.assetid: 'e2e5ab45-fce9-458d-bbbc-07f78c9e24e6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DnsServerCache class", "PS_DnsServerCache class, Set method"]
topic_type:
- apiref
api_name:
- PS_DnsServerCache.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_DnsServerCache class

Updates the settings of a DNS server cache.

## Syntax


```mof
uint32 Set(
  [in]  boolean        StoreEmptyAuthenticationResponse,
  [in]  uint32         MaxKBSize,
  [in]  boolean        PollutionProtection,
  [in]  string         ComputerName,
  [in]  uint32         LockingPercent,
  [in]  datetime       MaxNegativeTtl,
  [in]  datetime       MaxTtl,
  [in]  boolean        PassThru,
  [in]  boolean        IgnorePolicies,
  [out] DnsServerCache cmdletOutput
);
```



## Parameters

<dl> <dt>

*StoreEmptyAuthenticationResponse* \[in\]
</dt> <dd>

A boolean value indicating if the DNS server will store empty authoritative responses \[RFC2308\] in the cache. The value should be limited to 0x00000000 and 0x00000001, but it may be any value. The default value must be 0x00000001, and the value zero must be allowed and treated literally.

</dd> <dt>

*MaxKBSize* \[in\]
</dt> <dd>

Specifies the maximum size, in kilobytes, of the DNS server's memory cache.

</dd> <dt>

*PollutionProtection* \[in\]
</dt> <dd>

Determines whether DNS filters records that are saved in a cache. Saves all responses to name queries to a cache. This is the default setting. Saves only the records that belong to the same DNS subtree to a cache.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*LockingPercent* \[in\]
</dt> <dd>

The percentage of the original time-to-live value for which all cache entries from non-authoritative responses must be locked and must not be overwritten by data found in subsequent non-authoritative responses. Locked cache entries must still be considered for removal from the cache if the soft limit of the maximum cache size is reached (see the MaxCacheSize property described previously in this section). The value must be limited to the range 0x00000000 to 0x00000064. The default value must be 0x00000064, and the value zero must be allowed and treated literally. The Validation range = 0 to 100.

</dd> <dt>

*MaxNegativeTtl* \[in\]
</dt> <dd>

Specifies how many seconds (0x1-0xFFFFFFFF) an entry that records a negative answer to a query remains stored in the DNS cache. The default setting is 0x384 (900) seconds. Validation range = 0 to 2592000.

</dd> <dt>

*MaxTtl* \[in\]
</dt> <dd>

Determines how many seconds (0x0-0xFFFFFFFF) a record is saved in cache. If the 0x0 setting is used, then the DNS server does not cache records. The default setting is 0x15180 (86,400 seconds or 1 day). Validation range = 0 to 2592000.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*IgnorePolicies* \[in\]
</dt> <dd>

**true** if the policies of the cache are to be ignored; otherwise, **false.**

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

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

 

 





