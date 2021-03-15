---
title: DirectML constants
description: The following constants are declared in `DirectML.h`.
keywords:
- Constants
topic_type:
- apiref
api_name:
- DirectML constants
api_location:
- DirectML.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 11/04/2020
---

# DirectML constants

The following constants are declared in `DirectML.h`.

| Constant | Value | Description |
|-|-|-|
| DML_TENSOR_DIMENSION_COUNT_MAX | 5 | DirectML tensors support a maximum of 5 dimensions for DML_TARGET_VERSION < DML_FEATURE_LEVEL_3_0. |
| DML_TENSOR_DIMENSION_COUNT_MAX1 | 8 | DirectML tensors support a maximum of 8 dimensions for DML_TARGET_VERSION >= DML_FEATURE_LEVEL_3_0. |
| DML_TEMPORARY_BUFFER_ALIGNMENT | 256 | Temporary and persistent buffers must have a base address that is aligned to 256 bytes. |
| DML_PERSISTENT_BUFFER_ALIGNMENT | 256 | Temporary and persistent buffers must have a base address that is aligned to 256 bytes. |
| DML_MINIMUM_BUFFER_TENSOR_ALIGNMENT | 16 | Buffer tensors have a minimum base address alignment requirement of 16 bytes. |

## Requirements

| Requirement | Value |
|-|-|
| Header | D3D12.h |

## See also

* [DirectML reference](direct3d-directml-reference.md)
* [Core reference](direct3d-12-core-reference.md)
* [Direct3D 12 Reference](direct3d-12-reference.md)
