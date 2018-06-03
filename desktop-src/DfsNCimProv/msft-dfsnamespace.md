---
title: MSFT\_DFSNamespace class
description: Represents a DFS namespace (DFS-N).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b82c74a2-d6bc-4b07-8db2-19921d799655
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DFSNamespace class
- MSFT_DFSNamespace class, described
topic_type:
- apiref
api_name:
- MSFT_DFSNamespace
- MSFT_DFSNamespace.Description
- MSFT_DFSNamespace.NamespacePath
- MSFT_DFSNamespace.State
- MSFT_DFSNamespace.TimeToLive
- MSFT_DFSNamespace.Flags
- MSFT_DFSNamespace.GrantAdminAccess
- MSFT_DFSNamespace.Type
api_location:
- DfsNCimProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DFSNamespace class

Represents a DFS namespace (DFS-N). This class can be used to enumerate, modify, delete, and create new namespaces.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("dfsncimprov"), ClassVersion("1.0"), AMENDMENT]
class MSFT_DFSNamespace : MSFT_DfsNamespaceLinkBase
{
  string Description;
  string NamespacePath;
  uint32 State;
  uint32 TimeToLive;
  uint32 Flags;
  string GrantAdminAccess[];
  uint32 Type;
};
```

## Members

The **MSFT\_DFSNamespace** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DFSNamespace** class has these methods.



| Method                                                       | Description                                                                                                                          |
|:-------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| [**GetNamespaces**](getnamespaces-msft-dfsnamespace.md)     | Retrieves configuration settings for an existing namespace or enumerates namespaces by server, domain, or namespace path.<br/> |
| [**NewNamespace**](newnamespace-msft-dfsnamespace.md)       | Creates a new namespace.<br/>                                                                                                  |
| [**RemoveNamespace**](removenamespace-msft-dfsnamespace.md) | Removes a namespace and any child namespace links.<br/>                                                                        |
| [**SetNamespace**](setnamespace-msft-dfsnamespace.md)       | Updates a property on a namespace root.<br/>                                                                                   |



 

### Properties

The **MSFT\_DFSNamespace** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets a short description of the purpose of the DFS-N root or the DFS-N link.

This property is inherited from [**MSFT\_DfsNamespaceLinkBase**](msft-dfsnamespacelinkbase.md).

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**BitMap**](https://msdn.microsoft.com/library/aa393650) ("0", "1", "2", "3", "5"), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Flags"), [**BitValues**](https://msdn.microsoft.com/library/aa393650) ("InsiteReferrals", "RootScalability", "SiteCosting", "TargetFailback", "AccessBasedEnumeration")
</dt> </dl>

Gets or sets a bitwise combination of the enumeration values that represent the properties of the namespace.

<dt>

<span id="InsiteReferrals"></span><span id="insitereferrals"></span><span id="INSITEREFERRALS"></span>

<span id="InsiteReferrals"></span><span id="insitereferrals"></span><span id="INSITEREFERRALS"></span>**"InsiteReferrals"** ("0")


</dt> <dd>

**True** if in-site referrals are enabled for the namespace; otherwise, **false**. The default value is **false**.

</dd> <dt>

<span id="RootScalability"></span><span id="rootscalability"></span><span id="ROOTSCALABILITY"></span>

<span id="RootScalability"></span><span id="rootscalability"></span><span id="ROOTSCALABILITY"></span>**"RootScalability"** ("1")


</dt> <dd>

**True** if namespace polling mode is enabled for the namespace; otherwise, **false**. The default value is **false**.

</dd> <dt>

<span id="SiteCosting"></span><span id="sitecosting"></span><span id="SITECOSTING"></span>

<span id="SiteCosting"></span><span id="sitecosting"></span><span id="SITECOSTING"></span>**"SiteCosting"** ("2")


</dt> <dd>

**True** if cost-based site selection is enabled for the namespace; otherwise, **false**. The default value is **false**.

Site cost is a relative, numeric value that indicates the bandwidth or actual monetary cost of transmitting data between two sites, with the lower-cost site being preferred to a higher-cost site. Only a comparison between site costs is meaningful; a single site's cost value by itself does not provide any information.

</dd> <dt>

<span id="TargetFailback"></span><span id="targetfailback"></span><span id="TARGETFAILBACK"></span>

<span id="TargetFailback"></span><span id="targetfailback"></span><span id="TARGETFAILBACK"></span>**"TargetFailback"** ("3")


</dt> <dd>

**True** if target failback is enabled for the namespace; otherwise, **false**. The default value is **false**.

</dd> <dt>

<span id="AccessBasedEnumeration"></span><span id="accessbasedenumeration"></span><span id="ACCESSBASEDENUMERATION"></span>

<span id="AccessBasedEnumeration"></span><span id="accessbasedenumeration"></span><span id="ACCESSBASEDENUMERATION"></span>**"AccessBasedEnumeration"** ("5")


</dt> <dd>

**True** if access-based enumeration is enabled for the namespace; otherwise, **false**. The default value is **false**.

</dd> </dl>

</dd> <dt>

**GrantAdminAccess**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets an array that represents the list of user and group accounts that have been delegated administrative access to this namespace.

</dd> <dt>

**NamespacePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets or sets the Universal Naming Convention (UNC) path of the DFS-N root or the DFS-N link.

A DFS-N root or a DFS-N link can have one of the following UNC path formats:



|            | Server Format                     | Domain Format                     |
|------------|-----------------------------------|-----------------------------------|
| DFS-N Root | \\\\ServerName\\DFSName           | \\\\DomainName\\DFSName           |
| DFS-N Link | \\\\ServerName\\DFSName\\LinkPath | \\\\DomainName\\DFSName\\LinkPath |



 

where:

-   The ServerName component represents the host name of a DFS root target of a DFS namespace.
-   The DomainName component represents the domain name of the domain that hosts the domain-based DFS namespace.
-   The DFSName component represents the DFS-N name.
-   The LinkPath component represents the path of the DFS-N link relative to the DFS root target share.

Stand-alone DFS namespaces must have links and roots with the formats shown in the first column, as they must contain a server name. Domain-based DFS namespaces can have links and roots with the formats from either column, although the second column's formats (which contain a domain name instead of a server name) are the preferred format.

This property is inherited from [**MSFT\_DfsNamespaceLinkBase**](msft-dfsnamespacelinkbase.md).

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets the state of the DFS-N root or the DFS-N link. The default value is "ONLINE".

This property is inherited from [**MSFT\_DfsNamespaceLinkBase**](msft-dfsnamespacelinkbase.md).

<dt>

<span id="OFFLINE"></span><span id="offline"></span>

<span id="OFFLINE"></span><span id="offline"></span>**"OFFLINE"** (3)


</dt> <dd>

Not online.

</dd> <dt>

<span id="ONLINE"></span><span id="online"></span>

<span id="ONLINE"></span><span id="online"></span>**"ONLINE"** (4)


</dt> <dd>

Online.

</dd> </dl>

</dd> <dt>

**TimeToLive**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets the interval time, in seconds, of the time to live (TTL) of the referral. A referral TTL determines the amount of time that clients cache (store) referrals for this DFS-N root or DFS-N link. The default value is 300.

This property is inherited from [**MSFT\_DfsNamespaceLinkBase**](msft-dfsnamespacelinkbase.md).

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the type of namespace to create. The default value is "Domain v2".

<dt>

<span id="Stand-alone"></span><span id="stand-alone"></span><span id="STAND-ALONE"></span>

<span id="Stand-alone"></span><span id="stand-alone"></span><span id="STAND-ALONE"></span>**"Stand-alone"** (0)


</dt> <dd>

A stand-alone namespace.

</dd> <dt>

<span id="Domain_v1"></span><span id="domain_v1"></span><span id="DOMAIN_V1"></span>

<span id="Domain_v1"></span><span id="domain_v1"></span><span id="DOMAIN_V1"></span>**"Domain v1"** (1)


</dt> <dd>

A domain namespace of Windows 2000 Server mode.

</dd> <dt>

<span id="Domain_v2"></span><span id="domain_v2"></span><span id="DOMAIN_V2"></span>

<span id="Domain_v2"></span><span id="domain_v2"></span><span id="DOMAIN_V2"></span>**"Domain v2"** (2)


</dt> <dd>

A domain namespace of Windows Server 2008 mode.

</dd> </dl>

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

[**MSFT\_DfsNamespaceLinkBase**](msft-dfsnamespacelinkbase.md)
</dt> </dl>

 

 





