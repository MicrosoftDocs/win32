---
Description: 'A synchronous local provider that enumerates PnP resources and responds to function instance queries for PnP devices.'
ms.assetid: '9e411b97-eabf-40eb-b0d5-257a2951db9a'
title: PnP Provider
---

# PnP Provider

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

The Plug and Play (PnP) provider is a synchronous local provider that enumerates PnP resources and responds to function instance queries for PnP devices. The PnP provider can enumerate physical PnP devices connected to the computer, virtual PnP devices, and interfaces corresponding to physical or virtual PnP devices. Any resource that is discoverable by the SetupDI API can be discovered by the PnP provider. For more information about the SetupDI API, see [Device Installation Functions](http://go.microsoft.com/fwlink/p/?linkid=72683).

## Query Results

The PnP provider supports collection queries and instance queries. That means the provider supports both the [**IFunctionInstanceCollectionQuery::Execute**](ifunctioninstancecollectionquery-execute-method.md) and [**IFunctionInstanceQuery::Execute**](ifunctioninstancequery-execute-method.md) methods. Because the PnP provider is synchronous, an **Execute** method usually returns **S\_OK** for a successful query. An **Execute** method returns **E\_PENDING** only when a notification-only query is executed. A notification-only query is a query with the **PROVIDERPNP\_QUERYCONSTRAINT\_NOTIFICATIONSONLY** constraint applied. If a notification-only query is performed, then memory is not allocated to the [**IFunctionInstanceCollection**](ifunctioninstancecollection.md) pointer returned by the **IFunctionInstanceCollectionQuery::Execute** method and function instances are not returned.

The function instance(s) returned by a query represent the [*devnode*](function-discovery-glossary.md#devnode-ncd-gly) corresponding to a physical device. Many devnodes implement interfaces that communicate with the device. The interfaces, in turn, implement interface nodes. These interface nodes are not normally included in the query results, even when the **PROVIDERPNP\_QUERYCONSTRAINT\_INTERFACECLASS** constraint is applied to the query. If function instance(s) corresponding to the interface node(s) must be implemented on a devnode, [**IFunctionInstance::QueryService**](ifunctioninstance-queryservice.md) must be called on a returned devnode function instance. When calling **QueryService**, set the *guidService* parameter to `SID_PnpProvider` and set the *riid* parameter to `__uuidof(IFunctionInstanceCollection)`.

## Query Constraints

A query constraint can be added by calling [**IFunctionInstanceCollectionQuery::AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) on an [**IFunctionInstanceCollectionQuery**](ifunctioninstancecollectionquery.md) object before executing the query.

The following table shows the query constraints supported by the PnP provider. The table also shows the value to pass to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.



| Constraint Name                                     | Constraint Value                                                                                                                                     | Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PROVIDERPNP\_QUERYCONSTRAINT\_INTERFACECLASS**    | The **GUID** of the interface, for example, `L"{af9a3835-f8b1-4086-b779-df7c6dcc387e}"`.                                                             | When this constraint is specified, the query returns only devnode function instances that have corresponding interface node function instances that match the specified **GUID**.<br/> Many **PROVIDERPNP\_QUERYCONSTRAINT\_INTERFACECLASS** constraints can be applied to a query. When many constraints are specified, the query returns only devnode function instances that have multiple matching interface node function instances.<br/>                                                                                                                                                                                                                                                                                        |
| **PROVIDERPNP\_QUERYCONSTRAINT\_NOTIFICATIONSONLY** | **FD\_CONSTRAINTVALUE\_TRUE**                                                                                                                        | When this constraint is specified, an **Execute** method returns **E\_PENDING** and any query results are returned to the [**IFunctionDiscoveryNotification**](ifunctiondiscoverynotification.md) interface passed to the [**IFunctionDiscovery::CreateInstanceCollectionQuery**](ifunctiondiscovery-createinstancecollectionquery-method.md) or the [**IFunctionDiscovery::CreateInstanceQuery**](ifunctiondiscovery-createinstancequery-method.md) method. A non-**NULL**?**IFunctionDiscoveryNotification** pointer must be passed to the query creation methods.<br/> The **PROVIDERPNP\_QUERYCONSTRAINT\_NOTIFICATIONSONLY** and **PROVIDERPNP\_QUERYCONSTRAINT\_NOTPRESENT** constraints cannot be used simultaneously.<br/> |
| **PROVIDERPNP\_QUERYCONSTRAINT\_NOTPRESENT**        | **FD\_CONSTRAINTVALUE\_TRUE**                                                                                                                        | When this constraint is specified, the PnP provider returns both present and not present function instances.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **FD\_QUERYCONSTRAINT\_PROVIDERINSTANCEID**         | The provider instance identifier, as returned by [**IFunctionInstance::GetProviderInstanceID**](ifunctioninstance-getproviderinstanceid-method.md). | When this constraint is specified, the query returns the function instance matching the provider instance identifier. The function instance must be present on the system.<br/> Applying this query constraint is equivalent to calling [**IFunctionDiscovery::GetInstance**](ifunctiondiscovery-getinstance-method.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                        |



 

For more information about a named constraint, see [**Constraint Definitions**](constraint-definitions.md). For general information about query constraints, see [Constraints](constraints.md).

The **FD\_QUERYCONSTRAINT\_SUBCATEGORY** and the **FD\_QUERYCONSTRAINT\_VISIBILITY** constraints are not supported by the PnP Provider.

## Notifications

If a non-NULL [**IFunctionDiscoveryNotification**](ifunctiondiscoverynotification.md) pointer is passed to the query creation method (either [**CreateInstanceCollectionQuery**](ifunctiondiscovery-createinstancecollectionquery-method.md) or [**CreateInstanceQuery**](ifunctiondiscovery-createinstancequery-method.md)), then the PnP provider will listen for [**WM\_DEVICECHANGE**](https://msdn.microsoft.com/library/windows/desktop/aa363480) messages and send **QUA\_ADD** and **QUA\_REMOVE** notifications to the interface as appropriate. An implementation of the [**IFunctionDiscoveryNotification::OnUpdate**](ifunctiondiscoverynotification-onupdate-method.md) method should handle these two notifications.

The **QUA\_ADD** notification corresponds to the [DBT\_DEVICEARRIVAL](https://msdn.microsoft.com/library/windows/desktop/aa363205) device event. When **QUA\_ADD** is sent, a device was added to the system, or a device's presence changed from not present to present. The **QUA\_REMOVE** notification corresponds to the [DBT\_DEVICEREMOVECOMPLETE](https://msdn.microsoft.com/library/windows/desktop/aa363208) device event. When **QUA\_REMOVE** is sent, a device was removed from the system, or a device's presence was changed from present to not present. A device's properties may not be accessible after a **QUA\_REMOVE** event. The **QUA\_CHANGE** notification is not used.

## Property Store

The PnP provider implements writeable provider-side property stores. That means that there is no property store attached to a function instance enumerated by the PnP provider. Instead, property reads and writes are passed directly to the PnP provider and changes are committed immediately.

The [**IFunctionInstance::OpenPropertyStore**](ifunctioninstance-openpropertystore-method.md) method can be used to access the property keys (**PKEY**s) associated with the PnP function instance. The methods of the [**IPropertyStore**](shell_IPropertyStore_cpp) interface can be used to get and set **PKEY**s associated with the function instance. It is not necessary to call **IPropertyStore::Commit** after setting a PKEY value, as changes are committed immediately, but it is good programming practice to call the method in any case.

When an [**IPropertyStore**](shell_IPropertyStore_cpp) method is called to get or set a **PKEY**, the PnP provider persists the data using the SetupDI API.

## PKEY Types

The PnP Provider can get or set many types of **PKEY**s. The following table shows the list of **PKEY** types supported by the PnP provider. The table also shows the **DEVPROPTYPE** type corresponding to each PROPVARIANT type.



| **PROPVARIANT** Type             | **DEVPROPTYPE** Type                                    |
|----------------------------------|---------------------------------------------------------|
| **VT\_EMPTY**                    | **DEVPROP\_TYPE\_EMPTY**                                |
| **VT\_NULL**                     | **DEVPROP\_TYPE\_NULL**                                 |
| **VT\_I1**                       | **DEVPROP\_TYPE\_SBYTE**                                |
| **VT\_UI1**                      | **DEVPROP\_TYPE\_BYTE**                                 |
| **VT\_I2**                       | **DEVPROP\_TYPE\_INT16**                                |
| **VT\_UI2**                      | **DEVPROP\_TYPE\_UINT16**                               |
| **VT\_I4**                       | **DEVPROP\_TYPE\_INT32**                                |
| **VT\_UI4**                      | **DEVPROP\_TYPE\_UINT32**                               |
| **VT\_I8**                       | **DEVPROP\_TYPE\_INT64**                                |
| **VT\_UI8**                      | **DEVPROP\_TYPE\_UINT64**                               |
| **VT\_R4**                       | **DEVPROP\_TYPE\_FLOAT**                                |
| **VT\_R8**                       | **DEVPROP\_TYPE\_DOUBLE**                               |
| **VT\_BOOL**                     | **DEVPROP\_TYPE\_BOOLEAN**                              |
| **VT\_FILETIME**                 | **DEVPROP\_TYPE\_FILETIME**                             |
| **VT\_DECIMAL**                  | **DEVPROP\_TYPE\_DECIMAL**                              |
| **VT\_LPWSTR**                   | **DEVPROP\_TYPE\_STRING**                               |
| **VT\_CLSID**                    | **DEVPROP\_TYPE\_GUID**                                 |
| **VT\_ARRAY** \| **VT\_UI1**     | **DEVPROP\_TYPEMOD\_ARRAY** \| **DEVPROP\_TYPE\_BYTE**  |
| **VT\_VECTOR** \| **VT\_LPWSTR** | **DEVPROP\_TYPEMOD\_LIST** \| **DEVPROP\_TYPE\_STRING** |



 

When getting or setting a **PKEY** using the Function Discovery API, use the **PROPVARIANT** type. When getting or setting a **DEVPKEY** using the SetupDI API, use the **DEVPROPTYPE** type.

For more information about PnP property types, see [DEVPROPTYPE](http://go.microsoft.com/fwlink/p/?linkid=72707).

## Required and Optional PKEYs

The PnP provider supports an extensible property store. That means any **PKEY** of a supported **PKEY** type can be added to the property store associated with a PnP device.

The following list shows the required **PKEY**s for PnP function instances. For more information about these **PKEY**s, see [**General PKEYs**](general-pkeys.md).

-   **PKEY\_Device\_Interface**
-   **PKEY\_Device\_NotPresent**
-   **PKEY\_FD\_Visibility**

The **PKEY\_Device\_Interface** key can only be retrieved from PnP interface function instances. To obtain an interface function instance from a device function instance, call [**QueryService**](ifunctioninstance-queryservice.md) on a device function instance returned by the PnP provider.

The PnP provider supports all PnP device properties (**DEVPKEY**s). These properties are defined in the Devpkey.h header file included in the Windows Driver Kit (WDK). For more information about the device properties and **PKEY**s defined by PnP, see [System-Defined Device Properties](http://go.microsoft.com/fwlink/p/?linkid=72708).

**PKEY**s defined in FunctionDiscoveryKeys.h and **DEVPKEY**s defined in Devpkey.h can be used interchangeably. Whenever possible, use the property key defined in FunctionDiscoveryKeys.h. If a key is not defined in FunctionDiscoveryKeys.h, cast the **DEVPKEY** type (**DEVPROPKEY**) to a **PKEY** type (**PROPERTYKEY**) and use the exposed [**IPropertyStore**](shell_IPropertyStore_cpp) methods to get and set the key values.

## Related topics

<dl> <dt>

[Built-in Providers](built-in-providers.md)
</dt> </dl>

 

 




