---
title: ClusScsiAddress.Lun property
description: SCSI Lun of the Physical Disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 47ac3714-fe5c-4b3b-9271-57980981785d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Lun property Failover Cluster
- Lun property Failover Cluster , ClusScsiAddress object
- ClusScsiAddress object Failover Cluster , Lun property
topic_type:
- apiref
api_name:
- ClusScsiAddress.Lun
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusScsiAddress.Lun property

\[The **Lun** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the [*SCSI*](https://www.bing.com/search?q=*SCSI*) Lun of the [Physical Disk](physical-disk.md).

This property is read-only.

## Syntax


```VB
ClusScsiAddress.Lun
```



## Property value

A **Variant** that contains the Lun of the disk.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusScsiAddress is defined as f2e60728-2631-11d1-89f1-00a0c90d061e<br/>  |



## See also

<dl> <dt>

[**ClusDisk**](clusdisk-object.md)
</dt> <dt>

[**ClusScsiAddress**](clusscsiaddress-object.md)
</dt> <dt>

[**ClusScsiAddress.PathId**](clusscsiaddress-pathid.md)
</dt> <dt>

[**ClusScsiAddress.PortNumber**](clusscsiaddress-portnumber.md)
</dt> <dt>

[**ClusScsiAddress.TargetId**](clusscsiaddress-targetid.md)
</dt> </dl>

 

 





