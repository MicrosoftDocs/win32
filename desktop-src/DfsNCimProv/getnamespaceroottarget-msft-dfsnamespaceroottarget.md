---
title: GetNamespaceRootTarget method of the MSFT\_DfsNamespaceRootTarget class
description: Retrieves the properties of the target of a DFS namespace (DFS-N) root.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1c594c3c-327f-41f9-b21b-c21516bc65c2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-namespace'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetNamespaceRootTarget method", "GetNamespaceRootTarget method, MSFT_DfsNamespaceRootTarget class", "MSFT_DfsNamespaceRootTarget class, GetNamespaceRootTarget method"]
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceRootTarget.GetNamespaceRootTarget
api_location:
- DfsNCimProv.dll
api_type:
- COM
---

# GetNamespaceRootTarget method of the MSFT\_DfsNamespaceRootTarget class

Retrieves the properties of the target of a DFS namespace (DFS-N) root. If no target is specified, the properties of all targets of a DFS-N root are retrieved.

## Syntax


```mof
uint32 GetNamespaceRootTarget(
  [in]  string                      NamespaceRoot,
  [in]  string                      RootTargetPath,
  [out] MSFT_DfsNamespaceRootTarget cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*NamespaceRoot* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS-N root that has a target with properties to be retrieved. The UNC path can be in one of these two formats:



| Server Format           | Domain Format           |
|-------------------------|-------------------------|
| \\\\ServerName\\DFSName | \\\\DomainName\\DFSName |



 

where:

-   The ServerName component represents the host name of a DFS root target of a namespace.
-   The DomainName component represents the domain name of the domain that hosts the domain-based namespace.
-   The DFSName component represents the DFS-N name.

A stand-alone namespace must have a root with the format shown in the first column, as it must contain a server name. A domain-based namespace can have a root with the format from either column, although the second column's format (which contains a domain name instead of a server name) is the preferred format.

</dd> <dt>

*RootTargetPath* \[in\]
</dt> <dd>

The UNC path of the target of a DFS-N root.

The DFS-N root target has a format of \\\\ServerName\\ShareName, where the ServerName component is the host name of a DFS-N root target server, and the ShareName component is the share name corresponding to a namespace on the DFS-N root target server.

If this parameter is empty, the method retrieves the properties of all targets of the DFS-N root.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains an array that represents output from the **Get-DFSNamespaceRootTarget** cmdlet. This parameter is passed uninitialized.

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

[**MSFT\_DfsNamespaceRootTarget**](msft-dfsnamespaceroottarget.md)
</dt> </dl>

 

 





