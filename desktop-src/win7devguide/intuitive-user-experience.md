---
title: Intuitive User Experience
description: For the first time, Windows 7 allows developers and their end-users to control their computers by touching the screen.
ms.assetid: cf5be4d6-4284-43e3-86ba-293c4513b477
ms.topic: article
ms.date: 05/31/2018
---

# Intuitive User Experience

For the first time, Windows 7 allows developers and their end-users to control their computers by touching the screen. Touch and multi-touch features provide a natural, intuitive way for users to interact with PCs. The developer platform includes high-level gesture APIs, as well as low-level touch messages and touch input APIs. The top-level UI elements, such as the *Start* menu and *taskbar*, have larger targets than previous Windows releases, making them easier to select with a finger instead of a mouse. Visual feedback is provided for tap and double tap. Windows Explorer and Windows Internet Explorer 8 are both touch friendly and easily integrated with Windows 7 applications.

## Multi-Touch Gestures, and Manipulation and Inertia APIs

Windows 7 features improved touch and gesture support, empowering developers to quickly and easily create unique application experiences that go beyond simple mouse pointing, clicking, and dragging. The new multi-touch APIs support rich gestures, such as pan, zoom, and rotate. All gestures provide direct visual feedback, and interact with underlying content in a natural and intuitive manner. For example, a zoom gesture centers the view at the location of the gesture. Lower-level touch input APIs are also available for custom gesture definition and advanced touch-response experiences. Windows 7 provides a development platform that gives developers the tools they need to develop creative applications for multi-touch input devices, by processing user input from multi-touch devices and improving the user interface. The result is more intuitive environments, which enable innovations in PC interaction.

Windows 7 also provides platform support for object manipulation and inertia processing. A rich set of manipulation functions enable you to stretch, resize, or rotate multiple objects concurrently and in very fine granularity. For example, multiple digital photographs could be cropped, resized, and rotated in a single session using touch based gestures.

Windows 7 includes inertia APIs which simulate inertia when objects are moved, working hand-in-hand with the manipulation APIs. For example, in a photo application, you can use the manipulation APIs to let users rotate, resize, and move photos. Similarly, if a user "tosses" a photo, the inertia APIs provide natural interaction and enable the photo to coast to a stop or bounce off the borders of the application's window. (See [Windows Touch Programming Guide](../wintouch/programming-guide.md) and [Windows Touch: Developer Resources](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/Touch).)

## Single-Finger Panning

In many common applications, touch features are more useful for navigation than for text selection. With extended touch APIs, a developer's application can choose to enable panning rather than dragging. For example, if you created an application that uses multi-touch gestures for users playing music, you could allow these users to simply slide a finger up or down to adjust the volume, change songs, or download a file. No scrolling required.

Windows 7 provides endless opportunities for developers who are interested in creating applications for next-generation PCs. Best of all, it does the hard work of checking for scroll bars and implementing the panning semantics. Applications also receive a richer set of events and feedback for customized control of gestures than they did in previous versions of Windows. (See [Improving the Single-Finger Panning Experience](../wintouch/improving-the-single-finger-panning-experience.md).)

## Raw Touch Input Data

In Windows 7, new touch experiences are enabled by interaction models that access lower-level touch input messages, and provide customized responses to combinations of touch messages. The platform supports receiving raw touch input data for scenarios like multi-touch painting applications and custom gestures within an application. You can use the platform support for touch or create your own original, multi-touch experiences. (See [WM\_TOUCH Message](../wintouch/wm-touchdown.md).)

 

 