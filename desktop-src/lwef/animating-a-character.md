---
title: Animating a Character
description: Animating a Character
ms.assetid: ed42de30-acac-41e8-bacb-4caaff254724
ms.topic: article
ms.date: 05/31/2018
---

# Animating a Character

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Once a character is loaded, you can use several of Microsoft Agent's methods for animating the character. The first one you use is typically the [**Show**](show-method.md) method. **Show** makes the character's frame visible and plays the animation assigned to the character's **Showing** state.

Once the character's frame is visible, you can use the [**Play**](play-method.md) method, specifying the name of an animation, to play that animation. Animation names are specific to a character definition. As an animation plays, the shape of its window changes to match the image in the frame. This results in a movable graphic image, or *sprite*, displayed on top of the desktop and all windows, or *z-order*.

If the character's file is stored locally, you can simply call the [**Play**](play-method.md) method. In other cases, such as when you have loaded an .ACF character from an HTTP server, you must use the [**Get**](get-method.md) (or [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare)) method to first retrieve the animation data. This will cause Agent to request the animation file from the server and store it in the browser's buffer on the local machine.

The [**Speak**](speak-method.md) method enables you to program the character to speak, automatically lip-syncing the output. Further details are covered in the Output section of this document.

You can use the [**MoveTo**](moveto-method.md) method to position the character at a new location. When you call the **MoveTo** method, Microsoft Agent automatically plays the appropriate animation based on the character's current location, then moves the character's frame. Similarly, when you call [**GestureAt**](gestureat-method.md), Microsoft Agent plays the appropriate gesturing animation based on the character's location and the location specified in the call.

To hide the character, call the [Hide](hide-method.md) method. This automatically plays the character associated with the character's **Hiding** state, then hides the character's frame. However, you can also hide or show a character by setting the character's [**Visible**](visible-property.md) property.

Microsoft Agent processes all animation calls, or *requests*, asynchronously. This enables your application's code to continue handling other events while the request is being processed. For example, calls to the [**Play**](play-method.md) method place the animation in a queue for the character so that the animations can be played sequentially. However, this means you cannot assume that a call to other functions will necessarily execute after an animation it follows in your code. For example, typically, a statement following a call to **Play** or [**MoveTo**](moveto-method.md) will execute before the animation finishes.

You can synchronize your code with animations in a character's queue by creating an object reference to the animation request, and, when the animation starts or completes, monitoring the [Request](the-request-object.md) events that the server uses to notify clients of the character. For example, if you want a message box to appear when the character finishes an animation, you can put the message box call in your [**RequestComplete**](requestcomplete-event.md) event handling subroutine, checking for the particular request ID.

When a character is hidden, the server does not play animations; however, it still queues and processes the animation request (plays the animation) and passes a request status back to the client. In the hidden state, the character cannot become input-active. However, if the user speaks the name of the character (when speech input is enabled), the server automatically shows the character.

When your client application loads multiple characters at the same time, Microsoft Agent's animation services enable you to animate characters independently or use the [**Wait**](wait-method.md), [**Interrupt**](interrupt-method.md), or [**Stop**](stop-method.md) methods to synchronize their animation with each other.

Microsoft Agent also plays other animations automatically for you. For example, if the character's state has not changed for several seconds, Agent begins playing animations assigned to the character's **Idling** animations. Similarly, when speech input is enabled, Agent plays the character's **Listening** animations and then **Hearing** animations when an utterance is detected. These server-managed animations are called *states*, and are defined when a character is created. For more information, see [Designing Characters for Microsoft Agent](agent-states.md).

 

 