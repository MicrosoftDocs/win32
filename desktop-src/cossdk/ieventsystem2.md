---
description: Used by the Microsoft Internet Explorer System Event Notification Service (SENS) to access the event data store. This interface extends the IEventSystem interface.
ms.assetid: ad3c38a6-fa2d-4fcd-8782-1fac7595e829
title: IEventSystem2 interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEventSystem2
api_type: 
- COM
api_location: 
---

# IEventSystem2 interface

Used by the Microsoft Internet Explorer System Event Notification Service (SENS) to access the event data store. This interface extends the [**IEventSystem**](/windows/desktop/api/EventSys/nn-eventsys-ieventsystem) interface.

## When to implement

You do not need to implement the **IEventSystem2** interface. A system-supplied event system object (CLSID\_CEventSystem) implements **IEventSystem2**.

## When to use

If you use SENS, you can call the methods of **IEventSystem2** to add and remove objects to and from the event store and to obtain objects from the event store.

Because [**IEventPublisher**](/windows/desktop/api/eventsys/nn-eventsys-ieventpublisher) and the publisher object are no longer supported, [**IEventObjectChange**](/windows/desktop/api/Eventsys/nn-eventsys-ieventobjectchange) is not called on the [**ChangedPublisher**](/windows/desktop/api/Eventsys/nf-eventsys-ieventobjectchange-changedpublisher) method.

## Members

The **IEventSystem2** interface inherits from **IEventSystem**. **IEventSystem2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEventSystem2** interface has these methods.



| Method                                                                         | Description                                                                       |
|:-------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**GetVersion**](ieventsystem2-getversion.md)                                 | Retrieves the version number of the event system.<br/>                      |
| [**VerifyTransientSubscribers**](ieventsystem2-verifytransientsubscribers.md) | Verifies the existence of all transient subscribers in the data store.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**IEventSystem**](/windows/desktop/api/EventSys/nn-eventsys-ieventsystem)
</dt> </dl>

 

