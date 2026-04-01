---
title: PhysicalGestureRecognizer class (Windows.UI.Input)
description: Performs gesture recognition on pointer input with output in device-relative coordinates, suited for touchpad input where gestures should be recognized relative to the touchpad itself.
ms.topic: reference
ms.date: 03/28/2026
---

# PhysicalGestureRecognizer class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Performs gesture recognition on the pointer input fed to it, with the output returned in units relative to the device, rather than the display-independent pixels returned by [**GestureRecognizer**](/uwp/api/windows.ui.input.gesturerecognizer). These output units are better suited for touchpad input so that gestures can be recognized relative to the touchpad itself rather than to the display.

Once pointer input is fed to the recognizer, it becomes active. It stays active until the input interaction is complete — either by feeding departing input for all contacts or by forcibly completing it via **CompleteGesture()**.

All APIs function identically to their counterparts in **GestureRecognizer**. The only difference is the coordinate space of the recognized output exposed via the gesture events.

**Namespace:** Windows.UI.Input

## Members

### Constructor

```cpp
PhysicalGestureRecognizer();
```

Returns a new instance of the **PhysicalGestureRecognizer** runtimeclass.

### Properties

#### IsActive

```cpp
Boolean IsActive { get; }
```

Returns whether an input interaction is still being processed.

#### GestureSettings

```cpp
Windows.UI.Input.GestureSettings GestureSettings;
```

Gets or sets the gestures that are configured for recognition. The **PhysicalGestureRecognizer** supports the following subset of gestures:

- **Tap**
- **Hold**
- **ManipulationTranslate[Rails][X,Y]**
- **ManipulationRotate**
- **ManipulationScale**
- **ManipulationMultipleFingerPanning**

Touchpad input will never be recognized as Tap or Hold, since touchpad input is only received in scenarios where those gestures are no longer possible to perform.

#### TapMinContactCount

```cpp
UInt32 TapMinContactCount;
```

Gets or sets the minimum number of contacts required for a tap to be recognized.

#### TapMaxContactCount

```cpp
UInt32 TapMaxContactCount;
```

Gets or sets the maximum number of contacts required for a tap to be recognized.

#### HoldMinContactCount

```cpp
UInt32 HoldMinContactCount;
```

Gets or sets the minimum number of contacts required for a hold to be recognized.

#### HoldMaxContactCount

```cpp
UInt32 HoldMaxContactCount;
```

Gets or sets the maximum number of contacts required for a hold to be recognized.

#### HoldRadius

```cpp
Single HoldRadius;
```

Gets or sets the radius within which a contact must stay from its original down location for a tap or hold to be recognized.

#### HoldStartDelay

```cpp
Windows.Foundation.TimeSpan HoldStartDelay;
```

Gets or sets the amount of time a contact must stay down before a hold is recognized. If the contact's duration is less than this value when it departs, and it has not traveled further than the **HoldRadius**, then a tap is recognized.

#### TranslationMinContactCount

```cpp
UInt32 TranslationMinContactCount;
```

Gets or sets the minimum number of contacts required for a translation to be recognized.

#### TranslationMaxContactCount

```cpp
UInt32 TranslationMaxContactCount;
```

Gets or sets the maximum number of contacts required for a translation to be recognized.

### Methods

#### ProcessDownEvent, ProcessMoveEvents, ProcessUpEvent

```cpp
void ProcessDownEvent(Windows.UI.Input.PointerPoint value);
void ProcessMoveEvents(IVector<Windows.UI.Input.PointerPoint> value);
void ProcessUpEvent(Windows.UI.Input.PointerPoint value);
```

Feeds the specified pointer input to the **PhysicalGestureRecognizer** for gesture recognition.

#### CompleteGesture

```cpp
void CompleteGesture();
```

Completes the current interaction so that subsequent input is treated as a new gesture. If a gesture is currently in progress, events for its completion will be triggered.

### Events

#### ManipulationStarted

```cpp
event Windows.Foundation.TypedEventHandler<
    PhysicalGestureRecognizer,
    Windows.UI.Input.ManipulationStartedEventArgs> ManipulationStarted;
```

Triggered when the **PhysicalGestureRecognizer** begins recognizing a manipulation.

#### ManipulationUpdated

```cpp
event Windows.Foundation.TypedEventHandler<
    PhysicalGestureRecognizer,
    Windows.UI.Input.ManipulationUpdatedEventArgs> ManipulationUpdated;
```

Triggered when the **PhysicalGestureRecognizer** receives updated input during a manipulation.

#### ManipulationCompleted

```cpp
event Windows.Foundation.TypedEventHandler<
    PhysicalGestureRecognizer,
    Windows.UI.Input.ManipulationCompletedEventArgs> ManipulationCompleted;
```

Triggered when the **PhysicalGestureRecognizer** finishes recognizing a manipulation.

#### Tapped

```cpp
event Windows.Foundation.TypedEventHandler<
    PhysicalGestureRecognizer,
    Windows.UI.Input.TappedEventArgs> Tapped;
```

Triggered when the **PhysicalGestureRecognizer** recognizes a tap.

#### Holding

```cpp
event Windows.Foundation.TypedEventHandler<
    PhysicalGestureRecognizer,
    Windows.UI.Input.HoldingEventArgs> Holding;
```

Triggered when the **PhysicalGestureRecognizer** recognizes a hold gesture.

## Requirements

| Requirement | Value |
|-----|-----|
| Minimum supported client | Windows 11 |
| Namespace | Windows.UI.Input |
| API contract | Windows.Foundation.UniversalApiContract (version 19) |
| IID | IPhysicalGestureRecognizer: 79a29f4d-32a6-5aa5-a999-42b0b420c66d |

## See also

- [**GestureRecognizer**](/uwp/api/windows.ui.input.gesturerecognizer)
- [**TouchpadGesturesController**](touchpadgesturescontroller.md)
- [**IPointerPointPhysicalPosition**](ipointerpointphysicalposition.md)
- [Precision Touchpad Programming Guide](precision-touchpad-guide.md)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
