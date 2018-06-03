---
title: ClusPropertyValue object
description: Represents a single property value associated with a multi-value property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6a8ffae6-c4f3-42fb-9703-eeb695902877
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusPropertyValue object Failover Cluster
- ClusPropertyValue object Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusPropertyValue
- ISClusPropertyValue
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusPropertyValue object

\[The **ClusPropertyValue** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Represents a single [*property value*](https://www.bing.com/search?q=*property value*) associated with a multi-value property. The property value consists of one or more [*data values*](https://www.bing.com/search?q=*data values*).

## Members

The **ClusPropertyValue** object has these types of members:

-   [Properties](#properties)

### Properties

The **ClusPropertyValue** object has these properties.



| Property                                                     | Description                                                                                                                                                 |
|:-------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Data**](cluspropertyvalue-data.md)<br/>            | Returns a [**ClusPropertyValueData**](cluspropertyvaluedata-collection.md) collection containing all of the data values for the property value.<br/> |
| [**Format**](cluspropertyvalue-format.md)<br/>        | Returns or sets the format of the property value.<br/>                                                                                                |
| [**Length**](cluspropertyvalue-length.md)<br/>        | Returns the byte size of the property value.<br/>                                                                                                     |
| [**Type**](cluspropertyvalue-type.md)<br/>            | Returns or sets the type of the property value.<br/>                                                                                                  |
| [**Value**](cluspropertyvalue-value.md)<br/>          | Returns or sets the value of the property value.<br/>                                                                                                 |
| [**ValueCount**](cluspropertyvalue-datacount.md)<br/> | Returns the number of data values associated with the property value.<br/>                                                                            |



 

## Remarks

A **ClusPropertyValue** object can only be obtained from [**ClusPropertyValues.Item**](cluspropertyvalues-item.md).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>              |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>  |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>  |
| IID<br/>                      | IID\_ISClusPropertyValue is defined as F2E6071A-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Property Management Objects](property-management-objects.md)
</dt> </dl>

 

 





