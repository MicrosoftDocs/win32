---
title: RemoveNamespace method of the MSFT\_DFSNamespace class
description: Removes a DFS namespace (DFS-N) and any child namespace links.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f1cba646-2d78-4ef5-8f07-8a7854289bb9
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveNamespace method
- RemoveNamespace method, MSFT_DFSNamespace class
- MSFT_DFSNamespace class, RemoveNamespace method
topic_type:
- apiref
api_name:
- MSFT_DFSNamespace.RemoveNamespace
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveNamespace method of the MSFT\_DFSNamespace class

Removes a DFS namespace (DFS-N) and any child namespace links.

## Syntax


```mof
uint32 RemoveNamespace(
  [in] string NamespaceRoot
);
```



## Parameters

<dl> <dt>

*NamespaceRoot* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path to the root of the DFS namespace. The namespace root can take one of these two formats:



| Server Format           | Domain Format           |
|-------------------------|-------------------------|
| \\\\ServerName\\DFSName | \\\\DomainName\\DFSName |



 

where:

-   The ServerName component represents the host name of a DFS root target of a namespace.
-   The DomainName component represents the domain name of the domain that hosts the domain-based namespace.
-   The DFSName component represents the DFS-N name.

A stand-alone namespace must have a root with the format shown in the first column, as it must contain a server name. A domain-based namespace can have a root with the format from either column, although the second column's format (which contains a domain name instead of a server name) is the preferred format.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\dfsn<br/>                                                  |
| MOF<br/>                      | <dl> <dt>DfsNCimProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsNCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DFSNamespace**](msft-dfsnamespace.md)
</dt> </dl>

 

 





