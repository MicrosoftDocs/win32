---
title: DirectML interfaces
description: The following interfaces are declared in DirectML.h.
ms.localizationpriority: low
ms.topic: article
ms.date: 04/19/2019
ms.custom: 19H1
---

# DirectML interfaces

The following interfaces are declared in DirectML.h.

## In this section

| Topic | Description |
|-|-|
| [**IDMLBindingTable**](/windows/desktop/api/directml/nn-directml-idmlbindingtable) | Creates a DirectML device for a given Direct3D 12 device. |
| [**IDMLCommandRecorder**](/windows/desktop/api/directml/nn-directml-idmlcommandrecorder) | Records dispatches of DirectML work into a Direct3D 12 command list. |
| [**IDMLCompiledOperator**](/windows/desktop/api/directml/nn-directml-idmlcompiledoperator) | Represents a compiled, efficient form of an operator suitable for execution on the GPU. |
| [**IDMLDebugDevice**](/windows/desktop/api/directml/nn-directml-idmldebugdevice) | Controls the DirectML debug layer. |
| [**IDMLDevice**](/windows/desktop/api/directml/nn-directml-idmldevice) | Represents a DirectML device, which is used to create operators, binding tables, command recorders, and other objects. |
| [**IDMLDevice1**](/windows/desktop/api/directml/nn-directml-idmldevice1) | Represents a DirectML device, which is used to create operators, binding tables, command recorders, and other objects. |
| [**IDMLDeviceChild**](/windows/win32/api/directml/nn-directml-idmldevicechild) | An interface implemented by all objects created from the DirectML device. |
| [**IDMLDispatchable**](/windows/desktop/api/directml/nn-directml-idmldispatchable) | Implemented by objects that can be recorded into a command list for dispatch on the GPU, using [IDMLCommandRecorder::RecordDispatch](/windows/desktop/api/directml/nf-directml-idmlcommandrecorder-recorddispatch). |
| [**IDMLObject**](/windows/desktop/api/directml/nn-directml-idmlobject) | An interface from which [IDMLDevice](/windows/win32/api/directml/nn-directml-idmldevice) and [IDMLDeviceChild](/windows/desktop/api/directml/nn-directml-idmldevicechild) inherit directly (and all other interfaces, indirectly). Consequently, it provides methods common to all DirectML interfaces, specifically methods to associate private data, and to annotate object names. |
| [**IDMLOperator**](/windows/desktop/api/directml/nn-directml-idmloperator) | Represents a DirectML operator. |
| [**IDMLOperatorInitializer**](/windows/desktop/api/directml/nn-directml-idmloperatorinitializer) | Represents a specialized object whose purpose is to initialize compiled operators. |
| [**IDMLPageable**](/windows/desktop/api/directml/nn-directml-idmlpageable) | Implemented by objects that can be evicted from GPU memory, and hence that can be supplied to [IDMLDevice::Evict](/windows/desktop/api/directml/nf-directml-idmldevice-evict) and [IDMLDevice::MakeResident](/windows/desktop/api/directml/nf-directml-idmldevice-makeresident). |

## Related topics

* [DirectML reference](direct3d-directml-reference.md)
* [Core reference](direct3d-12-core-reference.md)
* [Direct3D 12 Reference](direct3d-12-reference.md)
