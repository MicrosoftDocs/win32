---
UID: NE:directml.DML_RANDOM_GENERATOR_TYPE
title: DML_RANDOM_GENERATOR_TYPE
description: Defines constants that specify types of random random-number generator.
helpviewer_keywords: ["DML_RANDOM_GENERATOR_TYPE","DML_RANDOM_GENERATOR_TYPE structure","direct3d12.dml_graph_node_type","directml/DML_RANDOM_GENERATOR_TYPE"]
ms.topic: reference
tech.root: directml
ms.date: 11/09/2020
ms.keywords: DML_RANDOM_GENERATOR_TYPE, DML_RANDOM_GENERATOR_TYPE structure, direct3d12.dml_graph_node_type, directml/DML_RANDOM_GENERATOR_TYPE
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
 - DML_RANDOM_GENERATOR_TYPE
 - directml/DML_RANDOM_GENERATOR_TYPE
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
 - DML_RANDOM_GENERATOR_TYPE
---

# DML_RANDOM_GENERATOR_TYPE enumeration (directml.h)

Defines constants that specify types of random random-number generator.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.4 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax
```cpp
enum DML_RANDOM_GENERATOR_TYPE
{
  DML_RANDOM_GENERATOR_TYPE_PHILOX_4X32_10
};
```

## Constants

| Name | Description |
| ---- |:---- |
| DML_RANDOM_GENERATOR_TYPE_PHILOX_4X32_10 | Specifies a generator for pseudo-random numbers according to the [Philox 4x32-10 algorithm](http://www.thesalmons.org/john/random123/papers/random123sc11.pdf). |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | directml.h |