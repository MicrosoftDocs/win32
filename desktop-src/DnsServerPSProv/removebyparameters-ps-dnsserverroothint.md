---
title: RemoveByParameters method of the PS\_DnsServerRootHint class
description: Removes root hints form the list on the server.
audience: developer
ms.assetid: 2e2ea297-2e36-4d2d-92ab-6676382f0c91
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByParameters method
- RemoveByParameters method, PS_DnsServerRootHint class
- PS_DnsServerRootHint class, RemoveByParameters method
topic_type:
- apiref
api_name:
- PS_DnsServerRootHint.RemoveByParameters
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveByParameters method of the PS\_DnsServerRootHint class

Removes root hints form the list on the server.

## Syntax


```mof
uint32 RemoveByParameters(
  [in]  string            IPAddress[],
  [in]  string            NameServer,
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [in]  boolean           Force,
  [out] DnsServerRootHint cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

Specifies an array of IPv4 or IPv6 addresses of DNS servers to remove. If you do not specify IPAddress, this method removes all root hints on the specified DNS server.

</dd> <dt>

*NameServer* \[in\]
</dt> <dd>

Specifies name of root hint to be removed.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a remote DNS server. The acceptable values for this parameter are: an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object representing the item with which you are working. By default, this method does not generate any output.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Removes the root hints without prompting you for confirmation. By default, the method prompts you for confirmation before it proceeds.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output type is the type of the objects that the method emits.

Microsoft.Management.Infrastructure.CimInstance\#DnsServerRootHint

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

[**PS\_DnsServerRootHint**](ps-dnsserverroothint.md)
</dt> </dl>

 

 





