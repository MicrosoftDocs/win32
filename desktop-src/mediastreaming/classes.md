---
title: Classes
description: The Media Streaming API provides the following classes.
ms.assetid: E537FCE0-5AE5-41BC-903D-AE67CE9F4D78
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Classes

The [Media Streaming API](media-streaming-api-portal.md) provides the following classes.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActiveBasicDevice**](activebasicdevice.md)<br/>                               | Implements the [**IActiveBasicDevice**](/windows/win32/Windows.Media.Streaming.Devices/?branch=master) interface that represents an active Digital Living Network Alliance (DLNA) device.<br/>                                                                                                                                                                                                                       |
| [**BasicDevice**](basicdevice.md)<br/>                                           | Implements the [**IBasicDevice**](ibasicdevice.md) interface that represents a DLNA device.<br/>                                                                                                                                                                                                                                                                             |
| [**CreateMediaRendererOperation**](createmediarendereroperation.md)<br/>         | Registers an event handler that is invoked when the asynchronous operation started by [**CreateMediaRendererAsync**](imediarendererfactory-createmediarendererasync.md) or [**CreateMediaRendererFromBasicDeviceAsync**](imediarendererfactory-createmediarendererfrombasicdeviceasync.md) completes, and provides a method that returns the results of the operation.<br/> |
| [**DeviceController**](devicecontroller.md)<br/>                                 | Implements the [**IDeviceController**](idevicecontroller.md) interface that retrieves a list of cached Digital Media Renderers (DMRs) and/or Digital Media Servers (DMSs), or to asynchronously find the DMRs and/or DMSs that are currently on the network.<br/>                                                                                                            |
| [**DevicePair**](devicepair.md)<br/>                                             | Implements the [**IDevicePair**](/windows/win32/Windows.Media.Streaming.Devices/?branch=master) interface that represents a pair of [**ActiveBasicDevice**](activebasicdevice.md) objects which is comprised of a renderer and a server.<br/>                                                                                                                                                                              |
| [**GetMuteOperation**](getmuteoperation.md)<br/>                                 | Registers an event handler that is invoked when the asynchronous operation started by [**GetMuteAsync**](imediarenderer-getmuteasync.md) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                                                    |
| [**GetPositionInformationOperation**](getpositioninformationoperation.md)<br/>   | Registers an event handler that is invoked when the asynchronous operation started by [**GetPositionInformationAsync**](imediarenderer-getpositioninformationasync.md) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                      |
| [**GetStreamPropertiesOperation**](getstreampropertiesoperation.md)<br/>         | Registers an event handler that is invoked when the asynchronous operation started by [**GetStreamPropertiesAsync**](streamselector-getstreampropertiesasync.md) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                            |
| [**GetTransportInformationOperation**](gettransportinformationoperation.md)<br/> | Registers an event handler that is invoked when the asynchronous operation started by [**GetTransportInformationAsync**](imediarenderer-gettransportinformationasync.md) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                    |
| [**GetVolumeOperation**](getvolumeoperation.md)<br/>                             | Registers an event handler that is invoked when the asynchronous operation started by [**GetVolumeAsync**](imediarenderer-getvolumeasync.md) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                                                |
| [**MediaRenderer**](mediarenderer.md)<br/>                                       | Implements the [**IMediaRenderer**](imediarenderer.md) interface that represents a DLNA Digital Media Renderer (DMR) device.<br/>                                                                                                                                                                                                                                            |
| [**PlaybackOperation**](playbackoperation.md)<br/>                               | Registers an event handler that is invoked when an asynchronous operation started by one of the [**MediaRenderer**](mediarenderer.md) playback methods completes, and provides a method that returns the results of the operation.<br/>                                                                                                                                      |
| [**StreamSelectOperation**](streamselectoperation.md)<br/>                       | Registers an event handler that is invoked when the asynchronous operation started by [**GetMuteAsync**](imediarenderer-getmuteasync.md) completes, and provides a method that returns the results of the operation.<br/>                                                                                                                                                    |
| [**StreamSelector**](streamselector.md)<br/>                                     | Implements the [**IStreamSelectorStatics**](istreamselectorstatics.md) interface and enables selecting a stream.<br/>                                                                                                                                                                                                                                                        |



 

 

 





