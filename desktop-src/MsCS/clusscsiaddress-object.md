---
title: ClusScsiAddress object
description: Provides access to SCSI information about a Physical Disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7becbcf6-bad9-44e2-9731-d53de8299b99'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusScsiAddress object Failover Cluster", "ClusScsiAddress object Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusScsiAddress
- ISClusScsiAddress
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusScsiAddress object

\[The **ClusScsiAddress** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to [*SCSI*](s-gly.md#-wolf-small-computer-system-interface-gly) information about a [Physical Disk](physical-disk.md).

## Members

The **ClusScsiAddress** object has these types of members:

-   [Properties](#properties)

### Properties

The **ClusScsiAddress** object has these properties.



| Property                                                    | Access type          | Description                                    |
|:------------------------------------------------------------|:---------------------|:-----------------------------------------------|
| [**Lun**](clusscsiaddress-lun.md)<br/>               | Read-only<br/> | Contains the Lun of the disk.<br/>       |
| [**PathId**](clusscsiaddress-pathid.md)<br/>         | Read-only<br/> | Contains the path ID of the disk.<br/>   |
| [**PortNumber**](clusscsiaddress-portnumber.md)<br/> | Read-only<br/> | Contains the port ID of the disk.<br/>   |
| [**TargetId**](clusscsiaddress-targetid.md)<br/>     | Read-only<br/> | Contains the target ID of the disk.<br/> |



 

## Remarks

A **ClusScsiAddress** object is obtained from [**ClusDisk.ScsiAddress**](clusdisk-scsiaddress.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusScsiAddress is defined as f2e60728-2631-11d1-89f1-00a0c90d061e<br/>  |



## See also

<dl> <dt>

[Disk Management Objects](disk-management-objects.md)
</dt> <dt>

[**CLUS\_SCSI\_ADDRESS**](clus-scsi-address.md)
</dt> </dl>

 

 





