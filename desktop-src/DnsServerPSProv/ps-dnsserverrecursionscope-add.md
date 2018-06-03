---
title: Add method of the PS\_DnsServerRecursionScope class
description: Adds a new recursion scope to a DNS server.
audience: developer
ms.assetid: D1EF62A1-0FFD-4633-BD0E-3F71B81AAD68
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DnsServerRecursionScope class
- PS_DnsServerRecursionScope class, Add method
topic_type:
- apiref
api_name:
- PS_DnsServerRecursionScope.Add
api_location:
- DNSServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_DnsServerRecursionScope class

Adds a new recursion scope to a DNS server.

## Syntax


```mof
uint32 Add(
  [in]  string                  Name,
  [in]  string                  Forwarder[],
  [in]  boolean                 EnableRecursion,
  [in]  boolean                 PassThru,
  [in]  string                  ComputerName,
  [out] DnsServerRecursionScope cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the scope.

</dd> <dt>

*Forwarder* \[in\]
</dt> <dd>

An array that contains the IP addresses of DNS servers to query.

</dd> <dt>

*EnableRecursion* \[in\]
</dt> <dd>

**True** to enable recursion on the DNS server; otherwise, **false**.

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

When this method returns, this parameter contains an array that contains the new recursion scope object.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DNSServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerRecursionScope**](ps-dnsserverrecursionscope.md)
</dt> </dl>

 

 





