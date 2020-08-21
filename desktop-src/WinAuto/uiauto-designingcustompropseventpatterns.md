---
title: Design custom properties, events, and control patterns
description: The design of a custom property, event, or control pattern should be useful in a wide variety of control implementations.
ms.assetid: e4b224a0-3958-4ae7-96cb-fe6dc16511a7
keywords:
- UI Automation,custom properties
- UI Automation,events overview
- UI Automation,control patterns overview
- UI Automation,designing custom properties
- UI Automation,designing events
- UI Automation,designing control patterns
- UI Automation,WinEvents
- custom properties,designing
- events,designing
- events,WinEvents
- control patterns,designing
- WinEvents
ms.topic: article
ms.date: 05/31/2018
---

# Design custom properties, events, and control patterns

The design of a custom property, event, or control pattern should be useful in a wide variety of control implementations. Control- or application-specific designs that are useful only in limited scenarios should be avoided. The design should follow the example of the existing Microsoft UI Automation properties, events, and control patterns, which were carefully specified to meet the needs of a wide variety of accessibility and automated testing applications.

Implementing the specification for a custom property, event, or control pattern involves the cooperation and agreement of parties on both the client and provider sides, and requires both parties to implement the specification consistently. Companies are encouraged to work with industry organizations such as the [Accessibility Interoperability Alliance (AIA)](https://www.atia.org/) to design and publish the specification for the custom property, event, or control pattern. In this way, consensus can be reached and interoperability with the widest variety of applications can be ensured.

This topic contains the following sections:

-   [When to Use Custom Properties and Events](#when-to-use-custom-properties-and-events)
-   [Designing Custom Properties](#designing-custom-properties)
-   [Designing Custom Events](#designing-custom-events)
    -   [Custom UI Automation Events and WinEvents](#custom-ui-automation-events-and-winevents)
-   [Designing Custom Control Patterns](#designing-custom-control-patterns)
-   [Custom Control Types](#custom-control-types)
-   [Related topics](#related-topics)

## When to Use Custom Properties and Events

Before creating a custom property, event, or control pattern, make sure that UI Automation does not provide an existing solution. For example, creating a custom "Click" control pattern is not necessary because the [Invoke](uiauto-implementinginvoke.md) control pattern already describes that functionality.

If you decide that a custom property, event, or control pattern is needed, make sure that it is not too vague or generic. For example, a control pattern called "Show" is not useful because the visibility of a control can be indicated by an availability property on the element, such as [**UIA\_IsExpandCollapsePatternAvailablePropertyId**](uiauto-control-pattern-availability-propids.md) or [**UIA\_IsScrollItemPatternAvailablePropertyId**](uiauto-control-pattern-availability-propids.md).

Before implementing a custom solution, carefully confirm it is needed and then design the functionality completely.

## Designing Custom Properties

UI Automation includes two basic types of properties: automation element properties, and control pattern properties. The automation element properties consist of a common set of properties, such as Name, AcceleratorKey, and ClassName, that are exposed by all UI Automation elements, regardless of the control type. Control pattern properties are exposed by a control through a particular control pattern. Each control pattern has a corresponding set of control pattern properties that the control must expose. For example, a control that supports the [Grid](uiauto-implementinggrid.md) control pattern exposes the ColumnCount and RowCount properties.

A custom automation element property or control pattern property should adhere to the following design guidelines:

-   A custom property must have one of the following data types specified by the [**UIAutomationType**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-uiautomationtype) enumeration. No other data types are supported for custom properties.
    -   **UIAutomationType\_Bool**
    -   **UIAutomationType\_Double**
    -   **UIAutomationType\_Element**
    -   **UIAutomationType\_Int**
    -   **UIAutomationType\_Point**
    -   **UIAutomationType\_String**
-   If the custom property contains string data ([**BSTR**](/previous-versions/windows/desktop/automat/bstr)), the specification must state whether the property is localizable (that is, whether the string can be translated into different UI languages).
-   The custom property should not overlap with the features or functionality of existing properties.

## Designing Custom Events

Applications use UI Automation event notifications to respond to changes and actions involving UI items. Most properties have associated property-changed events that UI Automation raises when the value of the property changes. If you introduce a custom property, you should consider introducing any corresponding custom events that may also be needed.

A custom event should adhere to the following design guidelines:

-   The custom event must be "stateless." It cannot be associated with a specific property or value.
-   The custom event should not overlap with the definition or role of any existing event.

### Custom UI Automation Events and WinEvents

[WinEvents](winevents-infrastructure.md) are a useful interprocess communication and eventing mechanism in the Microsoft Windows platform. However, introducing a new WinEvent ID is risky because it can cause collisions with other applications or the operating system, resulting in the system becoming unstable. To avoid collisions, Microsoft has defined several different categories of WinEvents and, for each category, has defined one or more ranges of values for use as WinEvent IDs. For more information, see [Allocation of WinEvent IDs](allocation-of-winevent-ids.md).

Custom UI Automation events avoid conflicts by allocating the event ID internally in the UI Automation framework.

## Designing Custom Control Patterns

A control pattern is an interface with properties, methods, and events that define a discrete piece of functionality available from an automation element. Control pattern methods allow UI Automation clients to manipulate a particular aspect of the control. The control pattern properties and events provide information about some aspect of the control, and provide information about the state of the automation element that implements the control pattern.

A custom control pattern should adhere to the following design guidelines:

-   A custom control pattern should cover a particular scenario. For example, the [ItemContainer](uiauto-implementingitemcontainer.md) control pattern is intended for querying a contained object regardless of the virtualization state, but it does not enumerate or count the contained objects.
-   A custom control pattern should not overlap with the features of existing control patterns. For example, the [Invoke](uiauto-implementinginvoke.md) and [ExpandCollapse](uiauto-implementingexpandcollapse.md) control patterns should not be combined and presented as a new control pattern. Either reuse existing control patterns or define unique scenarios with new control patterns.
-   Multiple custom control patterns can be designed together to support complex scenarios. For example, the [Selection](uiauto-implementingselection.md) and [SelectionItem](uiauto-implementingselectionitem.md) control patterns work together to support general object selection scenarios.

## Custom Control Types

Although this topic focuses on how to register custom UI Automation properties, events, and control patterns, it is also possible to introduce new control types. Unlike custom properties, events, and control patterns, a custom control type cannot be registered programmatically at runtime because it is actually just a potential value of the UI Automation ControlType property. However, a custom control type ID can be defined, published, and made available for other clients and providers to use. For more information about control types, see [UI Automation Control Types Overview](uiauto-controltypesoverview.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Registering Custom Properties, Events, and Control Patterns](uiauto-regcustompropseventpatterns.md)
</dt> <dt>

[UI Automation Properties Overview](uiauto-propertiesoverview.md)
</dt> <dt>

[UI Automation Events Overview](uiauto-eventsoverview.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> </dl>

 

 