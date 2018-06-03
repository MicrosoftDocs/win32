---
title: Get method of the PS\_DnsServerRecursionScope class
description: Retrieves a recursion scope from a DNS server.
audience: developer
ms.assetid: 4db57e06-00bf-4a8b-acbb-cd5e0fdc8aa6
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerRecursionScope class
- PS_DnsServerRecursionScope class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerRecursionScope.Get
api_location:
- DNSServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerRecursionScope class

Retrieves a recursion scope from a DNS server.

## Syntax


```mof
uint32 Get(
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [out] DnsServerRecursionScope cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the scope.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name of the DNS server. The acceptable values for this parameter are: an IPv4 address; an IPv6 address; and any other value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array that contains the retrieved recursion scope object.

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

 

 





