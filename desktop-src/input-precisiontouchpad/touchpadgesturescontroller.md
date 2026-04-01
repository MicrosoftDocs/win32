---
title: TouchpadGesturesController class (Windows.UI.Input)
description: Enables an application to receive global touchpad gestures (three or more finger taps, presses, and manipulations) while in foreground, overriding the default system behavior.
ms.topic: reference
ms.date: 03/28/2026
---

# TouchpadGesturesController class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Enables an application to register for global touchpad gestures involving three or more contacts, providing their own handler instead of the default system behavior.

Taps and swipes involving three or more contacts are considered global gestures. The system will first check for any controllers registered by the foreground process when a global touchpad gesture is performed. If none are found that are enabled and support the gesture, then the gesture will be routed to the system's own handler. Controllers in background processes are ignored.

**Namespace:** Windows.UI.Input

## Members

### Static methods

#### IsSupported

```cpp
static Boolean IsSupported();
```

Returns whether the **TouchpadGesturesController**'s functionality is supported on the system.

#### CreateForProcess

```cpp
static TouchpadGesturesController CreateForProcess();
```

Creates a **TouchpadGesturesController** for the associated process. Multiple controllers can be created for a given process, but if multiple controllers are enabled and declare support for the same gesture, only one will receive the associated events.

The controller creates a window on the thread on which it is created and therefore requires that the thread has a message pump. The controller's events will all be raised on this thread, although it can be configured from any thread. The controller's window is marked as touchpad-capable via [**RegisterTouchpadCapableWindow**](registertouchpadcapable.md) — see its documentation for how the thread is impacted.

### Properties

#### Enabled

```cpp
Boolean Enabled;
```

Gets or sets whether the controller is enabled. If disabled, it will not be considered by the system as a valid target for routing gestures.

#### SupportedGestures

```cpp
TouchpadGlobalGestureKinds SupportedGestures;
```

Gets or sets the gestures supported by the controller. The system will only route gestures to the controller if it has declared support for them. Manipulations refer to touchpad input where the fingers have moved (for example, swiping across the touchpad), whereas actions are caused by stationary fingers (for example, tapping or pressing the touchpad's surface button without moving).

### Events

#### PointerPressed, PointerMoved, PointerReleased

```cpp
event Windows.Foundation.TypedEventHandler<
    TouchpadGesturesController,
    Windows.UI.Core.PointerEventArgs> PointerPressed;

event Windows.Foundation.TypedEventHandler<
    TouchpadGesturesController,
    Windows.UI.Core.PointerEventArgs> PointerMoved;

event Windows.Foundation.TypedEventHandler<
    TouchpadGesturesController,
    Windows.UI.Core.PointerEventArgs> PointerReleased;
```

These events are triggered for the "manipulation" style gestures. They work identically to how pointer input would typically flow to an application — each finger will trigger **PointerPressed**, followed by zero or more **PointerMoved**, concluded by **PointerReleased**.

> [!NOTE]
> Pointer input for touchpads has some differences when compared to other pointer device types. See the remarks for [**GetPointerTouchpadInfo**](getpointertouchpadinfo.md) for more information.

> [!NOTE]
> While it is permissible to use Win32 APIs such as **GetPointerInfo** to query information about the pointer input while handling one of these events, **SkipPointerFrameMessages** should not be called. The **TouchpadGesturesController** performs processing on the input in addition to triggering the event and skipping the pointer messages could cause its processing to behave incorrectly.

#### GlobalActionPerformed

```cpp
event Windows.Foundation.TypedEventHandler<
    TouchpadGesturesController,
    TouchpadGlobalActionEventArgs> GlobalActionPerformed;
```

Triggered for the "action" style gestures.

- **[X]FingerTap**: Triggered by the user performing a multi-finger tap on the touchpad.
- **[X]FingerPress**: Triggered by the user pressing down on the touchpad's surface button with multiple fingers.
- **[X]FingerRelease**: Triggered by the user releasing the touchpad's surface button after the above event.

## Related enumerations

### TouchpadGlobalGestureKinds

```cpp
[flags]
enum TouchpadGlobalGestureKinds
{
    None                        = 0x0,
    ThreeFingerManipulations    = 0x1,
    FourFingerManipulations     = 0x2,
    FiveFingerManipulations     = 0x4,
    ThreeFingerActions          = 0x8,
    FourFingerActions           = 0x10,
    FiveFingerActions           = 0x20,
};
```

| Value | Meaning |
|-------|---------|
| **None** (0x0) | No gestures. |
| **ThreeFingerManipulations** (0x1) | Three-finger swipe/drag gestures. |
| **FourFingerManipulations** (0x2) | Four-finger swipe/drag gestures. |
| **FiveFingerManipulations** (0x4) | Five-finger swipe/drag gestures. |
| **ThreeFingerActions** (0x8) | Three-finger tap and button press gestures. |
| **FourFingerActions** (0x10) | Four-finger tap and button press gestures. |
| **FiveFingerActions** (0x20) | Five-finger tap and button press gestures. |

### TouchpadGlobalAction

```cpp
enum TouchpadGlobalAction
{
    ThreeFingerTap,
    FourFingerTap,
    FiveFingerTap,
    ThreeFingerPress,
    FourFingerPress,
    FiveFingerPress,
    ThreeFingerRelease,
    FourFingerRelease,
    FiveFingerRelease,
};
```

| Value | Meaning |
|-------|---------|
| **ThreeFingerTap** | Three-finger tap on the touchpad. |
| **FourFingerTap** | Four-finger tap on the touchpad. |
| **FiveFingerTap** | Five-finger tap on the touchpad. |
| **ThreeFingerPress** | Three-finger press on the touchpad's surface button. |
| **FourFingerPress** | Four-finger press on the touchpad's surface button. |
| **FiveFingerPress** | Five-finger press on the touchpad's surface button. |
| **ThreeFingerRelease** | Release after a three-finger press. |
| **FourFingerRelease** | Release after a four-finger press. |
| **FiveFingerRelease** | Release after a five-finger press. |

## Requirements

| Requirement | Value |
|-----|-----|
| Minimum supported client | Windows 11 |
| Namespace | Windows.UI.Input |
| API contract | Windows.Foundation.UniversalApiContract (version 19) |
| IIDs | ITouchpadGesturesController: 28c13cdd-e068-549f-89c6-1a440c6fc327, ITouchpadGesturesControllerStatics: 207ef171-1a73-51cd-a694-8840e09dbafa, ITouchpadGlobalActionEventArgs: 6edad206-e4e3-5f39-9d13-8575e8e2a12b |

## See also

- [**PhysicalGestureRecognizer**](physicalgesturerecognizer.md)
- [**RegisterTouchpadCapableWindow**](registertouchpadcapable.md)
- [**InjectTouchpadAction**](injecttouchpadaction.md)
- [Precision Touchpad Programming Guide](precision-touchpad-guide.md)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
