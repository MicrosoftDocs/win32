---
title: ClusPropertyValueData collection
description: All of the data values associated with a property value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d95a90f6-2a70-428b-aff3-3be9e9e66071
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusPropertyValueData collection Failover Cluster
- ClusPropertyValueData collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusPropertyValueData
- ISClusPropertyValueData
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusPropertyValueData collection

\[The **ClusPropertyValueData** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains all of the [*data values*](p-gly.md#-wolf-property-value-gly) associated with a *property value*.

## Members

The **ClusPropertyValueData** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusPropertyValueData** collection has these methods.



| Method                                                 | Description                                                        |
|:-------------------------------------------------------|:-------------------------------------------------------------------|
| [**CreateItem**](cluspropertyvaluedata-createitem.md) | Creates a new data value and adds it to the collection.<br/> |
| [**RemoveItem**](cluspropertyvaluedata-removeitem.md) | Deletes a data value from the collection.<br/>               |



 

### Properties

The **ClusPropertyValueData** collection has these properties.



| Property                                                | Access type          | Description                                                     |
|:--------------------------------------------------------|:---------------------|:----------------------------------------------------------------|
| [**Count**](cluspropertyvaluedata-count.md)<br/> | Read-only<br/> | Returns the number of data values in the collection.<br/> |
| [**Item**](clusresgroupresources-item.md)<br/>   | Read-only<br/> | Returns a single data value from the collection.<br/>     |



 

## Remarks

A **ClusPropertyValueData** collection:

-   Contains data values.
-   Is obtained from [**ClusPropertyValue.Data**](cluspropertyvalue-data.md).

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                  |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>        |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>      |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>      |
| IID<br/>                      | IID\_ISClusPropertyValueData is defined as F2E6071E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Property Management Objects](property-management-objects.md)
</dt> </dl>

 

 





