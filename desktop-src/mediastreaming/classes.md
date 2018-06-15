---
title: Classes
description: The Media Streaming API provides the following classes.
ms.assetid: E537FCE0-5AE5-41BC-903D-AE67CE9F4D78
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Classes

The [Media Streaming API](media-streaming-api-portal.md) provides the following classes.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActiveBasicDevice**](https://msdn.microsoft.com/en-us/library/Dn385755(v=VS.85).aspx)<br/>                               | Implements the [**IActiveBasicDevice**](https://msdn.microsoft.com/en-us/library/Dn385774(v=VS.85).aspx) interface that represents an active Digital Living Network Alliance (DLNA) device.<br/>                                                                                                                                                                                                                       |
| [**BasicDevice**](https://msdn.microsoft.com/en-us/library/Hh828813(v=VS.85).aspx)<br/>                                           | Implements the [**IBasicDevice**](ibasicdevice.md) interface that represents a DLNA device.<br/>                                                                                                                                                                                                                                                                             |
| [**CreateMediaRendererOperation**](createmediarendereroperation.md)<br/>         | Registers an event handler that is invoked when the asynchronous operation started by [**CreateMediaRendererAsync**](imediarendererfactory-createmediarendererasync.md) or [**CreateMediaRendererFromBasicDeviceAsync**](imediarendererfactory-createmediarendererfrombasicdeviceasync.md) completes, and provides a method that returns the results of the operation.<br/> |
| [**DeviceController**](https://msdn.microsoft.com/en-us/library/Hh828842(v=VS.85).aspx)<br/>                                 | Implements the [**IDeviceController**](https://msdn.microsoft.com/en-us/library/Hh828901(v=VS.85).aspx) interface that retrieves a list of cached Digital Media Renderers (DMRs) and/or Digital Media Servers (DMSs), or to asynchronously find the DMRs and/or DMSs that are currently on the network.<br/>                                                                                                            |
| [**DevicePair**](https://msdn.microsoft.com/en-us/library/Dn385771(v=VS.85).aspx)<br/>                                             | Implements the [**IDevicePair**](https://msdn.microsoft.com/en-us/library/Dn385796(v=VS.85).aspx) interface that represents a pair of [**ActiveBasicDevice**](https://msdn.microsoft.com/en-us/library/Dn385755(v=VS.85).aspx) objects which is comprised of a renderer and a server.<br/>                                                                                                                                                                              |
| [**GetMuteOperation**](getmuteoperation.md)<br/>                                 | Registers an event handler that is invoked when the asynchronous operation started by [**GetMuteAsync**](https://msdn.microsoft.com/en-us/library/Hh828930(v=VS.85).aspx) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                                                    |
| [**GetPositionInformationOperation**](getpositioninformationoperation.md)<br/>   | Registers an event handler that is invoked when the asynchronous operation started by [**GetPositionInformationAsync**](https://msdn.microsoft.com/en-us/library/Hh828931(v=VS.85).aspx) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                      |
| [**GetStreamPropertiesOperation**](getstreampropertiesoperation.md)<br/>         | Registers an event handler that is invoked when the asynchronous operation started by [**GetStreamPropertiesAsync**](https://msdn.microsoft.com/en-us/library/Hh829001(v=VS.85).aspx) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                            |
| [**GetTransportInformationOperation**](gettransportinformationoperation.md)<br/> | Registers an event handler that is invoked when the asynchronous operation started by [**GetTransportInformationAsync**](https://msdn.microsoft.com/en-us/library/Hh828932(v=VS.85).aspx) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                    |
| [**GetVolumeOperation**](getvolumeoperation.md)<br/>                             | Registers an event handler that is invoked when the asynchronous operation started by [**GetVolumeAsync**](https://msdn.microsoft.com/en-us/library/Hh828933(v=VS.85).aspx) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                                                |
| [**MediaRenderer**](mediarenderer.md)<br/>                                       | Implements the [**IMediaRenderer**](imediarenderer.md) interface that represents a DLNA Digital Media Renderer (DMR) device.<br/>                                                                                                                                                                                                                                            |
| [**PlaybackOperation**](playbackoperation.md)<br/>                               | Registers an event handler that is invoked when an asynchronous operation started by one of the [**MediaRenderer**](mediarenderer.md) playback methods completes, and provides a method that returns the results of the operation.<br/>                                                                                                                                      |
| [**StreamSelectOperation**](streamselectoperation.md)<br/>                       | Registers an event handler that is invoked when the asynchronous operation started by [**GetMuteAsync**](https://msdn.microsoft.com/en-us/library/Hh828930(v=VS.85).aspx) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                                                    |
| [**StreamSelector**](streamselector.md)<br/>                                     | Implements the [**IStreamSelectorStatics**](https://msdn.microsoft.com/en-us/library/Hh828953(v=VS.85).aspx) interface and enables selecting a stream.<br/>                                                                                                                                                                                                                                                        |



 

 

 





