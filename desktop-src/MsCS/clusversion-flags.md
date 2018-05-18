---
title: ClusVersion.Flags property
description: Returns flags associated with the cluster version.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f671f494-6c46-45e6-9756-fc27dc10783a'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Flags property Failover Cluster", "Flags property Failover Cluster , ClusVersion object", "ClusVersion object Failover Cluster , Flags property"]
topic_type:
- apiref
api_name:
- ClusVersion.Flags
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusVersion.Flags property

\[The **Flags** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns flags associated with the [*cluster version*](c-gly.md#-wolf-cluster-version-gly).

This property is read-only.

## Syntax


```VB
ClusVersion.Flags
```



## Property value

**Long** that receives the flags. Only one flag is defined by MsClus.h.

<dt>

<span id="CLUSTER_VERSION_FLAG_MIXED_MODE"></span><span id="cluster_version_flag_mixed_mode"></span>

<span id="CLUSTER_VERSION_FLAG_MIXED_MODE"></span><span id="cluster_version_flag_mixed_mode"></span>**CLUSTER\_VERSION\_FLAG\_MIXED\_MODE** (0x00000001)


</dt> <dd>

There is more than one version of the Cluster service running on the cluster nodes.

</dd> </dl>

## Remarks

All [**ClusVersion**](clusversion-object.md) properties are static values corresponding the state of the [*cluster*](c-gly.md#-wolf-cluster-gly) when the **ClusVersion** object was first created. To obtain the latest version information from the cluster, create a new **ClusVersion** object.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusVersion is defined as F2E60716-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusVersion**](clusversion-object.md)
</dt> <dt>

[**ClusVersion.CSDVersion**](clusversion-csdversion.md)
</dt> <dt>

[**ClusVersion.MajorVersion**](clusversion-majorversion.md)
</dt> <dt>

[**ClusVersion.MinorVersion**](clusversion-minorversion.md)
</dt> </dl>

 

 





