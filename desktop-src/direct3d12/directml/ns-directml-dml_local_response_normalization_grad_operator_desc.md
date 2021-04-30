---
UID: NS:directml.DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC
title: DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC
description: Computes backpropagation gradients for [local response normalization](/windows/win32/api/directml/ns-directml-dml_local_response_normalization_operator_desc).
helpviewer_keywords: ["DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC","DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC structure","direct3d12.dml_local_response_normalization_grad_operator_desc","directml/DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC"]
ms.topic: reference
tech.root: directml
ms.date: 03/15/2021
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
 - DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC
 - directml/DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC
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
 - DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC
---

# DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC (directml.h)

Computes backpropagation gradients for [local response normalization](/windows/win32/api/directml/ns-directml-dml_local_response_normalization_operator_desc).

The data type and size of all tensors must be the same.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.5 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax
```cpp
struct DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC
{
    const DML_TENSOR_DESC* InputTensor;
    const DML_TENSOR_DESC* InputGradientTensor;
    const DML_TENSOR_DESC* OutputGradientTensor;
    BOOL CrossChannel;
    UINT LocalSize;
    FLOAT Alpha;
    FLOAT Beta;
    FLOAT Bias;
};
```

## Members

`InputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The tensor containing the input data. This tensor's *Sizes* should be `{ BatchCount, ChannelCount, Height, Width }`.

`InputGradientTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The incoming gradient tensor. This is typically obtained from the output of backpropagation of a preceding layer.

`OutputGradientTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An output tensor containing the backpropagated gradients.

`CrossChannel`

Type: **[BOOL](/windows/win32/winprog/windows-data-types)**

**TRUE** if the LRN layer sums across channels; **FALSE** if the LRN layer sums across spatial dimensions.

`LocalSize`

Type: **[UINT](/windows/win32/winprog/windows-data-types)**

The maximum number of elements to sum over per dimension (the local region is clipped so that all elements are within bounds). If *CrossChannel* is **TRUE**, then this is the width and height of the local region. If *CrossChannel* is **FALSE**, then this is the number of elements in the local region. This value must be at least 1.

`Alpha`

Type: **[FLOAT](/windows/win32/winprog/windows-data-types)**

The value of the scaling parameter. We recommend a value of 0.0001 as default.

`Beta`

Type: **[FLOAT](/windows/win32/winprog/windows-data-types)**

The value of the exponent. We recommend a value of 0.75 as default.

`Bias`

Type: **[FLOAT](/windows/win32/winprog/windows-data-types)**

The value of bias. We recommend a value of 1 as default.

## Availability
This operator was introduced in `DML_FEATURE_LEVEL_3_1`.

## Tensor constraints
*InputGradientTensor*, *InputTensor*, and *OutputGradientTensor* must have the same *DataType* and *Sizes*.

## Tensor support
| Tensor | Kind | Supported dimension counts | Supported data types |
| ------ | ---- | -------------------------- | -------------------- |
| InputTensor | Input | 4 | FLOAT32, FLOAT16 |
| InputGradientTensor | Input | 4 | FLOAT32, FLOAT16 |
| OutputGradientTensor | Output | 4 | FLOAT32, FLOAT16 |

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |
