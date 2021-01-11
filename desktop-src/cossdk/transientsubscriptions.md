---
description: Contains an object for each transient subscription. Transient subscriptions can be created on the fly for running object instances, and they vanish when the object is destroyed.
ms.assetid: beee291c-e03f-4ee0-b1f2-99dcf113c46e
title: TransientSubscriptions collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TransientSubscriptions
api_type: 
- COM
api_location: 
---

# TransientSubscriptions collection

Contains an object for each transient subscription. Transient subscriptions can be created on the fly for running object instances, and they vanish when the object is destroyed.

This collection supports the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **TransientSubscriptions** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**TransientPublisherProperties**](transientpublisherproperties.md)
-   [**TransientSubscriberProperties**](transientsubscriberproperties.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [Description](#description)
-   [Enabled](#enabled)
-   [EventClassPartitionID](#eventclasspartitionid)
-   [EventCLSID](#eventclsid)
-   [FilterCriteria](#filtercriteria)
-   [ID](#transientsubscriptions-collection)
-   [InterfaceID](#interfaceid)
-   [MethodName](#methodname)
-   [Name](#methodname)
-   [PerUser](#peruser)
-   [PublisherID](#publisherid)
-   [SubscriberInterface](#subscriberinterface)
-   [SubscriberPartitionID](#subscriberpartitionid)
-   [UserName](#username)

### Description



| Entry | Value |
|----------------|-------------------------------------|
| Description    | A description for the subscription. |
| Access         | ReadWrite                           |
| Type           | String                              |
| Default        | ""                                  |
| Minimum system | Windows 2000                        |



 

### Enabled



| Entry | Value |
|----------------|----------------------------------------------------------|
| Description    | Indicates whether the subscription is presently enabled. |
| Access         | ReadWrite                                                |
| Type           | Bool                                                     |
| Default        | True                                                     |
| Minimum system | Windows 2000                                             |



 

### EventClassPartitionID



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | When subscribing to an event class, used to represent the GUID of the partition ID containing the event class. When subscribing to event classes, the subscriber has the option to subscribe to an event class in the same or different partition. |
| Access         | ReadWrite                                                                                                                                                                                                                                          |
| Type           | String                                                                                                                                                                                                                                             |
| Default        | NULL                                                                                                                                                                                                                                               |
| Minimum system | Windows Server 2003                                                                                                                                                                                                                                |



 

### EventCLSID



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------|
| Description    | The CLSID for the event class. You can indicate an EventCLSID or a PublisherID but not both. |
| Access         | WriteOnce                                                                                    |
| Type           | String                                                                                       |
| Default        | N/A                                                                                          |
| Minimum system | Windows 2000                                                                                 |



 

### FilterCriteria



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------|
| Description    | A string that indicates the filter criteria. Can be a CLSID for a [**PublisherFilter**](/windows/desktop/api/EventSys/nn-eventsys-ipublisherfilter) class. |
| Access         | ReadWrite                                                                                                            |
| Type           | String                                                                                                               |
| Default        | N/A                                                                                                                  |
| Minimum system | Windows 2000                                                                                                         |



 

### ID



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Identifier for the subscription. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                        |
| Type           | String                                                                                                                                                           |
| Default        | <Generated>                                                                                                                                                |
| Minimum system | Windows 2000                                                                                                                                                     |



 

### InterfaceID



| Entry | Value |
|----------------|----------------------------------|
| Description    | IID for interface subscribed to. |
| Access         | WriteOnce                        |
| Type           | String                           |
| Default        | N/A                              |
| Minimum system | Windows 2000                     |



 

### MethodName



| Entry | Value |
|----------------|----------------------------------------------|
| Description    | Method on the interface being subscribed to. |
| Access         | ReadWrite                                    |
| Type           | String                                       |
| Default        | N/A                                          |
| Minimum system | Windows 2000                                 |



 

### Name



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The name for the subscription. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadWrite                                                                                                                                                                                                                              |
| Type           | String                                                                                                                                                                                                                                 |
| Default        | "New Subscription"                                                                                                                                                                                                                     |
| Minimum system | Windows 2000                                                                                                                                                                                                                           |



 

### PerUser



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------|
| Description    | Indicates whether the subscription applies only for a given user, represented by the UserName property. |
| Access         | ReadWrite                                                                                               |
| Type           | Bool                                                                                                    |
| Default        | False                                                                                                   |
| Minimum system | Windows 2000                                                                                            |



 

### PublisherID



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------|
| Description    | ID for the publisher. You can indicate an EventCLSID or a PublisherID but not both. |
| Access         | WriteOnce                                                                           |
| Type           | String                                                                              |
| Default        | ""                                                                                  |
| Minimum system | Windows 2000                                                                        |



 

### SubscriberInterface



| Entry | Value |
|----------------|------------------------------------------|
| Description    | A pointer to the subscriber's interface. |
| Access         | ReadWrite                                |
| Type           | Variant                                  |
| Default        | N/A                                      |
| Minimum system | Windows 2000                             |



 

### SubscriberPartitionID



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | When subscribing to an event class in the same partition, used to represent the GUID of the partition ID of the subscriber. When subscribing to event classes, the subscriber has the option to subscribe to an event class in the same or different partition. |
| Access         | WriteOnce                                                                                                                                                                                                                                                       |
| Type           | String                                                                                                                                                                                                                                                          |
| Default        | <Generated>                                                                                                                                                                                                                                               |
| Minimum system | Windows Server 2003                                                                                                                                                                                                                                             |



 

### UserName



| Entry | Value |
|----------------|-------------------------------------------------------------------------|
| Description    | The name of user that the subscription applies to when PerUser is True. |
| Access         | ReadWrite                                                               |
| Type           | String                                                                  |
| Default        | N/A                                                                     |
| Minimum system | Windows 2000                                                            |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
