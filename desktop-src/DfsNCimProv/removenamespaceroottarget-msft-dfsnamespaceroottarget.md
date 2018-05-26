---
title: RemoveNamespaceRootTarget method of the MSFT\_DfsNamespaceRootTarget class
description: Removes a target of a DFS namespace (DFS-N) root.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f6d921dc-0e9c-4578-909e-d8cbb817ef67
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveNamespaceRootTarget method
- RemoveNamespaceRootTarget method, MSFT_DfsNamespaceRootTarget class
- MSFT_DfsNamespaceRootTarget class, RemoveNamespaceRootTarget method
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceRootTarget.RemoveNamespaceRootTarget
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveNamespaceRootTarget method of the MSFT\_DfsNamespaceRootTarget class

Removes a target of a DFS namespace (DFS-N) root. If the target being removed is the last root target, the user is notified.

## Syntax


```mof
uint32 RemoveNamespaceRootTarget(
  [in] string  NamespaceRoot,
  [in] string  RootTargetPath,
  [in] boolean ForceRemove
);
```



## Parameters

<dl> <dt>

*NamespaceRoot* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS-N root that has a target to be removed. The UNC path can be in one of these two formats:



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

</dd> <dt>

*ForceRemove* \[in\]
</dt> <dd>

**True** to force the removal of the target; otherwise, **false**.

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

[**MSFT\_DfsNamespaceRootTarget**](msft-dfsnamespaceroottarget.md)
</dt> </dl>

 

 





