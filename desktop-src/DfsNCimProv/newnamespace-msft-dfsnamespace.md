---
title: NewNamespace method of the MSFT\_DFSNamespace class
description: Creates a new DFS namespace (DFS-N).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0bd374e7-a06e-4104-802f-73e4e0224826
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NewNamespace method
- NewNamespace method, MSFT_DFSNamespace class
- MSFT_DFSNamespace class, NewNamespace method
topic_type:
- apiref
api_name:
- MSFT_DFSNamespace.NewNamespace
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NewNamespace method of the MSFT\_DFSNamespace class

Creates a new DFS namespace (DFS-N).

## Syntax


```mof
uint32 NewNamespace(
  [in]  uint32            Type,
  [in]  string            Description,
  [in]  uint32            Flags,
  [in]  uint32            TimeToLive,
  [in]  uint32            State,
  [in]  string            GrantAdminAccess[],
  [in]  string            NamespaceRootTarget,
  [in]  string            NamespaceRoot,
  [in]  uint32            TargetState,
  [in]  uint32            ReferralPriorityRank,
  [in]  sint32            ReferralPriorityClass,
  [out] MSFT_DFSNamespace cmdletOutput
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The type of namespace to create.

<dt>

<span id="Stand-alone"></span><span id="stand-alone"></span><span id="STAND-ALONE"></span>

<span id="Stand-alone"></span><span id="stand-alone"></span><span id="STAND-ALONE"></span>**Stand-alone** (0)


</dt> <dd>

A stand-alone namespace.

</dd> <dt>

<span id="Domain_v1"></span><span id="domain_v1"></span><span id="DOMAIN_V1"></span>

<span id="Domain_v1"></span><span id="domain_v1"></span><span id="DOMAIN_V1"></span>**Domain v1** (1)


</dt> <dd>

A domain namespace of Windows 2000 Server mode.

</dd> <dt>

<span id="Domain_v2"></span><span id="domain_v2"></span><span id="DOMAIN_V2"></span>

<span id="Domain_v2"></span><span id="domain_v2"></span><span id="DOMAIN_V2"></span>**Domain v2** (2)


</dt> <dd>

A domain namespace of Windows Server 2008 mode.

</dd> </dl> </dd> <dt>

*Description* \[in\]
</dt> <dd>

A short description of the purpose of the namespace.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

A bitwise combination of the enumeration values that represent the properties of the namespace.

<dt>

<span id="InsiteReferrals"></span><span id="insitereferrals"></span><span id="INSITEREFERRALS"></span>

<span id="InsiteReferrals"></span><span id="insitereferrals"></span><span id="INSITEREFERRALS"></span>**InsiteReferrals** (1 (0x1))


</dt> <dd>

Enables in-site referrals for the namespace.

</dd> <dt>

<span id="RootScalability"></span><span id="rootscalability"></span><span id="ROOTSCALABILITY"></span>

<span id="RootScalability"></span><span id="rootscalability"></span><span id="ROOTSCALABILITY"></span>**RootScalability** (2 (0x2))


</dt> <dd>

Enables namespace polling mode for the namespace.

</dd> <dt>

<span id="SiteCosting"></span><span id="sitecosting"></span><span id="SITECOSTING"></span>

<span id="SiteCosting"></span><span id="sitecosting"></span><span id="SITECOSTING"></span>**SiteCosting** (4 (0x4))


</dt> <dd>

Enables cost-based site selection for the namespace.

Site cost is a relative, numeric value that indicates the bandwidth or actual monetary cost of transmitting data between two sites, with the lower-cost site being preferred to a higher-cost site. Only a comparison between site costs is meaningful; a single site's cost value by itself does not provide any information.

</dd> <dt>

<span id="TargetFailback"></span><span id="targetfailback"></span><span id="TARGETFAILBACK"></span>

<span id="TargetFailback"></span><span id="targetfailback"></span><span id="TARGETFAILBACK"></span>**TargetFailback** (8 (0x8))


</dt> <dd>

Enables target failback for the namespace.

</dd> <dt>

<span id="AccessBasedEnumeration"></span><span id="accessbasedenumeration"></span><span id="ACCESSBASEDENUMERATION"></span>

<span id="AccessBasedEnumeration"></span><span id="accessbasedenumeration"></span><span id="ACCESSBASEDENUMERATION"></span>**AccessBasedEnumeration** (32 (0x20))


</dt> <dd>

Enables access-based enumeration for the namespace.

</dd> </dl> </dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

The interval time, in seconds, of the time to live (TTL) of the referral.

</dd> <dt>

*State* \[in\]
</dt> <dd>

The state of the DFS-N root.

<dt>

<span id="OFFLINE"></span><span id="offline"></span>

<span id="OFFLINE"></span><span id="offline"></span>**OFFLINE** (3)


</dt> <dd>

Not online.

</dd> <dt>

<span id="ONLINE"></span><span id="online"></span>

<span id="ONLINE"></span><span id="online"></span>**ONLINE** (4)


</dt> <dd>

Online.

</dd> </dl> </dd> <dt>

*GrantAdminAccess* \[in\]
</dt> <dd>

An array that represents the list of user and group accounts that have been delegated administrative access to this namespace.

</dd> <dt>

*NamespaceRootTarget* \[in\]
</dt> <dd>

The default root target of the namespace. The root target is a Universal Naming Convention (UNC) path of the format \\\\ServerName\\ShareName, where the ServerName component represents the host name of a DFS root target server, and the ShareName component represents the share name that corresponds to a namespace on the DFS root target server.

</dd> <dt>

*NamespaceRoot* \[in\]
</dt> <dd>

The UNC path of the root of the namespace. The namespace root can take one of these two formats:



| Server Format           | Domain Format           |
|-------------------------|-------------------------|
| \\\\ServerName\\DFSName | \\\\DomainName\\DFSName |



 

where:

-   The ServerName component represents the host name of a DFS root target of a namespace.
-   The DomainName component represents the domain name of the domain that hosts the domain-based namespace.
-   The DFSName component represents the DFS-N name.

A stand-alone namespace must have a root with the format shown in the first column, as it must contain a server name. A domain-based namespace can have a root with the format from either column, although the second column's format (which contains a domain name instead of a server name) is the preferred format. The *Type* parameter specifies whether the namespace is stand-alone or domain-based.

</dd> <dt>

*TargetState* \[in\]
</dt> <dd>

The state of the DFS-N root target.

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

The priority rank of the namespace.

</dd> <dt>

*ReferralPriorityClass* \[in\]
</dt> <dd>

The priority class of the namespace.

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

When this method returns, contains output from the **New-DFSNamespace** cmdlet. This parameter is passed uninitialized.

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

 

 





