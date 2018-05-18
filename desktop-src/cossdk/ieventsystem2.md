---
Description: 'Used by the Microsoft Internet Explorer System Event Notification Service (SENS) to access the event data store. This interface extends the IEventSystem interface.'
ms.assetid: 'ad3c38a6-fa2d-4fcd-8782-1fac7595e829'
title: IEventSystem2 interface
---

# IEventSystem2 interface

Used by the Microsoft Internet Explorer System Event Notification Service (SENS) to access the event data store. This interface extends the [**IEventSystem**](ieventsystem.md) interface.

## When to implement

You do not need to implement the **IEventSystem2** interface. A system-supplied event system object (CLSID\_CEventSystem) implements **IEventSystem2**.

## When to use

If you use SENS, you can call the methods of **IEventSystem2** to add and remove objects to and from the event store and to obtain objects from the event store.

Because [**IEventPublisher**](https://msdn.microsoft.com/library/windows/desktop/ms679672) and the publisher object are no longer supported, [**IEventObjectChange**](ieventobjectchange.md) is not called on the [**ChangedPublisher**](ieventobjectchange-changedpublisher.md) method.

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



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**IEventSystem**](ieventsystem.md)
</dt> </dl>

 

 




