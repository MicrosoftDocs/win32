---
UID: NS:directml.DML_CONVOLUTION_INTEGER_OPERATOR_DESC
title: DML_CONVOLUTION_INTEGER_OPERATOR_DESC
description: Performs a convolution of the *FilterTensor* with the *InputTensor*. This operator performs forward convolution on integer data.
helpviewer_keywords: ["DML_CONVOLUTION_INTEGER_OPERATOR_DESC","DML_CONVOLUTION_INTEGER_OPERATOR_DESC structure","direct3d12.dml_convolution_integer_operator_desc","directml/DML_CONVOLUTION_INTEGER_OPERATOR_DESC"]
ms.topic: reference
tech.root: directml
ms.date: 10/29/2020
ms.keywords: DML_CONVOLUTION_INTEGER_OPERATOR_DESC, DML_CONVOLUTION_INTEGER_OPERATOR_DESC structure, direct3d12.dml_convolution_integer_operator_desc, directml/DML_CONVOLUTION_INTEGER_OPERATOR_DESC
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
 - DML_CONVOLUTION_INTEGER_OPERATOR_DESC
 - directml/DML_CONVOLUTION_INTEGER_OPERATOR_DESC
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
 - DML_CONVOLUTION_INTEGER_OPERATOR_DESC
---

# DML_CONVOLUTION_INTEGER_OPERATOR_DESC structure (directml.h)

Performs a convolution of the *FilterTensor* with the *InputTensor*. This operator performs forward convolution on integer data. Optional zero point tensors can also be used to subtract zero point values from the input and filter tensor.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.4 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax
```cpp
struct DML_CONVOLUTION_INTEGER_OPERATOR_DESC {
  const DML_TENSOR_DESC *InputTensor;
  const DML_TENSOR_DESC *InputZeroPointTensor;
  const DML_TENSOR_DESC *FilterTensor;
  const DML_TENSOR_DESC *FilterZeroPointTensor;
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

A tensor containing the input data. The expected dimensions of the *InputTensor* are `{ BatchCount, InputChannelCount, InputHeight, InputWidth }`.


`InputZeroPointTensor`

Type: \_Maybenull\_ **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An optional tensor containing the input zero point data. The expected dimensions of the *InputZeroPointTensor* are `{ 1, 1, 1, 1 }`.


`FilterTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the filter data. The expected dimensions of the *FilterTensor* are `{ FilterBatchCount, FilterChannelCount, FilterHeight, FilterWidth }`.


`FilterZeroPointTensor`

Type: \_Maybenull\_ **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An optional tensor containing the filter zero point data. The expected dimensions of the *FilterZeroPointTensor* are `{ 1, 1, 1, 1 }` if per tensor quantization is required, or `{ 1, OutputChannelCount, 1, 1 }` if per-channel quantization is required.


`OutputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The tensor to write the results to. The expected dimensions of the *OutputTensor* are `{ BatchCount, OutputChannelCount, OutputHeight, OutputWidth }`.


`DimensionCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of spatial dimensions for the convolution operation. Spatial dimensions are the lower dimensions of the convolution *FilterTensor*. This value also determines the size of the *Strides*, *Dilations*, *StartPadding*, and *EndPadding* arrays. Only a value of 2 is supported.


`Strides`

Type: \_Field_size\_(DimensionCount) **const [UINT](/windows/win32/winprog/windows-data-types)\***

An array containing the strides of the convolution operation. These strides are applied to the convolution filter. They are separate from the tensor strides included in [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc).


`Dilations`

Type: \_Field_size\_(DimensionCount) **const [UINT](/windows/win32/winprog/windows-data-types)\***

An array containing the dilations of the convolution operation. Dilations are strides applied to the elements of the filter kernel. This has the effect of simulating a larger filter kernel by padding the internal filter kernel elements with zeros.


`StartPadding`

Type: \_Field_size\_(DimensionCount) **const [UINT](/windows/win32/winprog/windows-data-types)\***

An array containing the padding values to be applied to the beginning of each spatial dimension of the filter and input tensor of the convolution operation.


`EndPadding`

Type: \_Field_size\_(DimensionCount) **const [UINT](/windows/win32/winprog/windows-data-types)\***

An array containing the padding values to be applied to the end of each spatial dimension of the filter and input tensor of the convolution operation.


`GroupCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of groups which to divide the convolution operation up into. *GroupCount* can be used to achieve depth-wise convolution by setting the *GroupCount* equal to the input channel count. This divides the convolution up into a separate convolution per input channel.

## Availability
This operator was introduced in `DML_FEATURE_LEVEL_2_1`.

## Tensor constraints
* *FilterTensor* and *FilterZeroPointTensor* must have the same *DataType*.
* *InputTensor* and *InputZeroPointTensor* must have the same *DataType*.

## Tensor support
| Tensor | Kind | Dimensions | Supported dimension counts | Supported data types |
| ------ | ---- | ---------- | -------------------------- | -------------------- |
| InputTensor | Input | { BatchCount, InputChannelCount, InputHeight, InputWidth } | 4 | INT8, UINT8 |
| InputZeroPointTensor | Optional input | { 1, 1, 1, 1 } | 4 | INT8, UINT8 |
| FilterTensor | Input | { FilterBatchCount, FilterChannelCount, FilterHeight, FilterWidth } | 4 | INT8, UINT8 |
| FilterZeroPointTensor | Optional input | { 1, FilterZeroPointChannelCount, 1, 1 } | 4 | INT8, UINT8 |
| OutputTensor | Output | { BatchCount, OutputChannelCount, OutputHeight, OutputWidth } | 4 | INT32 |



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |