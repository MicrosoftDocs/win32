---
Description: Overview of using gestures.
ms.assetid: 5bc80086-7acf-4f86-a9fb-a663de489f8b
title: Using Gestures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Gestures

The Tablet PC platform provides the Microsoft gesture recognizer for supporting application gestures. For a list of gestures supported by the Microsoft gesture recognizer, see the table of application gestures in the [**ApplicationGesture**](/windows/win32/msinkaut/ne-msinkaut-inkapplicationgesture?branch=master) enumeration. The Tablet PC also supports system gestures. For a list of system gestures supported by the Tablet PC, see the table of system gestures in the [**SystemGesture**](/windows/win32/msinkaut/ne-msinkaut-inksystemgesture?branch=master) enumeration.

## Microsoft Gesture Recognizer

You can employ the Microsoft gesture recognizer by using the [**CollectionMode**](/windows/win32/msinkaut/nf-msinkaut-iinkcollector-put_collectionmode?branch=master) property of the [**InkCollector**](/windows/win32/msinkaut/?branch=master) object, the [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object, or the [InkPicture](inkpicture-control-reference.md) control. Setting the **CollectionMode** property to mixed mode (**InkAndGesture**) or gesture-only mode (**GestureOnly**) passes ink to the Microsoft gesture recognizer by default. You can employ the Microsoft gesture recognizer with the [InkEdit](inkedit-control-reference.md) control by setting the [**InkMode**](/windows/win32/inked/?branch=master) property to **InkAndGesture**. You can also use gesture recognition with the [**RealTimeStylus**](/windows/win32/RTSCom/nn-rtscom-irealtimestylus?branch=master) object by adding a [**GestureRecognizer**](/windows/win32/RTSCom/?branch=master) object to one of its plug-in collections.

However, if the gestures that you want to use are not supported by the current version of the Microsoft gesture recognizer, you can build your own recognizer and use it in conjunction with the Microsoft gesture recognizer. This allows full support for the gestures in your application.

The Tablet PC uses a pen for some or all input. This makes it extremely easy to write ink. The Tablet PC platform delivers architecture for pen input that supports a tiered structure of gestures. Gestures and mapping are defined to allow the user to write and invoke advanced gestures on new surfaces, while reserving gestures that invoke traditional mouse messages of other Windows-based applications.

The Tablet PC platform introduces two levels of gestures: system gestures, also known as system events, and application gestures. The pen architecture supports both system and application gestures. Both single-stroke and multiple-stroke application gestures are supported.

## Related topics

<dl> <dt>

[Application Gestures](application-gestures.md)
</dt> <dt>

[Flicks Gestures](flicks-gestures.md)
</dt> <dt>

[System Gestures](system-gestures.md)
</dt> </dl>

 

 



