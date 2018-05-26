---
title: GetNamespaces method of the MSFT\_DFSNamespace class
description: Retrieves configuration settings for an existing DFS namespace (DFS-N) or enumerates namespaces by server, domain, or namespace path.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 09558cee-5b3e-411e-802d-c333c7bd3c2d
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetNamespaces method
- GetNamespaces method, MSFT_DFSNamespace class
- MSFT_DFSNamespace class, GetNamespaces method
topic_type:
- apiref
api_name:
- MSFT_DFSNamespace.GetNamespaces
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetNamespaces method of the MSFT\_DFSNamespace class

Retrieves configuration settings for an existing DFS namespace (DFS-N) or enumerates namespaces by server, domain, or namespace path.

## Syntax


```mof
uint32 GetNamespaces(
  [in]  string            NamespaceRoot,
  [in]  string            Domain,
  [in]  string            Server,
  [out] MSFT_DFSNamespace cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*NamespaceRoot* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path to the root of a namespace. This value can be empty.

The UNC path can have one of these two formats:



| Server Format           | Domain Format           |
|-------------------------|-------------------------|
| \\\\ServerName\\DFSName | \\\\DomainName\\DFSName |



 

where:

-   The ServerName component represents the host name of a DFS root target of a namespace.
-   The DomainName component represents the domain name of the domain that hosts the domain-based namespace.
-   The DFSName component represents the DFS-N name.

A stand-alone namespace must have a root with the format shown in the first column, as it must contain a server name. A domain-based namespace can have a root with the format from either column, although the second column's format (which contains a domain name instead of a server name) is the preferred format. The **Type** property determines whether the namespace is stand-alone or domain-based.

</dd> <dt>

*Domain* \[in\]
</dt> <dd>

The domain that contains the DFS namespace(s) on which to retrieve the configuration settings. This value can be empty.

</dd> <dt>

*Server* \[in\]
</dt> <dd>

The server that contains the DFS namespace(s) on which to retrieve the configuration settings. This value can be empty.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains an array that represents output from the **Get-DFSNamespace** cmdlet. This parameter is passed uninitialized.

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

 

 





