---
Description: Client Interfaces
ms.assetid: 'fbe53f17-940a-485e-82b2-c11ae39b3300'
title: Client Interfaces
---

# Client Interfaces

Applications use the methods supported by the following interfaces to perform operations on portable devices. These operations include opening a connection to a device, retrieving data from a device, writing data to a device, and so on.



| Interface                                                                              | Description                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumPortableDeviceObjectIDs**](ienumportabledeviceobjectids.md)                   | Enumerates the objects on a portable device.                                                                                                                                                                                        |
| [**IPortableDevice**](iportabledevice.md)                                             | Provides low-level access to a portable device.                                                                                                                                                                                     |
| [**IPortableDeviceCapabilities**](iportabledevicecapabilities.md)                     | Retrieves a variety of device capabilities, including supported formats, commands, and functional objects.                                                                                                                          |
| [**IPortableDeviceContent**](iportabledevicecontent.md)                               | Provides methods to create, enumerate, and delete content on a device.                                                                                                                                                              |
| [**IPortableDeviceDataStream**](iportabledevicedatastream.md)                         | Exposes additional methods on an **IStream** used for data transfers.                                                                                                                                                               |
| [**IPortableDeviceEventCallback**](iportabledeviceeventcallback.md)                   | Implemented by the application to receive asynchronous callbacks.                                                                                                                                                                   |
| [**IPortableDeviceManager**](iportabledevicemanager.md)                               | Enumerates devices that are connected to the computer, and provides a simple way to request installation information for the device (including manufacturer, friendly name, and description).                                       |
| [**IPortableDeviceProperties**](iportabledeviceproperties.md)                         | Read and write properties for an object on the device.                                                                                                                                                                              |
| [**IPortableDevicePropertiesBulk**](iportabledevicepropertiesbulk.md)                 | Reads and writes multiple properties on multiple objects on a device, asynchronously.                                                                                                                                               |
| [**IPortableDevicePropertiesBulkCallback**](iportabledevicepropertiesbulkcallback.md) | Implemented by the application to track the progress of an asynchronous operation that was begun by using the **IPortableDevicePropertiesBulk** interface.                                                                          |
| [**IPortableDeviceResources**](iportabledeviceresources.md)                           | Provides access to an object's data.                                                                                                                                                                                                |
| [**IPortableDeviceService**](iportabledeviceservice.md)                               | Windows 7 only. Provides low-level access to a portable device service.                                                                                                                                                             |
| [**IPortableDeviceServiceCapabilities**](iportabledevicecapabilities.md)              | Windows 7 only. Retrieves a variety of service capabilities, including supported formats, commands, methods, and rendering profiles.                                                                                                |
| [**IPortableDeviceServiceMethods**](iportabledeviceservicemethods.md)                 | Windows 7 only. Invokes methods synchronously and asynchronously on a service.                                                                                                                                                      |
| [**IPortableDeviceServiceMethodCallback**](iportabledeviceservicemethodcallback.md)   | Windows 7 only. Implemented by the application to track the completion of an asynchronous service method operation begun by calling [**IPortableDeviceServiceMethods::InvokeAsync**](iportabledeviceservicemethods-invokeasync.md) |
| [**IPortableDeviceServiceManager**](iportabledeviceservicemanager.md)                 | Windows 7 only. Enumerates services that are supported by a device, and retrieves the device associated with a service.                                                                                                             |



 

The following diagram shows how an application gets most of the interfaces it needs. Not all methods of all the interfaces or the interfaces that are implemented by the application are shown.

![diagram showing creation and retrieval of most required client interfaces](images/wpd-sdk-interface-diagram.gif)

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



