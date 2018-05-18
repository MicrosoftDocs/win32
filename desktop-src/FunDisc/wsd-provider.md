---
Description: 'An asynchronous Function Discovery provider that enumerates devices that use the Devices Profile for Web Services (DPWS) for discovery.'
ms.assetid: 'a6f9cc02-1b40-46da-bc65-dcb94dad5f9e'
title: WSD Provider
---

# WSD Provider

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

The Web Services on Devices (WSD) provider is an asynchronous Function Discovery provider that enumerates devices that use the [Devices Profile for Web Services](http://go.microsoft.com/fwlink/p/?linkid=59069) (DPWS) for discovery. The WSD provider uses the [Web Services on Devices API](https://msdn.microsoft.com/library/windows/desktop/aa826001) (WSDAPI) to discover WSD-enabled devices, perform metadata exchange, and process metadata. Once a device is discovered, the WSD provider gets the device metadata, processes it, and returns a [function instance](function-objects.md) that represents the WSD device.

## Query Results

The WSD provider supports collection queries and instance queries. That means the provider supports both the [**IFunctionInstanceCollectionQuery::Execute**](ifunctioninstancecollectionquery-execute-method.md) and [**IFunctionInstanceQuery::Execute**](ifunctioninstancequery-execute-method.md) methods. Because the WSD provider is asynchronous, **Execute** always returns E\_PENDING for a successful query.

When a collection query is executed, the WSD provider sends a multicast [Probe message](https://msdn.microsoft.com/library/windows/desktop/bb513684), which is used to search for WSD devices on the local subnet that match the constraints (if any) specified in the Function Discovery query. When an instance query is executed, the WSD provider sends a multicast [Resolve message](https://msdn.microsoft.com/library/windows/desktop/bb513686), which is used to search for the target device. In either case, the WSD provider then performs metadata exchange with the devices that responded to the Probe or Resolve message, processes the metadata, and returns the corresponding function instances. Applications can then call [**IFunctionInstance::QueryService**](ifunctioninstance-queryservice.md) on a returned function instance to get the collection of function instances corresponding to each service hosted on the device.

Function instances are returned using the [**IFunctionDiscoveryNotification::OnUpdate**](ifunctiondiscoverynotification-onupdate-method.md) method. Also, after the WSD provider has finished enumerating resources, the provider sends a FD\_EVENTID\_SEARCHCOMPLETE notification using [**IFunctionDiscoveryNotification::OnEvent**](ifunctiondiscoverynotification-onevent.md).

After the initial query results have been returned, the WSD provider continues to listen for messages from devices on the network. When a device sends a [Hello message](https://msdn.microsoft.com/library/windows/desktop/bb513682), the WSD provider sends a QUA\_ADD notification to the Function Discovery client. When a device sends a [Bye message](https://msdn.microsoft.com/library/windows/desktop/bb513676), the WSD provider sends a QUA\_REMOVE notification to the Function Discovery client. That means the client application is notified whenever a device comes online or goes offline until the client releases the query object by calling **Release** on the [**IFunctionInstanceCollectionQuery**](ifunctioninstancecollectionquery.md) or on the [**IFunctionInstanceQuery**](ifunctioninstancequery.md) object.

## Query Constraints

Query constraint can be added by calling [**IFunctionInstanceCollectionQuery::AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) on an [**IFunctionInstanceCollectionQuery**](ifunctioninstancecollectionquery.md) object before executing the query.

The following table shows the query constraints supported by the WSD provider. The table also shows possible values to pass to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.



| Constraint Name                               | Possible Values                                                                                                                           | Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FD\_QUERYCONSTRAINT\_PROVIDERINSTANCEID       | A WS-Discovery endpoint.                                                                                                                  | This constraint limits query results to a single device. The WSD provider returns a function instance representing the device matching the specified endpoint address, if there is such a device. <br/> This constraint can be applied to collection queries. It can also be combined with the PROVIDERWSD\_QUERYCONSTRAINT\_DIRECTEDADDRESS constraint.<br/>                                                                                                                                                                                                                                                                             |
| PROVIDERWSD\_QUERYCONSTRAINT\_DIRECTEDADDRESS | A HTTP transport address.                                                                                                                 | When this constraint is used, a Probe message is sent over HTTP to search for a device at a known URL. The query results are limited to the device, if any, responding to Probe messages sent over HTTP at the given URL.<br/> This constraint can be applied to collection and instance queries. It can also be combined with the FD\_QUERYCONSTRAINT\_PROVIDERINSTANCEID constraint.<br/>                                                                                                                                                                                                                                               |
| PROVIDERWSD\_QUERYCONSTRAINT\_TYPE            | A string that specifies the type of device or service being searched. The string must be a URI that specifies the namespace and the type. | This constraint limits query results to devices or hosted services of the specified type. For example, to query for WSD devices of type "IBlinds" defined in the namespace "http://www.fabrikam.com/remotecontrolhome/Multi", use "http://www.fabrikam.com/remotecontrolhome/Multi/IBlinds" for the constraint value. <br/> Applications may specify multiple PROVIDERWSD\_QUERYCONSTRAINT\_TYPE constraints to search for devices (also referred to as discovery hosts) that support multiple types. <br/> This constraint can only be applied to collection queries. It cannot be combined with any other query constraints.<br/> |



 

For more information about a named constraint, see [**Constraint Definitions**](constraint-definitions.md). For general information about query constraints, see [Constraints](constraints.md).

## Notifications

Because the WSD provider is asynchronous, a non-NULL [**IFunctionDiscoveryNotification**](ifunctiondiscoverynotification.md) pointer must be passed to the query creation method (either [**IFunctionDiscovery::CreateInstanceCollectionQuery**](ifunctiondiscovery-createinstancecollectionquery-method.md) or [**IFunctionDiscovery::CreateInstanceQuery**](ifunctiondiscovery-createinstancequery-method.md)). The WSD provider will listen for Hello and Bye messages and send QUA\_ADD and QUA\_REMOVE notifications to the **IFunctionDiscoveryNotification** interface as appropriate. An implementation of the [**IFunctionDiscoveryNotification::OnUpdate**](ifunctiondiscoverynotification-onupdate-method.md) method should handle these two notifications. The QUA\_CHANGE notification is not used.

## Events

The FD\_EVENTID\_SEARCHCOMPLETE event is dispatched by the WSD provider. This event notifies the application that the initial search for devices has been completed and that the application will receive function instances for added or removed devices that match the query constraints. The semantics are similar to [**IWSDiscoveryProviderNotify::SearchComplete**](https://msdn.microsoft.com/library/windows/desktop/aa386016). Applications that must return results synchronously can wait for this event to return the result set to their callers. For more information about FD\_EVENTID\_SEARCHCOMPLETE, see [**IFunctionDiscoveryNotification::OnEvent**](ifunctiondiscoverynotification-onevent.md).

## Services

The WSD provider implements the SID\_PNPXServiceCollection service.

An application can use the SID\_PNPXServiceCollection service to get the collection of child function instances (representing hosted services) from a given function instance. To do this, the application calls [**IFunctionInstance::QueryService**](ifunctioninstance-queryservice.md) on a returned function instance with the *guidService* parameter set to `SID_PNPXServiceCollection` and the *riid* parameter set to `_uuidof(IFunctionInstanceCollection)`. If a function instance does not have any child function instances, then an empty collection is returned.

Although the WSD provider does not implement the SID\_PNPXAssociation service, function instances created by the WSD provider are returned when an application calls [**IFunctionInstance::QueryService**](ifunctioninstance-queryservice.md) on a function instance with the *guidService* parameter set to `SID_PNPXAssociation` and the *riid* parameter set to `_uuidof(IPNPXAssociation)`.

## Property Store

The WSD provider implements read-only property stores.

The [**IFunctionInstance::OpenPropertyStore**](ifunctioninstance-openpropertystore-method.md) method can be used to access the property keys (PKEYs) associated with a function instance. The methods of the [IPropertyStore](shell_IPropertyStore_cpp) interface can be used to get the PKEYs associated with the function instance.

## Supported PKEYs

The WSD provider supports a number of device and PnP-X PKEYs. These PKEYs are used to store information from discovery and metadata messages. For more information about these messages, see [Discovery and Metadata Exchange Message Patterns](https://msdn.microsoft.com/library/windows/desktop/bb513677). This section enumerates the PKEYs supported by the WSD provider and, when relevant, names the XML element from the original message that corresponds with the PKEY.

The following table shows the namespace prefixes used in this section.



| Prefix  | Namespace                                         |
|---------|---------------------------------------------------|
| wsa     | http://schemas.xmlsoap.org/ws/2004/08/addressing  |
| wsd     | http://schemas.xmlsoap.org/ws/2006/02/devprof     |
| wsdisco | http://schemas.xmlsoap.org/ws/2005/04/discovery   |
| pnpx    | http://schemas.microsoft.com/windows/pnpx/2005/10 |



 

The following table shows the identity-related PKEYs supported by the WSD provider, the type of each PKEY, and the XML element from which the PKEY value is derived.



| PKEY                       | Element     | Type       |
|----------------------------|-------------|------------|
| PKEY\_PNPX\_GlobalIdentity | wsa:Address | VT\_LPWSTR |
| PKEY\_PNPX\_ID             | wsa:Address | VT\_LPWSTR |



 

The following table shows the discovery-related PKEYs supported by the WSD provider, the type of each PKEY, and the XML element from which the PKEY value is derived. Discovery-related PKEYs are retrieved from [Hello](https://msdn.microsoft.com/library/windows/desktop/bb513682), [Bye](https://msdn.microsoft.com/library/windows/desktop/bb513676), [ResolveMatch](https://msdn.microsoft.com/library/windows/desktop/bb513685), and [ProbeMatch](https://msdn.microsoft.com/library/windows/desktop/bb513683) messages.



| PKEY                        | Element                 | Type                   |
|-----------------------------|-------------------------|------------------------|
| PKEY\_PNPX\_MetadataVersion | wsdisco:MetadataVersion | VT\_UI8                |
| PKEY\_PNPX\_Scopes          | wsdisco:Scopes          | VT\_VECTOR\|VT\_LPWSTR |
| PKEY\_PNPX\_Types           | wsdisco:Types           | VT\_VECTOR\|VT\_LPWSTR |
| PKEY\_PNPX\_XAddrs          | wsdisco:XAddrs          | VT\_VECTOR\|VT\_LPWSTR |



 

The following table shows the model-related PKEYs supported by the WSD provider, the type of each PKEY, and the XML element from which the PKEY value is derived.



| PKEY                        | Element                                                                     | Type                   |
|-----------------------------|-----------------------------------------------------------------------------|------------------------|
| PKEY\_PNPX\_CompatibleTypes | See [PnP-X specification](http://go.microsoft.com/fwlink/p/?linkid=100181). | VT\_VECTOR\|VT\_LPWSTR |
| PKEY\_PNPX\_DeviceCategory  | wsd:ThisModel/pnpx:DeviceCategory                                           | VT\_VECTOR\|VT\_LPWSTR |
| PKEY\_PNPX\_Manufacturer    | wsd:ThisModel/wsd:Manufacturer                                              | VT\_LPWSTR             |
| PKEY\_PNPX\_ManufacturerUrl | wsd:ThisModel/wsd:ManufacturerURL                                           | VT\_LPWSTR             |
| PKEY\_PNPX\_ModelName       | wsd:ThisModel/wsd:ModelName                                                 | VT\_LPWSTR             |
| PKEY\_PNPX\_ModelNumber     | wsd:ThisModel/wsd:ModelNumber                                               | VT\_LPWSTR             |
| PKEY\_PNPX\_ModelUrl        | wsd:ThisModel/wsd:ModelURL                                                  | VT\_LPWSTR             |
| PKEY\_PNPX\_PresentationUrl | wsd:ThisModel/wsd:PresentationURL                                           | VT\_LPWSTR             |



 

The following table shows the PnP-X device-related PKEYs supported by the WSD provider, the type of each PKEY, and the XML element from which the PKEY value is derived.



| PKEY                        | Element                            | Type       |
|-----------------------------|------------------------------------|------------|
| PKEY\_PNPX\_FirmwareVersion | wsd:ThisDevice/wsd:FirmwareVersion | VT\_LPWSTR |
| PKEY\_PNPX\_FriendlyName    | wsd:ThisDevice/wsd:FriendlyName    | VT\_LPWSTR |
| PKEY\_PNPX\_SerialNumber    | wsd:ThisDevice/wsd:SerialNumber    | VT\_LPWSTR |



 

The following table shows the PnP-X installation-related PKEYs supported by the WSD provider, the type of each PKEY, and the XML element from which the PKEY value is derived.



| PKEY                        | Element                      | Type                   |
|-----------------------------|------------------------------|------------------------|
| PKEY\_Device\_CompatibleIds | wsd:Hosted/pnpx:CompatibleID | VT\_VECTOR\|VT\_LPWSTR |
| PKEY\_Device\_HardwareIds   | wsd:Hosted/pnpx:hardwareID   | VT\_VECTOR\|VT\_LPWSTR |
| PKEY\_PNPX\_Installable     | n/a                          | VT\_BOOL               |



 

The following table shows the service-related PKEYs supported by the WSD provider, the type of each PKEY, and the XML element from which the PKEY value is derived.



| PKEY                       | Element                       | Type                   |
|----------------------------|-------------------------------|------------------------|
| PKEY\_PNPX\_ServiceAddress | wsd:Hosted/wsd:ServiceAddress | VT\_VECTOR\|VT\_LPWSTR |
| PKEY\_PNPX\_ServiceId      | wsd:Hosted/wsd:ServiceId      | VT\_LPWSTR             |
| PKEY\_PNPX\_ServiceTypes   | wsd:Hosted/wsd:ServiceTypes   | VT\_VECTOR\|VT\_LPWSTR |



 

The WSD provider supports the following networking-related PKEYs. For PKEY descriptions and PROPVARIANT types, see [**PnP-X Provider PKEYs**](pnp-x-provider-pkeys.md).

-   PKEY\_PNPX\_IpAddress
-   PKEY\_PNPX\_NetworkInterfaceGuid
-   PKEY\_PNPX\_NetworkInterfaceLuid
-   PKEY\_PNPX\_PhysicalAddress
-   PKEY\_PNPX\_RemoteAddress

The WSD provider supports the following PKEYs related to publication services device hosts. For PKEY descriptions and PROPVARIANT types, see [**General PKEYs**](general-pkeys.md).

-   PKEY\_PUBSVCS\_METADATA
-   PKEY\_PUBSVCS\_TYPE

The WSD provider sets PnP-X PKEYs. It also maps some PnP-X-specific keys to general device PKEYs. The following table shows the device PKEYs populated by the WSD provider and the PnP-X PKEY equivalents.



| Device PKEY                        | PnP-X PKEY                  |
|------------------------------------|-----------------------------|
| PKEY\_Device\_DeviceDesc           | PKEY\_PNPX\_ModelName       |
| PKEY\_Device\_FriendlyName         | PKEY\_PNPX\_FriendlyName    |
| PKEY\_Device\_LocationInfo         | PKEY\_PNPX\_XAddrs          |
| PKEY\_Device\_Manufacturer         | PKEY\_PNPX\_Manufacturer    |
| PKEY\_Device\_Model                | PKEY\_PNPX\_ModelName       |
| PKEY\_DriverPackage\_VendorWebSite | PKEY\_PNPX\_ManufacturerUrl |



 

The PKEY\_Device BIOSVersion key is also supported. This key does not have a PnP-X equivalent.

For more information about all PnP-X PKEYs, see [**PnP-X Provider PKEYs**](pnp-x-provider-pkeys.md). For information about the WSD device metadata requirements in general, and also about the relationship between WSD device elements and PKEYs, see [PnP-X: Plug and Play Extensions for Windows Specification](http://go.microsoft.com/fwlink/p/?linkid=100181).

## Related topics

<dl> <dt>

[Built-in Providers](built-in-providers.md)
</dt> </dl>

 

 




