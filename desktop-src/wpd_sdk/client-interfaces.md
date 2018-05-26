---
Description: Client Interfaces
ms.assetid: fbe53f17-940a-485e-82b2-c11ae39b3300
title: Client Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Client Interfaces

Applications use the methods supported by the following interfaces to perform operations on portable devices. These operations include opening a connection to a device, retrieving data from a device, writing data to a device, and so on.



| Interface                                                                              | Description                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumPortableDeviceObjectIDs**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-ienumportabledeviceobjectids?branch=master)                   | Enumerates the objects on a portable device.                                                                                                                                                                                        |
| [**IPortableDevice**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevice?branch=master)                                             | Provides low-level access to a portable device.                                                                                                                                                                                     |
| [**IPortableDeviceCapabilities**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecapabilities?branch=master)                     | Retrieves a variety of device capabilities, including supported formats, commands, and functional objects.                                                                                                                          |
| [**IPortableDeviceContent**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent?branch=master)                               | Provides methods to create, enumerate, and delete content on a device.                                                                                                                                                              |
| [**IPortableDeviceDataStream**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevicedatastream?branch=master)                         | Exposes additional methods on an **IStream** used for data transfers.                                                                                                                                                               |
| [**IPortableDeviceEventCallback**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledeviceeventcallback?branch=master)                   | Implemented by the application to receive asynchronous callbacks.                                                                                                                                                                   |
| [**IPortableDeviceManager**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevicemanager?branch=master)                               | Enumerates devices that are connected to the computer, and provides a simple way to request installation information for the device (including manufacturer, friendly name, and description).                                       |
| [**IPortableDeviceProperties**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledeviceproperties?branch=master)                         | Read and write properties for an object on the device.                                                                                                                                                                              |
| [**IPortableDevicePropertiesBulk**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevicepropertiesbulk?branch=master)                 | Reads and writes multiple properties on multiple objects on a device, asynchronously.                                                                                                                                               |
| [**IPortableDevicePropertiesBulkCallback**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevicepropertiesbulkcallback?branch=master) | Implemented by the application to track the progress of an asynchronous operation that was begun by using the **IPortableDevicePropertiesBulk** interface.                                                                          |
| [**IPortableDeviceResources**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledeviceresources?branch=master)                           | Provides access to an object's data.                                                                                                                                                                                                |
| [**IPortableDeviceService**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice?branch=master)                               | Windows 7 only. Provides low-level access to a portable device service.                                                                                                                                                             |
| [**IPortableDeviceServiceCapabilities**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecapabilities?branch=master)              | Windows 7 only. Retrieves a variety of service capabilities, including supported formats, commands, methods, and rendering profiles.                                                                                                |
| [**IPortableDeviceServiceMethods**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemethods?branch=master)                 | Windows 7 only. Invokes methods synchronously and asynchronously on a service.                                                                                                                                                      |
| [**IPortableDeviceServiceMethodCallback**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemethodcallback?branch=master)   | Windows 7 only. Implemented by the application to track the completion of an asynchronous service method operation begun by calling [**IPortableDeviceServiceMethods::InvokeAsync**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicemethods-invokeasync?branch=master) |
| [**IPortableDeviceServiceManager**](/windows/win32/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservicemanager?branch=master)                 | Windows 7 only. Enumerates services that are supported by a device, and retrieves the device associated with a service.                                                                                                             |



 

The following diagram shows how an application gets most of the interfaces it needs. Not all methods of all the interfaces or the interfaces that are implemented by the application are shown.

![diagram showing creation and retrieval of most required client interfaces](images/wpd-sdk-interface-diagram.gif)

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 



