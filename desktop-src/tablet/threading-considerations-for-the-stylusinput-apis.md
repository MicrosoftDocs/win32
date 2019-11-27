---
Description: Overview of threading considerations when using the StylusInput application programming interface (API).
ms.assetid: 5d98768a-c60b-4bb0-8640-9bf38254d41f
title: Threading Considerations for the StylusInput API
ms.topic: article
ms.date: 05/31/2018
---

# Threading Considerations for the StylusInput API

The [**RealTimeStylus**](realtimestylus-class.md) object is designed to provide real-time access to the data stream from the tablet pen. Plug-ins, objects which implement the [**IStylusSyncPlugin**](https://msdn.microsoft.com/library/ms704312(v=VS.85).aspx) or [**IStylusAsyncPlugin**](https://msdn.microsoft.com/library/ms702522(v=VS.85).aspx) interface can be added to a **RealTimeStylus** object. Synchronous plug-ins are generally called directly by the **RealTimeStylus** object on a high-priority thread, while asynchronous plug-ins are generally called on the application's user interface (UI) thread. Create or use synchronous plug-ins for tasks that require real-time access to the data stream and are computationally undemanding, such as packet filtering. Create or use asynchronous plug-ins for tasks that do not require real-time access to the data stream, such as ink collection.

Because the plug-in data for the [**RealTimeStylus**](realtimestylus-class.md) object's asynchronous plug-in collection is queued, asynchronous plug-ins may receive data prior to receiving a call to its [RealTimeStylusDisabled](https://msdn.microsoft.com/library/ms824774(v=MSDN.10).aspx) method but after the **RealTimeStylus** object is disabled. Note that some of the **RealTimeStylus** object's methods and properties throw an exception if the **RealTimeStylus** object is disabled.

The following [**IStylusSyncPlugin**](https://msdn.microsoft.com/library/ms704312(v=VS.85).aspx) interface methods may call on a thread other than the tablet pen data thread.

-   The [RealTimeStylusEnabled](https://msdn.microsoft.com/library/ms824758(v=MSDN.10).aspx) and [RealTimeStylusDisabled](https://msdn.microsoft.com/library/ms824757(v=MSDN.10).aspx) methods are called on the thread that updates the [**RealTimeStylus**](realtimestylus-class.md) object's [Enabled](https://msdn.microsoft.com/library/ms585380(v=VS.100).aspx) property or that adds or removes the plug-in while the **RealTimeStylus** object is enabled.
-   The [CustomStylusDataAdded](https://msdn.microsoft.com/library/ms824753(v=MSDN.10).aspx) method is called on the thread that calls the [**RealTimeStylus**](realtimestylus-class.md) object's [AddCustomStylusDataToQueue](https://msdn.microsoft.com/library/ms825761(v=MSDN.10).aspx) method.
-   The [Error](https://msdn.microsoft.com/library/ms824754(v=MSDN.10).aspx) method is called on the thread on which the synchronous plug-in is running when it throws an exception.

To interact with your application from a synchronous plug-in, use the [AddCustomStylusDataToQueue](https://msdn.microsoft.com/library/ms825761(v=MSDN.10).aspx) method of the [**RealTimeStylus**](realtimestylus-class.md) object and handle the custom stylus data in one of your asynchronous plug-ins. If you make a synchronous call to another thread from a synchronous plug-in, you may block the **RealTimeStylus** object and thus block ink collection.

Certain tasks may be computationally demanding yet still require real-time access to the tablet pen's data stream, such as for multistroke gesture recognition. The StylusInput APIs provide a cascaded [**RealTimeStylus**](realtimestylus-class.md) model that allows you to use two **RealTimeStylus** objects, each one calling its synchronous plug-ins from different threads. For more information about the cascaded **RealTimeStylus** model, see [The Cascaded RealTimeStylus Model](the-cascaded-realtimestylus-model.md).

> [!Note]  
> You cannot attach the [**RealTimeStylus**](realtimestylus-class.md) object to a window or control in a different process.

 

For more information about threading considerations for the Tablet PC in general, see [Tablet PC Threading Considerations](tablet-pc-threading-considerations.md)

 

 



