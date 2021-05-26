---
UID: NS:directml.DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC
title: DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC
description: Performs a convolution of the *FilterTensor* with the *InputTensor*. This operator performs forward convolution on quantized data. This operator is mathematically equivalent to dequantizing the inputs, convolving, and then quantizing the output.
helpviewer_keywords: ["DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC","DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC structure","direct3d12.dml_quantized_linear_convolution_operator_desc","directml/DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC"]
ms.topic: reference
tech.root: directml
ms.date: 11/03/2020
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
 - DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC
 - directml/DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC
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
 - DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC
---

# DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC structure (directml.h)
Performs a convolution of the *FilterTensor* with the *InputTensor*. This operator performs forward convolution on quantized data. This operator is mathematically equivalent to dequantizing the inputs, convolving, and then quantizing the output. 

The quantize linear functions used by this operator are the linear quantization functions

### Dequantize function

```
f(Input, Scale, ZeroPoint) = (Input - ZeroPoint) * Scale
```

### Quantize function

```
f(Input, Scale, ZeroPoint) = clamp(round(Input / Scale) + ZeroPoint, Min, Max)
```

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.4 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax
```cpp
struct DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC {
  const DML_TENSOR_DESC *InputTensor;
  const DML_TENSOR_DESC *InputScaleTensor;
  const DML_TENSOR_DESC *InputZeroPointTensor;
  const DML_TENSOR_DESC *FilterTensor;
  const DML_TENSOR_DESC *FilterScaleTensor;
  const DML_TENSOR_DESC *FilterZeroPointTensor;
  const DML_TENSOR_DESC *BiasTensor;
  const DML_TENSOR_DESC *OutputScaleTensor;
  const DML_TENSOR_DESC *OutputZeroPointTensor;
  const DML_TENSOR_DESC *OutputTensor;
  UINT                  DimensionCount;
  const UINT            *Strides;
  const UINT            *Dilations;
  const UINT            *StartPadding;
  const UINT            *EndPadding;
  UINT                  GroupCount;
};
```



## Members

`InputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the input data. The expected dimensions of the *InputTensor* are `{ InputBatchCount, InputChannelCount, InputHeight, InputWidth }`.


`InputScaleTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the input scale data. The expected dimensions of the `InputScaleTensor` are `{ 1, 1, 1, 1 }`. This scale value is used for dequantizing the input values.


`InputZeroPointTensor`

Type: _Maybenull\_ **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An optional tensor containing the input zero point data. The expected dimensions of the *InputZeroPointTensor* are `{ 1, 1, 1, 1 }`. This zero point value is used for dequantizing the input values.


`FilterTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the filter data. The expected dimensions of the *FilterTensor* are `{ FilterBatchCount, FilterChannelCount, FilterHeight, FilterWidth }`.


`FilterScaleTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the filter scale data. The expected dimensions of the `FilterScaleTensor` are `{ 1, 1, 1, 1 }` if per tensor quantization is required, or `{ 1, OutputChannelCount, 1, 1 }` if per channel quantization is required. This scale value is used for dequantizing the filter values.


`FilterZeroPointTensor`

Type: _Maybenull\_ **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An optional tensor containing the filter zero point data. The expected dimensions of the *FilterZeroPointTensor* are `{ 1, 1, 1, 1 }` if per tensor quantization is required, or `{ 1, OutputChannelCount, 1, 1 }` if per channel quantization is required. This zero point value is used for dequantizing the filter values.


`BiasTensor`

Type: \_Maybenull\_ **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the bias data. The bias tensor is a tensor containing data which is broadcasted across the output tensor at the end of the convolution which is added to the result. The expected dimensions of the BiasTensor are `{ 1, OutputChannelCount, 1, 1 }` for 4D.


`OutputScaleTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the output scale data. The expected dimensions of the OutputScaleTensor are `{ 1, 1, 1, 1 }`. This input scale value is used for quantizing the convolution output values.


`OutputZeroPointTensor`

Type: _Maybenull\_ **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An optional tensor containing the filter zero point data. The expected dimensions of the OutputZeroPointTensor are `{ 1, 1, 1, 1 }`. This input zero point value is used for quantizing the convolution the output values.


`OutputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor to write the results to. The expected dimensions of the OutputTensor are `{ OutputBatchCount, OutputChannelCount, OutputHeight, OutputWidth }`.


`DimensionCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of spatial dimensions for the convolution operation. Spatial dimensions are the lower dimensions of the convolution filter tensor *FilterTensor*. This value also determines the size of the *Strides*, *Dilations*, *StartPadding*, and *EndPadding* arrays. Only a value of 2 is supported.


`Strides`

Type: \_Field_size\_(DimensionCount) **const [UINT](../../winprog/windows-data-types.md)\***

The strides of the convolution operation. These strides are applied to the convolution filter. They are separate from the tensor strides included in [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc).


`Dilations`

Type: \_Field_size\_(DimensionCount) **const [UINT](../../winprog/windows-data-types.md)\***

The Dilations of the convolution operation. Dilations are strides applied to the elements of the filter kernel. This has the effect of simulating a larger filter kernel by padding the internal filter kernel elements with zeros.


`StartPadding`

Type: \_Field_size\_(DimensionCount) **const [UINT](../../winprog/windows-data-types.md)\***

The padding values to be applied to the beginning of each spatial dimension of the filter and input tensor of the convolution operation.


`EndPadding`

Type: \_Field_size\_(DimensionCount) **const [UINT](../../winprog/windows-data-types.md)\***

The padding values to be applied to the end of each spatial dimension of the filter and input tensor of the convolution operation.


`GroupCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of groups which to divide the convolution operation into. *GroupCount* can be used to achieve depth-wise convolution by setting the *GroupCount* equal to the input channel count. This divides the convolution up into a separate convolution per input channel. 

## Availability
This operator was introduced in `DML_FEATURE_LEVEL_2_1`.

## Tensor constraints
* *FilterTensor* and *FilterZeroPointTensor* must have the same *DataType*.
* *InputTensor* and *InputZeroPointTensor* must have the same *DataType*.
* *OutputTensor* and `OutputZeroPointTensor` must have the same *DataType*.

## Tensor support
| Tensor | Kind | Supported dimension counts | Supported data types |
| ------ | ---- | -------------------------- | -------------------- |
| InputTensor | Input | 4 | INT8, UINT8 |
| InputScaleTensor | Input | 4 | FLOAT32 |
| InputZeroPointTensor | Optional input | 4 | INT8, UINT8 |
| FilterTensor | Input | 4 | INT8, UINT8 |
| FilterScaleTensor | Input | 4 | FLOAT32 |
| FilterZeroPointTensor | Optional input | 4 | INT8, UINT8 |
| BiasTensor | Optional input | 4 | INT32 |
| OutputScaleTensor | Input | 4 | FLOAT32 |
| OutputZeroPointTensor | Optional input | 4 | INT8, UINT8 |
| OutputTensor | Output | 4 | INT8, UINT8 |



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |