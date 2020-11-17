---
UID: NS:directml.DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC
title: DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC
description: Performs a mean variance normalization function on the input tensor. This operator will calculate the mean and variance of the input tensor to perform normalization.
helpviewer_keywords: ["DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC","DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC structure","direct3d12.dml_mean_variance_normalization1_operator_desc","directml/DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC"]
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
 - DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC
 - directml/DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC
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
 - DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC
---

# DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC structure (directml.h)
Performs a mean variance normalization function on the input tensor. This operator will calculate the mean and variance of the input tensor to perform normalization. This operator performs the following computation.

```
Output = FusedActivation(Scale * ((Input - Mean) / sqrt(Variance + Epsilon)) + Bias).
```

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/). Also see [DirectML version history](/windows/win32/direct3d12/dml-version-history).

## Syntax
```cpp
struct DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC {
  const DML_TENSOR_DESC   *InputTensor;
  const DML_TENSOR_DESC   *ScaleTensor;
  const DML_TENSOR_DESC   *BiasTensor;
  const DML_TENSOR_DESC   *OutputTensor;
  UINT                    AxisCount;
  const UINT              *Axes;
  BOOL                    NormalizeVariance;
  FLOAT                   Epsilon;
  const DML_OPERATOR_DESC *FusedActivation;
};
```



## Members

`InputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the Input data. This tensor's dimensions should be `{ BatchCount, ChannelCount, Height, Width }`.


`ScaleTensor`

Type: \_Maybenull\_ **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An optional tensor containing the Scale data. This tensor's dimensions should be `{ BatchCount, ChannelCount, Height, Width }`. Any dimension can be replaced with 1 to broadcast in that dimension. This tensor is required if the *BiasTensor* is used.


`BiasTensor`

Type: \_Maybenull\_ **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An optional tensor containing the bias data. This tensor's dimensions should be `{ BatchCount, ChannelCount, Height, Width }`. Any dimension can be replaced with 1 to broadcast in that dimension. This tensor is required if the *ScaleTensor* is used.


`OutputTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor to write the results to. This tensor's dimensions are `{ BatchCount, ChannelCount, Height, Width }`.


`AxisCount`

Type: <b><a href="/windows/desktop/WinProg/windows-data-types">UINT</a></b>

The number of axes. This field determines the size of the *Axes* array.


`Axes`

Type: \_Field\_size\_(AxisCount) **const [UINT](/windows/desktop/WinProg/windows-data-types)\*** 

The axes along which to calculate the Mean and Variance.


`NormalizeVariance`

Type: <b><a href="/windows/desktop/WinProg/windows-data-types">BOOL</a></b>

**TRUE** if the Normalization layer includes Variance in the normalization calculation. Otherwise, **FALSE**. If **FALSE**, then normalization equation is `Output = FusedActivation(Scale * (Input - Mean) + Bias)`.


`Epsilon`

Type: <b><a href="/windows/desktop/WinProg/windows-data-types">FLOAT</a></b>

The epsilon value to use to avoid division by zero. A value of 0.00001 is recommended as default.


`FusedActivation`

Type: \_Maybenull\_ **const [DML_OPERATOR_DESC](/windows/win32/api/directml/ns-directml-dml_operator_desc)\***

An optional fused activation layer to apply after the normalization.


## Remarks
**DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC** is a superset of functionality of [DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC](/windows/win32/api/directml/ns-directml-dml_mean_variance_normalization_operator_desc). Here, setting the **Axes** array to `{ 0, 2, 3 }` is the equivalent of setting *CrossChannel* to **FALSE** in **DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC**; while setting the **Axes** array to `{ 1, 2, 3 }` is equivalent of setting *CrossChannel* to **TRUE**.

## Availability
This operator was introduced in `DML_FEATURE_LEVEL_2_1`.

## Tensor constraints
* *InputTensor* and *OutputTensor* must have the same *Sizes*.
* *BiasTensor*, *InputTensor*, *OutputTensor*, and *ScaleTensor* must have the same *DataType*.

## Tensor support
| Tensor | Kind | Dimensions | Supported dimension counts | Supported data types |
| ------ | ---- | ---------- | -------------------------- | -------------------- |
| InputTensor | Input | { BatchCount, ChannelCount, Height, Width } | 4 | FLOAT32, FLOAT16 |
| ScaleTensor | Optional input | { ScaleBatchCount, ScaleChannelCount, ScaleHeight, ScaleWidth } | 4 | FLOAT32, FLOAT16 |
| BiasTensor | Optional input | { BiasBatchCount, BiasChannelCount, BiasHeight, BiasWidth } | 4 | FLOAT32, FLOAT16 |
| OutputTensor | Output | { BatchCount, ChannelCount, Height, Width } | 4 | FLOAT32, FLOAT16 |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |

## See also

[Using fused operators for improved performance](/windows/win32/direct3d12/dml-fused-activations)