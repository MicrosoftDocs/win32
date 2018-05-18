---
title: ClusDisk object
description: Provides access to identification and configuration data about a Physical Disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6433d55f-f97a-4027-ba2a-7102b4cf33ae'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusDisk object Failover Cluster", "ClusDisk object Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusDisk
- ISClusDisk
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusDisk object

\[The **ClusDisk** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to identification and configuration data about a [Physical Disk](physical-disk.md).

## Members

The **ClusDisk** object has these types of members:

-   [Properties](#properties)

### Properties

The **ClusDisk** object has these properties.



| Property                                               | Description                                                                                                                 |
|:-------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**DiskNumber**](clusdisk-disknumber.md)<br/>   | Returns the disk number of the disk.<br/>                                                                             |
| [**Partitions**](clusdisk-partitions.md)<br/>   | Returns a [**ClusPartitions**](cluspartitions-collection.md) collection containing partition data for the disk.<br/> |
| [**ScsiAddress**](clusdisk-scsiaddress.md)<br/> | Returns a [**ClusScsiAddress**](clusscsiaddress-object.md) object describing SCSI information about the disk.<br/>   |
| [**Signature**](clusdisk-signature.md)<br/>     | Returns the signature of the disk.<br/>                                                                               |



 

## Remarks

A **ClusDisk** object is obtained from [**ClusDisks.Item**](clusdisks-item.md) or [**ClusResource.Disk**](clusresource-disk.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusDisk is defined as F2E60724-2631-11D1-89F1-00A0C90D061E<br/>         |



 

 





