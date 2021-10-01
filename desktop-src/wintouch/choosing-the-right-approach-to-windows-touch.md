---
title: Choosing the Right Approach to Windows Touch
description: This section explains the different approaches to Windows Touch that you can use.
ms.assetid: 983023e4-355b-45ba-8572-d93c460d2ff8
keywords:
- Windows Touch,different approaches
- Windows Touch,choosing approaches
- Windows Touch,enhancing applications
- Windows Touch,zoom support
- Windows Touch,legacy support
- Windows Touch,RealTimeStylus plug-in
ms.topic: article
ms.date: 10/01/2021
---

# Choosing the Right Approach to Windows Touch

This section explains the different approaches to Windows Touch that you can use.

You can enhance applications using Windows Touch features in many ways. Before you adopt a method, you should consider what you want to do with your application. The following scenarios are typical for Windows Touch:

- You want your application to behave the same as in legacy versions of Windows but want Windows Touch messages to behave consistently.
- You want custom object rotation, translation, panning, or zoom support in your application.
- You want your application to have fine-grained interpretation of Windows Touch gestures or to interpret multiple touches on an application that is specifically optimized for Windows Touch input.
- You have an application that uses the [**RealTimeStylus**](/windows/desktop/api/rtscom/nn-rtscom-irealtimestylus) object and want to enhance it with Windows Touch capabilities.

## You want your application to behave as it did in legacy versions of Windows

In Windows 7, applications by default generate messages that enable Windows Touch functionality. For example, pan gestures trigger WM\_\*SCROLL messages. In addition to pan support, the default WM\_GESTURE handler in Windows 7 supports boundary feedback, zoom, and press and tap. Boundary feedback is enabled through legacy support as well. See the [Windows Touch Gestures Overview](windows-touch-gestures-overview.md) for more information on how gestures map to messages. Developers who want only this basic functionality do not need to directly work with the Windows Touch API.

> [!Note]  
> Custom scroll bar handlers must support the **SM\_THUMBPOSITION** request for **WM\_VSCROLL** messages and must support the **SB\_LINELEFT** request and **SB\_LINERIGHT** request for **WM\_HSCROLL** messages.

- The [Legacy Support for Panning with Scroll Bars](legacy-support-for-panning-with-scrollbars.md) section explains how to ensure that your application behaves as users expect in Windows 7.

## You want custom object rotation, translation, panning, or zoom support

If you want limited support for touch but the default behavior that Windows 7 offers is not adequate for your application, you can use gestures to enhance your application. By using gestures, you can interpret the gesture commands by handling the [**WM\_GESTURE**](wm-gesture.md) message. More information on gestures can be found in the section [Windows Touch Gestures](guide-multi-touch-gestures.md). If your application needs support only for high-granularity rotations, improved zooming support, or single-finger panning, gestures is the best approach to take for Windows Touch development. In addition to interpreting the gesture message, you can opt to have support for boundary feedback. For more information on boundary feedback, see the [Boundary Feedback](boundary-feedback.md) section of the [Windows Touch Programming Reference](windows-touch-programming-reference.md). In Windows 7, the command prompt and Internet Explorer take advantage of boundary feedback and gestures.

- The [Improving the Single Finger Panning Experience](improving-the-single-finger-panning-experience.md) section explains how to customize the panning experience by handling the [**WM\_GESTURE**](wm-gesture.md) message.

## You want fine-grained gesture interpretation or custom handling of multiple touch points

If you want to have even more specific control of gestures than is offered by the [**WM\_GESTURE**](wm-gesture.md) message, or you want to interpret multiple gestures on multiple objects, you should use the manipulation processor. The manipulation processor essentially is a superset of gestures. Using the manipulation processor requires that you implement an event sink for manipulations that you feed raw touch data to.

If you want simple object physics in addition to interpreting the gestures, you should use an inertia processor in conjunction with the manipulation processor. The inertia processor works with the manipulation processor by taking velocity values from the manipulation processor upon manipulation completion.

If you want to interpret multiple touch points in your application, you should create a message handler for the [**WM\_TOUCH**](wm-touchdown.md) message.

- The [Windows Touch Input](guide-multi-touch-input.md) section explains how you can interpret the [**WM\_TOUCH**](wm-touchdown.md) message.
- The [Detecting and Tracking Multiple Touch Points](detecting-and-tracking-multiple-touch-points.md) section demonstrates how to create a simple application that interprets multiple inputs.
- The [Manipulations and Inertia](manipulation-and-inertia.md) section explains how to enable the most flexible approach to Windows Touch.

> [!Important]
> **Windows 11 and newer**
>
> *Some three- and four-finger touch interactions will no longer work in Windows apps by default.*
>
> By default, three- and four-finger touch interactions are now consumed by the system for operations such as switching or minimizing windows and changing virtual desktops. As these interactions are now handled at the system level, your app's functionality could be affected by this change.
>
> To support three- or four-finger interactions within an application, a new user setting has been introduced that specifies whether or not the system handles these interactions:
>
> **Bluetooth & devices > Touch > "Three- and four-finger touch gestures"**
>
> When set to "On" (default), the system will handle all three- and four-finger interactions (apps will not be able to support them).
>
> When set to "Off", three- and four-finger interactions can be supported by apps (they will not be handled by the system).
>
> If your application is reliant upon these interactions, you should direct users to this setting.

## You want to enable Windows Touch input to an application that uses the RealTimeStylus

If you want to enable input for multiple contacts on the Tablet PC platform, you must implement a custom RealTimeStylus plug-in that interprets the Windows Touch data. Microsoft introduced the [**ITablet3**](/windows/desktop/tablet/itablet3) and [**IRealTimeStylus3**](/windows/desktop/api/rtscom/nn-rtscom-irealtimestylus3) interfaces to enable input from multiple contacts in the RealTimeStylus plug-in. These interfaces simplify extending RealTimeStylus plug-ins to support multiple contact points.

To check whether support for multiple contacts is enabled, call [**IsMultiTouch**](/windows/desktop/tablet/itablet3-ismultitouch). To check the number of supported contacts, call [**GetMaximumCursors**](/windows/desktop/tablet/itablet3-getmaximumcursors). To enable or disable multiple contact support, call [**MultiTouchEnabled**](/windows/desktop/api/rtscom/nf-rtscom-irealtimestylus3-get_multitouchenabled).

> [!Note]  
> If you don't enable multiple contact points in the RealTimeStylus, you will receive gesture messages such as pan and zoom.

## Related topics

[Programming Guide](programming-guide.md)
