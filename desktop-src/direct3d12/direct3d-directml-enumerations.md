---
title: DirectML enumerations
description: The following enumerations are declared in DirectML.h.
ms.localizationpriority: low
ms.topic: article
ms.date: 11/06/2020
ms.custom: 19H1
---

# DirectML enumerations

The following enumerations are declared in DirectML.h.

## In this section

| Topic and description |
|-|
| [**DML_AXIS_DIRECTION**](/windows/desktop/api/directml/ne-directml-dml_axis_direction). Defines constants that specify the direction of an operation along the given axis for the operator (for example, summation, selecting the top-k elements, selecting the minimum element). |
| [**DML_BINDING_TYPE**](/windows/desktop/api/directml/ne-directml-dml_binding_type). Defines constants that specify the nature of the resource(s) referred to by a binding description [DML_BINDING_DESC structure](/windows/desktop/api/directml/ns-directml-dml_binding_desc). |
| [**DML_CONVOLUTION_DIRECTION**](/windows/desktop/api/directml/ne-directml-dml_convolution_direction). Defines constants that specify a direction for the DirectML convolution operator (as described by the [DML_CONVOLUTION_OPERATOR_DESC structure](/windows/desktop/api/directml/ns-directml-dml_convolution_operator_desc)). |
| [**DML_CONVOLUTION_MODE**](/windows/desktop/api/directml/ne-directml-dml_convolution_mode). Defines constants that specify a mode for the DirectML convolution operator (as described by the [DML_CONVOLUTION_OPERATOR_DESC structure](/windows/desktop/api/directml/ns-directml-dml_convolution_operator_desc)). |
| [**DML_CREATE_DEVICE_FLAGS**](/windows/desktop/api/directml/ne-directml-dml_create_device_flags). Supplies additional device creation options to [DMLCreateDevice](/windows/desktop/api/directml/nf-directml-dmlcreatedevice). |
| [**DML_DEPTH_SPACE_ORDER**](/windows/desktop/api/directml/ne-directml-dml_depth_space_order). Defines constants controlling the transform applied in the DirectML operators [DML_OPERATOR_DEPTH_TO_SPACE1](/windows/win32/api/directml/ne-directml-dml_operator_type) and **DML_OPERATOR_SPACE_TO_DEPTH1**. |
| [**DML_EXECUTION_FLAGS**](/windows/desktop/api/directml/ne-directml-dml_execution_flags). Supplies options to DirectML to control execution of operators. |
| [**DML_FEATURE**](/windows/desktop/api/directml/ne-directml-dml_feature). Defines a set of optional features and capabilities that can be queried from the DirectML device. |
| [**DML_GRAPH_EDGE_TYPE**](/windows/desktop/api/directml/ne-directml-dml_graph_edge_type). Defines constants that specify a type of graph edge. See [DML_GRAPH_EDGE_DESC](/windows/win32/api/directml/ns-directml-dml_graph_edge_desc) for the usage of this enumeration. |
| [**DML_GRAPH_NODE_TYPE**](/windows/desktop/api/directml/ne-directml-dml_graph_node_type). Defines constants that specify a type of graph node. See [DML_GRAPH_NODE_DESC](/windows/win32/api/directml/ns-directml-dml_graph_node_desc) for the usage of this enumeration. |
| [**DML_INTERPOLATION_MODE**](/windows/desktop/api/directml/ne-directml-dml_interpolation_mode). Defines constants that specify a mode for the DirectML upsample 2-D operator (as described by the [DML_UPSAMPLE_2D_OPERATOR_DESC structure](/windows/desktop/api/directml/ns-directml-dml_upsample_2d_operator_desc)). |
| [**DML_MATRIX_TRANSFORM**](/windows/desktop/api/directml/ne-directml-dml_matrix_transform). Defines constants that specify a matrix transform to be applied to a DirectML tensor. |
| [**DML_OPERATOR_TYPE**](/windows/desktop/api/directml/ne-directml-dml_operator_type). Defines the type of an operator description. |
| [**DML_PADDING_MODE**](/windows/desktop/api/directml/ne-directml-dml_padding_mode). Defines constants that specify a mode for the DirectML pad operator (as described by the [DML_PADDING_OPERATOR_DESC structure](/windows/desktop/api/directml/ns-directml-dml_padding_operator_desc)). |
| [**DML_RANDOM_GENERATOR_TYPE**](/windows/win32/api/directml/ne-directml-dml_random_generator_type). Defines constants that specify types of random random-number generator. |
| [**DML_RECURRENT_NETWORK_DIRECTION**](/windows/desktop/api/directml/ne-directml-dml_recurrent_network_direction). Defines constants that specify a direction for a recurrent DirectML operator. |
| [**DML_REDUCE_FUNCTION**](/windows/desktop/api/directml/ne-directml-dml_reduce_function). Defines constants that specify the specific reduction algorithm to use for the DirectML reduce operator (as described by the [DML_REDUCE_OPERATOR_DESC structure](/windows/desktop/api/directml/ns-directml-dml_reduce_operator_desc)). |
| [**DML_TENSOR_DATA_TYPE**](/windows/desktop/api/directml/ne-directml-dml_tensor_data_type). Specifies the data type of the values in a tensor. |
| [**DML_TENSOR_FLAGS**](/windows/desktop/api/directml/ne-directml-dml_tensor_flags). Specifies additional options in a tensor description. |
| [**DML_TENSOR_TYPE**](/windows/desktop/api/directml/ne-directml-dml_tensor_type). Identifies a type of tensor description. |

## Related topics

* [DirectML reference](direct3d-directml-reference.md)
* [Core reference](direct3d-12-core-reference.md)
* [Direct3D 12 Reference](direct3d-12-reference.md)