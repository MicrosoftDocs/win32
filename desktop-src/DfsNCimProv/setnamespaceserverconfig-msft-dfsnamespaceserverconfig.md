---
title: SetNamespaceServerConfig method of the MSFT\_DFSNamespaceServerConfig class
description: Modifies the configuration of a DFS namespace (DFS-N) server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c3ef7c36-ff45-4280-a274-ed51d5d0e781
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetNamespaceServerConfig method
- SetNamespaceServerConfig method, MSFT_DFSNamespaceServerConfig class
- MSFT_DFSNamespaceServerConfig class, SetNamespaceServerConfig method
topic_type:
- apiref
api_name:
- MSFT_DFSNamespaceServerConfig.SetNamespaceServerConfig
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetNamespaceServerConfig method of the MSFT\_DFSNamespaceServerConfig class

Modifies the configuration of a DFS namespace (DFS-N) server.

## Syntax


```mof
uint32 SetNamespaceServerConfig(
  [in]  string                        NamespaceServer,
  [in]  uint32                        LdapTimeout,
  [in]  boolean                       PreferLogonDC,
  [in]  boolean                       EnableSiteCostedReferrals,
  [in]  boolean                       EnableInsiteReferrals,
  [in]  uint32                        SyncInterval,
  [in]  boolean                       UseFullyQualifiedDomainNames,
  [out] MSFT_DFSNamespaceServerConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*NamespaceServer* \[in\]
</dt> <dd>

The DFS-N server for which to modify the configuration settings.

</dd> <dt>

*LdapTimeout* \[in\]
</dt> <dd>

The timeout interval, in seconds, to be enforced by the DFS-N server for Lightweight Directory Access Protocol (LDAP) calls. This value can be between 3 and 300 seconds.

</dd> <dt>

*PreferLogonDC* \[in\]
</dt> <dd>

**True** to place the logon server at the top of the referral list; otherwise, **false**.

</dd> <dt>

*EnableSiteCostedReferrals* \[in\]
</dt> <dd>

**True** to enable site-costed referrals; otherwise, **false**.

When site costing is enabled, SYSVOL and NETLOGON referrals sort domain controllers in the order of the the lowest cost. Domain controllers from the client's site are at the top of the referral list, followed by domain controllers from the server that are sorted by the lowest cost. When site costing is disabled, SYSVOL and NETLOGON referrals contain randomly ordered domain controllers from the client's site, followed by randomly ordered domain controllers from the server.

</dd> <dt>

*EnableInsiteReferrals* \[in\]
</dt> <dd>

**True** to enable in-site referrals; otherwise, **false**. When this setting is enabled, the DFS-N server provides referrals that belong to the same site as the client.

</dd> <dt>

*SyncInterval* \[in\]
</dt> <dd>

The interval time, in seconds, between attempts by domain-based root servers and domain controllers to poll the primary domain controller (PDC) emulator master to obtain the updated DFS metadata.

</dd> <dt>

*UseFullyQualifiedDomainNames* \[in\]
</dt> <dd>

**True** to use fully qualified domain names (FQDN) in referrals; **false** to use NetBIOS in referrals.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains output from the **Set-DFSNamespaceServerConfig** cmdlet. This parameter is passed uninitialized.

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

[**MSFT\_DFSNamespaceServerConfig**](msft-dfsnamespaceserverconfig.md)
</dt> </dl>

 

 





