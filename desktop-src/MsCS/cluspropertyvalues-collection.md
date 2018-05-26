---
title: ClusPropertyValues collection
description: Contains all of the property values associated with a multi-value property, with each value represented by a ClusPropertyValue object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 18ae71ee-5582-4ac9-bb0f-f1c077c0352a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusPropertyValues collection Failover Cluster
- ClusPropertyValues collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusPropertyValues
- ISClusPropertyValues
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusPropertyValues collection

\[The **ClusPropertyValues** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains all of the [*property values*](p-gly.md#-wolf-property-value-gly) associated with a multi-value property, with each value represented by a [**ClusPropertyValue**](cluspropertyvalue-object.md) object.

## Members

The **ClusPropertyValues** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusPropertyValues** collection has these methods.



| Method                                              | Description                                              |
|:----------------------------------------------------|:---------------------------------------------------------|
| [**CreateItem**](cluspropertyvalues-createitem.md) | Adds a property value to the collection.<br/>      |
| [**RemoveItem**](cluspropertyvalues-removeitem.md) | Deletes a property value from the collection.<br/> |



 

### Properties

The **ClusPropertyValues** collection has these properties.



| Property                                              | Access type          | Description                                                         |
|:------------------------------------------------------|:---------------------|:--------------------------------------------------------------------|
| [**Count**](cluspropertyvalues-count.md)<br/>  | Read-only<br/> | Returns the number of property values in the collection.<br/> |
| [**Item**](clusresgroupresources-item.md)<br/> | Read-only<br/> | Returns a single property value from the collection.<br/>     |



 

## Remarks

A **ClusPropertyValues** collection:

-   Contains [**ClusPropertyValue**](cluspropertyvalue-object.md) objects.
-   Is obtained from [**ClusProperty.Values**](clusproperty-values.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>               |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>   |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>   |
| IID<br/>                      | IID\_ISClusPropertyValues is defined as F2E6071C-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Property Management Objects](property-management-objects.md)
</dt> </dl>

 

 





