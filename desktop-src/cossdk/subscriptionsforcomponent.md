---
Description: Contains an object for each subscription for the parent Components collection.
ms.assetid: ec93d500-32bf-4e67-9eda-c1fe0349faa2
title: SubscriptionsForComponent collection
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# SubscriptionsForComponent collection

Contains an object for each subscription for the parent [**Components**](components.md) collection.

This collection supports the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](/windows/desktop/api/ComAdmin/) object.

## Members

The **SubscriptionsForComponent** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**PublisherProperties**](publisherproperties.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**SubscriberProperties**](subscriberproperties.md)

You can navigate to this collection from the following collections:

-   [**Components**](components.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/desktop/api/ComAdmin/) object within the collection:

-   [Description](#description)
-   [Enabled](#enabled)
-   [EventClassPartitionID](#eventclasspartitionid)
-   [EventCLSID](#eventclsid)
-   [FilterCriteria](#filtercriteria)
-   [ID](#subscriptionsforcomponent-collection)
-   [InterfaceID](#interfaceid)
-   [MachineName](#machinename)
-   [MethodName](#methodname)
-   [Name](#machinename)
-   [PerUser](#peruser)
-   [PublisherID](#publisherid)
-   [Queued](#queued)
-   [SubscriberMoniker](#subscribermoniker)
-   [SubscriberPartitionID](#subscriberpartitionid)
-   [UserName](#username)

### Description



|                |                                     |
|----------------|-------------------------------------|
| Description    | A description for the subscription. |
| Access         | ReadWrite                           |
| Type           | String                              |
| Default        | ""                                  |
| Minimum system | Windows 2000                        |



 

### Enabled



|                |                                                          |
|----------------|----------------------------------------------------------|
| Description    | Indicates whether the subscription is presently enabled. |
| Access         | ReadWrite                                                |
| Type           | Bool                                                     |
| Default        | True                                                     |
| Minimum system | Windows 2000                                             |



 

### EventClassPartitionID



|                |                                                                                                                                                                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | When subscribing to an event class, used to represent the GUID of the partition ID containing the event class. When subscribing to event classes, the subscriber has the option to subscribe to an event class in the same or different partition. |
| Access         | ReadWrite                                                                                                                                                                                                                                          |
| Type           | String                                                                                                                                                                                                                                             |
| Default        | NULL                                                                                                                                                                                                                                               |
| Minimum system | Windows Server 2003                                                                                                                                                                                                                                |



 

### EventCLSID



|                |                                                                                              |
|----------------|----------------------------------------------------------------------------------------------|
| Description    | The CLSID for the event class. You can indicate an EventCLSID or a PublisherID but not both. |
| Access         | WriteOnce                                                                                    |
| Type           | String                                                                                       |
| Default        | N/A                                                                                          |
| Minimum system | Windows 2000                                                                                 |



 

### FilterCriteria



|                |                                                                                                                  |
|----------------|------------------------------------------------------------------------------------------------------------------|
| Description    | A string indicating the filter criteria. Can be a CLSID for a [**PublisherFilter**](/windows/desktop/api/EventSys/nn-eventsys-ipublisherfilter) class. |
| Access         | ReadWrite                                                                                                        |
| Type           | String                                                                                                           |
| Default        | N/A                                                                                                              |
| Minimum system | Windows 2000                                                                                                     |



 

### ID



|                |                                                                                                                                                                  |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Identifier for the subscription. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                        |
| Type           | String                                                                                                                                                           |
| Default        | &lt;Generated&gt;                                                                                                                                                |
| Minimum system | Windows 2000                                                                                                                                                     |



 

### InterfaceID



|                |                                          |
|----------------|------------------------------------------|
| Description    | The IID for the interface subscribed to. |
| Access         | ReadWrite                                |
| Type           | String                                   |
| Default        | N/A                                      |
| Minimum system | Windows 2000                             |



 

### MachineName



|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| Description    | A remote computer name for subscriptions to event classes on a remote computer. |
| Access         | ReadWrite                                                                       |
| Type           | String                                                                          |
| Default        | ""                                                                              |
| Minimum system | Windows 2000                                                                    |



 

### MethodName



|                |                                              |
|----------------|----------------------------------------------|
| Description    | Method on the interface being subscribed to. |
| Access         | ReadWrite                                    |
| Type           | String                                       |
| Default        | N/A                                          |
| Minimum system | Windows 2000                                 |



 

### Name



|                |                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Name for the subscription. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadWrite                                                                                                                                                                                                                          |
| Type           | String                                                                                                                                                                                                                             |
| Default        | "New Subscription"                                                                                                                                                                                                                 |
| Minimum system | Windows 2000                                                                                                                                                                                                                       |



 

### PerUser



|                |                                                                             |
|----------------|-----------------------------------------------------------------------------|
| Description    | Indicates whether the subscription applies only for a given user, UserName. |
| Access         | ReadWrite                                                                   |
| Type           | Bool                                                                        |
| Default        | False                                                                       |
| Minimum system | Windows 2000                                                                |



 

### PublisherID



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| Description    | The ID for the publisher. You can indicate an EventCLSID or a PublisherID but not both. |
| Access         | WriteOnce                                                                               |
| Type           | String                                                                                  |
| Default        | ""                                                                                      |
| Minimum system | Windows 2000                                                                            |



 

### Queued



|                |                                               |
|----------------|-----------------------------------------------|
| Description    | Indicates whether the subscription is queued. |
| Access         | ReadWrite                                     |
| Type           | Bool                                          |
| Default        | False                                         |
| Minimum system | Windows 2000                                  |



 

### SubscriberMoniker



|                |                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| Description    | A moniker for a subscriber marked as Queued. A default value is generated when Queued is initially set to True. |
| Access         | ReadWrite                                                                                                       |
| Type           | String                                                                                                          |
| Default        | N/A                                                                                                             |
| Minimum system | Windows 2000                                                                                                    |



 

### SubscriberPartitionID



|                |                                                                                                                                                                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | When subscribing to an event class in the same partition, used to represent the GUID of the partition ID of the subscriber. When subscribing to event classes, the subscriber has the option to subscribe to an event class in the same or different partition. |
| Access         | WriteOnce                                                                                                                                                                                                                                                       |
| Type           | String                                                                                                                                                                                                                                                          |
| Default        | &lt;Generated&gt;                                                                                                                                                                                                                                               |
| Minimum system | Windows Server 2003                                                                                                                                                                                                                                             |



 

### UserName



|                |                                                                          |
|----------------|--------------------------------------------------------------------------|
| Description    | The name of user that the subscription applies to, when PerUser is True. |
| Access         | ReadWrite                                                                |
| Type           | String                                                                   |
| Default        | N/A                                                                      |
| Minimum system | Windows 2000                                                             |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



