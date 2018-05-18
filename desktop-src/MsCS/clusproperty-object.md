---
title: ClusProperty object
description: Represents a single property within a ClusProperties collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8c285882-915c-45de-9840-cfc5becd55ee'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusProperty object Failover Cluster", "ClusProperty object Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusProperty
- ISClusProperty
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusProperty object

\[The **ClusProperty** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Represents a single property within a [**ClusProperties**](clusproperties-collection.md) collection.

## Members

The **ClusProperty** object has these types of members:

-   [Properties](#properties)

### Properties

The **ClusProperty** object has these properties.



| Property                                                 | Description                                                                                                                                                                                 |
|:---------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Format**](clusproperty-format.md)<br/>         | Returns or sets the format of the [cluster object property](cluster-object-properties.md).<br/>                                                                                      |
| [**Length**](clusproperty-length.md)<br/>         | Returns the byte size of the cluster object property.<br/>                                                                                                                            |
| [**Modified**](clusproperty-modified.md)<br/>     | Indicates whether the value of the property has changed since the last [**Refresh**](clusproperties-refresh.md) or [**SaveChanges**](clusproperties-savechanges.md) operation.<br/> |
| [**Name**](clusproperty-name.md)<br/>             | Returns the name of the cluster object property.<br/>                                                                                                                                 |
| [**Type**](clusproperty-type.md)<br/>             | Returns or sets the type of the cluster object property.<br/>                                                                                                                         |
| [**Value**](clusproperty-value.md)<br/>           | Returns or sets the [*property value*](p-gly.md#-wolf-property-value-gly) of the cluster object property.<br/>                                                                       |
| [**ValueCount**](clusproperty-valuecount.md)<br/> | Returns the number of property values stored in the cluster object property.<br/>                                                                                                     |
| [**Values**](clusproperty-values.md)<br/>         | Returns a [**ClusPropertyValues**](cluspropertyvalues-collection.md) collection containing all of the property values associated with the cluster object property.<br/>              |



 

## Remarks

A **ClusProperty** object contains a local copy of real property data stored in the cluster database. Changes to the **ClusProperty** object do not take effect in the [*cluster*](c-gly.md#-wolf-cluster-gly) until the parent [**ClusProperties.SaveChanges**](clusproperties-savechanges.md) method is invoked. Similarly, changes to the cluster database are not reflected in the object until the [**ClusProperties.Refresh**](clusproperties-refresh.md) method is called.

A **ClusProperty** object can only be obtained from a [**ClusProperties**](clusproperties-collection.md) collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperty is defined as F2E606FE-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[Property Management Objects](property-management-objects.md)
</dt> </dl>

 

 





