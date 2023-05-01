---
title: UI Automation Events Overview
description: Microsoft UI Automation event notification is a key feature for assistive technologies, such as screen readers and screen magnifiers.
ms.assetid: 0ded64ba-188e-427e-897f-4381237ace75
keywords:
- UI Automation,events overview
- UI Automation,event categories
- UI Automation,event notifications
- event notifications
- events,categories
- events,event notifications
- Property change events
- Element action events
- Structure change events
- Global desktop change events
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation Events Overview

Microsoft UI Automation event notification is a key feature for assistive technologies, such as screen readers and screen magnifiers. These UI Automation clients track events that are raised by UI Automation providers when something happens in the UI and use the information to notify end users.

Efficiency is improved by allowing provider applications to raise events selectively, depending on whether any clients are subscribed to those events, or not at all, if no clients are listening for any events.

UI Automation events fall into the following categories.



| Event Category        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Property change       | Raised when a property on UI Automation element or control pattern changes. For example, if a client needs to monitor an application check box control, it can register to listen for a property change event on the [**IUIAutomationTogglePattern::CurrentToggleState**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtogglepattern-get_currenttogglestate) property. When the check box control is checked or unchecked, the provider raises the event and the client can act as necessary. |
| Element action        | Raised when a change in the UI results from end user or programmatic activity, for example, when a button is clicked or invoked through [**IUIAutomationInvokePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationinvokepattern).                                                                                                                                                                                                                                                     |
| Structure change      | Raised when the structure of the UI Automation tree changes. The structure changes when new UI items become visible, hidden, or removed on the desktop.                                                                                                                                                                                                                                                                                                              |
| Global desktop change | Raised when actions of global interest to the client occur, such as when the focus shifts from one element to another, or when a window closes.                                                                                                                                                                                                                                                                                                                      |
| Notification          | Raised when an app calls the [**UiaRaiseNotificationEvent**](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaraisenotificationevent) function. [**NotificationKind**](/windows/win32/api/uiautomationcore/ne-uiautomationcore-notificationkind) indicates the type of the notification.                                                                                                                                                                                                                                                 |



 

Some events do not necessarily mean that the state of the UI has changed. For example, if the user tabs to a text entry field, and then clicks a button to update the field, a [**UIA\_Text\_TextChangedEventId**](uiauto-event-ids.md) event is raised, even if the user did not actually change the text. When processing an event, it may be necessary for a client application to check whether anything has actually changed before taking action.

The following events may be raised even when the state of the UI has not changed.

-   [**UIA\_AutomationPropertyChangedEventId**](uiauto-event-ids.md) (depending on the property that has changed)
-   [**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md)
-   [**UIA\_Selection\_InvalidatedEventId**](uiauto-event-ids.md)
-   [**UIA\_Text\_TextChangedEventId**](uiauto-event-ids.md)

For a description of all UI Automation events, see [Event Identifiers](uiauto-event-ids.md).

## Related topics

<dl> <dt>

[Subscribing to UI Automation Events](uiauto-eventsforclients.md)
</dt> </dl>

 

 