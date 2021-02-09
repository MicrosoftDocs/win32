---
UID: NS:directml.DML_CUMULATIVE_SUMMATION_OPERATOR_DESC
title: DML_CUMULATIVE_SUMMATION_OPERATOR_DESC
description: Sums the elements of a tensor along an axis, writing the running tally of the summation into the output tensor.
helpviewer_keywords: ["DML_CUMULATIVE_SUMMATION_OPERATOR_DESC","DML_CUMULATIVE_SUMMATION_OPERATOR_DESC structure","direct3d12.dml_cumulative_summation_operator_desc","directml/DML_CUMULATIVE_SUMMATION_OPERATOR_DESC"]
ms.topic: reference
tech.root: directml
ms.date: 10/29/2020
ms.keywords: DML_CUMULATIVE_SUMMATION_OPERATOR_DESC, DML_CUMULATIVE_SUMMATION_OPERATOR_DESC structure, direct3d12.dml_cumulative_summation_operator_desc, directml/DML_CUMULATIVE_SUMMATION_OPERATOR_DESC
req.header: directml.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
f1_keywords:
 - DML_CUMULATIVE_SUMMATION_OPERATOR_DESC
 - directml/DML_CUMULATIVE_SUMMATION_OPERATOR_DESC
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - HeaderDef
api_location:
 - DirectML.h
api_name:
 - DML_CUMULATIVE_SUMMATION_OPERATOR_DESC
---

# DML_CUMULATIVE_SUMMATION_OPERATOR_DESC structure (directml.h)

Sums the elements of a tensor along an axis, writing the running tally of the summation into the output tensor.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/). Also see [DirectML version history](../dml-version-history.md).

## Syntax
```cpp
struct DML_CUMULATIVE_SUMMATION_OPERATOR_DESC {
  const DML_TENSOR_DESC *InputTensor;
  const DML_TENSOR_DESC *OutputTensor;
  UINT                  Axis;
  DML_AXIS_DIRECTION    AxisDirection;
  BOOL                  HasExclusiveSum;
};
```



## Members

`InputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The input tensor containing elements to be summed.


`OutputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The output tensor to write the resulting cumulative summations to. This tensor must have the same sizes and data type as the *InputTensor*.


`Axis`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The index of the dimension to sum elements over. This value must be less than the *DimensionCount* of the *InputTensor*.


`AxisDirection`

Type: **[DML_AXIS_DIRECTION](./ne-directml-dml_axis_direction.md)**

One of the values of the [DML_AXIS_DIRECTION](./ne-directml-dml_axis_direction.md) enumeration. If set to **DML_AXIS_DIRECTION_INCREASING**, then the summation occurs by traversing the tensor along the specified axis by ascending element index. If set to **DML_AXIS_DIRECTION_DECREASING**, the reverse is true, and the summation occurs by traversing elements by descending index.


`HasExclusiveSum`




## Remarks
This operator supports in-place execution, meaning that the *OutputTensor* is permitted to alias the *InputTensor* during binding.

## Availability
This operator was introduced in `DML_FEATURE_LEVEL_2_1`.

## Tensor constraints
*InputTensor* and *OutputTensor* must have the same *DataType* and *Sizes*.

## Tensor support
| Tensor | Kind | Supported dimension counts | Supported data types |
| ------ | ---- | -------------------------- | -------------------- |
| InputTensor | Input | 4 | FLOAT32, FLOAT16, UINT32, UINT16 |
| OutputTensor | Output | 4 | FLOAT32, FLOAT16, UINT32, UINT16 |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |