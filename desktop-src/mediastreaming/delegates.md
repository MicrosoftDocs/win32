---
title: Delegates
description: The Media Streaming API provides the following event handler functions.
ms.assetid: CDE7B829-D0D1-479D-9B35-4445E711AF58
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Delegates

The [Media Streaming API](media-streaming-api-portal.md) provides the following event handler functions.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ConnectionStatusHandler**](/windows/win32/mfidl/?branch=master)<br/>                   | Represents the function that will handle the [**ConnectionStatusChanged**](connectionstatuschanged.md) event which notifies the client of changes in the device s network connection status.<br/>               |
| [**DeviceControllerFinderHandler**](/windows/win32/mfidl/?branch=master)<br/>       | Represents the function that will handle the [**DeviceArrival**](devicearrival.md) and [**DeviceDeparture**](devicedeparture.md) events which notify the client of changes in the list of cached devices.<br/> |
| [**RenderingParametersUpdateHandler**](/windows/win32/mfidl/?branch=master)<br/> | Represents the function that will handle the [**RenderingParametersUpdate**](renderingparametersupdate.md) event which notifies the client of an update to any of the DMR s rendering control parameters.<br/>  |
| [**TransportParametersUpdateHandler**](/windows/win32/mfidl/?branch=master)<br/> | Represents the function that will handle the [**TransportParametersUpdate**](transportparametersupdate.md) event which notifies the client of an update to any of the DMR s transport parameters.<br/>          |



 

 

 





