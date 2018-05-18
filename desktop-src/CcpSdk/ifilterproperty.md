---
Description: 'An opaque interface that defines a filter to use for filtering lists of jobs, tasks or nodes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a620ddae-5dc9-45bc-bb38-864153277760'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IFilterProperty interface
---

# IFilterProperty interface

An opaque interface that defines a filter to use for filtering lists of jobs, tasks or nodes.

To get this interface, use the [**IFilterCollection::GetEnumerator**](ifiltercollection-getenumerator.md) method to enumerate the filter properties or access the [**IFilterCollection::Item**](ifiltercollection-item.md) property.

## Members

The **IFilterProperty** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface but does not have additional members.

## Requirements



|                         |                                                                                                         |
|-------------------------|---------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                            |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**ISortProperty**](isortproperty.md)
</dt> </dl>

 

 




