---
title: Precision Touchpad Input
description: Overview of the Precision Touchpad APIs for Windows, which enable applications to interact with touchpads at higher fidelity including two-finger gestures, global gestures, and input injection.
ms.topic: reference
ms.date: 03/28/2026
---

# Precision Touchpad Input

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

## Purpose

Precision Touchpads were introduced in Windows 8.1 as the successor to existing touchpads whose input would be reported to Windows as a mouse. Precision Touchpads instead report to Windows the locations and state of the user's fingers on the touchpad, and Windows determines what action the user is performing. Broadly, the user's actions fall into three categories: mousing, actions, gesturing. When mousing, the original touchpad input is discarded and the appropriate mouse input is generated. When gesturing, the original touchpad input is more closely preserved and delivered to the hit-tested destination (or the shell for global gestures). Actions are more specialized, such as stopping inertia or global actions such as three-finger taps.

Applications do not directly receive gesturing touchpad input by default. The following technologies are enlightened to handle touchpad input, if the application uses them for its user interface:
* [Direct Manipulation](../directmanipulation/direct-manipulation-portal.md)
* [InteractionTracker](/uwp/api/windows.ui.composition.interactions.interactiontracker)

Otherwise, the touchpad input is redirected to ninput.dll for default input handling, which typically results in the generation of mouse wheel messages.

The Precision Touchpad APIs allow applications to interact with touchpads at a higher fidelity, overriding the default experiences:

- For two-finger gestures, register your window or thread as touchpad-capable with [**RegisterTouchpadCapableWindow** or **RegisterTouchpadCapableThread**](registertouchpadcapable.md). You'll then receive **WM_POINTER** messages for these gestures and can call [**GetPointerTouchpadInfo**](getpointertouchpadinfo.md) variants for extended information.
- Report window content inertia with [**ReportWindowContentInertia**](reportwindowcontentinertia.md) so that touchpad input can properly halt motion when appropriate.
- Use the [**TouchpadGesturesController**](touchpadgesturescontroller.md) runtimeclass to receive three or more finger global gestures and actions while your application is in foreground.
- Use the [**PhysicalGestureRecognizer**](physicalgesturerecognizer.md) runtimeclass for gesture recognition with device-relative coordinates, or feed an [Interaction Context](../input_intcontext/interaction-context-portal.md) of your own using [**ProcessPointerFramesInteractionContext2** or **BufferPointerPacketsInteractionContext2**](processpointerframesinteractioncontext2.md).

There is also support for injecting touchpad input:

- Use [**CreateSyntheticPointerDevice2**](createsyntheticpointerdevice2.md) to create touchpad injection devices, and [**InjectTouchpadAction**](injecttouchpadaction.md) for direct action injection when using gesture-only touchpad injection.

## In this section

| Topic | Description |
|---|---|
| [Precision Touchpad Programming Guide](precision-touchpad-guide.md)<br/> | How to use the Precision Touchpad APIs with code examples.<br/> |
| [Precision Touchpad Reference](precision-touchpad-reference.md)<br/> | Reference documentation for the Precision Touchpad functions, structures, enumerations, and interfaces.<br/> |

## Developer audience

The Precision Touchpad APIs are designed for developers who need high-fidelity touchpad input in their applications. This includes Remote Desktop client developers, accessibility tool developers, and application developers who want to provide custom touchpad gesture handling.

## Related topics

[Touch Injection](../input_touchinjection/touch-injection-portal.md)

[Pointer Device Input Stack](../input_pointerdevice/pointer-device-stack-portal.md)

[Interaction Context](../input_intcontext/interaction-context-portal.md)

[Keyboard and Mouse Input](../inputdev/user-input.md)
