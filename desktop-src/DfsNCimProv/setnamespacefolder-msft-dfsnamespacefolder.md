---
title: SetNamespaceFolder method of the MSFT\_DfsNamespaceFolder class
description: Updates the properties of a DFS folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 97045f58-3ecb-4cf0-a0fd-be5603658968
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetNamespaceFolder method
- SetNamespaceFolder method, MSFT_DfsNamespaceFolder class
- MSFT_DfsNamespaceFolder class, SetNamespaceFolder method
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceFolder.SetNamespaceFolder
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetNamespaceFolder method of the MSFT\_DfsNamespaceFolder class

Updates the properties of a DFS folder.

## Syntax


```mof
uint32 SetNamespaceFolder(
  [in]  string                  NamespacePath,
  [in]  string                  Description,
  [in]  uint32                  Flags,
  [in]  uint32                  State,
  [in]  uint32                  TimeToLive,
  [out] MSFT_DfsNamespaceFolder cmdletOutput
);
```



## Parameters

<dl> <dt>

*NamespacePath* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS folder that contains the properties to be updated. The UNC path has a format of \\\\HostName\\SharedName\[\\ObjectName\]\*, where:

-   The HostName component represents either the host name of a server or the domain name of a domain that hosts resources.
-   The SharedName component represents the share name or the name of the resource that is being accessed.
-   Each ObjectName component represents the name of a directory on the resource that is being accessed.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

A short description to use for the DFS folder.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

A bitwise combination of the enumeration values that represent the new properties of the DFS folder.

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

The new state of the DFS folder.

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

The new interval time, in seconds, of the time to live (TTL) of the referral.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains output from the **Set-DFSNamespaceFolder** cmdlet. This parameter is passed uninitialized.

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

 

 





