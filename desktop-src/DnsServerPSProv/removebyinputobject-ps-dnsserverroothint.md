---
title: RemoveByInputObject method of the PS\_DnsServerRootHint class
description: Removes root hints form the list on the server.
audience: developer
ms.assetid: '03e6dae2-d303-41b4-a2b7-99d2578f4905'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveByInputObject method", "RemoveByInputObject method, PS_DnsServerRootHint class", "PS_DnsServerRootHint class, RemoveByInputObject method"]
topic_type:
- apiref
api_name:
- PS_DnsServerRootHint.RemoveByInputObject
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# RemoveByInputObject method of the PS\_DnsServerRootHint class

Removes root hints form the list on the server.

## Syntax


```mof
uint32 RemoveByInputObject(
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [in]  boolean           Force,
  [in]  DnsServerRootHint InputObject,
  [out] DnsServerRootHint cmdletOutput
);
```



## Parameters

<dl> <dt>

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

Removes the root hints without prompting you for confirmation. By default, the method prompts you for confirmation before it proceeds

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

Specifies the input to this method. You can use this parameter, or you can pipe the input to this method. This parameter takes an object of type Microsoft.Management.Infrastructure.CimInstance.DnsServerRootHint as input.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded instance of [**DnsServerRootHint**](dnsserverroothint.md). This parameter returns a value only if *PassThru* is set to **true**.

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

[**PS\_DnsServerRootHint**](ps-dnsserverroothint.md)
</dt> </dl>

 

 





