---
title: ClusResource.Disk property
description: ClusDisk object providing access to information about the disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4f85a491-3cb7-409a-a7fb-9fc0f896e787'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Disk property Failover Cluster", "Disk property Failover Cluster , ClusResource class", "ClusResource class Failover Cluster , Disk property"]
topic_type:
- apiref
api_name:
- ClusResource.Disk
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResource.Disk property

\[The **Disk** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

For [Physical Disk](physical-disk.md), the **Disk** property returns a [**ClusDisk**](clusdisk-object.md) object providing access to information about the disk. For other types of resources, the **Disk** property returns nothing.

This property is read-only.

## Syntax


```VB
ClusResource.Disk
```



## Property value

A [**ClusDisk**](clusdisk-object.md) object that receives the disk information.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusDisk**](clusdisk-object.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





