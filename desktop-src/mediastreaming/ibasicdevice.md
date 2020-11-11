---
title: IBasicDevice interface
description: Encapsulates the methods and events needed to model a DLNA Device.
ms.assetid: E4F99A11-4ED5-44CB-BE16-CBB558412ED4
keywords:
- IBasicDevice interface Media Streaming API
- IBasicDevice interface Media Streaming API , described
topic_type:
- apiref
api_name:
- IBasicDevice
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice interface

Encapsulates the methods and events needed to model a DLNA Device.

## Members

The **IBasicDevice** interface inherits from [**IInspectable**](/windows/desktop/api/inspectable/nn-inspectable-iinspectable). **IBasicDevice** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBasicDevice** interface has these methods.



| Method                                                                                 | Description                                                                                                                    |
|:---------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**add\_ConnectionStatusChanged**](ibasicdevice-add-connectionstatuschanged.md)       | Registers an event handler for the [**ConnectionStatusChanged**](connectionstatuschanged.md) event.<br/>                |
| [**CanWakeDevices**](ibasicdevice-canwakedevices.md)                                  | Retrieves a value that indicates if the device can wake.<br/>                                                            |
| [**ConnectionStatus**](/previous-versions/windows/desktop/legacy/hh828873(v=vs.85))                              | Returns an enumeration value indicating whether the device is currently on-line, off-line or sleeping but wakeable.<br/> |
| [**Description**](ibasicdevice-description.md)                                        | Retrieves a description of the device.<br/>                                                                              |
| [**DiscoveredOnCurrentNetwork**](ibasicdevice-discoveredoncurrentnetwork.md)          | Retrieves a value that indicates if the device is on the current network.<br/>                                           |
| [**FriendlyName**](ibasicdevice-friendlyname.md)                                      | Retrieves the device s friendly name.<br/>                                                                               |
| [**Icons**](ibasicdevice-icons.md)                                                    | Returns a vector of [**IDeviceIcon**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-ideviceicon) interfaces.<br/>                                                  |
| [**IpAddresses**](ibasicdevice-ipaddresses.md)                                        | Returns a vector of IP addresses.<br/>                                                                                   |
| [**ManufacturerName**](ibasicdevice-manufacturername.md)                              | Retrieves the device s manufacturer name.<br/>                                                                           |
| [**ManufacturerUrl**](ibasicdevice-manufacturerurl.md)                                | Retrieves the device s manufacturer URL.<br/>                                                                            |
| [**ModelName**](ibasicdevice-modelname.md)                                            | Retrieves the device s model name.<br/>                                                                                  |
| [**ModelNumber**](ibasicdevice-modelnumber.md)                                        | Retrieves the device s model number.<br/>                                                                                |
| [**ModelUrl**](ibasicdevice-modelurl.md)                                              | Retrieves the device s model URL.<br/>                                                                                   |
| [**PhysicalAddresses**](ibasicdevice-physicaladdresses.md)                            | Returns a vector of physical addresses.<br/>                                                                             |
| [**PresentationUrl**](ibasicdevice-presentationurl.md)                                | Retrieves the device s presentation URL.<br/>                                                                            |
| [**RemoteStreamingUrls**](ibasicdevice-remotestreamingurls.md)                        | Returns a vector of remote streaming URLs.<br/>                                                                          |
| [**remove\_ConnectionStatusChanged**](ibasicdevice-remove-connectionstatuschanged.md) | Unregisters an event handler for the [**ConnectionStatusChanged**](connectionstatuschanged.md) event.<br/>              |
| [**SerialNumber**](ibasicdevice-serialnumber.md)                                      | Retrieves the device s serial number.<br/>                                                                               |
| [**Type**](ibasicdevice-type.md)                                                      | Retrieves an enumeration value indicating the device type of the DLNA device.<br/>                                       |
| [**UniqueDeviceName**](ibasicdevice-uniquedevicename.md)                              | Retrieves the device s unique device name (UDN).<br/>                                                                    |



 

## See also

<dl> <dt>

[**IInspectable**](/windows/desktop/api/inspectable/nn-inspectable-iinspectable)
</dt> </dl>

 

