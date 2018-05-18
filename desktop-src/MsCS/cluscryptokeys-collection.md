---
title: ClusCryptoKeys collection
description: Provides access to the checkpointed crypto keys of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0078ba7a-24d7-4de6-af05-f1a03d9deb0a'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusCryptoKeys collection Failover Cluster", "ClusCryptoKeys collection Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusCryptoKeys
- ISClusCryptoKeys
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusCryptoKeys collection

\[The **ClusCryptoKeys** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [checkpointed](checkpointing.md) crypto keys of a resource. Crypto keys are created using the Crypto API. Checkpointed keys are moved to the resource's new host [node](nodes.md) during [failover](failover.md).

## Members

The **ClusCryptoKeys** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusCryptoKeys** collection has these methods.



| Method                                          | Description                                                     |
|:------------------------------------------------|:----------------------------------------------------------------|
| [**AddItem**](cluscryptokeys-additem.md)       | Adds an object to the **ClusCryptoKeys** collection.<br/> |
| [**Refresh**](cluscryptokeys-refresh.md)       | Refreshes the data in the collection.<br/>                |
| [**RemoveItem**](cluscryptokeys-removeitem.md) | Deletes an object from the collection.<br/>               |



 

### Properties

The **ClusCryptoKeys** collection has these properties.



| Property                                              | Access type          | Description                                                 |
|:------------------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**Count**](cluscryptokeys-count.md)<br/>      | Read-only<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](clusresgroupresources-item.md)<br/> | Read-only<br/> | Returns a single object from the collection.<br/>     |



 

## Remarks

A **ClusCryptoKeys** collection:

-   Contains crypto keys (registry keys) as strings.
-   Is obtained from [**ClusResource.CryptoKeys**](clusresource-cryptokeys.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusCryptoKeys is defined as F2E6072C-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[Property Management Objects](property-management-objects.md)
</dt> </dl>

 

 





