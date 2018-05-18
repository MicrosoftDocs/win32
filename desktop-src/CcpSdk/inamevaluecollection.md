---
Description: 'Represents a collection of name/value pairs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4f2e2c32-1696-4e00-af2d-c705b62a5183'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: INameValueCollection interface
---

# INameValueCollection interface

Represents a collection of name/value pairs.

Collections returned by the CCP API are read-only. CCP uses the methods that modify the collection.

The following methods return this interface:

-   [**ICluster::get\_EnvironmentVariables**](icluster-get-environmentvariables.md)
-   [**ICluster::get\_Parameters**](icluster-get-parameters.md)
-   [**IJob:get\_ExtendedJobTerms**](ijob-get-extendedjobterms.md)
-   [**ITask::get\_EnvironmentVariables**](itask-get-environmentvariables.md)
-   [**ITask::get\_ExtendedTaskTerms**](itask-get-extendedtaskterms.md)

## Members

The **INameValueCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INameValueCollection** also has these types of members:

-   [Methods](#methods)

### Methods

The **INameValueCollection** interface has these methods.



| Method                                                      | Description                                                                                          |
|:------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**Add**](inamevaluecollection-add.md)                     | Adds a name/value pair to the end of the collection.<br/>                                      |
| [**Clear**](inamevaluecollection-clear.md)                 | Removes all name/value pairs from the collection.<br/>                                         |
| [**Clone**](inamevaluecollection-clone.md)                 | Creates an identical copy of the collection.<br/>                                              |
| [**get\_Count**](inamevaluecollection-get-count.md)        | Retrieves the number of items in the collection.<br/>                                          |
| [**GetEnumerator**](inamevaluecollection-getenumerator.md) | Retrieves an enumerator that you use to enumerate the name/value pairs in the collection.<br/> |
| [**Insert**](inamevaluecollection-insert.md)               | Adds a name/value pair to the collection at the specified index.<br/>                          |
| [**Remove**](inamevaluecollection-remove.md)               | Removes a name/value pair from the collection.<br/>                                            |
| [**RemoveAt**](inamevaluecollection-removeat.md)           | Removes the name/value pair at the specified index from the collection.<br/>                   |
| [**Set**](inamevaluecollection-set.md)                     | Creates a name/value pair and adds it to the collection.<br/>                                  |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**INameValue**](inamevalue.md)
</dt> <dt>

[CCP Interfaces](interfaces.md)
</dt> </dl>

 

 




