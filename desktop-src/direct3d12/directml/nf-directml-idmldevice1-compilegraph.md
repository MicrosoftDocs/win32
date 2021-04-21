---
UID: NF:directml.IDMLDevice1.CompileGraph
title: IDMLDevice1::CompileGraph
description: Compiles a graph of DirectML operators into an object that can be dispatched to the GPU.
helpviewer_keywords: ["CompileGraph","CompileGraph method","CompileGraph method","IDMLDevice1 interface","IDMLDevice1 interface","CompileGraph method","IDMLDevice1.CompileGraph","IDMLDevice1::CompileGraph","direct3d12.idmldevice1_compileoperator","directml/IDMLDevice1::CompileGraph"]
ms.topic: reference
tech.root: directml
ms.date: 11/04/2020
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
req.lib: DirectML.lib
req.dll: DirectML.dll
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
f1_keywords:
 - IDMLDevice1::CompileGraph
 - directml/IDMLDevice1::CompileGraph
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - COM
api_location:
 - DirectML.dll
api_name:
 - IDMLDevice1.CompileGraph
---

# IDMLDevice1::CompileGraph method (directml.h)

Compiles a graph of DirectML operators into an object that can be dispatched to the GPU.

A compiled operator represents the efficient, baked form of an operator suitable for execution on the GPU. A compiled operator holds state (such as shaders and other objects) required for execution. Because a compiled operator implements the [IDMLPageable](/windows/win32/api/directml/nn-directml-idmlpageable) interface, you're able to evict one from GPU memory if you wish. See [IDMLDevice1::Evict](/windows/win32/api/directml/nf-directml-idmldevice-evict) and [IDMLDevice1::MakeResident](/windows/win32/api/directml/nf-directml-idmldevice-makeresident) for more info.

The compiled operator doesn't use nor reference the [IDMLOperator](/windows/win32/api/directml/nn-directml-idmloperator) objects supplied within the graph description after this method returns.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.4 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax

```cpp
HRESULT CompileGraph(
  const DML_GRAPH_DESC *desc,
  DML_EXECUTION_FLAGS  flags,
  REFIID               riid,
  void                 **ppv
);
```

## Parameters

`desc`

Type: **[DML_GRAPH_DESC](./ns-directml-dml_graph_desc.md)\***

A description of the graph to compile. See [DML_GRAPH_DESC](./ns-directml-dml_graph_desc.md).

`flags`

Type: [**DML_EXECUTION_FLAGS**](/windows/win32/api/directml/ne-directml-dml_execution_flags)

Any flags to control the execution of this operator.

`riid`

Type: <b>REFIID</b>

A reference to the globally unique identifier (GUID) of the interface that you wish to be returned in <i>ppv</i>. This is expected to be the GUID of [IDMLCompiledOperator](/windows/win32/api/directml/nn-directml-idmlcompiledoperator).

`ppv`

Type: <b>void**</b>

A pointer to a memory block that receives a pointer to the compiled operator. This is the address of a pointer to an [IDMLCompiledOperator](/windows/win32/api/directml/nn-directml-idmlcompiledoperator), representing  the compiled operator created.


## Return value

Type: [**HRESULT**](/windows/desktop/winprog/windows-data-types)

If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The DirectML operator graph API provides an abstract way to use DirectML efficiently across diverse hardware. DirectML applies tensor-level optimizations such as choosing the most efficient tensor layout based on the adapter being used. It also applies optimizations such as the removal of Join or Split operators.

We recommend that you apply high-level optimizations before building a DirectML graph. For example, fusing Convolution operators with BatchNorm, constant folding, and common subexpression elimination. The optimizations within DirectML's graph optimizer are intended to complement such device-independent optimizations, which are typically handled generically by machine learning frameworks.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | directml.h |
| **Library** | DirectML.lib |
| **DLL** | DirectML.dll |

## See also

[IDMLDevice1](/windows/win32/api/directml/nn-directml-idmldevice)