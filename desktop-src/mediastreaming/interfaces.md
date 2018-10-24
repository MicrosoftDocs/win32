---
title: Interfaces
description: The Media Streaming API provides the following interfaces.
ms.assetid: 1E25B452-D23C-4A1D-BC39-A5B719DF2C5D
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces

The [Media Streaming API](media-streaming-api-portal.md) provides the following interfaces.

## In this section



| Topic                                                                                 | Description                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IActiveBasicDevice**](https://msdn.microsoft.com/en-us/library/Dn385774(v=VS.85).aspx)<br/>                           | Represents an active [**IBasicDevice**](ibasicdevice.md) that is associated with a UPnP device. <br/>                                                                                                                                          |
| [**IActiveBasicDeviceStatics**](https://msdn.microsoft.com/en-us/library/Dn385775(v=VS.85).aspx)<br/>             | Provides static methods for creating [**IActiveBasicDevice**](https://msdn.microsoft.com/en-us/library/Dn385774(v=VS.85).aspx) objects. <br/>                                                                                                                                            |
| [**IBasicDevice**](ibasicdevice.md)<br/>                                       | Encapsulates the methods and events needed to model a DLNA Device.<br/>                                                                                                                                                                         |
| [**IDeviceController**](https://msdn.microsoft.com/en-us/library/Hh828901(v=VS.85).aspx)<br/>                             | Encapsulates the methods and events needed to retrieve a list of cached Digital Media Renderers (DMRs) and/or Digital Media Servers (DMSs), or to asynchronously find the DMRs and/or DMSs that are currently on the network.<br/>              |
| [**IDeviceIcon**](https://msdn.microsoft.com/en-us/library/Hh828909(v=VS.85).aspx)<br/>                                         | Encapsulates the methods needed to provide information about the icon of a DLNA Device.<br/>                                                                                                                                                    |
| [**IDevicePair**](https://msdn.microsoft.com/en-us/library/Dn385796(v=VS.85).aspx)<br/>                                         | Represents a pair of [**ActiveBasicDevice**](https://msdn.microsoft.com/en-us/library/Dn385755(v=VS.85).aspx) objects which is comprised of a renderer and a server.<br/>                                                                                                                 |
| [**IMediaRenderer**](imediarenderer.md)<br/>                                   | Encapsulates the methods and events needed to represent a DLNA Digital Media Renderer (DMR) device.<br/>                                                                                                                                        |
| [**IMediaRendererActionInformation**](https://msdn.microsoft.com/en-us/library/Hh828915(v=VS.85).aspx)<br/> | Encapsulates the methods needed to provide information about what methods can currently be invoked on the DMR.<br/>                                                                                                                             |
| [**IMediaRendererFactory**](https://msdn.microsoft.com/en-us/library/Hh828924(v=VS.85).aspx)<br/>                     | Encapsulates the methods needed to asynchronously create a new instance of an object that implements the [**IMediaRenderer**](imediarenderer.md) interface.<br/>                                                                               |
| [**IStreamSelectorStatics**](https://msdn.microsoft.com/en-us/library/Hh828953(v=VS.85).aspx)<br/>                   | Encapsulates the methods needed to asynchronously select a stream.<br/>                                                                                                                                                                         |
| [**ITransportParameters**](https://msdn.microsoft.com/en-us/library/Hh828956(v=VS.85).aspx)<br/>                       | Encapsulates the methods needed to provide information about the current transport-related settings of the DMR. These settings include the current transport state and information about what methods can currently be invoked on the DMR.<br/> |



 

 

 





