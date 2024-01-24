---
description: Description of ways to enhance performance when using the StylusInput application programming interfaces (APIs).
ms.assetid: 2a541715-2d9e-4eb2-ab60-ec95368fca5a
title: Performance Considerations for the StylusInput API
ms.topic: article
ms.date: 05/31/2018
---

# Performance Considerations for the StylusInput API

The following list describes some ways in which to improve the performance of applications that use the StylusInput APIs.

-   Use the [Microsoft.StylusInput.IStylusSyncPlugin.DataInterest](/previous-versions/ms824752(v=msdn.10)) or [Microsoft.StylusInput.IStylusAsyncPlugin.DataInterest](/previous-versions/ms824769(v=msdn.10)) property to subscribe only to the data that is relevant to your plug-in. This reduces the overall number of method calls the [**RealTimeStylus**](realtimestylus-class.md) object makes and also reduces the complexity of your plug-in. The **RealTimeStylus** object only checks the DataInterest property when the plug-in is attached.
-   Minimize the complexity of synchronous plug-ins. Synchronous plug-ins generally called by the [**RealTimeStylus**](realtimestylus-class.md) object's thread and may contribute to delays in ink collection.
-   Consider making your plug-in asynchronous. If your plug-in is complex and needs to add custom data to the [**RealTimeStylus**](realtimestylus-class.md) object's queue, consider using a cascaded **RealTimeStylus** model and adding the plug-in to the secondary **RealTimeStylus** object's synchronous plug-in collection. For more information about the cascaded **RealTimeStylus** model, see [The Cascaded RealTimeStylus Model](the-cascaded-realtimestylus-model.md).

 

 
