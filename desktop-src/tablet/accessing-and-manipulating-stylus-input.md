---
description: The Tablet PC includes technology for interacting with tablet pen data as it is being gathered.
ms.assetid: e026f860-be4d-40a5-b951-15b8be3cd626
title: Accessing and Manipulating Stylus Input
ms.topic: article
ms.date: 05/31/2018
---

# Accessing and Manipulating Stylus Input

The Tablet PC includes technology for interacting with tablet pen data as it is being gathered. The [**RealTimeStylus**](realtimestylus-class.md) class is part of the StylusInput application programming interfaces (API), which provide access to the tablet pen data stream. These APIs allow you to capture, interrupt, and modify the stream independently from rendering and collecting ink.

The StylusInput APIs are designed to:

-   Provide real-time access to the tablet pen data stream.
-   Keep the user interface (UI) thread from blocking dynamic ink rendering by queuing the packet data on the UI thread and making ink collection single threaded.
-   Increase the performance and lower the overall thread usage over using the [**InkCollector**](inkcollector-class.md) object, [**InkOverlay**](inkoverlay-class.md) object, [InkPicture](inkpicture-control-reference.md) control, or [InkEdit](inkedit-control-reference.md) control to collect ink.

The StylusInput APIs are not designed to work with the [**InkCollector**](inkcollector-class.md) object, [**InkOverlay**](inkoverlay-class.md) object, [InkPicture](inkpicture-control-reference.md) control, or [InkEdit](inkedit-control-reference.md) control.

When you need to interact directly with the tablet pen data stream or when your application may block real-time inking, use the [**RealTimeStylus**](realtimestylus-class.md) object. Use the [**InkCollector**](inkcollector-class.md) object, [**InkOverlay**](inkoverlay-class.md) object, [InkPicture](inkpicture-control-reference.md) control, or [InkEdit](inkedit-control-reference.md) control when the default behavior of these objects provides the behavior you need.

## In This Section

The following sections describe elements of the StylusInput APIs:

-   [Architecture of the StylusInput APIs](architecture-of-the-stylusinput-apis.md)
-   [Working with the StylusInput APIs](working-with-the-stylusinput-apis.md)
    -   [Working with the RealTimeStylus Class](working-with-the-realtimestylus-class.md)
    -   [Plug-ins and the RealTimeStylus Class](plug-ins-and-the-realtimestylus-class.md)
    -   [Plug-in Data and the RealTimeStylus Class](plug-in-data-and-the-realtimestylus-class.md)
    -   [Implementation Notes for the StylusInput APIs](implementation-notes-for-the-stylusinput-apis.md)
    -   [Ink-Collection Plug-ins](ink-collection-plug-ins.md)
    -   [Dynamic-Renderer Plug-ins](dynamic-renderer-plug-ins.md)
    -   [Recognizer Plug-ins](recognizer-plug-ins.md)
-   [Considerations when Using the StylusInput APIs](considerations-when-using-the-stylusinput-apis.md)
    -   [Design Considerations for the StylusInput APIs](design-considerations-for-the-stylusinput-apis.md)
    -   [Threading Considerations for the StylusInput APIs](threading-considerations-for-the-stylusinput-apis.md)

[The Cascaded RealTimeStylus Model](the-cascaded-realtimestylus-model.md)

-   [Error Handling Considerations for the StylusInput APIs](error-handling-considerations-for-the-stylusinput-apis.md)
-   [Performance Considerations for the StylusInput APIs](performance-considerations-for-the-stylusinput-apis.md)
-   [Partial Trust Considerations for the StylusInput APIs](partial-trust-considerations-for-the-stylusinput-apis.md)

## Related topics

<dl> <dt>

[RealTimeStylus Plug-in Sample](realtimestylus-plug-in-sample.md)
</dt> <dt>

[RealTimeStylus Ink Collection Sample](realtimestylus-ink-collection-sample.md)
</dt> </dl>

 

 



