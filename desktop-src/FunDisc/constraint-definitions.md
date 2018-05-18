---
Description: 'Most built-in providers support only a subset of the constraints defined below. For general information about query constraints, see Constraints.'
ms.assetid: '13502fbd-bc88-4c28-939e-3e964ab6bb5d'
title: Constraint Definitions
---

# Constraint Definitions

\[Function Discovery is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Most built-in providers support only a subset of the constraints defined below. For general information about query constraints, see [Constraints](constraints.md).

The following are common constraints and values.

<dl> <dt>

<span id="FD_CONSTRAINTVALUE_RECURSESUBCATEGORY_TRUE"></span><span id="fd_constraintvalue_recursesubcategory_true"></span>**FD\_CONSTRAINTVALUE\_RECURSESUBCATEGORY\_TRUE**
</dt> <dd> <dl> <dt>

L"TRUE"
</dt> <dt>



Queries should be recursive if the provider supports subcategories.


</dt> </dl> </dd> <dt>

<span id="FD_CONSTRAINTVALUE_VISIBILITY_ALL"></span><span id="fd_constraintvalue_visibility_all"></span>**FD\_CONSTRAINTVALUE\_VISIBILITY\_ALL**
</dt> <dd> <dl> <dt>

L"1"
</dt> <dt>



Query for all instances, including hidden instances.


</dt> </dl> </dd> <dt>

<span id="FD_CONSTRAINTVALUE_VISIBILITY_DEFAULT"></span><span id="fd_constraintvalue_visibility_default"></span>**FD\_CONSTRAINTVALUE\_VISIBILITY\_DEFAULT**
</dt> <dd> <dl> <dt>

L"0"
</dt> <dt>



Query for visible instances.


</dt> </dl> </dd> <dt>

<span id="FD_QUERYCONSTRAINT_COMCLSCONTEXT"></span><span id="fd_queryconstraint_comclscontext"></span>**FD\_QUERYCONSTRAINT\_COMCLSCONTEXT**
</dt> <dd> <dl> <dt>

L"COMClsContext"
</dt> <dt>



Specifies whether the provider used for the query should be launched inside of the caller's process or outside of the caller's process. A constraint value of FD\_QUERYCONSTRAINT\_COMCLSCONTEXT\_INPROC\_SERVER or FD\_QUERYCONSTRAINT\_COMCLSCONTEXT\_LOCAL\_SERVER must be passed to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.

By default, queries for SSDP devices, WSD devices, and devices discovered using a custom provider will be launched outside of the caller's process.


</dt> </dl> </dd> <dt>

<span id="FD_CONSTRAINTVALUE_COMCLSCONTEXT_INPROC_SERVER"></span><span id="fd_constraintvalue_comclscontext_inproc_server"></span>**FD\_CONSTRAINTVALUE\_COMCLSCONTEXT\_INPROC\_SERVER**
</dt> <dd> <dl> <dt>

L"1"
</dt> <dt>



The provider used to execute the query will be launched inside of the caller's process.


</dt> </dl> </dd> <dt>

<span id="FD_CONSTRAINTVALUE_COMCLSCONTEXT_LOCAL_SERVER"></span><span id="fd_constraintvalue_comclscontext_local_server"></span>**FD\_CONSTRAINTVALUE\_COMCLSCONTEXT\_LOCAL\_SERVER**
</dt> <dd> <dl> <dt>

L"4"
</dt> <dt>



The provider used to execute the query will be launched outside of the caller's process.

This constraint is ignored for the NetBIOS, WCN, PnP, and Registry providers. These providers are always loaded inside the caller's process.


</dt> </dl> </dd> <dt>

<span id="FD_QUERYCONSTRAINT_PROVIDERINSTANCEID"></span><span id="fd_queryconstraint_providerinstanceid"></span>**FD\_QUERYCONSTRAINT\_PROVIDERINSTANCEID**
</dt> <dd> <dl> <dt>

L"ProviderInstanceID"
</dt> <dt>



Query for instances with the specified provider identifier.


</dt> </dl> </dd> <dt>

<span id="FD_QUERYCONSTRAINT_RECURSESUBCATEGORY"></span><span id="fd_queryconstraint_recursesubcategory"></span>**FD\_QUERYCONSTRAINT\_RECURSESUBCATEGORY**
</dt> <dd> <dl> <dt>

L"RecurseSubcategory"
</dt> <dt>



Indicates whether queries should be recursive if the provider supports subcategories. See FD\_CONSTRAINTVALUE\_RECURSESUBCATEGORY\_TRUE.


</dt> </dl> </dd> <dt>

<span id="FD_QUERYCONSTRAINT_SUBCATEGORY"></span><span id="fd_queryconstraint_subcategory"></span>**FD\_QUERYCONSTRAINT\_SUBCATEGORY**
</dt> <dd> <dl> <dt>

L"Subcategory"
</dt> <dt>



Query for instances with the specified subcategory.


</dt> </dl> </dd> <dt>

<span id="FD_QUERYCONSTRAINT_VISIBILITY"></span><span id="fd_queryconstraint_visibility"></span>**FD\_QUERYCONSTRAINT\_VISIBILITY**
</dt> <dd> <dl> <dt>

L"Visibility"
</dt> <dt>



Query for instances based on visibility.


</dt> </dl> </dd> <dt>

<span id="FD_QUERYCONSTRAINT_ROUTINGSCOPE"></span><span id="fd_queryconstraint_routingscope"></span>**FD\_QUERYCONSTRAINT\_ROUTINGSCOPE**
</dt> <dd> <dl> <dt>

L"RoutingScope"
</dt> <dt>



Specifies whether the provider should be used to search for resources that can be contacted through provider-specific discovery infrastructure. One of the following values must be passed to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.

<dl> <dt>

<span id="FD_CONSTRAINTVALUE_ROUTINGSCOPE_ALL__L_All__"></span><span id="fd_constraintvalue_routingscope_all__l_all__"></span><span id="FD_CONSTRAINTVALUE_ROUTINGSCOPE_ALL__L_ALL__"></span>FD\_CONSTRAINTVALUE\_ROUTINGSCOPE\_ALL (L"All")
</dt> <dd>

The provider can rely on discovery infrastructure to find remote resources.

</dd> <dt>

<span id="FD_CONSTRAINTVALUE_ROUTINGSCOPE_DIRECT__L_Direct__"></span><span id="fd_constraintvalue_routingscope_direct__l_direct__"></span><span id="FD_CONSTRAINTVALUE_ROUTINGSCOPE_DIRECT__L_DIRECT__"></span>FD\_CONSTRAINTVALUE\_ROUTINGSCOPE\_DIRECT (L"Direct")
</dt> <dd>

The provider can search only for resources that can be directly contacted.

</dd> </dl>

</dl> </dd> </dl>

The following constraints and values are specific to NetBIOS.

<dl> <dt>

<span id="PROVIDERWNET_QUERYCONSTRAINT_PROPERTIES"></span><span id="providerwnet_queryconstraint_properties"></span>**PROVIDERWNET\_QUERYCONSTRAINT\_PROPERTIES**
</dt> <dd> <dl> <dt>

L"Properties"
</dt> <dt>



Specifies the properties in the property store to be populated from the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider. A constraint value of WNET\_CONSTRAINTVALUE\_PROPERTIES\_ALL or WNET\_CONSTRAINTVALUE\_PROPERTIES\_LIMITED should be passed to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.

If this constraint is not specified, then a default value of WNET\_CONSTRAINTVALUE\_PROPERTIES\_LIMITED is used.


</dt> </dl> </dd> <dt>

<span id="PROVIDERWNET_QUERYCONSTRAINT_RESOURCETYPE"></span><span id="providerwnet_queryconstraint_resourcetype"></span>**PROVIDERWNET\_QUERYCONSTRAINT\_RESOURCETYPE**
</dt> <dd> <dl> <dt>

L"ResourceType"
</dt> <dt>



Specifies the resource types to be queried. A constraint value of WNET\_CONSTRAINTVALUE\_RESOURCETYPE\_DISK, WNET\_CONSTRAINTVALUE\_RESOURCETYPE\_DISKORPRINTER, or WNET\_CONSTRAINTVALUE\_RESOURCETYPE\_PRINTER should be passed to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.

This constraint is not used by default.


</dt> </dl> </dd> <dt>

<span id="PROVIDERWNET_QUERYCONSTRAINT_TYPE"></span><span id="providerwnet_queryconstraint_type"></span>**PROVIDERWNET\_QUERYCONSTRAINT\_TYPE**
</dt> <dd> <dl> <dt>

L"Type"
</dt> <dt>



Specifies the resource display types to be queried. A constraint value of WNET\_CONSTRAINTVALUE\_TYPE\_ALL, WNET\_CONSTRAINTVALUE\_TYPE\_DOMAIN, or WNET\_CONSTRAINTVALUE\_TYPE\_SERVER should be passed to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.

If this constraint is not specified, then a default value of WNET\_CONSTRAINTVALUE\_TYPE\_SERVER is used.


</dt> </dl> </dd> <dt>

<span id="WNET_CONSTRAINTVALUE_PROPERTIES_ALL"></span><span id="wnet_constraintvalue_properties_all"></span>**WNET\_CONSTRAINTVALUE\_PROPERTIES\_ALL**
</dt> <dd> <dl> <dt>

L"All"
</dt> <dt>



All properties in the property store are populated from the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider.


</dt> </dl> </dd> <dt>

<span id="WNET_CONSTRAINTVALUE_PROPERTIES_LIMITED"></span><span id="wnet_constraintvalue_properties_limited"></span>**WNET\_CONSTRAINTVALUE\_PROPERTIES\_LIMITED**
</dt> <dd> <dl> <dt>

L"Limited"
</dt> <dt>



Only the PKEY\_WNET\_DisplayType and PKEY\_WNET\_Comment property keys are populated from the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider.


</dt> </dl> </dd> <dt>

<span id="WNET_CONSTRAINTVALUE_TYPE_ALL"></span><span id="wnet_constraintvalue_type_all"></span>**WNET\_CONSTRAINTVALUE\_TYPE\_ALL**
</dt> <dd> <dl> <dt>

L"All"
</dt> <dt>



Query all resources discoverable by the NetBIOS provider.


</dt> </dl> </dd> <dt>

<span id="WNET_CONSTRAINTVALUE_TYPE_DOMAIN"></span><span id="wnet_constraintvalue_type_domain"></span>**WNET\_CONSTRAINTVALUE\_TYPE\_DOMAIN**
</dt> <dd> <dl> <dt>

L"Domain"
</dt> <dt>



Query only the resources with a display type less than or equal to RESOURCEDISPLAYTYPE\_DOMAIN. Services, files, and printers are not queried. For more information, see [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353).


</dt> </dl> </dd> <dt>

<span id="WNET_CONSTRAINTVALUE_TYPE_SERVER"></span><span id="wnet_constraintvalue_type_server"></span>**WNET\_CONSTRAINTVALUE\_TYPE\_SERVER**
</dt> <dd> <dl> <dt>

L"Server"
</dt> <dt>



Query only the resources with a display type less than or equal to RESOURCEDISPLAYTYPE\_Server. Files and printers are not queried. For more information, see [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353).


</dt> </dl> </dd> <dt>

<span id="WNET_CONSTRAINTVALUE_RESOURCETYPE_DISK"></span><span id="wnet_constraintvalue_resourcetype_disk"></span>**WNET\_CONSTRAINTVALUE\_RESOURCETYPE\_DISK**
</dt> <dd> <dl> <dt>

L"Disk"
</dt> <dt>



Query the disk shares. A disk share is a resource with a display type of RESOURCEDISPLAYTYPE\_SHARE and a resource type of RESOURCETYPE\_DISK. For more information, see [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353).


</dt> </dl> </dd> <dt>

<span id="WNET_CONSTRAINTVALUE_RESOURCETYPE_DISKORPRINTER"></span><span id="wnet_constraintvalue_resourcetype_diskorprinter"></span>**WNET\_CONSTRAINTVALUE\_RESOURCETYPE\_DISKORPRINTER**
</dt> <dd> <dl> <dt>

L"DiskOrPrinter"
</dt> <dt>



Query the disk and printer shares. Disk and printer shares are resources with a display type of RESOURCEDISPLAYTYPE\_SHARE. For more information, see [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353).


</dt> </dl> </dd> <dt>

<span id="WNET_CONSTRAINTVALUE_RESOURCETYPE_PRINTER"></span><span id="wnet_constraintvalue_resourcetype_printer"></span>**WNET\_CONSTRAINTVALUE\_RESOURCETYPE\_PRINTER**
</dt> <dd> <dl> <dt>

L"Printer"
</dt> <dt>



Query the printer shares. A printer share is a resource with a display type of RESOURCEDISPLAYTYPE\_SHARE and a resource type of RESOURCETYPE\_PRINTER. For more information, see [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353).


</dt> </dl> </dd> </dl>

The following constraints and values are specific to PnP.

<dl> <dt>

<span id="PNP_CONSTRAINTVALUE_NOTPRESENT"></span><span id="pnp_constraintvalue_notpresent"></span>**PNP\_CONSTRAINTVALUE\_NOTPRESENT**
</dt> <dd> <dl> <dt>

L"TRUE"
</dt> <dt>



Query for instances that are not present, in addition to present instances. A *not present instance* is a PnP function instance that was once available on your computer but is no longer available for use.


</dt> </dl> </dd> <dt>

<span id="PNP_CONSTRAINTVALUE_NOTIFICATIONSONLY"></span><span id="pnp_constraintvalue_notificationsonly"></span>**PNP\_CONSTRAINTVALUE\_NOTIFICATIONSONLY**
</dt> <dd> <dl> <dt>

L"TRUE"
</dt> <dt>



A query will send the appropriate notification to the [**IFunctionDiscoveryNotification**](ifunctiondiscoverynotification.md) object, and not populate the instance collection.


</dt> </dl> </dd> <dt>

<span id="PROVIDERPNP_QUERYCONSTRAINT_INTERFACECLASS"></span><span id="providerpnp_queryconstraint_interfaceclass"></span>**PROVIDERPNP\_QUERYCONSTRAINT\_INTERFACECLASS**
</dt> <dd> <dl> <dt>

L"InterfaceClass"
</dt> <dt>



Query for [*devnode*](function-discovery-glossary.md#devnode-ncd-gly) function instances that have a corresponding interface instance which implements the specified interface.


</dt> </dl> </dd> <dt>

<span id="PROVIDERPNP_QUERYCONSTRAINT_NOTIFICATIONSONLY"></span><span id="providerpnp_queryconstraint_notificationsonly"></span>**PROVIDERPNP\_QUERYCONSTRAINT\_NOTIFICATIONSONLY**
</dt> <dd> <dl> <dt>

L"NotifyOnly"
</dt> <dt>



Queries will not populate the [**IFunctionInstanceCollection**](ifunctioninstancecollection.md) passed into the [**IFunctionInstanceCollectionQuery::Execute**](ifunctioninstancecollectionquery-execute-method.md) method, but will send appropriate notifications to the [**IFunctionDiscoveryNotification**](ifunctiondiscoverynotification.md) object. See PNP\_CONSTRAINTVALUE\_NOTIFICATIONSONLY.


</dt> </dl> </dd> <dt>

<span id="PROVIDERPNP_QUERYCONSTRAINT_NOTPRESENT"></span><span id="providerpnp_queryconstraint_notpresent"></span>**PROVIDERPNP\_QUERYCONSTRAINT\_NOTPRESENT**
</dt> <dd> <dl> <dt>

L"NotPresent"
</dt> <dt>



Indicates whether or not queries should return not present instances. See PNP\_CONSTRAINTVALUE\_NOTPRESENT.

If this constraint is not specified, then by default only present instances are returned.


</dt> </dl> </dd> </dl>

The following constraints and values are specific to SSDP.

<dl> <dt>

<span id="PROVIDERSSDP_QUERYCONSTRAINT_TYPE"></span><span id="providerssdp_queryconstraint_type"></span>**PROVIDERSSDP\_QUERYCONSTRAINT\_TYPE**
</dt> <dd> <dl> <dt>

L"Type"
</dt> <dt>



Query for SSDP devices of particular type. One of the SSDP constraint values specified below should be passed to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_ALL"></span><span id="ssdp_constraintvalue_type_all"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_ALL**
</dt> <dd> <dl> <dt>

L"ssdp:all"
</dt> <dt>



Query for all SSDP devices and services.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_ROOT"></span><span id="ssdp_constraintvalue_type_root"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_ROOT**
</dt> <dd> <dl> <dt>

L"upnp:rootdevice"
</dt> <dt>



Query for UPnP root devices.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEVICE_PREFIX"></span><span id="ssdp_constraintvalue_type_device_prefix"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEVICE\_PREFIX**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:"
</dt> <dt>



Query for UPnP devices.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_SVC_PREFIX"></span><span id="ssdp_constraintvalue_type_svc_prefix"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_SVC\_PREFIX**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:service:"
</dt> <dt>



Query for UPnP services.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEV_IGD"></span><span id="ssdp_constraintvalue_type_dev_igd"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_IGD**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:InternetGatewayDevice:1"
</dt> <dt>



Query for UPnP internet gateway devices.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEV_LANDEVICE"></span><span id="ssdp_constraintvalue_type_dev_landevice"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_LANDEVICE**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:LANDevice:1"
</dt> <dt>



Query for UPnP LAN devices.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEV_LIGHTING"></span><span id="ssdp_constraintvalue_type_dev_lighting"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_LIGHTING**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:Lighting:1"
</dt> <dt>



Query for UPnP lighting devices.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEV_LUXMETER"></span><span id="ssdp_constraintvalue_type_dev_luxmeter"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_LUXMETER**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:Luxmeter:1"
</dt> <dt>



Query for UPnP luxometers.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEV_MDARNDR"></span><span id="ssdp_constraintvalue_type_dev_mdarndr"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_MDARNDR**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:MediaRenderer:1"
</dt> <dt>



Query for UPnP media renderers.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEV_MDASRVR"></span><span id="ssdp_constraintvalue_type_dev_mdasrvr"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_MDASRVR**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:MediaServer:1"
</dt> <dt>



Query for UPnP media servers.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEV_POWERDEVICE"></span><span id="ssdp_constraintvalue_type_dev_powerdevice"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_POWERDEVICE**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:PowerDevice:1"
</dt> <dt>



Query for UPnP power devices.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEV_REMINDER"></span><span id="ssdp_constraintvalue_type_dev_reminder"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_REMINDER**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:Reminder:1"
</dt> <dt>



Query for UPnP reminder devices.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEV_WANDEVICE"></span><span id="ssdp_constraintvalue_type_dev_wandevice"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_WANDEVICE**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:WANDevice:1"
</dt> <dt>



Query for UPnP WAN devices.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_DEV_WANCONNDEVICE"></span><span id="ssdp_constraintvalue_type_dev_wanconndevice"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_WANCONNDEVICE**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:device:WANConnectionDevice:1"
</dt> <dt>



Query for UPnP WAN connection devices.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_SVC_DIMMING"></span><span id="ssdp_constraintvalue_type_svc_dimming"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_SVC\_DIMMING**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:service:DimmingService:1"
</dt> <dt>



Query for UPnP dimming service devices.


</dt> </dl> </dd> <dt>

<span id="SSDP_CONSTRAINTVALUE_TYPE_SVC_SCANNER"></span><span id="ssdp_constraintvalue_type_svc_scanner"></span>**SSDP\_CONSTRAINTVALUE\_TYPE\_SVC\_SCANNER**
</dt> <dd> <dl> <dt>

L"urn:schemas-upnp-org:service:Scanner:1"
</dt> <dt>



Query for UPnP scanners.


</dt> </dl> </dd> </dl>

The following constraints and values are specific to WSD.

<dl> <dt>

<span id="PROVIDERWSD_QUERYCONSTRAINT_DIRECTEDADDRESS"></span><span id="providerwsd_queryconstraint_directedaddress"></span>**PROVIDERWSD\_QUERYCONSTRAINT\_DIRECTEDADDRESS**
</dt> <dd> <dl> <dt>

L"RemoteAddress"
</dt> <dt>



Query for a WSD device discovered by directed discovery at a specified address. A string representing the device address should be passed to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.


</dt> </dl> </dd> <dt>

<span id="PROVIDERWSD_QUERYCONSTRAINT_SCOPE"></span><span id="providerwsd_queryconstraint_scope"></span>**PROVIDERWSD\_QUERYCONSTRAINT\_SCOPE**
</dt> <dd> <dl> <dt>

L"Scope"
</dt> <dt>



Not implemented.


</dt> </dl> </dd> <dt>

<span id="PROVIDERWSD_QUERYCONSTRAINT_TYPE"></span><span id="providerwsd_queryconstraint_type"></span>**PROVIDERWSD\_QUERYCONSTRAINT\_TYPE**
</dt> <dd> <dl> <dt>

L"Type"
</dt> <dt>



Query for WSD devices of particular type. A string representing the device type to query should be passed to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method. The string must be a URI that specifies the namespace and the type.

For example, to query for WSD devices of type "IBlinds" defined in the namespace "http://www.fabrikam.com/remotecontrolhome/Multi", pass the string "http://www.fabrikam.com/remotecontrolhome/Multi/IBlinds" to *pszConstraintValue*.


</dt> </dl> </dd> <dt>

<span id="PROVIDERWSD_QUERYCONSTRAINT_SSL_CERT_FOR_CLIENT_AUTH"></span><span id="providerwsd_queryconstraint_ssl_cert_for_client_auth"></span>**PROVIDERWSD\_QUERYCONSTRAINT\_SSL\_CERT\_FOR\_CLIENT\_AUTH**
</dt> <dd> <dl> <dt>

L"SSLClientAuthCert"
</dt> <dt>



Specifies what client authentication certificate should be used for an HTTPS connection to a device that requires client authentication. The constraint value passed through the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method must be a BASE-64-encoded value of the SHA1 hash of the certificate. The caller needs to have read access to the private key of this client certificate. This query constraint can be used only if the WSD provider is launched inside of the caller’s process (see **FD\_QUERYCONSTRAINT\_COMCLSCONTEXT**).


</dt> </dl> </dd> <dt>

<span id="PROVIDERWSD_QUERYCONSTRAINT_SECURITY_REQUIREMENTS"></span><span id="providerwsd_queryconstraint_security_requirements"></span>**PROVIDERWSD\_QUERYCONSTRAINT\_SECURITY\_REQUIREMENTS**
</dt> <dd> <dl> <dt>

L"SecurityRequirements"
</dt> <dt>



Query for devices based on their security capabilities. One of the following values must be passed to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.

<dl> <dt>

<span id="WSD_CONSTRAINTVALUE_REQUIRE_SECURECHANNEL__L_1__"></span><span id="wsd_constraintvalue_require_securechannel__l_1__"></span>WSD\_CONSTRAINTVALUE\_REQUIRE\_SECURECHANNEL (L"1")
</dt> <dd>

Only devices that support HTTPS endpoints for metadata transfer and service messaging will be discovered.

</dd> <dt>

<span id="WSD_CONSTRAINTVALUE_REQUIRE_SECURECHANNEL_AND_COMPACTSIGNATURE__L_2__"></span><span id="wsd_constraintvalue_require_securechannel_and_compactsignature__l_2__"></span>WSD\_CONSTRAINTVALUE\_REQUIRE\_SECURECHANNEL\_AND\_COMPACTSIGNATURE (L"2")
</dt> <dd>

Only devices that both sign their discovery messages using the compact signature format and use HTTPS endpoints for metadata transfer and service messaging will be discovered.

</dd> </dl>

</dl> </dd> </dl>

## Requirements



|                                     |                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>FunctionDiscoveryConstraints.h</dt> </dl> |



## See also

<dl> <dt>

[Constraints](constraints.md)
</dt> </dl>

 

 




