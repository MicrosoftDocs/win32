---
title: Set method of the PS\_DnsServerRecursionScope class
description: Updates a recursion scope on a DNS server.
audience: developer
ms.assetid: '72c6cd14-b3c1-427d-a7e4-eac172a68697'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DnsServerRecursionScope class", "PS_DnsServerRecursionScope class, Set method"]
topic_type:
- apiref
api_name:
- PS_DnsServerRecursionScope.Set
api_location:
- DNSServerPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_DnsServerRecursionScope class

Updates a recursion scope on a DNS server.

## Syntax


```mof
uint32 Set(
  [in]  boolean                 EnableRecursion,
  [in]  string                  Forwarder[],
  [in]  string                  Name,
  [in]  boolean                 PassThru,
  [in]  string                  ComputerName,
  [out] DnsServerRecursionScope cmdletOutput
);
```



## Parameters

<dl> <dt>

*EnableRecursion* \[in\]
</dt> <dd>

**True** to enable recursion on the DNS server; otherwise, **false**.

</dd> <dt>

*Forwarder* \[in\]
</dt> <dd>

An array that contains the IP addresses of DNS servers to query.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the scope.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the deleted recursion scope object in the *cmdletOutput* parameter; otherwise, **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name of the DNS server. The acceptable values for this parameter are: an IPv4 address; an IPv6 address; and any other value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array that contains the updated recursion scope object.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DNSServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerRecursionScope**](ps-dnsserverrecursionscope.md)
</dt> </dl>

 

 





