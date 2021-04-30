---
UID: NS:directml.DML_ADAM_OPTIMIZER_OPERATOR_DESC
title: DML_ADAM_OPTIMIZER_OPERATOR_DESC
description: Computes updated weights (parameters) using the supplied gradients, based on the Adam (**ADA**ptive **M**oment estimation) algorithm. This operator is an optimizer, and is typically used in the weight update step of a training loop to perform gradient descent.
helpviewer_keywords: ["DML_ADAM_OPTIMIZER_OPERATOR_DESC","DML_ADAM_OPTIMIZER_OPERATOR_DESC structure","direct3d12.dml_convolution_integer_operator_desc","directml/DML_ADAM_OPTIMIZER_OPERATOR_DESC"]
ms.topic: reference
tech.root: directml
ms.date: 11/09/2020
ms.keywords: DML_ADAM_OPTIMIZER_OPERATOR_DESC, DML_ADAM_OPTIMIZER_OPERATOR_DESC structure, direct3d12.dml_convolution_integer_operator_desc, directml/DML_ADAM_OPTIMIZER_OPERATOR_DESC
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
 - DML_ADAM_OPTIMIZER_OPERATOR_DESC
 - directml/DML_ADAM_OPTIMIZER_OPERATOR_DESC
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
 - DML_ADAM_OPTIMIZER_OPERATOR_DESC
---

# DML_ADAM_OPTIMIZER_OPERATOR_DESC structure (directml.h)

Computes updated weights (parameters) using the supplied gradients, based on the Adam (**ADA**ptive **M**oment estimation) algorithm. This operator is an optimizer, and is typically used in the weight update step of a training loop to perform gradient descent.

This operator performs the following computation:

```
X = InputParametersTensor
M = InputFirstMomentTensor
V = InputSecondMomentTensor
G = GradientTensor
T = TrainingStepTensor

// Compute updated first and second moment estimates.
M = Beta1 * M + (1.0 - Beta1) * G
V = Beta2 * V + (1.0 - Beta2) * G * G

// Compute bias correction factor for first and second moment estimates.
Alpha = sqrt(1.0 - pow(Beta2, T)) / (1.0 - pow(Beta1, T))

X -= LearningRate * Alpha * M / (sqrt(V) + Epsilon)

OutputParametersTensor = X
OutputFirstMomentTensor = M
OutputSecondMomentTensor = V
```

In addition to computing the updated weight parameters (returned in *OutputParametersTensor*), this operator also returns the updated first and second moment estimates in *OutputFirstMomentTensor* and *OutputSecondMomentTensor*, respectively. Typically, you should store these first and second moment estimates, and supply them as inputs during the subsequent training step.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.4 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax
```cpp
struct DML_ADAM_OPTIMIZER_OPERATOR_DESC
{ 
  const DML_TENSOR_DESC* InputParametersTensor;
  const DML_TENSOR_DESC* InputFirstMomentTensor;
  const DML_TENSOR_DESC* InputSecondMomentTensor;
  const DML_TENSOR_DESC* GradientTensor;
  const DML_TENSOR_DESC* TrainingStepTensor;
  const DML_TENSOR_DESC* OutputParametersTensor;
  const DML_TENSOR_DESC* OutputFirstMomentTensor;
  const DML_TENSOR_DESC* OutputSecondMomentTensor;
  FLOAT LearningRate;
  FLOAT Beta1;
  FLOAT Beta2;
  FLOAT Epsilon;
};
```

## Members

`InputParametersTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the parameters (weights) to apply this optimizer to. The gradient, first, and second moment estimates, current training step, as well as hyperparameters *LearningRate*, *Beta1*, and *Beta2*, are used by this operator to perform gradient descent on the weight values supplied in this tensor.

`InputFirstMomentTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the first moment estimate of the gradient for each weight value. These values are typically obtained as the result of a previous execution of this operator, via the *OutputFirstMomentTensor*.

When applying this optimizer to a set of weights for the first time (for example, during the initial training step) the values of this tensor should typically be initialized to zero. Subsequent executions should use the values returned in *OutputFirstMomentTensor*.

The *Sizes* and *DataType* of this tensor must exactly match those of the *InputParametersTensor*.

`InputSecondMomentTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A tensor containing the second moment estimate of the gradient for each weight value. These values are typically obtained as the result of a previous execution of this operator, via the *OutputSecondMomentTensor*.

When applying this optimizer to a set of weights for the first time (for example, during the initial training step) the values of this tensor should typically be initialized to zero. Subsequent executions should use the values returned in *OutputSecondMomentTensor*.

The *Sizes* and *DataType* of this tensor must exactly match those of the *InputParametersTensor*.

`GradientTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

The gradients to apply to the input parameters (weights) for gradient descent. Gradients are typically obtained in a backpropagation pass during training.

The *Sizes* and *DataType* of this tensor must exactly match those of the *InputParametersTensor*.

`TrainingStepTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

A scalar tensor containing a single integer value representing the current training step count. This value along with *Beta1* and *Beta2* is used to compute the exponential decay of the first and second moment estimate tensors.

Typically the training step value starts at 0 at the beginning of training, and is incremented by 1 on each successive training step. This operator doesn't update the training step value; you should do that manually, for example using [DML_OPERATOR_ELEMENT_WISE_ADD](/windows/win32/api/directml/ns-directml-dml_element_wise_add_operator_desc).

This tensor must be a scalar (that is, all *Sizes* equal to 1) and have data type [**DML_TENSOR_DATA_TYPE_UINT32**](/windows/win32/api/directml/ne-directml-dml_tensor_data_type).

`OutputParametersTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An output tensor that holds the updated parameter (weight) values after gradient descent is applied.

During binding, this tensor is permitted to alias an eligible input tensor, which can be used to perform an in-place update of this tensor. See the [Remarks](#remarks) section for more details.

The *Sizes* and *DataType* of this tensor must exactly match those of the *InputParametersTensor*.

`OutputFirstMomentTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An output tensor containing updated first moment estimates. You should store the values of this tensor, and supply them in *InputFirstMomentTensor* during the subsequent training step.

During binding, this tensor is permitted to alias an eligible input tensor, which can be used to perform an in-place update of this tensor. See the [Remarks](#remarks) section for more details.

The *Sizes* and *DataType* of this tensor must exactly match those of the *InputParametersTensor*.

`OutputSecondMomentTensor`

Type: **const [DML_TENSOR_DESC](/windows/win32/api/directml/ns-directml-dml_tensor_desc)\***

An output tensor containing updated second moment estimates. You should store the values of this tensor and supply them in *InputSecondMomentTensor* during the subsequent training step.

During binding, this tensor is permitted to alias an eligible input tensor, which can be used to perform an in-place update of this tensor. See the [Remarks](#remarks) section for more details.

The *Sizes* and *DataType* of this tensor must exactly match those of the *InputParametersTensor*.

`LearningRate`

Type: **float**

The learning rate, also commonly referred to as the *step size*. The learning rate is a hyperparameter that determines the magnitude of the weight update along the gradient vector on each training step.

`Beta1`

Type: **float**

A hyperparameter representing the exponential decay rate of the gradient's first moment estimate. This value should be between 0.0 and 1.0. A value of 0.9f is typical.

`Beta2`

Type: **float**

A hyperparameter representing the exponential decay rate of the gradient's second moment estimate. This value should be between 0.0 and 1.0. A value of 0.999f is typical.

`Epsilon`

Type: **float**

A small value used to help numerical stability by preventing division-by-zero. For 32-bit floating-point inputs, typical values include 1e-8 or `FLT_EPSILON`.

## Remarks
This operator supports in-place execution, meaning that each output tensor is permitted to alias an eligible input tensor during binding. For example, it's possible to bind the same resource for both the *InputParametersTensor* and *OutputParametersTensor* in order to effectively achieve an in-place update of the input parameters. All of this operator's input tensors, with the exception of the *TrainingStepTensor*, are eligible to be aliased in this way.

## Availability
This operator was introduced in `DML_FEATURE_LEVEL_3_0`.

## Tensor constraints
* *GradientTensor*, *InputFirstMomentTensor*, *InputParametersTensor*, *InputSecondMomentTensor*, *OutputFirstMomentTensor*, *OutputParametersTensor*, *OutputSecondMomentTensor*, and *TrainingStepTensor* must have the same *DataType*.
* *GradientTensor*, *InputFirstMomentTensor*, *InputParametersTensor*, *InputSecondMomentTensor*, *OutputFirstMomentTensor*, *OutputParametersTensor*, and *OutputSecondMomentTensor* must have the same *Sizes*.

## Tensor support
| Tensor | Kind | Dimensions | Supported dimension counts | Supported data types |
| ------ | ---- | ---------- | -------------------------- | -------------------- |
| InputParametersTensor | Input | { D0, D1, D2, D3 } | 4 | FLOAT32, FLOAT16 |
| InputFirstMomentTensor | Input | { D0, D1, D2, D3 } | 4 | FLOAT32, FLOAT16 |
| InputSecondMomentTensor | Input | { D0, D1, D2, D3 } | 4 | FLOAT32, FLOAT16 |
| GradientTensor | Input | { D0, D1, D2, D3 } | 4 | FLOAT32, FLOAT16 |
| TrainingStepTensor | Input | { 1, 1, 1, 1 } | 4 | FLOAT32, FLOAT16 |
| OutputParametersTensor | Output | { D0, D1, D2, D3 } | 4 | FLOAT32, FLOAT16 |
| OutputFirstMomentTensor | Output | { D0, D1, D2, D3 } | 4 | FLOAT32, FLOAT16 |
| OutputSecondMomentTensor | Output | { D0, D1, D2, D3 } | 4 | FLOAT32, FLOAT16 |

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |