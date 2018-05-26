---
Description: Function Discovery clients use queries to enumerate resources and to be notified when resources have been added, removed, or updated.
ms.assetid: 3c255fb4-8f9d-47a2-9770-1aa528d07f43
title: Function Discovery Queries
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Function Discovery Queries

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

Function Discovery clients use queries to enumerate resources and to be notified when resources have been added, removed, or updated. Resources in Function Discovery are represented by [function instances](function-objects.md). Function instances provide a unique identifier for a resource (such as a device) and metadata about the resource. Queries can be constrained, so that only function instances of interest to the client are returned.

Function Discovery provides a general framework for the representation of resources (function instances) and for the representation of query results (errors and events). However, each Function Discovery provider may implement only a subset of the query constraints, events, notifications, and metadata properties defined by Function Discovery. For information about how a specific provider implements queries, events, and metadata, follow the link to the provider documentation from the [Built-in Providers](built-in-providers.md) topic.

## Query Types

Function Discovery supports the following query types.



| Term                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Instance_query"></span><span id="instance_query"></span><span id="INSTANCE_QUERY"></span>Instance query<br/>         | Queries for a specified function instance. You can create an instance query by calling [**IFunctionDiscovery::CreateInstanceQuery**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctiondiscovery-createinstancequery?branch=master). You cannot use query constraints or property constraints with this query.<br/> An instance query is functionally equivalent to a provider query with the **FD\_QUERYCONSTRAINT\_PROVIDERINSTANCEID** constraint applied. Instance queries are usually constructed after a provider query or predefined query has been executed. A specific function instance identifier can be retrieved from provider query or predefined query results, and then an instance query can be created using this identifier.<br/> |
| <span id="Provider_query"></span><span id="provider_query"></span><span id="PROVIDER_QUERY"></span>Provider query<br/>         | Queries a specific provider for a collection of function instances. You can create a provider query by calling [**IFunctionDiscovery::CreateInstanceCollectionQuery**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctiondiscovery-createinstancecollectionquery?branch=master) and passing a category string beginning with "Provider\\" to the *pszCategory* parameter. <br/> You can constrain the results returned by a provider query. For more information, see [Constraints](constraints.md).<br/>                                                                                                                                                                                                                                           |
| <span id="Predefined_query"></span><span id="predefined_query"></span><span id="PREDEFINED_QUERY"></span>Predefined query<br/> | Aggregates one or more queries. A predefined query is composed of one or more provider queries and/or one or more predefined queries. You can create a predefined query by calling [**IFunctionDiscovery::CreateInstanceCollectionQuery**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctiondiscovery-createinstancecollectionquery?branch=master) and passing a category string beginning with "Layered\\" to the *pszCategory* parameter. For more information about layered categories, see [Category Metadata Manifests](category-metadata-manifests.md).<br/> You can constrain the results returned by a predefined query. For more information, see [Constraints](constraints.md).<br/>                                                    |



 

## Query Objects

A query object can be type [**IFunctionInstanceQuery**](/windows/win32/FunctionDiscoveryAPI/nn-functiondiscoveryapi-ifunctioninstancequery?branch=master) or [**IFunctionInstanceCollectionQuery**](/windows/win32/FunctionDiscoveryAPI/nn-functiondiscoveryapi-ifunctioninstancecollectionquery?branch=master). These objects are created by calling [**IFunctionDiscovery::CreateInstanceQuery**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctiondiscovery-createinstancequery?branch=master) or [**IFunctionDiscovery::CreateInstanceCollectionQuery**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctiondiscovery-createinstancecollectionquery?branch=master) respectively. Before any results can be retrieved from a query object, you must call the appropriate query execution method ([**IFunctionInstanceQuery::Execute**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancequery-execute?branch=master) or [**IFunctionInstanceCollectionQuery::Execute**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancecollectionquery-execute?branch=master)).

Once a query has finished enumerating function instances, the query object will remain open until it is explicitly released. Do not **Release** a query object from a callback method. If you initialized COM using the single-threaded apartment model, then calling **Release** from a callback method will cause a deadlock. Although you can **Release** a query object from a callback method if you initialized COM using the multithreaded apartment model, it is not recommended.

## Query Constraints

Provider queries and predefined queries can be constrained. For general information about query constraints, see [Constraints](constraints.md). For a list of available query constraints, see [**Constraint Definitions**](constraint-definitions.md).

Not all providers support all query constraints. Furthermore, each query constraint may be interpreted differently by two different providers. For provider-specific information about supported query constraints, follow the link to the provider documentation from the [Built-in Providers](built-in-providers.md) topic.

## Query Results

Query results may be returned synchronously or asynchronously. Network providers, such as the WSD, SSDP, and NetBIOS providers, return results asynchronously. When results are returned asynchronously, the query execution method ([**IFunctionInstanceCollectionQuery::Execute**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancecollectionquery-execute?branch=master) or [**IFunctionInstanceQuery::Execute**](/windows/win32/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstancequery-execute?branch=master)) returns **E\_PENDING** and results are returned using the [**IFunctionDiscoveryNotification**](/windows/win32/FunctionDiscoveryNotification/nn-functiondiscoveryapi-ifunctiondiscoverynotification?branch=master) interface.

The [**IFunctionDiscoveryNotification::OnEvent**](ifunctiondiscoverynotification-onevent.md) callback method is used by network protocol providers to signal the completion of a query where the protocol specifies a defined interval in which search results will be accepted. The [NetBIOS](netbios-provider.md), WSD, and [SSDP](ssdp-provider.md) providers use a *dwEventId* of **FD\_EVENTID\_SEARCHCOMPLETE** to indicate search completion. Once this notification is sent, a query ignores all incoming responses to the initial search or probe request. However, the query will still monitor for Hello or Bye messages (used to indicate when a device is added or removed). The query will continue to monitor for these events until **Release** is called on the query object. This notification will not be sent if a catastrophic error occurs.

Each provider handles query results slightly differently. For information about the types of function instances returned by a specific provider, see [Built-in Providers](built-in-providers.md).

## Related topics

<dl> <dt>

[Function Discovery Categories](function-discovery-categories.md)
</dt> <dt>

[Category Metadata Manifests](category-metadata-manifests.md)
</dt> <dt>

[Constraints](constraints.md)
</dt> <dt>

[Built-in Providers](built-in-providers.md)
</dt> </dl>

 

 




