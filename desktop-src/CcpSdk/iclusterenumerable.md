---
Description: 'Represents a collection of objects. Many of the CCP API methods return collections. For example, the ICluster::ListJobs method returns a collection of jobs for a specified user.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '00c88d34-ae9f-4bb9-803c-fa4793add944'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IClusterEnumerable interface
---

# IClusterEnumerable interface

Represents a collection of objects. Many of the CCP API methods return collections. For example, the [**ICluster::ListJobs**](icluster-listjobs.md) method returns a collection of jobs for a specified user.

To enumerate the objects in the collection, call the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method to get an [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface pointer. Use the **IEnumVARIANT::Next** method to enumerate the items of the collection. Each item in the collection is a variant whose type is VT\_DISPATCH. Query the **pdispVal** member of the variant to get the interface to the object. For example, if you called [**ListJobs**](icluster-listjobs.md), you would query **pdispVal** for the [**IJob**](ijob.md) interface.

This interface is also used to build a collection of objects (for example, when calling the [**ICluster::AddJobs**](icluster-addjobs.md) method). To create an instance of this object for building a collection, call the [**ICluster::CreateClusterEnumerable**](icluster-createclusterenumerable.md) method.

## Members

The **IClusterEnumerable** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IClusterEnumerable** also has these types of members:

-   [Methods](#methods)

### Methods

The **IClusterEnumerable** interface has these methods.



| Method                                                       | Description                                                                               |
|:-------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**Add**](iclusterenumerable-add.md)                        | Adds an object to the collection.<br/>                                              |
| [**get\_IsReadOnly**](iclusterenumerable-get-isreadonly.md) | Indicates whether the collection is read-only.<br/>                                 |
| [**GetEnumerator**](iclusterenumerable-getenumerator.md)    | Retrieves an enumerator that you use to enumerate the items of the collection.<br/> |
| [**Remove**](iclusterenumerable-remove.md)                  | Removes an object from the collection.<br/>                                         |



 

## Examples

For an example that enumerates the items in a collection, see [Listing Jobs](listing-jobs.md). For an example that builds a collection, see the second example in [Submitting a Job to the Scheduling Queue](submitting-a-job-to-the-scheduling-queue.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[CCP Interfaces](interfaces.md)
</dt> </dl>

 

 




