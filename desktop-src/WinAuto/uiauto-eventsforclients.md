---
title: Subscribing to UI Automation Events
description: Microsoft UI Automation allows clients to subscribe to events of interest. This capability improves performance by eliminating the need to continually poll the UI elements in the system to see if any information, structure, or state has changed.
ms.assetid: '7019ecb8-6123-4e00-926c-6725d7e71385'
keywords: ["clients,UI Automation events", "clients,events for UI Automation", "UI Automation,events for clients", "UI Automation,client events", "UI Automation,subscribing to events", "UI Automation,subscription methods", "UI Automation,code examples", "UI Automation,examples", "UI Automation,samples", "subscribing to UI Automation events", "events,UI Automation subscription", "Samples"]
---

# Subscribing to UI Automation Events

Microsoft UI Automation allows clients to subscribe to events of interest. This capability improves performance by eliminating the need to continually poll the UI elements in the system to see if any information, structure, or state has changed.

Efficiency is also improved by the ability to listen for events only within a defined scope. For example, a client can listen for selection changes on an item in a list, on the list itself, or on an entire dialog box.

> [!Note]  
> Do not assume that all possible events are raised by a UI Automation provider. For example, not all property changes cause events to be raised by the standard proxy providers for Windows Forms and Microsoft Win32 controls.

 

For a broader view of UI Automation events, see [UI Automation Events Overview](uiauto-eventsoverview.md).

> [!Note]  
> Before implementing an event handler, you should be familiar with the threading issues described in [Understanding Threading Issues](uiauto-threading.md).

 

This topic contains the following sections.

-   [Registering Event Handlers](#registering-event-handlers)
-   [Examples](#examples)
-   [Related topics](#related-topics)

## Registering Event Handlers

Client applications subscribe to events of a particular kind by registering an event handler, using one of the following [**IUIAutomation**](uiauto-iuiautomation.md) methods.



| Subscription Method                                                                                                                                                                                                | Event Type       | Callback Interface                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------------------------------------|
| [**AddFocusChangedEventHandler**](uiauto-iuiautomation-addfocuschangedeventhandler.md)                                                                                                                            | Focus change     | [**IUIAutomationFocusChangedEventHandler**](uiauto-iuiautomationfocuschangedeventhandler.md)         |
| [**AddPropertyChangedEventHandler**](uiauto-iuiautomation-addpropertychangedeventhandler.md), [**AddPropertyChangedEventHandlerNativeArray**](uiauto-iuiautomation-addpropertychangedeventhandlernativearray.md) | Property change  | [**IUIAutomationPropertyChangedEventHandler**](uiauto-iuiautomationpropertychangedeventhandler.md)   |
| [**AddStructureChangedEventHandler**](uiauto-iuiautomation-addstructurechangedeventhandler.md)                                                                                                                    | Structure change | [**IUIAutomationStructureChangedEventHandler**](uiauto-iuiautomationstructurechangedeventhandler.md) |
| [**AddNotificationEventHandler**](uiauto-iuiautomation5-addnotificationeventhandler.md)                                                                                                                           | Notification     | [**IUIAutomationNotificationEventHandler**](uiauto-iuiautomationnotificationeventhandler.md)         |
| [**AddAutomationEventHandler**](uiauto-iuiautomation-addautomationeventhandler.md)                                                                                                                                | Other events     | [**IUIAutomationEventHandler**](uiauto-iuiautomationeventhandler.md)                                 |



 

When a client adds an event handler for all descendants ([**TreeScope\_Descendants**](uiauto-treescopeenum.md#treescope-descendants)), UI Automation adds only one handler for the root of sub-tree, and the handler listens across all descendents. UI Automation does not add event handlers recursively.

When a client calls the [**IUIAutomation::RemoveAllEventHandlers**](uiauto-iuiautomation-removealleventhandlers.md) method, UI Automation removes all event handlers from the client process.

To receive and handle events, you implement an event-handling object that exposes a callback interface, and you must register the object by calling an event registration method such as [**IUIAutomation::AddPropertyChangedEventHandler**](uiauto-iuiautomation-addpropertychangedeventhandler.md). The callback interface has a single method; UI Automation calls this method when the event is processed.

On shutdown, or when UI Automation events are no longer of interest to the application, UI Automation clients should call one or more of the following [**IUIAutomation**](uiauto-iuiautomation.md) methods.

> [!Note]  
> A UI Automation client should not use multiple threads to add or remove event handlers. Unexpected behavior can result if one event handler is being added or removed while another is being added or removed in the same client process.

 



| Method                                                                                                | Description                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RemoveAutomationEventHandler**](uiauto-iuiautomation-removeautomationeventhandler.md)             | Unregisters an event handler that was registered by using [**AddAutomationEventHandler**](uiauto-iuiautomation-addautomationeventhandler.md).                                                                                                                                  |
| [**RemoveFocusChangedEventHandler**](uiauto-iuiautomation-removefocuschangedeventhandler.md)         | Unregisters an event handler that was registered by using [**AddFocusChangedEventHandler**](uiauto-iuiautomation-addfocuschangedeventhandler.md).                                                                                                                              |
| [**RemovePropertyChangedEventHandler**](uiauto-iuiautomation-removepropertychangedeventhandler.md)   | Unregisters an event handler that was registered by using [**AddPropertyChangedEventHandler**](uiauto-iuiautomation-addpropertychangedeventhandler.md) or [**AddPropertyChangedEventHandlerNativeArray**](uiauto-iuiautomation-addpropertychangedeventhandlernativearray.md). |
| [**RemoveStructureChangedEventHandler**](uiauto-iuiautomation-removestructurechangedeventhandler.md) | Unregisters an event handler that was registered by using [**AddStructureChangedEventHandler**](uiauto-iuiautomation-addstructurechangedeventhandler.md).                                                                                                                      |
| [**RemoveNotificationEventHandler**](uiauto-iuiautomation5-removenotificationeventhandler.md)        | Unregisters an event handler that weas registered by using [**AddNotificationEventHandler**](uiauto-iuiautomation5-addnotificationeventhandler.md).                                                                                                                            |
| [**RemoveAllEventHandlers**](uiauto-iuiautomation-removealleventhandlers.md)                         | Unregisters all registered event handlers.                                                                                                                                                                                                                                      |



 

It is possible for an event to be delivered to an event handler after the handler has been unsubscribed, if the event is received simultaneously with the request to unsubscribe the event. The best practice is to follow the Component Object Model (COM) standard and avoid destroying the event handler object until its reference count has reached zero. Destroying an event handler immediately after unsubscribing for events may result in an access violation if an event is delivered late.

## Examples

For code examples that show how to handle UI Automation events, see [How to Implement Event Handlers](uiauto-howto-implement-event-handlers.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Events Overview](uiauto-eventsoverview.md)
</dt> <dt>

[Understanding Threading Issues](uiauto-threading.md)
</dt> </dl>

 

 




