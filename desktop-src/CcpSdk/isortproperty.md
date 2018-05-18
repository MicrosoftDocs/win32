---
Description: 'An opaque interface that defines the sort order used when returning lists of jobs, tasks, or nodes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2804538b-ed45-4f14-a525-27352c9f96b4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISortProperty interface
---

# ISortProperty interface

An opaque interface that defines the sort order used when returning lists of jobs, tasks, or nodes.

To get this interface, use the [**ISortCollection::GetEnumerator**](isortcollection-getenumerator.md) method to enumerate the filter properties or access the [**ISortCollection::Item**](isortcollection-item.md) property.

## Members

The **ISortProperty** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface but does not have additional members.

## Requirements



|                         |                                                                                                         |
|-------------------------|---------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                            |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**IFilterProperty**](ifilterproperty.md)
</dt> </dl>

 

 




