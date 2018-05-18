---
title: Import method of the PS\_DnsServerRootHint class
description: Copies DNS root hints from another server.
audience: developer
ms.assetid: '5959ab13-61f8-4d51-bc70-fa4aaf492a69'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Import method", "Import method, PS_DnsServerRootHint class", "PS_DnsServerRootHint class, Import method"]
topic_type:
- apiref
api_name:
- PS_DnsServerRootHint.Import
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Import method of the PS\_DnsServerRootHint class

Copies DNS root hints from another server.

## Syntax


```mof
uint32 Import(
  [in]  string            NameServer,
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [out] DnsServerRootHint cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*NameServer* \[in\]
</dt> <dd>

Copies the root hints from the specified server.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return an object that represents the item with which you are working. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives the object that represents the item with which you are working.

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

 

 





