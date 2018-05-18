---
title: SetNamespaceRootTarget method of the MSFT\_DfsNamespaceRootTarget class
description: Modifies the properties of the target of a DFS namespace (DFS-N) root.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f2d0f78f-717a-4bc8-a4fa-432a277f767d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-namespace'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetNamespaceRootTarget method", "SetNamespaceRootTarget method, MSFT_DfsNamespaceRootTarget class", "MSFT_DfsNamespaceRootTarget class, SetNamespaceRootTarget method"]
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceRootTarget.SetNamespaceRootTarget
api_location:
- DfsNCimProv.dll
api_type:
- COM
---

# SetNamespaceRootTarget method of the MSFT\_DfsNamespaceRootTarget class

Modifies the properties of the target of a DFS namespace (DFS-N) root.

## Syntax


```mof
uint32 SetNamespaceRootTarget(
  [in]  string                      NamespaceRoot,
  [in]  string                      RootTargetPath,
  [in]  uint32                      State,
  [in]  uint32                      ReferralPriorityRank,
  [in]  sint32                      ReferralPriorityClass,
  [out] MSFT_DfsNamespaceRootTarget cmdletOutput
);
```



## Parameters

<dl> <dt>

*NamespaceRoot* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS-N root that has a target with properties to be modified. The UNC path can be in one of these two formats:



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

*State* \[in\]
</dt> <dd>

The new state of the target of a DFS-N root.

<dt>

<span id="OFFLINE"></span><span id="offline"></span>

<span id="OFFLINE"></span><span id="offline"></span>**OFFLINE** (3)


</dt> <dd>

Not online. Referrals are disabled.

</dd> <dt>

<span id="ONLINE"></span><span id="online"></span>

<span id="ONLINE"></span><span id="online"></span>**ONLINE** (4)


</dt> <dd>

Online. Referrals are enabled.

</dd> </dl> </dd> <dt>

*ReferralPriorityRank* \[in\]
</dt> <dd>

The new priority rank of the target of a DFS-N root.

</dd> <dt>

*ReferralPriorityClass* \[in\]
</dt> <dd>

The new priority class of the target of a DFS-N root.

<dt>

<span id="Invalid"></span><span id="invalid"></span><span id="INVALID"></span>

<span id="Invalid"></span><span id="invalid"></span><span id="INVALID"></span>**Invalid** (-1)


</dt> <dd>

Invalid priority.

</dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>**Normal** (0)


</dt> <dd>

Site cost, normal priority.

</dd> <dt>

<span id="global-high"></span><span id="GLOBAL-HIGH"></span>

<span id="global-high"></span><span id="GLOBAL-HIGH"></span>**global-high** (1)


</dt> <dd>

Global, high priority.

</dd> <dt>

<span id="sitecost-high"></span><span id="SITECOST-HIGH"></span>

<span id="sitecost-high"></span><span id="SITECOST-HIGH"></span>**sitecost-high** (2)


</dt> <dd>

Site cost, high priority.

</dd> <dt>

<span id="sitecost-low"></span><span id="SITECOST-LOW"></span>

<span id="sitecost-low"></span><span id="SITECOST-LOW"></span>**sitecost-low** (3)


</dt> <dd>

Site cost, low priority.

</dd> <dt>

<span id="global-low"></span><span id="GLOBAL-LOW"></span>

<span id="global-low"></span><span id="GLOBAL-LOW"></span>**global-low** (4)


</dt> <dd>

Global, low priority.

</dd> </dl> </dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains output from the **Set-DFSNamespaceRootTarget** cmdlet. This parameter is passed uninitialized.

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

 

 





