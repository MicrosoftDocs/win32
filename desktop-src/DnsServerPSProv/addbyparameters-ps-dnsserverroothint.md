---
title: AddByParameters method of the PS\_DnsServerRootHint class
description: Add a root hint to a DNS server based on the specified parameters.
audience: developer
ms.assetid: 147b5352-ce6c-40de-9b30-58a75b9a13e0
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByParameters method
- AddByParameters method, PS_DnsServerRootHint class
- PS_DnsServerRootHint class, AddByParameters method
topic_type:
- apiref
api_name:
- PS_DnsServerRootHint.AddByParameters
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByParameters method of the PS\_DnsServerRootHint class

Add a root hint to a DNS server based on the specified parameters.

## Syntax


```mof
uint32 AddByParameters(
  [in]  string            IPAddress[],
  [in]  string            NameServer,
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [out] DnsServerRootHint cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

The IPv4/IPv6 address of the Name server.

</dd> <dt>

*NameServer* \[in\]
</dt> <dd>

The name server.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The remote computer on which to execute the command

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method returns an object that represents the item with which you are working. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded instance of the [**DnsServerRootHint**](dnsserverroothint.md) class.

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

 

 





