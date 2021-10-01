---
title: HeaderItem Control Type
description: This topic provides information about Microsoft UI Automation support for the HeaderItem control type.
ms.assetid: c70420d6-d9f3-47c8-a09f-35ed170f815f
keywords:
- UI Automation,support for HeaderItem control type
- UI Automation,HeaderItem control type
- UI Automation,tree structure for HeaderItem control type
- UI Automation,properties for HeaderItem control type
- UI Automation,control patterns for HeaderItem control type
- UI Automation,events for HeaderItem control type
- tree structures,HeaderItem control type
- properties,HeaderItem control type
- control patterns,HeaderItem control type
- events,HeaderItem control type
- support for HeaderItem control type
- HeaderItem control type
- control types,tree structure for HeaderItem control type
- control types,control patterns for HeaderItem control type
- control types,support for HeaderItem
- control types,HeaderItem
ms.topic: article
ms.date: 05/31/2018
---

# HeaderItem Control Type

This topic provides information about Microsoft UI Automation support for the **HeaderItem** control type.

The **HeaderItem** control type provides a visual label for a row or column of information.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **HeaderItem** control type. The UI Automation requirements apply to all header item controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to header item controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>HeaderItem</li></ul> | (Not applicable) | 




 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **HeaderItem** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value          | Notes                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.     | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.     | The outermost rectangle that contains the whole control.                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.     | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **HeaderItem** | This value is the same for all UI frameworks.                                                                                                                                                        |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | FALSE          | The header item control is not included in the content view of the UI Automation tree.                                                                                                               |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE           | The header item control is always included in the control view of the UI Automation tree.                                                                                                            |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.     | If the control can receive keyboard focus, it must support this property.                                                                                                                            |
| [**UIA\_ItemStatusPropertyId**](uiauto-automation-element-propids.md)                     | See notes      | This property provides information for sort orders by the header item.                                                                                                                               |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | NULL           | Header item controls do not have a static text label.                                                                                                                                                |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.     | Localized string corresponding to the **HeaderItem** control type. The default value is "header item" for en-US or English (United States).                                                          |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.     | The header item control is always self-labeling.                                                                                                                                                     |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all header item controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                         | Support | Notes                                                                                                                             |
|---------------------------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider)       | Depends | Implement the [Invoke](uiauto-implementinginvoke.md) control pattern if the header item control can be clicked to sort the data. |
| [**ITransformProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itransformprovider) | Depends | Implement the [Transform](uiauto-implementingtransform.md) control pattern if the header item control can be resized.            |



 

## Required Events

The following table lists the UI Automation events that header item controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_Invoke\_InvokedEventId**](uiauto-event-ids.md)                                                     | If the control supports the [Invoke](uiauto-implementinginvoke.md) control pattern, it must support this event.           |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




