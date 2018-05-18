---
title: GetNamespaceServerConfig method of the MSFT\_DFSNamespaceServerConfig class
description: Retrieves the configuration of a DFS namespace (DFS-N) server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0361fa6f-7ae8-4681-aa25-c7d88af918a5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-namespace'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetNamespaceServerConfig method", "GetNamespaceServerConfig method, MSFT_DFSNamespaceServerConfig class", "MSFT_DFSNamespaceServerConfig class, GetNamespaceServerConfig method"]
topic_type:
- apiref
api_name:
- MSFT_DFSNamespaceServerConfig.GetNamespaceServerConfig
api_location:
- DfsNCimProv.dll
api_type:
- COM
---

# GetNamespaceServerConfig method of the MSFT\_DFSNamespaceServerConfig class

Retrieves the configuration of a DFS namespace (DFS-N) server.

## Syntax


```mof
uint32 GetNamespaceServerConfig(
  [in]  string                        NamespaceServer,
  [out] MSFT_DFSNamespaceServerConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*NamespaceServer* \[in\]
</dt> <dd>

The DFS namespace server for which to retrieve the configuration settings.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains output from the **Get-DFSNamespaceServerConfig** cmdlet. This parameter is passed uninitialized.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\dfsn<br/>                                                  |
| MOF<br/>                      | <dl> <dt>DfsNCimProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsNCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DFSNamespaceServerConfig**](msft-dfsnamespaceserverconfig.md)
</dt> </dl>

 

 





