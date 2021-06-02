---
title: Interaction
description: Interaction is the variety of ways users interact with your app, including touch, keyboard, mouse, and so on. Use these guidelines to create intuitive and distinctive experiences that are optimized for touch but work consistently across input devices.
ms.assetid: 1509c885-f4dc-4cf9-86a3-cc6754d3b4a0
ms.topic: article
ms.date: 10/20/2020
---

# Interaction

> [!NOTE]
> This design guide was created for Windows 7 and has not been updated for newer versions of Windows. Much of the guidance still applies in principle, but the presentation and examples do not reflect our [current design guidance](/windows/uwp/design/).

Interaction is the variety of ways users interact with your app, including touch, keyboard, mouse, and so on. Use these guidelines to create intuitive and distinctive experiences that are optimized for touch but work consistently across input devices.

## Design for a touch-first experience

First and foremost, design your app with the expectation that touch will be the primary input method of your users. If you use the platform controls, support for touchpad, mouse, and pen/stylus requires no additional programming, because Windows provides this for free.

However, keep in mind that a UI optimized for touch is not always superior to a traditional UI. Both provide advantages and disadvantages unique to the technology and application. In the move to a touch-first UI, it's important to understand the core differences between touch (including touchpad), pen/stylus, mouse, and keyboard input. Don't take familiar input device properties and behaviors for granted, as touch in Windows 8 does more than simply emulate that functionality.

As you'll soon discover, touch input requires a different approach to UI design.

**Compare touch interaction requirements**

This table shows some of the differences between input devices that you should consider when you design touch-optimized Windows Store apps.



|                                 |                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                 |                                                     |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **Factor**<br/>           | **Touch interactions**<br/>                                                                                                                                                                                | **Mouse, keyboard, pen/stylus interactions**<br/>                                                                                                                                                                                                                                                         | **Touchpad**<br/>                             |
| **Precision**<br/>        | The contact area of a fingertip is greater than a single x-y coordinate, which increases the chances of unintended command activations.<br/>                                                               | The mouse and pen/stylus supply a precise x-y coordinate.<br/>                                                                                                                                                                                                                                            | Same as mouse.<br/>                           |
|                                 | The shape of the contact area changes throughout the movement. <br/>                                                                                                                                       | Mouse movements and pen/stylus strokes supply precise x-y coordinates. Keyboard focus is explicit.<br/>                                                                                                                                                                                                   | Same as mouse.<br/>                           |
|                                 | There is no mouse cursor to assist with targeting.<br/>                                                                                                                                                    | The mouse cursor, pen/stylus cursor, and keyboard focus all assist with targeting.<br/>                                                                                                                                                                                                                   | Same as mouse.<br/>                           |
| **Human anatomy**<br/>    | Fingertip movements are imprecise, because a straight-line motion with one or more fingers is difficult. This is due to the curvature of hand joints and the number of joints involved in the motion.<br/> | It's easier to perform a straight-line motion with the mouse or pen/stylus because the hand that controls them travels a shorter physical distance than the cursor on the screen.<br/>                                                                                                                    | Same as mouse.<br/>                           |
|                                 | Some areas on the touch surface of a display device can be difficult to reach due to finger posture and the user's grip on the device.<br/>                                                                | The mouse and pen/stylus can reach any part of the screen while any control should be accessible by the keyboard through tab order. <br/>                                                                                                                                                                 | Finger posture and grip can be an issue.<br/> |
|                                 | Objects might be obscured by one or more fingertips or the user's hand. This is known as occlusion.<br/>                                                                                                   | Indirect input devices do not cause occlusion.<br/>                                                                                                                                                                                                                                                       | Same as mouse.<br/>                           |
| **Object state**<br/>     | Touch uses a two-state model: the touch surface of a display device is either touched (on) or not (off). There is no hover state that can trigger additional visual feedback.<br/>                         | A mouse, pen/stylus, and keyboard all expose a three-state model: up (off), down (on), and hover (focus).<br/> Hover lets users explore and learn through tooltips associated with UI elements. Hover and focus effects can relay which objects are interactive and also help with targeting. <br/> | Same as mouse.<br/>                           |
| **Rich interaction**<br/> | Supports multi-touch: multiple input points (fingertips) on a touch surface.<br/>                                                                                                                          | Supports a single input point.<br/>                                                                                                                                                                                                                                                                       | Same as touch.<br/>                           |
|                                 | Supports direct manipulation of objects through gestures such as tapping, dragging, sliding, pinching, and rotating.<br/>                                                                                  | No support for direct manipulation as mouse, pen/stylus, and keyboard are indirect input devices.<br/>                                                                                                                                                                                                    | Same as mouse.<br/>                           |



 

**Note**

Indirect input has had the benefit of more than 25 years of refinement. Features such as hover-triggered tooltips have been designed to solve UI exploration specifically for touchpad, mouse, pen/stylus, and keyboard input. UI features like this have been re-designed for the rich experience provided by touch input, without compromising the user experience for these other devices.

We provide some general user interaction guidelines here and cover device-specific guidelines in these topics.

-   [Touch](/windows/desktop/uxguide/inter-touch)
-   [Mouse](/windows/desktop/uxguide/inter-mouse)
-   [Pen](/windows/desktop/uxguide/inter-pen)
-   [Keyboard](/windows/desktop/uxguide/inter-keyboard)
-   [Accessibility](/windows/desktop/uxguide/inter-accessibility)

## Visuals for feedback

Appropriate visual feedback during interactions with your app helps users recognize, learn, and adapt to how their interactions are interpreted by both the app and Windows Visual feedback can indicate successful interactions, relay system status, improve the sense of control, reduce errors, help users understand the system and input device, and encourage interaction.

Visual feedback is critical when the user relies on touch input for activities that require accuracy and precision based on location. Display feedback whenever and wherever touch input is detected, to help the user understand any custom targeting rules that are defined by your app and its controls.

## Optimize for accuracy

Touch input involves the entire contact area of the finger. This contact geometry is used to determine the most likely target object. Size your controls to ensure a comfortable UI with objects and controls that are easy and safe to target.

Size, space, and position your controls to help eliminate finger and hand occlusion, where the UI is obscured by the user interaction itself.

Position menus, pop-ups, and tooltips above the contact area whenever possible.

## Constrain for confidence

Avoid, or minimize, sloppy interactions by using UI constraints.

-   Snap points can make it easier to stop at desired locations. Snap points specify logical stops in your app content. Cognitively, snap points act as a paging mechanism for the user and minimize fatigue from excessive sliding, swiping, or rotating. With them, you can handle imprecise user input and ensure a specific subset of content or key information is displayed.
-   Directional "rails" that emphasize the axis of motion (vertical or horizontal).

## Avoid timed interactions

Interactions should not be distinguished by time. The same interaction should have the same outcome regardless of the time taken to perform it. Time-based activations introduce mandatory delays for users and detract from both the immersive nature of direct manipulation and the perception of system responsiveness.

Timed interactions typically depend on invisible thresholds like time, distance, or speed to determine what command to perform. Timed interactions have no visual feedback until the system performs the action and users must reach arbitrary and invisible thresholds to achieve a result. Instant visual feedback during interactions make users feel more engaged, confident, and in control.

Interactions that directly affect objects and mimic real world interactions are more intuitive, discoverable, and memorable. They don't rely on obscure or abstract interactions.

**Note:** An exception to this is where you use specific timed interactions to assist in learning and exploration (for example, press and hold). Using appropriate descriptions and visual cues has a great effect on the use of advanced interactions.

