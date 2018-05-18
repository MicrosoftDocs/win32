---
title: Get method of the PS\_DAMultiSite class
description: Retrieves global settings applied to all entry points in a multisite deployment.
audience: developer
ms.assetid: 'bee905b2-56f4-41bd-b5c0-bb340745a91b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DAMultiSite class", "PS_DAMultiSite class, Get method"]
topic_type:
- apiref
api_name:
- PS_DAMultiSite.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DAMultiSite class

Retrieves global settings applied to all entry points in a multisite deployment.

## Syntax


```mof
uint32 Get(
  [in]  string      ComputerName,
  [out] DAMultiSite cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name or address (IPv4 or IPv6) of a remote access server that is included in a multisite deployment. If no value is specified, the local machine is used.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Multisite deployment name. 2. List of entrypoints included in the deployment along with the servers contained in each entrypoint. 3. Global load balancing FQDN (if defined). 4. Whether remote access clients can manually select an entry point.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAMultiSite**](ps-damultisite.md)
</dt> </dl>

 

 





