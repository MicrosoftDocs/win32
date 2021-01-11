---
description: The RealTimeStylus class enables you to interact with the data stream from the tablet pen. To interact with the data stream, add a RealTimeStylus object to your application, and add plug-ins to the RealTimeStylus object.
ms.assetid: 4009aeac-d290-4ea5-a6f5-199010acc84d
title: Working with the StylusInput APIs
ms.topic: article
ms.date: 05/31/2018
---

# Working with the StylusInput APIs

The [**RealTimeStylus**](realtimestylus-class.md) class enables you to interact with the data stream from the tablet pen. To interact with the data stream, add a **RealTimeStylus** object to your application, and add plug-ins to the **RealTimeStylus** object.

The plug-ins can modify the data associated with in-air packets, stylus down, packets, and stylus up notification methods. The plug-ins can cancel the in-air packets and packets notification methods. The plug-ins can also add application data to the stream in the form of [CustomStylusData](/previous-versions/ms575208(v=vs.100)) objects. The following list offers ideas for common categories of plug-ins that you may want to use or create.

-   Filter plug-in: An object that selectively removes or cancels data in the tablet pen data stream.
-   Modifier plug-in: An object that selectively modifies data in the tablet pen data stream.
-   Dynamic-renderer plug-in: An object that displays the tablet pen data in real-time as it is being handled by the [**RealTimeStylus**](realtimestylus-class.md) object. Later, for events such as a form refresh, the dynamic renderer plug-in or an ink collection plug-in might redraw the ink.
-   Recognizer plug-in: An object that scans the movement of the tablet pen for gestures, handwriting, or other glyphs.
-   Ink-collector plug-in: An object that from the tablet pen data stream creates and stores ink.
-   Wrapper plug-in: A plug-in that acts as an interface between the [**RealTimeStylus**](realtimestylus-class.md) object and another plug-in or object as a way of modifying the behavior of the wrapped object.

Both dynamic-renderer and ink-collection plug-ins can be created to render to various contexts—such as to a file, a stream, or to a display device. Ink can also be stored in various formats, such as an [Ink](/previous-versions/aa515768(v=msdn.10)) object, a fortified Graphics Interchange Format (GIF) file, an Ink Serialized Format (ISF) file, or other formats.

Two plug-ins are provided with the StylusInput APIs: the [**DynamicRenderer**](/previous-versions/windows/desktop/legacy/ms701168(v=vs.85)) class and the [**GestureRecognizer**](gesturerecognizer-class.md) class. The **DynamicRenderer** class provides basic rendering of the ink data in real time and is streamlined to have a minimal performance impact. The **GestureRecognizer** class provides gesture recognition for the [**RealTimeStylus**](realtimestylus-class.md) class.

## In This Section

-   [Working with the RealTimeStylus Class](working-with-the-realtimestylus-class.md)
-   [Plug-ins and the RealTimeStylus Class](plug-ins-and-the-realtimestylus-class.md)
-   [Plug-in Data and the RealTimeStylus Class](plug-in-data-and-the-realtimestylus-class.md)
-   [Implementation Notes for the StylusInput APIs](implementation-notes-for-the-stylusinput-apis.md)
-   [Ink-Collection Plug-ins](ink-collection-plug-ins.md)
-   [Dynamic-Renderer Plug-ins](dynamic-renderer-plug-ins.md)
-   [Recognizer Plug-ins](recognizer-plug-ins.md)

 

 
