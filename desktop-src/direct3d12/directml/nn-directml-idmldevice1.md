---
UID: NN:directml.IDMLDevice1
title: IDMLDevice1
description: Represents a DirectML device, which is used to create operators, binding tables, command recorders, and other objects.
helpviewer_keywords: ["IDMLDevice1","IDMLDevice1 interface","IDMLDevice1 interface","described","direct3d12.idmldevice1","directml/IDMLDevice1"]
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
req.lib: 
req.dll: 
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
f1_keywords:
 - IDMLDevice1
 - directml/IDMLDevice1
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - COM
api_location:
 - DirectML.h
api_name:
 - IDMLDevice1
---

# IDMLDevice1 interface (directml.h)

Represents a DirectML device, which is used to create operators, binding tables, command recorders, and other objects. The **IDMLDevice1** interface inherits from [IDMLDevice](/windows/win32/api/directml/nn-directml-idmldevice).

A DirectML device is always associated with exactly one underlying Direct3D 12 device. All objects created by the DirectML device maintain a strong reference to their parent device. Unlike the Direct3D 12 device, the DML device is not a singleton. Therefore, it's possible to create multiple DirectML devices over the same Direct3D 12 device. However, this isn't recommended as the DirectML device has no mutable state, so there's little advantage to creating multiple DML devices over the same Direct3D 12 device.

This object is thread-safe.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.4 and later. Also see [DirectML version history](../dml-version-history.md).

## Availability
This API was introduced in DirectML version `1.1.0`.

## Tensor constraints
**Target Platform**: Windows


## Inheritance


The IDMLDevice1 interface inherits from the IDMLDevice interface.



## Methods

<p>The <b>IDMLDevice1</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDMLDevice1::CompileGraph](../directml/nf-directml-idmldevice1-compilegraph.md) | Compiles a graph of DirectML operators into an object that can be dispatched to the GPU. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | directml.h |

## See also

[IDMLDevice interface](/windows/win32/api/directml/nn-directml-idmldevice)