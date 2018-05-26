---
title: UI Automation Properties Overview
description: Microsoft UI Automation providers expose properties on UI Automation elements. Properties enable client applications to retrieve information about controls.
ms.assetid: 35f017cb-f50a-4680-9f01-5079aa59da73
keywords:
- UI Automation,properties overview
- UI Automation,properties vs. events
- UI Automation,events vs. properties
- properties,about
- properties,identifiers
- properties,values
- properties,events
- events,properties
- properties,dynamic
- dynamic properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UI Automation Properties Overview

Microsoft UI Automation providers expose properties on UI Automation elements. Properties enable client applications to retrieve information about controls.

UI Automation exposes two different kinds of properties: *automation element properties*, and *control pattern propertes*. The automation element properties consist of a common set of properties, such as Name, AcceleratorKey, and ClassName, that are exposed by all UI Automation elements, regardless of the control type. Most automation element properties are static values.

Control pattern properties are those that are exposed by a control that supports a particular control pattern. Each control pattern has a corresponding set of control pattern properties that the control must expose. For example, a control that supports the [Grid](uiauto-implementinggrid.md) control pattern exposes the ColumnCount and RowCount properties. Most control pattern properties are dynamic values.

This topic contains the following sections.

-   [Property Identifiers](#property-identifiers)
-   [Property Values](#property-values)
-   [Properties and Events](#properties-and-events)
-   [Related topics](#related-topics)

## Property Identifiers

Every property is identified by a **PROPERTYID** numeric value called a *property identifier* (ID). Providers and clients use the numeric IDs in method calls such as [**IRawElementProviderAdviseEvents::AdviseEventAdded**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irawelementprovideradviseevents-adviseeventadded?branch=master) and [**IUIAutomationElement::GetCachedPropertyValue**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedpropertyvalue?branch=master) to identify property requests. For a detailed description of each UI Automation property identifier, including the data type and default value of each property, see [Property Identifiers](uiauto-entry-propids.md).

## Property Values

All properties are read-only, although some can be changed by using methods that act on the control, such as [**IDockProvider::SetDockPosition**](/windows/win32/UIAutomationCore/nf-uiautomationcore-idockprovider-setdockposition?branch=master) (provider) or [**IUIAutomationDockPattern::SetDockPosition**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationdockpattern-setdockposition?branch=master) (client).

For information about retrieving property values, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).

## Properties and Events

Closely associated with the properties in UI Automation is the concept of *property-changed events*. For dynamic properties, a client application needs a way to know that a property value has changed, so that it can update its cache of information or react to the new information in some other way. Clients can register to listen for property-changed events on any property.

Providers raise events when something in the UI changes. For example, if a check box is selected or cleared, a property-changed event is raised by the provider implementation of the [Toggle](uiauto-implementingtoggle.md) control pattern. Providers can raise events selectively, depending on whether any clients are listening for events, or listening for specific events.

Not all property changes raise events; that is entirely up to the implementation of the UI Automation provider for the element. For example, the standard proxy providers for list boxes do not raise a property-changed event when the Selection property changes. In this case, the application must listen for the event raised when the selection changes ([**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md#uia-selectionitem-elementselectedeventid)).

Clients listen for events by subscribing to them, as described at [Subscribing to UI Automation Events](uiauto-eventsforclients.md). For property-changed events in particular, clients must implement [**IUIAutomationPropertyChangedEventHandler**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationpropertychangedeventhandler?branch=master) and pass the interface to [**IUIAutomation::AddPropertyChangedEventHandler**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-addpropertychangedeventhandler?branch=master) or [**IUIAutomation::AddPropertyChangedEventHandlerNativeArray**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-addpropertychangedeventhandlernativearray?branch=master).

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**GetCurrentPropertyValue**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpropertyvalue?branch=master)
</dt> <dt>

[**GetCurrentPropertyValueEx**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpropertyvalueex?branch=master)
</dt> <dt>

[**GetCachedPropertyValue**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedpropertyvalue?branch=master)
</dt> <dt>

[**GetCachedPropertyValueEx**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedpropertyvalueex?branch=master)
</dt> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Events Overview](uiauto-eventsoverview.md)
</dt> </dl>

 

 




