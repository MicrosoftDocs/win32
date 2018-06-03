---
title: AddByInputObject method of the PS\_DnsServerRootHint class
description: Adds a root hint to a DNS server based on the specified DnsServerRootHint object.
audience: developer
ms.assetid: 799266d0-adbf-4a88-9369-31c683db2bdd
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByInputObject method
- AddByInputObject method, PS_DnsServerRootHint class
- PS_DnsServerRootHint class, AddByInputObject method
topic_type:
- apiref
api_name:
- PS_DnsServerRootHint.AddByInputObject
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByInputObject method of the PS\_DnsServerRootHint class

Adds a root hint to a DNS server based on the specified [**DnsServerRootHint**](dnsserverroothint.md) object.

## Syntax


```mof
uint32 AddByInputObject(
  [in]  string            ComputerName,
  [in]  DnsServerRootHint InputObject,
  [in]  boolean           PassThru,
  [out] DnsServerRootHint cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command. The acceptable values for this parameter are: an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

The [**DnsServerRootHint**](dnsserverroothint.md) object to add to the server.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object representing the item with which you are working. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives the [**DnsServerRootHint**](dnsserverroothint.md) object that was added to the server.

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

 

 





