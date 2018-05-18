---
title: Remove method of the PS\_DnsServerRecursionScope class
description: Deletes a recursion scope from a DNS server.
audience: developer
ms.assetid: 'd29533ea-3308-4896-954a-0269d3cd7a42'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_DnsServerRecursionScope class", "PS_DnsServerRecursionScope class, Remove method"]
topic_type:
- apiref
api_name:
- PS_DnsServerRecursionScope.Remove
api_location:
- DNSServerPSProvider.dll
api_type:
- COM
---

# Remove method of the PS\_DnsServerRecursionScope class

Deletes a recursion scope from a DNS server.

## Syntax


```mof
uint32 Remove(
  [in]  string                  Name,
  [in]  boolean                 PassThru,
  [in]  boolean                 Force,
  [in]  string                  ComputerName,
  [out] DnsServerRecursionScope cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the scope.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the deleted recursion scope object in the *cmdletOutput* parameter; otherwise, **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to not require user confirmation before continuing with the operation; **false** to require user confirmation. The default value is **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name of the DNS server. The acceptable values for this parameter are: an IPv4 address; an IPv6 address; and any other value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array that contains the deleted recursion scope object.

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

 

 





