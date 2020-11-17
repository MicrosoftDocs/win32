---
UID: NS:directml.DML_INTERMEDIATE_GRAPH_EDGE_DESC
title: DML_INTERMEDIATE_GRAPH_EDGE_DESC
description: Describes a connection within a graph of DirectML operators defined by [DML_GRAPH_DESC](/windows/desktop/direct3d12/directml/ns-directml-dml_graph_desc) and passed to [IDMLDevice1::CompileGraph](/windows/desktop/direct3d12/directml/nf-directml-idmldevice1-compilegraph). This structure is used to define a connection between internal nodes.
helpviewer_keywords: ["DML_INTERMEDIATE_GRAPH_EDGE_DESC","DML_INTERMEDIATE_GRAPH_EDGE_DESC structure","direct3d12.dml_intermediate_graph_edge_desc","directml/DML_INTERMEDIATE_GRAPH_EDGE_DESC"]
ms.topic: reference
tech.root: directml
ms.date: 11/02/2020
ms.keywords: DML_INTERMEDIATE_GRAPH_EDGE_DESC, DML_INTERMEDIATE_GRAPH_EDGE_DESC structure, direct3d12.dml_intermediate_graph_edge_desc, directml/DML_INTERMEDIATE_GRAPH_EDGE_DESC
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
 - DML_INTERMEDIATE_GRAPH_EDGE_DESC
 - directml/DML_INTERMEDIATE_GRAPH_EDGE_DESC
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
 - DML_INTERMEDIATE_GRAPH_EDGE_DESC
---

# DML_INTERMEDIATE_GRAPH_EDGE_DESC structure (directml.h)
Describes a connection within a graph of DirectML operators defined by [DML_GRAPH_DESC](/windows/desktop/direct3d12/directml/ns-directml-dml_graph_desc) and passed to [IDMLDevice1::CompileGraph](/windows/desktop/direct3d12/directml/nf-directml-idmldevice1-compilegraph). This structure is used to define a connection between internal nodes.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/). Also see [DirectML version history](/windows/win32/direct3d12/dml-version-history).

## Syntax
```cpp
struct DML_INTERMEDIATE_GRAPH_EDGE_DESC {
  UINT       FromNodeIndex;
  UINT       FromNodeOutputIndex;
  UINT       ToNodeIndex;
  UINT       ToNodeInputIndex;
  const char *Name;
};
```



## Members

`FromNodeIndex`

Type: **[UINT](/windows/desktop/winprog/windows-data-types)**

The index of the graph node from which a connection to another node is specified.


`FromNodeOutputIndex`

Type: **[UINT](/windows/desktop/winprog/windows-data-types)**

The index of the output on the node at index *FromNodeIndex* where the connection is specified.


`ToNodeIndex`

Type: **[UINT](/windows/desktop/winprog/windows-data-types)**

The index of the graph node into which a connection from another node is specified.


`ToNodeInputIndex`

Type: **[UINT](/windows/desktop/winprog/windows-data-types)**

The index of the input on the node at index *ToNodeIndex* where the connection is specified.


`Name`

Type: \_Field\_z\_ \_Maybenull\_ **const char\***

An optional name for the graph connection. If provided, this might be used within certain error messages emitted by the DirectML debug layer.

## Availability

This API was introduced in DirectML version `1.1.0`.



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |

## See also

* [IDMLDevice1::CompileGraph method](/windows/desktop/direct3d12/directml/nf-directml-idmldevice1-compilegraph)
* [DML_GRAPH_DESC structure](/windows/desktop/direct3d12/directml/ns-directml-dml_graph_desc)
* [DML_GRAPH_EDGE_DESC structure](/windows/desktop/direct3d12/directml/ns-directml-dml_graph_edge_desc)