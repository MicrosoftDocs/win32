---
UID: NS:directml.DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC
title: DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC
description: Computes backpropagation gradients for [batch normalization](/windows/win32/api/directml/ns-directml-dml_batch_normalization_operator_desc).
helpviewer_keywords: ["DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC","DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC structure","direct3d12.dml_batch_normalization_grad_operator_desc","directml/DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC"]
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
 - DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC
 - directml/DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC
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
 - DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC
---

# DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC (directml.h)

Computes backpropagation gradients for [batch normalization](/windows/win32/api/directml/ns-directml-dml_batch_normalization_operator_desc). **DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC** performs multiple computations, which are detailed in the separate output descriptions.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.5 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax
```cpp
struct DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC
{
    const DML_TENSOR_DESC* InputTensor;
    const DML_TENSOR_DESC* InputGradientTensor;
    const DML_TENSOR_DESC* MeanTensor;
    const DML_TENSOR_DESC* VarianceTensor;
    const DML_TENSOR_DESC* ScaleTensor;

    const DML_TENSOR_DESC* OutputGradientTensor;
    const DML_TENSOR_DESC* OutputScaleGradientTensor;
    const DML_TENSOR_DESC* OutputBiasGradientTensor;

    FLOAT Epsilon;
};
```

## Members

`InputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the input data. This is typically the same tensor that was provided as the *InputTensor* to [**DML_BATCH_NORMALIZATION_OPERATOR_DESC**](/windows/win32/api/directml/ns-directml-dml_batch_normalization_operator_desc) in the forward pass.

`InputGradientTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The incoming gradient tensor. This is typically obtained from the output of backpropagation of a preceding layer. This tensor must have the same dimension sizes as *InputTensor*.

`MeanTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the mean data. This is typically the same tensor that was provided as the *MeanTensor* to [**DML_BATCH_NORMALIZATION_OPERATOR_DESC**](/windows/win32/api/directml/ns-directml-dml_batch_normalization_operator_desc) in the forward pass.

Any dimensions that don't have the same size as the corresponding dimension of *InputTensor* must have a size of 1 so that they can be broadcast to match the input.

For example, the following sizes are acceptable.

```
InputTensor: [3, 4, 5, 6]  
MeanTensor : [1, 4, 1, 1] or [3, 4, 1, 1] or [3, 4, 5, 1] or [3, 4, 5, 6] or [1, 1, 1, 1]
```

The following is an error since, in order to be broadcast compatible, any dimensions that don't match must be size 1.

```
InputTensor: [3, 4, 5, 6]  
MeanTensor : [1, 2, 1, 1]  // 2 causes an error.
```

`VarianceTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the variance data. This is typically the same tensor that was provided as the *VarianceTensor* to [**DML_BATCH_NORMALIZATION_OPERATOR_DESC**](/windows/win32/api/directml/ns-directml-dml_batch_normalization_operator_desc) in the forward pass. This tensor must have the same dimension sizes as *MeanTensor*.

`ScaleTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the scale data. This is typically the same tensor that was provided as the *ScaleTensor* to [**DML_BATCH_NORMALIZATION_OPERATOR_DESC**](/windows/win32/api/directml/ns-directml-dml_batch_normalization_operator_desc) in the forward pass. This tensor must have the same dimension sizes as *MeanTensor*.

`OutputGradientTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

For every corresponding value in the inputs,
`OutputGradient = InputGradient * (Scale / sqrt(Variance + Epsilon))`.

This tensor must have the same dimension sizes as *InputTensor*/*InputGradientTensor*.

`OutputScaleGradientTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

This tensor must have the same dimension sizes as *MeanTensor*/*VarianceTensor*/*ScaleTensor`*.

The following computation is done or every corresponding value in the inputs.

`OutputScaleGradient = sum(InputGradient * (Input - Mean) / sqrt(Variance + Epsilon))`

The `sum` is computed across any dimensions that need to be broadcast. If there is no broadcast needed, then no sum is needed.

Here's an example.

```
InputTensor              : [3, 4, 5, 6]  
MeanTensor               : [1, 4, 1, 1] // dimensions 0, 2, 3 needed broadcasting  
OutputScaleGradientTensor: [1, 4, 1, 1]  
```

Element [0, **0**, 0, 0] of `OutputScaleGradientTensor` is the sum of `(InputGradient * (Input - Mean) / sqrt(variance + Epsilon)` for all 90 (3\*5\*6) elements [[0,2], **0**, [0,4], [0,5]].

`OutputBiasGradientTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

This tensor must have the same dimension sizes as *MeanTensor*/*VarianceTensor*/*ScaleTensor`*.

The following computation is done or every corresponding value in the inputs.

`OutputBiasGradient = sum(InputGradient)`  

The `sum` is computed across any dimensions that need to be broadcast (see the example for *OutputScaleGradientTensor*). If there is no broadcast needed, then no sum is needed.

`Epsilon`

Type: **[FLOAT](../../winprog/windows-data-types.md)**

A small value added to the variance to avoid zero.

## Availability
This operator was introduced in `DML_FEATURE_LEVEL_3_1`.

## Tensor constraints
*InputGradientTensor*, *InputTensor*, *MeanTensor*, *OutputBiasGradientTensor*, *OutputGradientTensor*, *OutputScaleGradientTensor*, *ScaleTensor*, and *VarianceTensor* must have the same *DataType* and *DimensionCount*.

## Tensor support
| Tensor | Kind | Supported dimension counts | Supported data types |
| ------ | ---- | -------------------------- | -------------------- |
| InputTensor | Input | 1 to 8 | FLOAT32, FLOAT16 |
| InputGradientTensor | Input | 1 to 8 | FLOAT32, FLOAT16 |
| MeanTensor | Input | 1 to 8 | FLOAT32, FLOAT16 |
| VarianceTensor | Input | 1 to 8 | FLOAT32, FLOAT16 |
| ScaleTensor | Input | 1 to 8 | FLOAT32, FLOAT16 |
| OutputGradientTensor | Output | 1 to 8 | FLOAT32, FLOAT16 |
| OutputScaleGradientTensor | Output | 1 to 8 | FLOAT32, FLOAT16 |
| OutputBiasGradientTensor | Output | 1 to 8 | FLOAT32, FLOAT16 |

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |