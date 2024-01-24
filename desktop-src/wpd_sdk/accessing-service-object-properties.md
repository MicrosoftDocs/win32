---
description: Accessing Service Object Properties
ms.assetid: 66d9802b-ad28-47a4-8151-9df7aff07d61
title: Accessing Service Object Properties
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Service Object Properties

An application can read and write properties for a single object on a service, for multiple objects identified by object identifiers, or for multiple objects of the same type. The [Retrieving Object Properties](retrieving-content-object-properties.md) topic describes reading properties for a single object on a service. The [Writing Object Properties](writing-content-object-properties.md) topic describes writing properties for a single object on a service.

Refer to the [Advanced Tasks](advanced-tasks.md) section for a description of property retrieval for multiple objects.

## When to use Service Property Definitions

The WPD API calls used for retrieving and setting object properties for a service are the same as the calls for retrieving object properties for a device (compare "Retrieving Properties for a Single Object" for an example). The key difference is that a different set of PROPERTYKEYs are used to query object properties. For the WpdServiceApiSample, device service PROPERTYKEYs are used (such as **PKEY\_GenericObj\_Name**); for the WpdApiSample, WPD PROPERTYKEYs are used (such as **WPD\_OBJECT\_NAME**).

Device service PROPERTYKEYs are defined in BridgeDeviceServices.h (included by each service header file), and represent the common set of PROPERTYKEYS employed by both device services applications and the firmware implementation on the device. This allows a consistent set of definitions throughout the device stack with minimal translation, groups PROPERTYKEYs based on the service, and enables new services to be more easily defined without having to update the WPD schema.

The set of PROPERTYKEYs used will depend on your application's needs:

-   If your application is communicating with the device by calling [**IPortableDevice::Open**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-open), use the PROPERTYKEYs defined in PortableDevice.h. An example of such an application is the WpdApiSample.
-   If your application is communicating with device services by calling [**IPortableDeviceService::Open**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservice-open), use the PROPERTYKEYS defined in BridgeDeviceServices.h. An example of such an application is the WpdServicesApiSample.
-   If you are writing a complex application that needs to support a hybrid of both device services and the device (this means your application calls both **IPortableDevice::Open** and **IPortableDeviceService::Open**), you will need to use the WPD PROPERTYKEYs when using IPortableDevice and its derived interfaces, and device service PROPERTYKEYs when using [IPortableDeviceService](/windows/desktop/api/PortableDeviceAPI/nn-portabledeviceapi-iportabledeviceservice) and its derived interfaces.

Most WPD applications should fall into the first or second category.

## Related topics

<dl> <dt>

[**IPortableDeviceContent2**](/windows/desktop/api/PortableDeviceAPI/nn-portabledeviceapi-iportabledevicecontent2)
</dt> <dt>

[**IPortableDeviceProperties**](/windows/desktop/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceproperties)
</dt> <dt>

[Retrieving Object Properties](retrieving-content-object-properties.md)
</dt> <dt>

[Writing Object Properties](writing-content-object-properties.md)
</dt> <dt>

[WpdServicesApiSample](wpdapisample-sample-service-application.md)
</dt> </dl>

 

 



