---
title: Set method of the PS\_DnsServerRootHint class
description: Updates a DNS root hint.
audience: developer
ms.assetid: '0333ec95-d7f6-4478-9ad3-00c7f422ac9d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DnsServerRootHint class", "PS_DnsServerRootHint class, Set method"]
topic_type:
- apiref
api_name:
- PS_DnsServerRootHint.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_DnsServerRootHint class

Updates a DNS root hint.

## Syntax


```mof
uint32 Set(
  [in]  DnsServerRootHint InputObject,
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [out] DnsServerRootHint cmdletOutput
);
```



## Parameters

<dl> <dt>

*InputObject* \[in\]
</dt> <dd>

The [**DnsServerRootHint**](dnsserverroothint.md) object that contains the new DNS root hint.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a remote DNS server. The acceptable values for this parameter are: an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether this method returns the [**DnsServerRootHint**](dnsserverroothint.md) object. **True** returns the object, **False** does not.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives the [**DnsServerRootHint**](dnsserverroothint.md) object returned by the method if *PassThru* is set to **True**.

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

 

 





