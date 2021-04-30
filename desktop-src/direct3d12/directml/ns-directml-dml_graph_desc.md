---
UID: NS:directml.DML_GRAPH_DESC
title: DML_GRAPH_DESC
description: Describes a graph of DirectML operators used to compile a combined, optimized operator.
helpviewer_keywords: ["DML_GRAPH_DESC","DML_GRAPH_DESC structure","direct3d12.dml_graph_desc","directml/DML_GRAPH_DESC"]
ms.topic: reference
tech.root: directml
ms.date: 11/02/2020
ms.keywords: DML_GRAPH_DESC, DML_GRAPH_DESC structure, direct3d12.dml_graph_desc, directml/DML_GRAPH_DESC
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
 - DML_GRAPH_DESC
 - directml/DML_GRAPH_DESC
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
 - DML_GRAPH_DESC
---

# DML_GRAPH_DESC structure (directml.h)

Describes a graph of DirectML operators used to compile a combined, optimized operator. See [IDMLDevice1::CompileGraph](/windows/desktop/direct3d12/directml/nf-directml-idmldevice1-compilegraph).

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.4 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax
```cpp
struct DML_GRAPH_DESC {
  UINT                      InputCount;
  UINT                      OutputCount;
  UINT                      NodeCount;
  const DML_GRAPH_NODE_DESC *Nodes;
  UINT                      InputEdgeCount;
  const DML_GRAPH_EDGE_DESC *InputEdges;
  UINT                      OutputEdgeCount;
  const DML_GRAPH_EDGE_DESC *OutputEdges;
  UINT                      IntermediateEdgeCount;
  const DML_GRAPH_EDGE_DESC *IntermediateEdges;
};
```



## Members

`InputCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of inputs of the overall graph. Each graph input may be connected to a variable number of internal nodes, therefore this may be different from *InputEdgeCount*.


`OutputCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of outputs of the overall graph. Each graph output may be connected to a variable number of internal nodes, therefore this may be different from *OutputEdgeCount*.


`NodeCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of internal nodes in the graph.


`Nodes`

Type: \_Field\_size\_(NodeCount) **const [DML_GRAPH_NODE_DESC](./ns-directml-dml_graph_node_desc.md)\***

The internal nodes in the graph.


`InputEdgeCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of connections between graph inputs and inputs of internal nodes in the graph.


`InputEdges`

Type: \_Field\_size\_(InputEdgeCount) **const [DML_GRAPH_EDGE_DESC](./ns-directml-dml_graph_edge_desc.md)\***

An array of connections between graph inputs and inputs of internal nodes in the graph. The *Type* field within each element should be set to [DML_GRAPH_EDGE_TYPE_INPUT](./ne-directml-dml_graph_edge_type.md).


`OutputEdgeCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of connections between graph outputs and outputs of internal nodes in the graph.


`OutputEdges`

Type: \_Field\_size\_(OutputEdgeCount) **const [DML_GRAPH_EDGE_DESC](./ns-directml-dml_graph_edge_desc.md)\***

An array of connections between graph outputs and outputs of internal nodes in the graph. The *Type* field within each element should be set to [DML_GRAPH_EDGE_TYPE_OUTPUT](./ne-directml-dml_graph_edge_type.md).


`IntermediateEdgeCount`

Type: [**UINT**](/windows/desktop/winprog/windows-data-types)

The number of internal connections between nodes in the graph.


`IntermediateEdges`

Type: \_Field\_size\_(IntermediateEdgeCount) **const [DML_GRAPH_EDGE_DESC](./ns-directml-dml_graph_edge_desc.md)\***

An array of connections between inputs and outputs of internal nodes in the graph. The Type field within each element should be set to [DML_GRAPH_EDGE_TYPE_INTERMEDIATE](./ne-directml-dml_graph_edge_type.md)


## Remarks
The graph described by this structure must be a directed acyclic graph. You must define a connection for the input and output of each supplied node, except for inputs and outputs that are optional for the associated operator.

Nodes may use operators that were created using the [DML_TENSOR_FLAG_OWNED_BY_DML](/windows/win32/api/directml/ne-directml-dml_tensor_flags) flag for certain inputs. Any operator inputs using this flag must be connected to graph inputs. All operator inputs connected to the same graph input must use or omit this flag equivalently.

It is legal to connect operators whose connected inputs and outputs use different dimension counts, sizes, and data types. This implies that the tensor data blob is interpreted differently by each operator. The *TotalTensorSizeInBytes* field of connected tensor inputs and outputs must be identical, though. Operators should only read regions of tensors written by earlier operators. Any padding regions in the output of an operation (resulting from the use of strides) are not guaranteed to be read as zero by down-stream operators.

## Availability

This API was introduced in DirectML version `1.1.0`.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |

## See also

* [IDMLDevice1::CompileGraph method](/windows/desktop/direct3d12/directml/nf-directml-idmldevice1-compilegraph)
* [DML_GRAPH_NODE_DESC struct](./ns-directml-dml_graph_node_desc.md)
* [DML_GRAPH_EDGE_DESC struct](./ns-directml-dml_graph_edge_desc.md)