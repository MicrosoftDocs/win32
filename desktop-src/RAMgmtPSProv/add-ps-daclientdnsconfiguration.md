---
title: Add method of the PS\_DAClientDnsConfiguration class
description: This cmdlet adds the specified DNS suffix, DNS server addresses, proxy server set to the NRPT table.
audience: developer
ms.assetid: '601a82cd-1997-422c-ae9e-11f04c075133'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DAClientDnsConfiguration class", "PS_DAClientDnsConfiguration class, Add method"]
topic_type:
- apiref
api_name:
- PS_DAClientDnsConfiguration.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Add method of the PS\_DAClientDnsConfiguration class

This cmdlet adds the specified DNS suffix, DNS server addresses, proxy server set to the NRPT table.

## Syntax


```mof
uint32 Add(
  [in]  string            DnsIPAddress[],
  [in]  string            DnsSuffix,
  [in]  string            ProxyServer,
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [out] DnsClientNrptRule cmdletOutput
);
```



## Parameters

<dl> <dt>

*DnsIPAddress* \[in\]
</dt> <dd>

IPv4/IPv6 address of the corresponding DNS servers that should be used for the specified DNS suffix

</dd> <dt>

*DnsSuffix* \[in\]
</dt> <dd>

Specifies a single DNS suffix

</dd> <dt>

*ProxyServer* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the proxy server configured for web traffic. The proxy server is specified in the format, Proxy\_Hostname:port or Proxy\_IPAddress:port

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the NRPT object that contains the NRPT rules. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

NRPT object for the NRPT entry that was added

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAClientDnsConfiguration**](ps-daclientdnsconfiguration.md)
</dt> </dl>

 

 





