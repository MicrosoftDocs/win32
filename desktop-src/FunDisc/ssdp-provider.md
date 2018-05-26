---
Description: An asynchronous Function Discovery provider that enumerates UPnP devices that use SSDP for discovery.
ms.assetid: 41d65b08-7601-430e-9702-6a6fd9854027
title: SSDP Provider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SSDP Provider

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

The Simple Search and Discovery Protocol (SSDP) provider is an asynchronous Function Discovery provider that enumerates UPnP devices that use SSDP for discovery. Any UPnP device that supports SSDP for discovery and is compatible with the Microsoft SSDP media stack is discoverable by the SSDP provider. Once a device is discovered, the SSDP provider gets the device description document from the device, processes it, and returns a [function instance](function-objects.md) that represents the root device.

## Query Results

The SSDP provider supports collection queries and instance queries. This means that the provider supports both the [**IFunctionInstanceCollectionQuery::Execute**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancecollectionquery-execute?branch=master) and [**IFunctionInstanceQuery::Execute**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancequery-execute?branch=master) methods. Because the SSDP provider is asynchronous, **Execute** always returns **E\_PENDING** for a successful query.

When a query is executed, the provider sends a SSDP M-SEARCH request. This request is used to search for devices or device types that match the parameters specified in the Function Discovery query. The SSDP provider gets the description documents from devices that respond to the M-SEARCH request. After processing the description documents, the SSDP provider returns the function instances corresponding to the root devices. Although the description documents describe both services and devices, the services are ignored and only the devices are enumerated.

Function instances are returned using the [**IFunctionDiscoveryNotification::OnUpdate**](ifunctiondiscoverynotification-onupdate-method.md) method. Also, after the SSDP provider has finished enumerating resources, the provider sends a FD\_EVENTID\_SEARCHCOMPLETE notification using [**IFunctionDiscoveryNotification::OnEvent**](ifunctiondiscoverynotification-onevent.md).

After the initial query results have been returned, the SSDP provider continues to listen for messages from devices on the network. When a device sends a ssdp:alive message, the SSDP provider sends a QUA\_ADD notification to the Function Discovery client. When a device sends a ssdp:byebye message, the SSDP provider sends a QUA\_REMOVE notification to the Function Discovery client. This means that the client application is notified whenever a device comes online or goes offline until the client releases the query object by calling **Release** on the [**IFunctionInstanceCollectionQuery**](/windows/win32/FunctionDiscoveryAPI/nn-functiondiscoveryapi-ifunctioninstancecollectionquery?branch=master) or on the [**IFunctionInstanceQuery**](/windows/win32/FunctionDiscoveryAPI/nn-functiondiscoveryapi-ifunctioninstancequery?branch=master) object.

Function Discovery applications can query the SSDP provider for different types of UPnP devices by specifying the **PROVIDERSSDP\_QUERYCONSTRAINT\_TYPE** query constraint. For more information, see the Query Constraints section below.

If the SSDP provider finds a multi-function device in response to a query, the returned function instance corresponds to the root device. Applications can then call [**IFunctionInstance::QueryService**](/windows/win32/FunctionDiscoveryAPI/?branch=master) on the returned function instance to get the collection of function instances corresponding to each child device. For multi-function devices, each child device corresponds to a function on the multi-function device.

## Query Constraints

Query constraint can be added by calling [**IFunctionInstanceCollectionQuery::AddQueryConstraint**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancecollectionquery-addqueryconstraint?branch=master) on an [**IFunctionInstanceCollectionQuery**](/windows/win32/FunctionDiscoveryAPI/nn-functiondiscoveryapi-ifunctioninstancecollectionquery?branch=master) object before executing the query.

The following table shows the query constraints supported by the SSDP provider. The table also shows possible values to pass to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancecollectionquery-addqueryconstraint?branch=master) method.

> [!Note]  
> The SSDP provider always returns function instances that correspond to the matching root devices. If a multi-function device has at least one child device that matches the specified query constraints, the function instance representing the root device is returned. An application must call [**IFunctionInstance::QueryService**](/windows/win32/FunctionDiscoveryAPI/?branch=master) and pass the appropriate service identifier to get the function instances associated with the child devices. All child devices of the root device are returned, not just child devices that match the original query constraints.

 



| Constraint name                         | Possible values                                                       | Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FD\_QUERYCONSTRAINT\_PROVIDERINSTANCEID | A device UUID.                                                        | This constraint limits query results to a single device. The SSDP provider returns a function instance representing the device matching the specified UUID, if there is such a device.<br/> This constraint takes precedence over all other query constraints. If this constraint is specified, all other query constraints are ignored. <br/>                                                                                                             |
| PROVIDERSSDP\_QUERYCONSTRAINT\_TYPE     | Any string corresponding to a device type supported by a SSDP device. | This constraint limits query results to the specified UPnP device type. If this constraint is not specified, the SSDP provider searches for devices of type **SSDP\_CONSTRAINTVALUE\_TYPE\_ROOT**.<br/> Some supported device type strings are predefined in FunctionDiscoveryConstraints.h. For a list of predefined types, see the SSDP\_CONSTRAINTVALUE\_TYPE\_\* constants in the topic [**Constraint Definitions**](constraint-definitions.md).<br/> |



 

For more information about a named constraint, see [**Constraint Definitions**](constraint-definitions.md). For general information about query constraints, see [Constraints](constraints.md).

## Notifications

Because the SSDP provider is asynchronous, a non-NULL [**IFunctionDiscoveryNotification**](/windows/win32/FunctionDiscoveryNotification/nn-functiondiscoveryapi-ifunctiondiscoverynotification?branch=master) pointer must be passed to the query creation method (either [**IFunctionDiscovery::CreateInstanceCollectionQuery**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctiondiscovery-createinstancecollectionquery?branch=master) or [**IFunctionDiscovery::CreateInstanceQuery**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctiondiscovery-createinstancequery?branch=master)). The SSDP provider will listen for ssdp:alive and ssdp:byebye messages and send QUA\_ADD and QUA\_REMOVE notifications to the **IFunctionDiscoveryNotification** interface as appropriate. An implementation of the [**IFunctionDiscoveryNotification::OnUpdate**](ifunctiondiscoverynotification-onupdate-method.md) method should handle these two notifications. The QUA\_CHANGE notification is not used.

## Events

The FD\_EVENTID\_SEARCHCOMPLETE event is dispatched by the SSDP provider. This event notifies the application that the initial search for devices has been completed and that the application will receive function instances for added or removed devices that match the query constraints. The semantics are similar to [**IUPnPDeviceFinderCallback::SearchComplete**](https://msdn.microsoft.com/library/windows/desktop/aa381587). Applications that must return results synchronously can wait for this event to return the result set to their callers. For more information about FD\_EVENTID\_SEARCHCOMPLETE, see [**IFunctionDiscoveryNotification::OnEvent**](ifunctiondiscoverynotification-onevent.md).

## Services

The SSDP provider implements the SID\_PNPXServiceCollection and SID\_UPnPActivator services. The SSDP provider creates function instances that are returned by the SID\_PNPXAssociation service.

### SID\_PNPXAssociation Service

Although the SSDP provider does not implement the SID\_PNPXAssociation service, function instances created by the SSDP provider are returned when an application calls [**IFunctionInstance::QueryService**](/windows/win32/FunctionDiscoveryAPI/?branch=master) on a function instance with the *guidService* parameter set to `SID_PNPXAssociation` and the *riid* parameter set to `_uuidof(IPNPXAssociation)`.

### SID\_PNPXServiceCollection Service

The SSDP provider implements the SID\_PNPXServiceCollection service.

An application can use the SID\_PNPXServiceCollection service to get the collection of child function instances (representing child devices) from a given function instance. To do this, the application calls [**IFunctionInstance::QueryService**](/windows/win32/FunctionDiscoveryAPI/?branch=master) on a returned function instance with the *guidService* parameter set to `SID_PNPXServiceCollection` and the *riid* parameter set to `_uuidof(IFunctionInstanceCollection)`. If a function instance does not have any child function instances, then an empty collection is returned.

Although the UPnP device description document supports an arbitrary number of nested devices, the SSDP provider supports only one level of device nesting. That means that the collection of child devices returned by the SSDP provider is never nested. That means that direct children of the root device and children of these direct children appear in the same flat collection.

### SID\_UPnPActivator Service

The SSDP provider implements the SID\_UPnPActivator service.

An application can use the SID\_UPnPActivator service to get the [**IUPnPDevice**](https://msdn.microsoft.com/library/windows/desktop/aa381561) interface associated with a given function instance. To do this, the application calls [**IFunctionInstance::QueryService**](/windows/win32/FunctionDiscoveryAPI/?branch=master) on a returned function instance with the *guidService* parameter set to `SID_PNPXServiceCollection` and the *riid* parameter set to `_uuidof(IUPnPDevice)`.

## Property Store

The SSDP provider implements read-only property stores.

The [**IFunctionInstance::OpenPropertyStore**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstance-openpropertystore?branch=master) method can be used to access the property keys (PKEYs) associated with a function instance. The methods of the [IPropertyStore](shell_IPropertyStore_cpp) interface can be used to get the PKEYs associated with the function instance.

## Supported PKEYs

The following PnP-X PKEYs are supported by the SSDP provider.

-   PKEY\_Device\_CompatibleIds
-   PKEY\_Device\_DeviceDesc
-   PKEY\_Device\_FriendlyName
-   PKEY\_Device\_HardwareIds
-   PKEY\_Device\_LocationInfo
-   PKEY\_Device\_Manufacturer
-   PKEY\_Device\_Model
-   PKEY\_DriverPackage\_VendorWebSite
-   PKEY\_PNPX\_CompatibleIds
-   PKEY\_PNPX\_CompatibleTypes
-   PKEY\_PNPX\_DeviceCategory
-   PKEY\_PNPX\_FriendlyName
-   PKEY\_PNPX\_GlobalIdentity
-   PKEY\_PNPX\_HardwareIds
-   PKEY\_PNPX\_ID
-   PKEY\_PNPX\_Installable
-   PKEY\_PNPX\_IpAddress
-   PKEY\_PNPX\_Manufacturer
-   PKEY\_PNPX\_ManufacturerUrl
-   PKEY\_PNPX\_ModelName
-   PKEY\_PNPX\_ModelNumber
-   PKEY\_PNPX\_ModelUrl
-   PKEY\_PNPX\_NetworkInterfaceGuid
-   PKEY\_PNPX\_PhysicalAddress
-   PKEY\_PNPX\_PresentationUrl
-   PKEY\_PNPX\_SerialNumber
-   PKEY\_PNPX\_Types
-   PKEY\_PNPX\_Upc
-   PKEY\_PNPX\_XAddrs

For more information about these PKEYs, see [**PnP-X Provider PKEYs**](pnp-x-provider-pkeys.md). For information about SSDP device metadata requirements in general, and also for information about the relationship between UPnP device elements and PKEYs, see [PnP-X: Plug and Play Extensions for Windows Specification](http://go.microsoft.com/fwlink/p/?linkid=100181).

## Related topics

<dl> <dt>

[Built-in Providers](built-in-providers.md)
</dt> </dl>

 

 




