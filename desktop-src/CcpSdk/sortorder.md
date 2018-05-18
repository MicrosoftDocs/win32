---
Description: 'Defines the order in which the server returns the list.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8c27f57a-a172-4156-99b2-2ae400894b16'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: SortOrder enumeration
---

# SortOrder enumeration

Defines the order in which the server returns the list.

## Syntax


```C++
typedef enum  { 
  SortOrder_Ascending   = 0,
  SortOrder_Descending  = 1
} SortOrder;
```



## Constants

<dl> <dt>

<span id="SortOrder_Ascending"></span><span id="sortorder_ascending"></span><span id="SORTORDER_ASCENDING"></span>**SortOrder\_Ascending**
</dt> <dd>

The list is returned in ascending order.

</dd> <dt>

<span id="SortOrder_Descending"></span><span id="sortorder_descending"></span><span id="SORTORDER_DESCENDING"></span>**SortOrder\_Descending**
</dt> <dd>

The list is returned in descending order.

</dd> </dl>

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> <dt>

[**ISortCollection::Add**](isortcollection-add.md)
</dt> </dl>

 

 




