---
Description: The StylusInput APIs allow you to interact with the tablet pen data stream. To interact with the data stream add a RealTimeStylus object to your application, and add plug-ins to the RealTimeStylus object.
ms.assetid: 88bab0ab-df9f-4813-9a9f-9a137813f0b4
title: Architecture of the StylusInput APIs
ms.topic: article
ms.date: 05/31/2018
---

# Architecture of the StylusInput APIs

The StylusInput APIs allow you to interact with the tablet pen data stream. To interact with the data stream add a [**RealTimeStylus**](realtimestylus-class.md) object to your application, and add plug-ins to the **RealTimeStylus** object.

Two plug-ins are provided in the StylusInput APIs. The [**DynamicRenderer**](https://msdn.microsoft.com/en-us/library/ms701168(v=VS.85).aspx) object implements the [**IStylusSyncPlugin**](https://msdn.microsoft.com/en-us/library/ms704312(v=VS.85).aspx) interface. The **DynamicRenderer** object renders the ink in real time, as it is being drawn. The [**GestureRecognizer**](gesturerecognizer-class.md) object implements the **IStylusSyncPlugin** and [**IStylusAsyncPlugin**](https://msdn.microsoft.com/en-us/library/ms702522(v=VS.85).aspx) interfaces. The **GestureRecognizer** object recognizes application gestures.

## Definitions

The following terms are used in the sections describing the StylusInput APIs:

Synchronous plug-in

A class that implements the [**IStylusSyncPlugin**](https://msdn.microsoft.com/en-us/library/ms704312(v=VS.85).aspx) interface. Synchronous plug-ins are generally called directly by the [**RealTimeStylus**](realtimestylus-class.md) object.

Asynchronous plug-in

A class that implements the [**IStylusAsyncPlugin**](https://msdn.microsoft.com/en-us/library/ms702522(v=VS.85).aspx) interface. Asynchronous plug-ins are generally called on the application's user interface (UI) thread.

Synchronous plug-in collection

A [StylusSyncPluginCollection](https://msdn.microsoft.com/library/ms824788(v=MSDN.10).aspx) collection, which is an ordered collection of [IStylusSyncPlugin](https://msdn.microsoft.com/library/ms824751(v=MSDN.10).aspx) objects. A synchronous plug-in collection usually refers to the collection assigned to the [SyncPluginCollection](https://msdn.microsoft.com/library/ms824833(v=MSDN.10).aspx) property of a [RealTimeStylus](https://msdn.microsoft.com/library/ms824830(v=MSDN.10).aspx) object. Only synchronous plug-ins may be added to a synchronous plug-in collection.

Asynchronous plug-in collection

A [StylusAsyncPluginCollection](https://msdn.microsoft.com/library/ms824808(v=MSDN.10).aspx) collection, which is an ordered collection of [IStylusAsyncPlugin](https://msdn.microsoft.com/library/ms824768(v=MSDN.10).aspx) objects. An asynchronous plug-in collection usually refers to the collection assigned to the [AsyncPluginCollection](https://msdn.microsoft.com/library/ms824831(v=MSDN.10).aspx) property of a [RealTimeStylus](https://msdn.microsoft.com/library/ms824830(v=MSDN.10).aspx) object. Only asynchronous plug-ins may be added to an asynchronous plug-in collection.

## Synchronous and Asynchronous Plug-ins

The [**RealTimeStylus**](realtimestylus-class.md) object is designed to provide real-time access to the data stream from a tablet pen. Create or use synchronous plug-ins for tasks that require real-time access to the data stream and are computationally undemanding, such as for packet filtering. Create or use asynchronous plug-ins for tasks that do not require real-time access to the data stream, such as for creating and storing strokes in an [**InkDisp**](inkdisp-class.md) object.

Certain tasks may be computationally demanding yet require real-time access to the data stream, such as multistroke gesture recognition. To address these needs, the StylusInput APIs provide a cascaded [**RealTimeStylus**](realtimestylus-class.md) model that allows you to use two **RealTimeStylus** objects, each running on its own thread. For more information about the cascaded **RealTimeStylus** model, see [The Cascaded RealTimeStylus Model](the-cascaded-realtimestylus-model.md).

For more information about using and creating plug-ins, see [Working with the StylusInput APIs](working-with-the-stylusinput-apis.md).

## The Tablet Pen Data Stream

The [**RealTimeStylus**](realtimestylus-class.md) object has two internal queues that carry the tablet pen data, the input queue and the output queue. The pen data is converted into instances of the classes in the [Microsoft.StylusInput.PluginData](https://msdn.microsoft.com/library/ms823992(v=MSDN.10).aspx) namespace. The following list describes how the **RealTimeStylus** object handles the tablet pen data:

The [**RealTimeStylus**](realtimestylus-class.md) object checks for plug-in data objects first on its input queue and then from the tablet pen data stream.

The [**RealTimeStylus**](realtimestylus-class.md) object sends one plug-in data object to the objects in its synchronous plug-in collection. Each synchronous plug-in can add data to either the input or output queue.

After the plug-in data object has been sent to all members of the synchronous plug-in collection, the plug-in data object is placed on the [**RealTimeStylus**](realtimestylus-class.md) object's output queue.

The [**RealTimeStylus**](realtimestylus-class.md) object then checks for the next plug-in data object to process.

While the [**RealTimeStylus**](realtimestylus-class.md) object's output queue contains data, the **RealTimeStylus** object sends one plug-in data object from its output queue to the objects in its asynchronous plug-in collection. Each asynchronous plug-in can add data to either the input or output queue. However, because the asynchronous plug-ins run on the UI thread, the data is added to the queue in relation to the current pen data the **RealTimeStylus** object is processing, and not in relation to the data that the asynchronous plug-in is processing.

The following diagram illustrates the flow of tablet pen data through the [**RealTimeStylus**](realtimestylus-class.md) object and its plug-in collections.

![flow of tablet pen data through the realtimestylus object and its plug-in collections](images/5a698bc9-833b-4b24-9fa2-70be0ca61032.gif)

In this diagram, the circles labeled "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](realtimestylus-class.md) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle labeled "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. It is sent to the synchronous plug-in collection and placed on the output queue. The empty circle represents the position in the output queue where future tablet pen data is added.

For more information about how specific data is added to the queue and processed, see [Plug-in Data and the RealTimeStylus Class](plug-in-data-and-the-realtimestylus-class.md).

## The StylusInput APIs

The StylusInput APIs reside primarily in the [Microsoft.StylusInput](https://msdn.microsoft.com/library/ms824750(v=MSDN.10).aspx) and [Microsoft.StylusInput.PluginData](https://msdn.microsoft.com/library/ms823992(v=MSDN.10).aspx) namespaces. However, the StylusInput APIs also reference some classes in the [Microsoft.Ink](https://msdn.microsoft.com/library/ms826516(v=MSDN.10).aspx) namespace, such as the [Tablet](https://msdn.microsoft.com/library/ms827783(v=MSDN.10).aspx) class, the [TabletPropertyDescriptionCollection](https://msdn.microsoft.com/library/ms827760(v=MSDN.10).aspx) collection, and the [ApplicationGesture](https://msdn.microsoft.com/library/ms827547(v=MSDN.10).aspx) and [SystemGesture](https://msdn.microsoft.com/library/ms827134(v=MSDN.10).aspx) enumerations.

## Related topics

<dl> <dt>

[**DynamicRenderer**](https://msdn.microsoft.com/en-us/library/ms701168(v=VS.85).aspx)
</dt> <dt>

[**GestureRecognizer**](gesturerecognizer-class.md)
</dt> <dt>

[**RealTimeStylus**](realtimestylus-class.md)
</dt> <dt>

[**IStylusAsyncPlugin**](https://msdn.microsoft.com/en-us/library/ms702522(v=VS.85).aspx)
</dt> <dt>

[**IStylusSyncPlugin**](https://msdn.microsoft.com/en-us/library/ms704312(v=VS.85).aspx)
</dt> <dt>

[Working with the StylusInput APIs](working-with-the-stylusinput-apis.md)
</dt> <dt>

[The Cascaded RealTimeStylus Model](the-cascaded-realtimestylus-model.md)
</dt> </dl>

 

 



