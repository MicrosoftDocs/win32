---
Description: 'A synchronous local provider that enumerates resources discoverable by the Registry API and responds to function instance queries for these resources.'
ms.assetid: '335b11f1-99f3-42ab-ba22-681f572da246'
title: Registry Provider
---

# Registry Provider

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

The registry provider is a synchronous local provider that enumerates resources discoverable by the [Registry API](https://msdn.microsoft.com/library/windows/desktop/ms724875) and responds to function instance queries for these resources. The registry provider can enumerate specially-formatted REG\_BINARY registry values that are located in the area of the registry assigned to the Function Discovery registry store.

## Query Results

The registry provider supports collection queries and instance queries. That means the provider supports both the [**IFunctionInstanceCollectionQuery::Execute**](ifunctioninstancecollectionquery-execute-method.md) and [**IFunctionInstanceQuery::Execute**](ifunctioninstancequery-execute-method.md) methods. Because the registry provider is synchronous, an **Execute** method returns S\_OK for a successful query.

In addition, the registry provider supports subcategory queries. A subcategory is used to limit the results returned by a query. To specify a subcategory, pass a non-NULL value to the *pszSubCategory* parameter of the [**IFunctionDiscovery::CreateInstanceCollectionQuery**](ifunctiondiscovery-createinstancecollectionquery-method.md) method.

## Query Constraints

A query constraint can be added by calling [**IFunctionInstanceCollectionQuery::AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) on an [**IFunctionInstanceCollectionQuery**](ifunctioninstancecollectionquery.md) object before executing the query.

The following table shows the query constraints supported by the registry provider. The table also shows the value to pass to the *pszConstraintValue* parameter of the [**AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md) method.



| Constraint Name                         | Constraint Value                                                                                                                                                       | Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FD\_QUERYCONSTRAINT\_PROVIDERINSTANCEID | The provider instance identifier, as returned by [**IFunctionInstance::GetProviderInstanceID**](ifunctioninstance-getproviderinstanceid-method.md).                   | When this constraint is specified, the query returns the function instance matching the provider instance identifier. The function instance must be present on the system.Applying this query constraint is equivalent to calling [**IFunctionDiscovery::GetInstance**](ifunctiondiscovery-getinstance-method.md).<br/> The FD\_QUERYCONSTRAINT\_PROVIDERINSTANCEID and FD\_QUERYCONSTRAINT\_SUBCATEGORY constraints cannot be used simultaneously.<br/> |
| FD\_QUERYCONSTRAINT\_SUBCATEGORY        | The relative path of the registry folder to search for matching keys. The path contains one or more folders, separated by backslashes; for example, `folder1\folder2`. | When this constraint is specified, the returned set of function instances correspond to keys stored in the named folder.By default, this constraint is not specified, and the registry provider searches for matching function instances from the root of the registry provider namespace.<br/>                                                                                                                                                                 |
| FD\_QUERYCONSTRAINT\_RECURSESUBCATEGORY | FD\_CONSTRAINTVALUE\_RECURSESUBCATEGORY\_TRUE                                                                                                                          | When this constraint is specified, the registry provider searches the specified folder and all subfolders for matching function instances. Specifying this constraint may affect the timeliness of received notifications. For more information, see [Notifications](#notifications).By default, this constraint is not specified.<br/>                                                                                                                         |



 

For more information about a named constraint, see [**Constraint Definitions**](constraint-definitions.md). For general information about query constraints, see [Constraints](constraints.md).

The FD\_QUERYCONSTRAINT\_VISIBILITY constraint is not supported by the registry Provider.

## Notifications

If a non-NULL [**IFunctionDiscoveryNotification**](ifunctiondiscoverynotification.md) pointer is passed to the query creation method (either [**CreateInstanceCollectionQuery**](ifunctiondiscovery-createinstancecollectionquery-method.md) or [**CreateInstanceQuery**](ifunctiondiscovery-createinstancequery-method.md)), then the registry provider will listen for events and send QUA\_ADD, QUA\_REMOVE, and QUA\_CHANGE notifications to the interface as appropriate. An implementation of the [**IFunctionDiscoveryNotification::OnUpdate**](ifunctiondiscoverynotification-onupdate-method.md) method should handle these notifications.

The registry provider sends a QUA\_ADD notification when a new function instance has been added to the registry store in the folder location being monitored by the active query. The registry provider sends a QUA\_REMOVE notification when a function instance known to both the client and provider was removed from the registry store location being monitored by the active query. The registry provider sends a QUA\_CHANGE notification when the property store associated with a function instance known to both the client and provider has been modified.

The native registry store has a single notification handle, which it uses to notify the listening application (such as the registry provider) that a registry key has changed. Unfortunately, the handle does not specify which key has changed.

This particular fact is most important for recursive queries. The registry provider must then re-examine every registry value in the query space and compare it to the cache to determine what kind if any notification to send to the listening client application. Due to timing issues, it is possible to misinterpret a native notification. For example, if a registry value (function instance) is removed and then re-added very quickly before the registry provider has a chance to re-examine all of the function instances, it is possible for the registry provider to send a QUA\_CHANGE to the client application rather than a QUA\_REMOVE followed by a QUA\_ADD. Conversely, if a registry value (function instance) is quickly added and then removed before the registry provider has a change to re-examine all the function instances, it is also possible for the provider to send no notification to the client application rather than a QUA\_ADD followed by a QUA\_REMOVE, because the provider would not have had a chance to see the value in the registry.

When writing applications, the limitations of the notification mechanisms must be kept in mind. Do not use the registry provider as a synchronization object. In addition, avoid recursive queries that result in a large number (tens of thousands) of returned function instances.

## Property Store

The registry provider implements writeable property stores. The [**IFunctionInstance::OpenPropertyStore**](ifunctioninstance-openpropertystore-method.md) method can be used to access the property keys (PKEYs) associated with a registry function instance. The methods of the [**IPropertyStore**](shell_IPropertyStore_cpp) interface can be used to get and set PKEYs associated with the function instance. **IPropertyStore::Commit** must be called after setting a PKEY value. When **Commit** is called, the registry provider serializes the property store into a binary blob and writes the blob to the registry. A QUA\_ADD or QUA\_CHANGE notification is generated when values are written to the registry.

## Required and Optional PKEYs

The registry provider supports an extensible property store. That means any PKEY can be added to the property store associated with a registry resource. For more information about PKEYs, see [**Key Definitions**](key-definitions.md).

There is only one PKEY required by the registry provider: PKEY\_Write\_Time. For a definition of this key, see [**General PKEYs**](general-pkeys.md).

## Related topics

<dl> <dt>

[Built-in Providers](built-in-providers.md)
</dt> </dl>

 

 




