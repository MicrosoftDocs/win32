---
title: NewNamespaceFolder method of the MSFT\_DfsNamespaceFolder class
description: Creates a new DFS folder in the existing namespace.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05180de7-a112-4a73-9c1f-e72c389c499b
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NewNamespaceFolder method
- NewNamespaceFolder method, MSFT_DfsNamespaceFolder class
- MSFT_DfsNamespaceFolder class, NewNamespaceFolder method
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceFolder.NewNamespaceFolder
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NewNamespaceFolder method of the MSFT\_DfsNamespaceFolder class

Creates a new DFS folder in the existing namespace.

## Syntax


```mof
uint32 NewNamespaceFolder(
  [in]  string                  NamespacePath,
  [in]  string                  TargetPath,
  [in]  string                  Description,
  [in]  uint32                  Flags,
  [in]  uint32                  State,
  [in]  uint32                  TimeToLive,
  [in]  uint32                  TargetState,
  [in]  uint32                  ReferralPriorityRank,
  [in]  sint32                  ReferralPriorityClass,
  [out] MSFT_DfsNamespaceFolder cmdletOutput
);
```



## Parameters

<dl> <dt>

*NamespacePath* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS folder to be created. The UNC path has a format of \\\\HostName\\SharedName\[\\ObjectName\]\*, where:

-   The HostName component represents either the host name of a server or the domain name of a domain that hosts resources.
-   The SharedName component represents the share name or the name of the resource that is being accessed.
-   Each ObjectName component represents the name of a directory on the resource that is being accessed.

</dd> <dt>

*TargetPath* \[in\]
</dt> <dd>

The UNC path of the folder target of the created DFS folder.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

A short description of the purpose of the new DFS folder.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

A bitwise combination of the enumeration values that represent the properties of the DFS folder.

<dt>

<span id="InsiteReferrals"></span><span id="insitereferrals"></span><span id="INSITEREFERRALS"></span>

<span id="InsiteReferrals"></span><span id="insitereferrals"></span><span id="INSITEREFERRALS"></span>**InsiteReferrals** (1 (0x1))


</dt> <dd>

Enables in-site referrals for the DFS folder.

</dd> <dt>

<span id="TargetFailback"></span><span id="targetfailback"></span><span id="TARGETFAILBACK"></span>

<span id="TargetFailback"></span><span id="targetfailback"></span><span id="TARGETFAILBACK"></span>**TargetFailback** (8 (0x8))


</dt> <dd>

Enables target failback for the DFS folder.

</dd> </dl> </dd> <dt>

*State* \[in\]
</dt> <dd>

The state of the DFS namespace folder.

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

*TargetState* \[in\]
</dt> <dd>

The state of the folder target of the created DFS folder.

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

The priority rank of the DFS folder.

</dd> <dt>

*ReferralPriorityClass* \[in\]
</dt> <dd>

The priority class of the DFS folder.

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

When this method returns, contains output from the **New-DFSNamespaceFolder** cmdlet. This parameter is passed uninitialized.

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

[**MSFT\_DfsNamespaceFolder**](msft-dfsnamespacefolder.md)
</dt> </dl>

 

 





