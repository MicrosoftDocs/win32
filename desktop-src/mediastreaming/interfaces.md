---
title: Interfaces
description: The Media Streaming API provides the following interfaces.
ms.assetid: '1E25B452-D23C-4A1D-BC39-A5B719DF2C5D'
---

# Interfaces

The [Media Streaming API](media-streaming-api-portal.md) provides the following interfaces.

## In this section



| Topic                                                                                 | Description                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IActiveBasicDevice**](iactivebasicdevice.md)<br/>                           | Represents an active [**IBasicDevice**](ibasicdevice.md) that is associated with a UPnP device. <br/>                                                                                                                                          |
| [**IActiveBasicDeviceStatics**](iactivebasicdevicestatics.md)<br/>             | Provides static methods for creating [**IActiveBasicDevice**](iactivebasicdevice.md) objects. <br/>                                                                                                                                            |
| [**IBasicDevice**](ibasicdevice.md)<br/>                                       | Encapsulates the methods and events needed to model a DLNA Device.<br/>                                                                                                                                                                         |
| [**IDeviceController**](idevicecontroller.md)<br/>                             | Encapsulates the methods and events needed to retrieve a list of cached Digital Media Renderers (DMRs) and/or Digital Media Servers (DMSs), or to asynchronously find the DMRs and/or DMSs that are currently on the network.<br/>              |
| [**IDeviceIcon**](ideviceicon.md)<br/>                                         | Encapsulates the methods needed to provide information about the icon of a DLNA Device.<br/>                                                                                                                                                    |
| [**IDevicePair**](idevicepair.md)<br/>                                         | Represents a pair of [**ActiveBasicDevice**](activebasicdevice.md) objects which is comprised of a renderer and a server.<br/>                                                                                                                 |
| [**IMediaRenderer**](imediarenderer.md)<br/>                                   | Encapsulates the methods and events needed to represent a DLNA Digital Media Renderer (DMR) device.<br/>                                                                                                                                        |
| [**IMediaRendererActionInformation**](imediarendereractioninformation.md)<br/> | Encapsulates the methods needed to provide information about what methods can currently be invoked on the DMR.<br/>                                                                                                                             |
| [**IMediaRendererFactory**](imediarendererfactory.md)<br/>                     | Encapsulates the methods needed to asynchronously create a new instance of an object that implements the [**IMediaRenderer**](imediarenderer.md) interface.<br/>                                                                               |
| [**IStreamSelectorStatics**](istreamselectorstatics.md)<br/>                   | Encapsulates the methods needed to asynchronously select a stream.<br/>                                                                                                                                                                         |
| [**ITransportParameters**](itransportparameters.md)<br/>                       | Encapsulates the methods needed to provide information about the current transport-related settings of the DMR. These settings include the current transport state and information about what methods can currently be invoked on the DMR.<br/> |



 

 

 





