---
UID: NS:directml.DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC
title: DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC
description: Fills a tensor with a sequence.
helpviewer_keywords: ["DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC","DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC structure","direct3d12.dml_fill_value_sequence_operator_desc","directml/DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC"]
ms.topic: reference
tech.root: directml
ms.date: 10/30/2020
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
 - DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC
 - directml/DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC
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
 - DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC
---

# DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC structure (directml.h)

Fills a tensor with a sequence. This operator performs the following pseudocode.

```
for each coordinate in OutputTensor
    OutputTensor[coordinate] = Value
    Value += Delta
endfor
```

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.4 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax
```cpp
struct DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC {
  const DML_TENSOR_DESC *OutputTensor;
  DML_TENSOR_DATA_TYPE  ValueDataType;
  DML_SCALAR_UNION      ValueStart;
  DML_SCALAR_UNION      ValueDelta;
};
```



## Members

`OutputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The tensor to write the results to. This tensor may have any size.


`ValueDataType`

Type: **[DML_TENSOR_DATA_TYPE](/windows/win32/api/directml/ne-directml-dml_tensor_data_type)**

The data type of *Value* field, which must match *OutputTensor.DataType*.


`ValueStart`

Type: **[DML_SCALAR_UNION](./ns-directml-dml_scalar_union.md)**

The initial value to fill the first element in the output, with *ValueDataType* determining how to interpret the field.


`ValueDelta`

Type: **[DML_SCALAR_UNION](./ns-directml-dml_scalar_union.md)**

A step to add to the value for each element written, with *ValueDataType* determining how to interpret the field.

## Examples

### Example 1. 1D ascending step

```
ValueStart = 3
ValueDelta = 2
ValueDataType = DML_TENSOR_DATA_TYPE_FLOAT32

OutputTensor: (Sizes:{1,1,1,3}, DataType:FLOAT32)
    [[[[3, 5, 7]]]]
```

### Example 2. 2D ascending step

```
ValueStart = 10
ValueDelta = -2
ValueDataType = DML_TENSOR_DATA_TYPE_UINT8

OutputTensor: (Sizes:{1,1,2,2}, DataType:UINT8)
    [[[[10, 8],
       [ 6, 4]]]]
```

## Availability
This operator was introduced in `DML_FEATURE_LEVEL_2_1`.

## Tensor support
| Tensor | Kind | Supported dimension counts | Supported data types |
| ------ | ---- | -------------------------- | -------------------- |
| OutputTensor | Output | 4 | FLOAT32, FLOAT16, INT32, INT16, INT8, UINT32, UINT16, UINT8 |



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |