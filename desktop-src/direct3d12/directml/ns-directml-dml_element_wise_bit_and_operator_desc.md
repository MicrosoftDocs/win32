---
UID: NS:directml.DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC
title: DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC
description: Computes the bitwise AND between each corresponding element of the input tensors, and writes the result into the output tensor.
helpviewer_keywords: ["DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC","DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC structure","direct3d12.dml_convolution_integer_operator_desc","directml/DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC"]
ms.topic: reference
tech.root: directml
ms.date: 11/09/2020
ms.keywords: DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC, DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC structure, direct3d12.dml_convolution_integer_operator_desc, directml/DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC
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
 - DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC
 - directml/DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC
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
 - DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC
---

# DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC structure (directml.h)

Computes the bitwise AND between each corresponding element of the input tensors, and writes the result into the output tensor.

The input and output tensor must have the same *DimensionCount*, *Sizes*, and *DataType*.

This operator supports in-place execution, meaning that the output tensor is permitted to alias one or more of the input tensors during binding.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/). Also see [DirectML version history](/windows/win32/direct3d12/dml-version-history).

## Syntax

```cpp
struct DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC
{
  const DML_TENSOR_DESC* ATensor;
  const DML_TENSOR_DESC* BTensor;
  const DML_TENSOR_DESC* OutputTensor;
};
```

## Members

`ATensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the left-hand side inputs.

`BTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the right-hand side inputs.

`OutputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The output tensor to write the results to.

## Availability
This operator was introduced in `DML_FEATURE_LEVEL_3_0`.

## Tensor constraints
*ATensor*, *BTensor*, and *OutputTensor* must have the same *DataType*, *DimensionCount*, and *Sizes*.

## Tensor support
| Tensor | Kind | Supported dimension counts | Supported data types |
| ------ | ---- | -------------------------- | -------------------- |
| ATensor | Input | 1 to 8 | UINT32, UINT16, UINT8 |
| BTensor | Input | 1 to 8 | UINT32, UINT16, UINT8 |
| OutputTensor | Output | 1 to 8 | UINT32, UINT16, UINT8 |

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |
