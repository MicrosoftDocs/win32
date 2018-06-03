---
title: Set method of the PS\_DAClientDnsConfiguration class
description: This cmdlet does the following1. Configures the DNS server and proxy server addresses of an NRPT entry 2. Configures the local name resolution property.
audience: developer
ms.assetid: 2e7a3e34-fbff-41e9-b028-3d807c2029e5
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DAClientDnsConfiguration class
- PS_DAClientDnsConfiguration class, Set method
topic_type:
- apiref
api_name:
- PS_DAClientDnsConfiguration.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DAClientDnsConfiguration class

This cmdlet does the following1. Configures the DNS server and proxy server addresses of an NRPT entry 2. Configures the local name resolution property.

## Syntax


```mof
uint32 Set(
  [in]  string                   DnsSuffix,
  [in]  string                   DnsIPAddress[],
  [in]  string                   ProxyServer,
  [in]  string                   Local,
  [in]  string                   ComputerName,
  [in]  boolean                  PassThru,
  [out] DAClientDnsConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*DnsSuffix* \[in\]
</dt> <dd>

Specifies the DNS suffix entry in the NRPT table that needs to be modified

</dd> <dt>

*DnsIPAddress* \[in\]
</dt> <dd>

The new list of DNS server IPv4/IPv6 addresses for the specified DNS suffix in the NRPT table

</dd> <dt>

*ProxyServer* \[in\]
</dt> <dd>

The new proxy server for the specified DNS suffix in the NRPT table

</dd> <dt>

*Local* \[in\]
</dt> <dd>

Specifies the property of the local name resolution. Can be one of the following 1. FallbackSecure: Only use local name resolution if the name doesn't exist in DNS (Most Restrictive) 2. FallbackPrivate: Fall back to local name resolution if the name does not exist in the DNS or the DNS servers are unreachable when the client computer is on a private network (Recommended) 3. FallbackUnsecure: Fallback to local name resolution for any kind of DNS resolution error (Least Secure)

<dt>

<span id="FallbackSecure"></span><span id="fallbacksecure"></span><span id="FALLBACKSECURE"></span>

**FallbackSecure** ("FallbackSecure")


</dt> <dd></dd> <dt>

<span id="FallbackPrivate"></span><span id="fallbackprivate"></span><span id="FALLBACKPRIVATE"></span>

**FallbackPrivate** ("FallbackPrivate")


</dt> <dd></dd> <dt>

<span id="FallbackUnsecure"></span><span id="fallbackunsecure"></span><span id="FALLBACKUNSECURE"></span>

**FallbackUnsecure** ("FallbackUnsecure")


</dt> <dd></dd> </dl> </dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object for the DA DNS configuration consisting of the NRPT rules and local name resolution settings. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. NRPT object for the entry that was modified. 2. Property of local name resolution

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAClientDnsConfiguration**](ps-daclientdnsconfiguration.md)
</dt> </dl>

 

 





