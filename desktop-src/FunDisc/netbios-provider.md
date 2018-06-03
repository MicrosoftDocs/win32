---
Description: An asynchronous network provider that enumerates resources discoverable by NetBIOS and responds to function instance queries for NetBIOS devices.
ms.assetid: 80ed1db2-94ff-4d7c-96e9-4d0aa34cae80
title: NetBIOS Provider
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NetBIOS Provider

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

The NetBIOS provider is an asynchronous network provider that enumerates resources discoverable by NetBIOS and responds to function instance queries for NetBIOS devices. The NetBIOS provider can enumerate WNet network providers, domains, servers, and shares. Any resource that is discoverable by the WNet API can be discovered by the NetBIOS provider. For more information about the WNet API, see [Windows Networking (WNet)](https://msdn.microsoft.com/library/windows/desktop/aa385406).

## Query Results

The NetBIOS provider only supports collection queries. Instance queries are not supported. Collection queries are executed by calling [**IFunctionInstanceCollectionQuery::Execute**](/windows/desktop/api/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancecollectionquery-execute). Because the NetBIOS provider is asynchronous, **Execute** always returns E\_PENDING for a successful query.

Results are returned using [**IFunctionDiscoveryNotification::OnUpdate**](https://www.bing.com/search?q=**IFunctionDiscoveryNotification::OnUpdate**). In addition, after the NetBIOS provider has finished enumerating resources, the provider sends a FD\_EVENTID\_SEARCHCOMPLETE notification using [**IFunctionDiscoveryNotification::OnEvent**](https://www.bing.com/search?q=**IFunctionDiscoveryNotification::OnEvent**).

## Query Constraints

A query constraint can be added by calling [**IFunctionInstanceCollectionQuery::AddQueryConstraint**](/windows/desktop/api/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancecollectionquery-addqueryconstraint) on an [**IFunctionInstanceCollectionQuery**](/windows/desktop/api/FunctionDiscoveryAPI/nn-functiondiscoveryapi-ifunctioninstancecollectionquery) object before executing the query.

The following table shows the query constraints supported by the NetBIOS provider. The table also shows possible values to pass to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](/windows/desktop/api/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancecollectionquery-addqueryconstraint) method.



| Constraint Name                             | Possible Values                                             | Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROVIDERWNET\_QUERYCONSTRAINT\_TYPE         | All<br/> Server<br/> Domain<br/>          | Specifies the resource display types to be enumerated by the NetBIOS provider. By default, the NetBIOS provider enumerates resources with a display type less than or equal to RESOURCEDISPLAYTYPE\_SERVER, which means that files and printers are not returned. The default setting is equivalent to applying this constraint with a value of Server. If this constraint has a value of All, the NetBIOS provider enumerates all discoverable resources. If this constraint has a value of Server, the NetBIOS provider enumerates resources with a display type less than or equal to RESOURCEDISPLAYTYPE\_SERVER, which means that files and printers are not returned. If this constraint has a value of Domain, the NetBIOS provider enumerates resources with a display type less than or equal to RESOURCEDISPLAYTYPE\_DOMAIN, which means that servers, files, and printers are not returned. <br/> Each enumerated resource is returned in the query results, unless the PROVIDERWNET\_QUERYCONSTRAINT\_RESOURCETYPE constraint is also supplied.<br/> |
| PROVIDERWNET\_QUERYCONSTRAINT\_PROPERTIES   | All<br/> Limited<br/>                           | Specifies the properties in the property store to be populated from the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure. By default, the NetBIOS provider populates only the PKEY\_WNET\_DisplayType and PKEY\_WNET\_Comment PKEYs from the **NETRESOURCE** structure. The default setting is equivalent to applying this constraint with a value of Limited. If this constraint has a value of All, the NetBIOS provider populates all WNet properties in the property store from the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PROVIDERWNET\_QUERYCONSTRAINT\_RESOURCETYPE | Disk<br/> Printer<br/> DiskOrPrinter<br/> | Specifies the resource types to be returned by the NetBIOS provider in the query results. This constraint does not change the types of resources enumerated by the provider, it only changes the query results returned by the provider. This constraint is not specified by default. If this constraint is used, then the PROVIDERWNET\_QUERYCONSTRAINT\_TYPE must be applied with a value of All.If this constraint has a value of Disk, only disk shares (with a display type of RESOURCEDISPLAYTYPE\_SHARE and a resource type of RESOURCETYPE\_DISK) are returned in the query results. If this constraint has a value of Printer, only printer shares (display type of RESOURCEDISPLAYTYPE\_SHARE and a resource type of RESOURCETYPE\_PRINTER) are returned in the query results. If this constraint has a value of DiskOrPrinter, then only disk and printer shares (with a display type of RESOURCEDISPLAYTYPE\_SHARE) are returned in the query results.<br/>                                                                                                |



 

For more information about a named constraint, see [**Constraint Definitions**](constraint-definitions.md). For general information about query constraints, see [Constraints](constraints.md).

The FD\_QUERYCONSTRAINT\_PROVIDERINSTANCEID, FD\_QUERYCONSTRAINT\_SUBCATEGORY, and the FD\_QUERYCONSTRAINT\_VISIBILITY constraints are not supported by the NetBIOS Provider.

## Property Store

The NetBIOS provider implements read-only property stores.

The [**IFunctionInstance::OpenPropertyStore**](/windows/desktop/api/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstance-openpropertystore) method can be used to access the property keys (PKEYs) associated with a NetBIOS function instance. The methods of the [IPropertyStore](https://www.bing.com/search?q=IPropertyStore) interface can be used to get the PKEYs associated with the function instance.

## Supported PKEYs

The following table shows the PnP-X PKEYs supported by the NetBIOS provider, and the values assigned to the keys. For more information, see [**PnP-X Provider PKEYs**](pnp-x-provider-pkeys.md).



| PKEY                             | Description of PKEY Value                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PKEY\_PNPX\_DeviceCategory       | For servers (resources with a display type of RESOURCEDISPLAYTYPE\_SERVER), this key has the value **Computer**.For disk shares (resources with a resource type of RESOURCETYPE\_DISK), this key has the value **Storage**.<br/> For printer shares (resources with a resource type of RESOURCETYPE\_PRINTER), this key has the value **Printer**.<br/>                                                                       |
| PKEY\_PNPX\_NetworkInterfaceGuid | The NetBIOS provider determines the GUID by calling [**GetBestInterfaceEx**](https://msdn.microsoft.com/library/windows/desktop/aa365922) on the first server discovered in a domain, and then stores the results in this PKEY.                                                                                                                                                                                                                                              |
| PKEY\_PNPX\_NetworkInterfaceLuid | The NetBIOS provider converts the network interface GUID to a LUID, and then stores the results in this PKEY.                                                                                                                                                                                                                                                                                                                             |
| PKEY\_PNPX\_DomainName           | For domains (resources with a display type RESOURCEDISPLAYTYPE\_DOMAIN), the value of this key is set to the **lpRemoteName** member of the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure associated with the resource. For servers or other resources discovered within a domain container, the value of this key is set to the **lpRemoteName** member of the **NETRESOURCE** structure associated with the parent domain resource. |
| PKEY\_PNPX\_ShareName            | For shares (resources with a display type of RESOURCEDISPLAYTYPE\_SHARE), the value of this key is set to the **lpRemoteName** member of the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure associated with the resource.                                                                                                                                                                                                              |



 

In addition, the PKEYs described in the topic [**WNet Provider PKEYs**](wnet-provider-pkeys.md) are supported by the NetBIOS provider.

## Related topics

<dl> <dt>

[Built-in Providers](built-in-providers.md)
</dt> </dl>

 

 




