---
title: ClusVersion.BuildNumber property
description: Returns the build number of the operating system installed on the local node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2862d1b8-42b6-437f-8979-e3d385905801'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["BuildNumber property Failover Cluster", "BuildNumber property Failover Cluster , ClusVersion object", "ClusVersion object Failover Cluster , BuildNumber property"]
topic_type:
- apiref
api_name:
- ClusVersion.BuildNumber
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusVersion.BuildNumber property

\[The **BuildNumber** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the build number of the operating system installed on the local [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusVersion.BuildNumber
```



## Property value

Short that receives the build number.

## Remarks

All [**ClusVersion**](clusversion-object.md) properties are static values corresponding the state of the [*cluster*](c-gly.md#-wolf-cluster-gly) when the **ClusVersion** object was first created. To obtain the latest version information from the cluster, create a new **ClusVersion** object.

## Examples

See [**ClusVersion**](clusversion-object.md) for an example.

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

 

 





