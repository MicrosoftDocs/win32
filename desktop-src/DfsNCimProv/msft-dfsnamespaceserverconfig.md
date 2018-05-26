---
title: MSFT\_DFSNamespaceServerConfig class
description: Represents the configuration of a DFS namespace (DFS-N) server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 53b6d005-4d13-4c2c-8278-a514ff4a886f
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DFSNamespaceServerConfig class
- MSFT_DFSNamespaceServerConfig class, described
topic_type:
- apiref
api_name:
- MSFT_DFSNamespaceServerConfig
- MSFT_DFSNamespaceServerConfig.EnableInsiteReferrals
- MSFT_DFSNamespaceServerConfig.EnableSiteCostedReferrals
- MSFT_DFSNamespaceServerConfig.LdapTimeout
- MSFT_DFSNamespaceServerConfig.NamespaceServer
- MSFT_DFSNamespaceServerConfig.PreferLogonDC
- MSFT_DFSNamespaceServerConfig.SyncInterval
- MSFT_DFSNamespaceServerConfig.UseFullyQualifiedDomainNames
api_location:
- DfsNCimProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DFSNamespaceServerConfig class

Represents the configuration of a DFS namespace (DFS-N) server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("dfsncimprov"), ClassVersion("1.0"), AMENDMENT]
class MSFT_DFSNamespaceServerConfig
{
  boolean EnableInsiteReferrals;
  boolean EnableSiteCostedReferrals;
  uint32  LdapTimeout;
  string  NamespaceServer;
  boolean PreferLogonDC;
  uint32  SyncInterval;
  boolean UseFullyQualifiedDomainNames;
};
```

## Members

The **MSFT\_DFSNamespaceServerConfig** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DFSNamespaceServerConfig** class has these methods.



| Method                                                                                     | Description                                                               |
|:-------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| [**GetNamespaceServerConfig**](getnamespaceserverconfig-msft-dfsnamespaceserverconfig.md) | Retrieves the configuration of a DFS namespace (DFS-N) server.<br/> |
| [**SetNamespaceServerConfig**](setnamespaceserverconfig-msft-dfsnamespaceserverconfig.md) | Modifies the configuration of a DFS namespace (DFS-N) server.<br/>  |



 

### Properties

The **MSFT\_DFSNamespaceServerConfig** class has these properties.

<dl> <dt>

**EnableInsiteReferrals**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if in-site referrals are enabled for the DFS-N server; otherwise, **false**. When this setting is enabled, the DFS-N server provides referrals that belong to the same site as the client. The default value is **false**.

</dd> <dt>

**EnableSiteCostedReferrals**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if site-costed referrals are enabled for the DFS-N server; otherwise, **false**. The default value is **false**.

When site costing is enabled, SYSVOL and NETLOGON referrals sort domain controllers in the order of the the lowest cost. Domain controllers from the client's site are at the top of the referral list, followed by domain controllers from the server that are sorted by the lowest cost. When site costing is disabled, SYSVOL and NETLOGON referrals contain randomly ordered domain controllers from the client's site, followed by randomly ordered domain controllers from the server.

</dd> <dt>

**LdapTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets the timeout interval, in seconds, to be enforced by the DFS-N server for Lightweight Directory Access Protocol (LDAP) calls. This property can be between 3 and 300 seconds, and the default value is 30 seconds.

</dd> <dt>

**NamespaceServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets or sets the name of the DFS-N server for which to retrieve the configuration settings.

</dd> <dt>

**PreferLogonDC**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the logon server is placed at the top of the referral list; otherwise, **false**. The default value is **false**.

</dd> <dt>

**SyncInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets the interval time, in seconds, between attempts by domain-based root servers and domain controllers to poll the primary domain controller (PDC) emulator master to obtain the updated DFS metadata.

</dd> <dt>

**UseFullyQualifiedDomainNames**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the DFS-N server uses fully qualified domain names (FQDN) in referrals; **false** if the DFS-N server uses NetBIOS in referrals. The default value is **false**.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\dfsn<br/>                                                  |
| MOF<br/>                      | <dl> <dt>DfsNCimProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsNCimProv.dll</dt> </dl> |



 

 





