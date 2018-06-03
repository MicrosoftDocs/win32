---
Description: Overview of error handling when using the StylusInput application programming interfaces (APIs).
ms.assetid: 7d7ff5b2-3eda-4570-96fe-b3b8f41ff69b
title: Error Handling Considerations for the StylusInput API
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling Considerations for the StylusInput API

Unhandled exceptions thrown by a plug-in are caught by the [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object. When a plug-in throws an exception, the normal flow of data is interrupted. The **RealTimeStylus** object:

1.  Creates an [ErrorData](https://www.bing.com/search?q=ErrorData) object (in managed code).
2.  Calls the [**Error**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-error) method (in managed code, either the [Microsoft.StylusInput.IStylusSyncPlugin.Error](https://www.bing.com/search?q=Microsoft.StylusInput.IStylusSyncPlugin.Error) or [Microsoft.StylusInput.IStylusAsyncPlugin.Error](https://www.bing.com/search?q=Microsoft.StylusInput.IStylusAsyncPlugin.Error) method) of the plug-in that threw the exception.
3.  Calls the [**Error**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-error) method of the remaining plug-ins in that collection.
4.  If the plug-in that threw the exception is a synchronous plug-in, the [ErrorData](https://www.bing.com/search?q=ErrorData) object (in managed code) is added to the output queue.
5.  The [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object resumes normal processing of the original data.

If a plug-in throws an exception from its [**Error**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-error) method, the [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object catches the exception but does not generate a new [ErrorData](https://www.bing.com/search?q=ErrorData) object. For more information about how ErrorData is added to the queue, see [Plug-in Data and the RealTimeStylus Class](plug-in-data-and-the-realtimestylus-class.md).

The [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object does not stop processing data from the tablet pen's data stream when one of its plug-ins throws an exception. Depending on your design, some of your plug-ins may need to subscribe to the [ErrorData](https://www.bing.com/search?q=ErrorData) notification and modify their behavior when an exception occurs.

 

 



