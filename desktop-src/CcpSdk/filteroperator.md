---
Description: 'Defines the operator used to compare the property value to the filter value.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '77fdff93-3e14-4114-badd-a8cb04375b06'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: FilterOperator enumeration
---

# FilterOperator enumeration

Defines the operator used to compare the property value to the filter value.

## Syntax


```C++
typedef enum  { 
  FilterOperator_GreaterThan         = 0,
  FilterOperator_GreaterThanOrEqual  = 1,
  FilterOperator_LessThan            = 2,
  FilterOperator_LessThanOrEqual     = 3,
  FilterOperator_Equal               = 4,
  FilterOperator_NotEqual            = 5,
  FilterOperator_HasBitSet           = 6,
  FilterOperator_HasNoBitSet         = 7,
  FilterOperator_IsNull              = 8,
  FilterOperator_IsNotNull           = 9,
  FilterOperator_HasExclusiveBitSet  = 10,
  FilterOperator_In                  = 11,
  FilterOperator_StartWith           = 12
} FilterOperator;
```



## Constants

<dl> <dt>

<span id="FilterOperator_GreaterThan"></span><span id="filteroperator_greaterthan"></span><span id="FILTEROPERATOR_GREATERTHAN"></span>**FilterOperator\_GreaterThan**
</dt> <dd>

Include the object in the result if the property value is greater than the filter value.

</dd> <dt>

<span id="FilterOperator_GreaterThanOrEqual"></span><span id="filteroperator_greaterthanorequal"></span><span id="FILTEROPERATOR_GREATERTHANOREQUAL"></span>**FilterOperator\_GreaterThanOrEqual**
</dt> <dd>

Include the object in the result if the property value is greater than or equal to the filter value.

</dd> <dt>

<span id="FilterOperator_LessThan"></span><span id="filteroperator_lessthan"></span><span id="FILTEROPERATOR_LESSTHAN"></span>**FilterOperator\_LessThan**
</dt> <dd>

Include the object in the result if the property value is less than the filter value.

</dd> <dt>

<span id="FilterOperator_LessThanOrEqual"></span><span id="filteroperator_lessthanorequal"></span><span id="FILTEROPERATOR_LESSTHANOREQUAL"></span>**FilterOperator\_LessThanOrEqual**
</dt> <dd>

Include the object in the result if the property value is less than or equal to the filter value.

</dd> <dt>

<span id="FilterOperator_Equal"></span><span id="filteroperator_equal"></span><span id="FILTEROPERATOR_EQUAL"></span>**FilterOperator\_Equal**
</dt> <dd>

Include the object in the result if the property value equals the filter value.

</dd> <dt>

<span id="FilterOperator_NotEqual"></span><span id="filteroperator_notequal"></span><span id="FILTEROPERATOR_NOTEQUAL"></span>**FilterOperator\_NotEqual**
</dt> <dd>

Include the object in the result if the property value is not equal to the filter value.

</dd> <dt>

<span id="FilterOperator_HasBitSet"></span><span id="filteroperator_hasbitset"></span><span id="FILTEROPERATOR_HASBITSET"></span>**FilterOperator\_HasBitSet**
</dt> <dd>

Include the object in the result if the property value has one or more bits set. For example, you can use this operator to test if the state of the job is failed or canceled by using the bitwise **OR** to set the filter value to both states.

</dd> <dt>

<span id="FilterOperator_HasNoBitSet"></span><span id="filteroperator_hasnobitset"></span><span id="FILTEROPERATOR_HASNOBITSET"></span>**FilterOperator\_HasNoBitSet**
</dt> <dd>

Include the object in the result if the property value has no bits set.

</dd> <dt>

<span id="FilterOperator_IsNull"></span><span id="filteroperator_isnull"></span><span id="FILTEROPERATOR_ISNULL"></span>**FilterOperator\_IsNull**
</dt> <dd>

Include the object in the result if the property value is null.

</dd> <dt>

<span id="FilterOperator_IsNotNull"></span><span id="filteroperator_isnotnull"></span><span id="FILTEROPERATOR_ISNOTNULL"></span>**FilterOperator\_IsNotNull**
</dt> <dd>

Include the object in the result if the property value is not null.

</dd> <dt>

<span id="FilterOperator_HasExclusiveBitSet"></span><span id="filteroperator_hasexclusivebitset"></span><span id="FILTEROPERATOR_HASEXCLUSIVEBITSET"></span>**FilterOperator\_HasExclusiveBitSet**
</dt> <dd>

Include the object in the result if the property value has a single bit set.

</dd> <dt>

<span id="FilterOperator_In"></span><span id="filteroperator_in"></span><span id="FILTEROPERATOR_IN"></span>**FilterOperator\_In**
</dt> <dd>

Include the object in the result if the property value equals one of the values in a **SAFEARRAY** of filter values. This value is supported only for HPC Pack 2008 R2.

</dd> <dt>

<span id="FilterOperator_StartWith"></span><span id="filteroperator_startwith"></span><span id="FILTEROPERATOR_STARTWITH"></span>**FilterOperator\_StartWith**
</dt> <dd>

Include the object in the result if the property value starts with the filter value. This value is supported only for HPC Pack 2008 R2.

</dd> </dl>

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> <dt>

[**IFilterCollection::Add**](ifiltercollection-add.md)
</dt> </dl>

 

 




