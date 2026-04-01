---
title: Precision Touchpad Reference
description: Reference documentation for the Precision Touchpad API functions, structures, enumerations, and interfaces.
ms.topic: reference
ms.date: 03/28/2026
---

# Precision Touchpad Reference

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This section provides reference documentation for the Precision Touchpad API functions, structures, enumerations, and interfaces.

## Functions

| Topic | Description |
|---|---|
| [**RegisterTouchpadCapableWindow**](registertouchpadcapable.md)<br/> | Registers a window as touchpad-capable.<br/> |
| [**RegisterTouchpadCapableThread**](registertouchpadcapable.md)<br/> | Registers the current thread as touchpad-capable.<br/> |
| [**GetPointerTouchpadInfo**](getpointertouchpadinfo.md)<br/> | Retrieves touchpad information for a pointer.<br/> |
| [**GetPointerTouchpadInfoHistory**](getpointertouchpadinfo.md)<br/> | Retrieves touchpad history for a pointer.<br/> |
| [**GetPointerFrameTouchpadInfo**](getpointertouchpadinfo.md)<br/> | Retrieves touchpad info for all pointers in a frame.<br/> |
| [**GetPointerFrameTouchpadInfoHistory**](getpointertouchpadinfo.md)<br/> | Retrieves touchpad history for all pointers in a frame.<br/> |
| [**ReportWindowContentInertia**](reportwindowcontentinertia.md)<br/> | Reports inertia state of window content.<br/> |
| [**ProcessPointerFramesInteractionContext2**](processpointerframesinteractioncontext2.md)<br/> | Processes pointer frames with extended info.<br/> |
| [**BufferPointerPacketsInteractionContext2**](processpointerframesinteractioncontext2.md)<br/> | Buffers pointer packets with extended info.<br/> |
| [**CreateSyntheticPointerDevice2**](createsyntheticpointerdevice2.md)<br/> | Creates a synthetic pointer device with extended parameters.<br/> |
| [**InjectTouchpadAction**](injecttouchpadaction.md)<br/> | Injects a touchpad action.<br/> |

## Structures

| Topic | Description |
|---|---|
| [**SYNTHETIC\_DEVICE\_CREATION\_PARAMS**](createsyntheticpointerdevice2.md#synthetic_device_creation_params)<br/> | Parameters for creating a synthetic injection device.<br/> |

## Enumerations

| Topic | Description |
|---|---|
| [**SYNTHETIC\_DEVICE\_CREATION\_OPTIONS**](createsyntheticpointerdevice2.md#synthetic_device_creation_options)<br/> | Options for synthetic device creation.<br/> |
| [**TOUCHPAD\_ACTION**](injecttouchpadaction.md#touchpad_action)<br/> | Touchpad actions for injection.<br/> |

## Interfaces and Classes

| Topic | Description |
|---|---|
| [**TouchpadGesturesController**](touchpadgesturescontroller.md)<br/> | WinRT runtimeclass for handling global touchpad gestures.<br/> |
| [**PhysicalGestureRecognizer**](physicalgesturerecognizer.md)<br/> | WinRT runtimeclass for device-relative gesture recognition.<br/> |
| [**IPointerPointPhysicalPosition**](ipointerpointphysicalposition.md)<br/> | Interface for device-relative pointer position.<br/> |
| [**IPointerDeviceInterop**](ipointerdeviceinterop.md)<br/> | Interop interface for pointer device handles.<br/> |

## Related topics

[Precision Touchpad Programming Guide](precision-touchpad-guide.md)

[Precision Touchpad Input](precision-touchpad-portal.md)
