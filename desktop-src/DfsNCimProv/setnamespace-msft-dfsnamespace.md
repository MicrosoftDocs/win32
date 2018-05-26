---
title: SetNamespace method of the MSFT\_DFSNamespace class
description: Updates a property on a DFS namespace (DFS-N).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 991f98ac-0371-4d74-bc19-0b8b798bff9d
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetNamespace method
- SetNamespace method, MSFT_DFSNamespace class
- MSFT_DFSNamespace class, SetNamespace method
topic_type:
- apiref
api_name:
- MSFT_DFSNamespace.SetNamespace
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetNamespace method of the MSFT\_DFSNamespace class

Updates a property on a DFS namespace (DFS-N).

## Syntax


```mof
uint32 SetNamespace(
  [in]  uint32            State,
  [in]  uint32            TimeToLive,
  [in]  uint32            Flags,
  [in]  string            Description,
  [in]  string            NamespaceRoot,
  [in]  string            GrantAdminAccess[],
  [in]  string            RevokeAdminAccess[],
  [out] MSFT_DFSNamespace cmdletOutput
);
```



## Parameters

<dl> <dt>

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

*TimeToLive* \[in\]
</dt> <dd>

The interval time, in seconds, of the time to live (TTL) of the referral.

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

Enables cost-based site selection for the DFS namespace.

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

*Description* \[in\]
</dt> <dd>

A short description of the purpose of the namespace.

</dd> <dt>

*NamespaceRoot* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the root of the DFS namespace. The namespace root can take one of these two formats:



| Server Format           | Domain Format           |
|-------------------------|-------------------------|
| \\\\ServerName\\DFSName | \\\\DomainName\\DFSName |



 

where:

-   The ServerName component represents the host name of a DFS root target of a namespace.
-   The DomainName component represents the domain name of the domain that hosts the domain-based namespace.
-   The DFSName component represents the DFS-N name.

A stand-alone namespace must have a root with the format shown in the first column, as it must contain a server name. A domain-based namespace can have a root with the format from either column, although the second column's format (which contains a domain name instead of a server name) is the preferred format.

</dd> <dt>

*GrantAdminAccess* \[in\]
</dt> <dd>

An array that represents the list of user and group accounts to grant administrative access to on this namespace.

</dd> <dt>

*RevokeAdminAccess* \[in\]
</dt> <dd>

An array that represents the list of user and group accounts to revoke administrative access from on this namespace.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains output from the **Set-DFSNamespace** cmdlet. This parameter is passed uninitialized.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\dfsn<br/>                                                  |
| Header<br/>                   | <dl> <dt>Sbe.h</dt> </dl>           |
| MOF<br/>                      | <dl> <dt>DfsNCimProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsNCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DFSNamespace**](msft-dfsnamespace.md)
</dt> </dl>

 

 





