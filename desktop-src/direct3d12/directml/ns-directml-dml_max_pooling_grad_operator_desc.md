---
UID: NS:directml.DML_MAX_POOLING_GRAD_OPERATOR_DESC
title: DML_MAX_POOLING_GRAD_OPERATOR_DESC
description: Computes backpropagation gradients for max pooling (see [DML_MAX_POOLING2_OPERATOR_DESC](./ns-directml-dml_max_pooling2_operator_desc.md)).
helpviewer_keywords: ["DML_MAX_POOLING_GRAD_OPERATOR_DESC","DML_MAX_POOLING_GRAD_OPERATOR_DESC structure","direct3d12.dml_convolution_integer_operator_desc","directml/DML_MAX_POOLING_GRAD_OPERATOR_DESC"]
ms.topic: reference
tech.root: directml
ms.date: 11/09/2020
ms.keywords: DML_MAX_POOLING_GRAD_OPERATOR_DESC, DML_MAX_POOLING_GRAD_OPERATOR_DESC structure, direct3d12.dml_convolution_integer_operator_desc, directml/DML_MAX_POOLING_GRAD_OPERATOR_DESC
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
 - DML_MAX_POOLING_GRAD_OPERATOR_DESC
 - directml/DML_MAX_POOLING_GRAD_OPERATOR_DESC
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
 - DML_MAX_POOLING_GRAD_OPERATOR_DESC
---

# DML_MAX_POOLING_GRAD_OPERATOR_DESC structure (directml.h)

Computes backpropagation gradients for max pooling (see [DML_MAX_POOLING2_OPERATOR_DESC](./ns-directml-dml_max_pooling2_operator_desc.md)).

Consider a 2x2 **DML_MAX_POOLING2_OPERATOR_DESC** without padding nor dilations and a stride of 1, which performs the following.

```
InputTensor             OutputTensor    IndicesTensor
[[1, 2, 3],   MaxPool    [[4, 4],        [[4, 4],
 [2, 4, 2],     -->       [6, 7]]         [7, 8]]
 [5, 6, 7]]
```

The largest element of each 2x2 window in the input tensor produces one element of the output. Below is an example of the output of **DML_MAX_POOLING_GRAD_OPERATOR_DESC**, given similar parameters.

```
InputTensor   InputGradientTensor            OutputGradientTensor
[[1, 2, 3],       [[1, 2],     MaxPoolGrad   [[0, 0, 0],
 [2, 4, 2],        [4, 5]]         -->        [0, 3, 0],
 [5, 6, 7]]                                   [0, 4, 5]]
```

In effect, this operator uses the *InputTensor* to determine the index of the largest element from each window, and distributes the values of *InputGradientTensor* into the *OutputGradientTensor* based on these indices. Where indices overlap, the values are summed. Any unreferenced output elements are zeroed.

In the case of a tie (where more than one element in a window has the same maximum value), the element with the lowest logical element index is chosen.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/). Also see [DirectML version history](../dml-version-history.md).

## Syntax

```cpp
struct DML_MAX_POOLING_GRAD_OPERATOR_DESC
{
  const DML_TENSOR_DESC* InputTensor;
  const DML_TENSOR_DESC* InputGradientTensor;
  const DML_TENSOR_DESC* OutputGradientTensor;
  UINT DimensionCount;
  _Field_size_(DimensionCount) const UINT* Strides;
  _Field_size_(DimensionCount) const UINT* WindowSize;
  _Field_size_(DimensionCount) const UINT* StartPadding;
  _Field_size_(DimensionCount) const UINT* EndPadding;
  _Field_size_(DimensionCount) const UINT* Dilations;
};
```

## Members

`InputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The input feature tensor. This is typically the same tensor that was provided as the *InputTensor* to [DML_MAX_POOLING2_OPERATOR_DESC](./ns-directml-dml_max_pooling2_operator_desc.md) in the forward pass.

`InputGradientTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The incoming gradient tensor. This is typically obtained from the output of backpropagation of a preceding layer. Typically this tensor would have the same sizes as the *output* of the corresponding [DML_MAX_POOLING2_OPERATOR_DESC](./ns-directml-dml_max_pooling2_operator_desc.md) in the forward pass.

`OutputGradientTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An output tensor containing the backpropagated gradients. Typically this tensor would have the same sizes as the *input* of the corresponding [DML_MAX_POOLING2_OPERATOR_DESC](./ns-directml-dml_max_pooling2_operator_desc.md) in the forward pass.

`DimensionCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of elements in the *Strides*, *WindowSize*, *StartPadding*, *EndPadding*, and *Dilations* arrays. This value must equal the spatial dimension count (InputTensor's DimensionCount - 2). As this operator only supports 4D tensors, the only valid value for this parameter is 2.

`Strides`

Type: \_Field\_size\_(DimensionCount) <b>const [UINT](/windows/desktop/winprog/windows-data-types)*</b>

See *Strides* in [DML_MAX_POOLING2_OPERATOR_DESC](./ns-directml-dml_max_pooling2_operator_desc.md).

`WindowSize`

Type: \_Field\_size\_(DimensionCount) <b>const [UINT](/windows/desktop/winprog/windows-data-types)*</b>

See *WindowSize* in [DML_MAX_POOLING2_OPERATOR_DESC](./ns-directml-dml_max_pooling2_operator_desc.md).

`StartPadding`

Type: \_Field\_size\_(DimensionCount) <b>const [UINT](/windows/desktop/winprog/windows-data-types)*</b>

See *StartPadding* in [DML_MAX_POOLING2_OPERATOR_DESC](./ns-directml-dml_max_pooling2_operator_desc.md).

`EndPadding`

Type: \_Field\_size\_(DimensionCount) <b>const [UINT](/windows/desktop/winprog/windows-data-types)*</b>

See *EndPadding* in [DML_MAX_POOLING2_OPERATOR_DESC](./ns-directml-dml_max_pooling2_operator_desc.md).

`Dilations`

Type: \_Field\_size\_(DimensionCount) <b>const [UINT](/windows/desktop/winprog/windows-data-types)*</b>

See *Dilations* in [DML_MAX_POOLING2_OPERATOR_DESC](./ns-directml-dml_max_pooling2_operator_desc.md).

## Availability
This operator was introduced in `DML_FEATURE_LEVEL_3_0`.

## Tensor constraints
* *InputTensor* and *OutputGradientTensor* must have the same *Sizes*.
* *InputGradientTensor*, *InputTensor*, and *OutputGradientTensor* must have the same *DataType*.

## Tensor support
| Tensor | Kind | Dimensions | Supported dimension counts | Supported data types |
| ------ | ---- | ---------- | -------------------------- | -------------------- |
| InputTensor | Input | { BatchCount, ChannelCount, InputHeight, InputWidth } | 4 | FLOAT32, FLOAT16 |
| InputGradientTensor | Input | { BatchCount, ChannelCount, OutputHeight, OutputWidth } | 4 | FLOAT32, FLOAT16 |
| OutputGradientTensor | Output | { BatchCount, ChannelCount, InputHeight, InputWidth } | 4 | FLOAT32, FLOAT16 |

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |